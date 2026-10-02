import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from IA.scripts.agent_projections import (
    PROMPT_MARKER_CONTENT,
    SKILL_MARKER_CONTENT,
    extract_internal_references,
    is_exact_legacy_projection,
    marker_matches,
    prompt_projection_content,
    prompt_projection_is_valid,
    remove_generated_directory,
    replace_generated_directory,
    resolve_internal_reference,
    validate_skill_frontmatter,
)


class PromptProjectionTests(unittest.TestCase):
    def setUp(self):
        self.temporary_directory = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary_directory.name)
        self.source = self.root / "review.prompt.md"
        self.source.write_text(
            '---\nname: "Review"\ndescription: "Review a source."\n'
            'argument-hint: "Provide a source."\nagent: "agent"\n---\n\n'
            "Analyze this source: ${input:source}\n",
            encoding="utf-8",
        )

    def tearDown(self):
        self.temporary_directory.cleanup()

    def test_projection_templates_preserve_each_agent_input_contract(self):
        copilot = prompt_projection_content(self.source, "copilot")
        claude = prompt_projection_content(self.source, "claude")
        codex = prompt_projection_content(self.source, "codex")

        self.assertIn("${input:source}", copilot)
        self.assertIn("$ARGUMENTS", claude)
        self.assertIn("IA/prompts/review.prompt.md", codex)

    def test_prompt_check_rejects_changed_wrapper(self):
        target = self.root / "review.prompt.md"
        target.write_text(prompt_projection_content(self.source, "copilot"), encoding="utf-8")
        self.assertTrue(prompt_projection_is_valid(target, self.source, "copilot"))

        target.write_text(target.read_text(encoding="utf-8") + "extra instruction\n", encoding="utf-8")
        self.assertFalse(prompt_projection_is_valid(target, self.source, "copilot"))

    def test_copilot_projection_requires_one_input_variable(self):
        self.source.write_text(
            '---\nname: "Review"\ndescription: "Review."\n---\n'
            "${input:source} ${input:node}\n",
            encoding="utf-8",
        )
        with self.assertRaises(ValueError):
            prompt_projection_content(self.source, "copilot")


class GeneratedDirectorySafetyTests(unittest.TestCase):
    def setUp(self):
        self.temporary_directory = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary_directory.name)

    def tearDown(self):
        self.temporary_directory.cleanup()

    def test_clean_refuses_unrecognized_marker_and_preserves_files(self):
        target = self.root / "skills"
        target.mkdir()
        (target / ".generated-by-rizome-sync").write_text("not a valid marker", encoding="utf-8")
        content = target / "user-file.txt"
        content.write_text("keep", encoding="utf-8")

        self.assertFalse(remove_generated_directory(target, SKILL_MARKER_CONTENT))
        self.assertEqual(content.read_text(encoding="utf-8"), "keep")

    def test_clean_removes_directory_with_matching_generated_marker(self):
        target = self.root / "skills"
        target.mkdir()
        (target / ".generated-by-rizome-sync").write_text(SKILL_MARKER_CONTENT, encoding="utf-8")
        self.assertTrue(remove_generated_directory(target, SKILL_MARKER_CONTENT))
        self.assertFalse(target.exists())

    def test_marker_comparison_checks_content(self):
        target = self.root / "prompts"
        target.mkdir()
        marker = target / ".generated-by-rizome-sync"
        marker.write_text(PROMPT_MARKER_CONTENT, encoding="utf-8")
        self.assertTrue(marker_matches(target, PROMPT_MARKER_CONTENT))
        self.assertFalse(marker_matches(target, SKILL_MARKER_CONTENT))

    def test_legacy_projection_with_extra_files_is_not_owned(self):
        canonical = self.root / "canonical" / "node-review"
        projected_root = self.root / "projection" / "family"
        projected_skill = projected_root / "node-review"
        canonical.mkdir(parents=True)
        projected_skill.mkdir(parents=True)
        (canonical / "SKILL.md").write_text("canonical", encoding="utf-8")
        (projected_skill / "SKILL.md").write_text("canonical", encoding="utf-8")
        self.assertTrue(is_exact_legacy_projection(projected_root, {"node-review": canonical}))

        (projected_root / "user-file.txt").write_text("keep", encoding="utf-8")
        self.assertFalse(is_exact_legacy_projection(projected_root, {"node-review": canonical}))

    def test_directory_swap_failure_restores_previous_projection(self):
        source = self.root / "source"
        target = self.root / "target"
        source.mkdir()
        target.mkdir()
        (source / "SKILL.md").write_text("new", encoding="utf-8")
        (target / "SKILL.md").write_text("old", encoding="utf-8")

        import os

        real_replace = os.replace
        replace_count = 0

        def fail_new_target_swap(source_path, target_path):
            nonlocal replace_count
            replace_count += 1
            if replace_count == 2:
                raise PermissionError("simulated destination lock")
            return real_replace(source_path, target_path)

        with patch("os.replace", side_effect=fail_new_target_swap):
            with self.assertRaises(PermissionError):
                replace_generated_directory(source, target)

        self.assertEqual((target / "SKILL.md").read_text(encoding="utf-8"), "old")

    def test_directory_swap_replaces_projection_after_staging(self):
        source = self.root / "source"
        target = self.root / "target"
        source.mkdir()
        target.mkdir()
        (source / "SKILL.md").write_text("new", encoding="utf-8")
        (target / "SKILL.md").write_text("old", encoding="utf-8")

        replace_generated_directory(source, target)

        self.assertEqual((target / "SKILL.md").read_text(encoding="utf-8"), "new")


class RepositoryMetadataAndPathTests(unittest.TestCase):
    def setUp(self):
        self.temporary_directory = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary_directory.name)

    def tearDown(self):
        self.temporary_directory.cleanup()

    def test_skill_frontmatter_requires_matching_name_and_description(self):
        skill_file = self.root / "sample-skill" / "SKILL.md"
        skill_file.parent.mkdir()
        skill_file.write_text(
            '---\nname: "sample-skill"\ndescription: "A sample skill."\n---\n',
            encoding="utf-8",
        )
        self.assertEqual(validate_skill_frontmatter(skill_file), [])

        skill_file.write_text("# Skill without metadata\n", encoding="utf-8")
        self.assertTrue(validate_skill_frontmatter(skill_file))

    def test_internal_reference_resolution_respects_document_location(self):
        canonical_document = self.root / "IA" / "agents" / "agent.md"
        root_document = self.root / "AGENTS.md"
        self.assertEqual(
            resolve_internal_reference(canonical_document, "skills/node/SKILL.md", self.root),
            self.root / "IA" / "skills/node/SKILL.md",
        )
        self.assertEqual(
            resolve_internal_reference(root_document, "IA/skills/node/SKILL.md", self.root),
            self.root / "IA/skills/node/SKILL.md",
        )

    def test_url_paths_are_not_treated_as_internal_references(self):
        self.assertEqual(
            extract_internal_references("See https://example.test/IA/skills/not-a-local-link"),
            [],
        )

    def test_local_markdown_paths_are_normalized_to_canonical_root(self):
        source_file = self.root / "IA" / "prompts" / "review.prompt.md"
        reference = extract_internal_references("[Skill](../skills/example/SKILL.md)")[0]
        self.assertEqual(reference, "../skills/example/SKILL.md")
        self.assertEqual(
            resolve_internal_reference(source_file, reference, self.root),
            self.root / "IA" / "skills" / "example" / "SKILL.md",
        )


if __name__ == "__main__":
    unittest.main()