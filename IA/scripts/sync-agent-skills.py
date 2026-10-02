from __future__ import annotations

import argparse
import os
import shutil
import sys
import tempfile
from pathlib import Path

from agent_projections import (
    GENERATED_MARKER,
    LEGACY_PROMPT_MARKER_CONTENT,
    PROMPT_MARKER_CONTENT,
    SKILL_MARKER_CONTENT,
    is_exact_legacy_projection,
    marker_matches,
    prompt_name,
    prompt_projection_content,
    prompt_projection_is_valid,
    remove_generated_directory,
    replace_generated_directory,
)

ROOT = Path(__file__).resolve().parents[2]
CANONICAL_ROOT = ROOT / "IA"
CANONICAL_SKILLS = CANONICAL_ROOT / "skills"
CANONICAL_PROMPTS = CANONICAL_ROOT / "prompts"

# Canonical Skills remain organized by family. Agent discovery directories are flat.
# Codex project Skills are exposed through .agents/skills.
TARGETS = {
    "copilot": ROOT / ".github" / "skills",
    "claude": ROOT / ".claude" / "skills",
    "codex": ROOT / ".agents" / "skills",
}

PROMPT_TARGETS = {
    "copilot": ROOT / ".github" / "prompts",
    "claude": ROOT / ".claude" / "commands",
    "codex": ROOT / ".codex" / "prompts",
}

def discover_skills() -> list[Path]:
    if not CANONICAL_SKILLS.exists():
        return []
    skills = []
    for skill_file in CANONICAL_SKILLS.rglob("SKILL.md"):
        skill_dir = skill_file.parent
        if "_shared" in skill_dir.relative_to(CANONICAL_SKILLS).parts:
            continue
        skills.append(skill_dir)
    return sorted(skills)


def discover_prompts() -> list[Path]:
    if not CANONICAL_PROMPTS.exists():
        return []
    return sorted(CANONICAL_PROMPTS.glob("*.prompt.md"))


def skill_name(skill_dir: Path) -> str:
    return skill_dir.name


def relative_canonical_path(skill_dir: Path) -> Path:
    return skill_dir.relative_to(CANONICAL_SKILLS)


def relative_prompt_path(prompt_file: Path) -> Path:
    return prompt_file.relative_to(CANONICAL_PROMPTS)


def validate_skill_names(skills: list[Path]) -> bool:
    """Families are repository organization; agent projections are flat."""
    print("\n== Skill name validation ==")
    names: dict[str, list[Path]] = {}
    for skill in skills:
        names.setdefault(skill_name(skill), []).append(skill)
    valid = True
    for name, paths in sorted(names.items()):
        if len(paths) == 1:
            print(f"PASS     {name}")
            continue
        print(f"ERROR    Skill name collision: {name}")
        for path in paths:
            print(f"         - {relative_canonical_path(path)}")
        valid = False
    return valid


def validate_canonical_skills(skills: list[Path]) -> bool:
    print("\n== Canonical Skills ==")
    if not CANONICAL_SKILLS.exists() or not skills:
        print("ERROR    No canonical Skills found.")
        return False
    valid = True
    for skill in skills:
        if not (skill / "SKILL.md").is_file():
            print(f"ERROR    Missing SKILL.md: {relative_canonical_path(skill)}")
            valid = False
        else:
            print(f"PASS     {relative_canonical_path(skill)}")
    print(f"\nFound {len(skills)} canonical Skills.")
    return valid


def marker_path(target_root: Path) -> Path:
    return target_root / GENERATED_MARKER


def atomic_write_text(target: Path, content: str) -> None:
    with tempfile.NamedTemporaryFile(
        mode="w", encoding="utf-8", dir=tempfile.gettempdir(), delete=False
    ) as handle:
        handle.write(content)
        temporary = Path(handle.name)
    try:
        os.replace(temporary, target)
    finally:
        temporary.unlink(missing_ok=True)


def write_marker(target_root: Path) -> None:
    target_root.mkdir(parents=True, exist_ok=True)
    marker = marker_path(target_root)
    if marker.is_file() and marker.read_text(encoding="utf-8") == SKILL_MARKER_CONTENT:
        return
    atomic_write_text(marker, SKILL_MARKER_CONTENT)


def write_prompt_marker(target_root: Path) -> None:
    target_root.mkdir(parents=True, exist_ok=True)
    marker = marker_path(target_root)
    if marker.is_file() and marker.read_text(encoding="utf-8") == PROMPT_MARKER_CONTENT:
        return
    atomic_write_text(marker, PROMPT_MARKER_CONTENT)


def relative_files(directory: Path, exclude_marker: bool = False) -> set[Path]:
    if not directory.exists():
        return set()
    result = set()
    for path in directory.rglob("*"):
        if not path.is_file():
            continue
        relative = path.relative_to(directory)
        if exclude_marker and relative == Path(GENERATED_MARKER):
            continue
        result.add(relative)
    return result


def files_are_equal(source: Path, target: Path) -> bool:
    source_content = source.read_bytes().splitlines()
    target_content = target.read_bytes().splitlines()
    return source_content == target_content


def directories_are_equal(source: Path, target: Path) -> bool:
    if not source.is_dir() or not target.is_dir():
        return False
    source_files = relative_files(source)
    target_files = relative_files(target, exclude_marker=True)
    if source_files != target_files:
        return False
    return all(files_are_equal(source / relative, target / relative) for relative in source_files)


def validate_target_root(target_root: Path) -> bool:
    if not target_root.exists():
        return True
    if target_root.is_symlink():
        print(f"ERROR    Refusing to modify linked target: {target_root.relative_to(ROOT)}")
        return False
    if not target_root.is_dir():
        print(f"ERROR    Target is not a directory: {target_root.relative_to(ROOT)}")
        return False
    if not marker_matches(target_root, SKILL_MARKER_CONTENT):
        print(f"ERROR    Refusing to modify unmarked directory: {target_root.relative_to(ROOT)}")
        return False
    return True


def legacy_nested_dirs(target_root: Path, skills: list[Path]) -> list[Path]:
    """Find old family-nested projections, without touching arbitrary content."""
    expected = {skill_name(skill) for skill in skills}
    result = []
    if not target_root.exists():
        return result
    for child in target_root.iterdir():
        if not child.is_dir() or child.name == GENERATED_MARKER:
            continue
        if (child / "SKILL.md").is_file():
            continue
        nested = list(child.rglob("SKILL.md"))
        if nested and {p.parent.name for p in nested}.issubset(expected):
            result.append(child)
    return sorted(result)


def sync_target(name: str, target_root: Path, skills: list[Path], dry_run: bool = False) -> bool:
    print(f"\n== SYNC {name.upper()} ==")
    print(f"Target: {target_root.relative_to(ROOT)}")
    if not validate_target_root(target_root):
        return False
    if not dry_run:
        target_root.mkdir(parents=True, exist_ok=True)
        try:
            write_marker(target_root)
        except OSError as error:
            print(f"ERROR    Cannot write generated marker: {target_root / GENERATED_MARKER}")
            print(f"         {error}")
            return False

    canonical_by_name = {skill_name(skill): skill for skill in skills}
    legacy_candidates = legacy_nested_dirs(target_root, skills)
    unsafe_legacy = [
        legacy for legacy in legacy_candidates
        if not is_exact_legacy_projection(legacy, canonical_by_name)
    ]
    if unsafe_legacy:
        for legacy in unsafe_legacy:
            print(f"ERROR    Refusing to remove modified legacy directory: {legacy.relative_to(ROOT)}")
        return False

    for legacy in legacy_candidates:
        print(f"REMOVE   legacy nested projection {legacy.relative_to(ROOT)}")
        if not dry_run:
            shutil.rmtree(legacy)

    expected = {skill_name(skill) for skill in skills}
    existing = {
        child.name for child in target_root.iterdir()
        if child.is_dir() and child.name != GENERATED_MARKER and (child / "SKILL.md").is_file()
    } if target_root.exists() else set()

    for stale in sorted(existing - expected):
        target = target_root / stale
        print(f"REMOVE   {target.relative_to(ROOT)}")
        if not dry_run:
            shutil.rmtree(target)

    synchronized = unchanged = 0
    for source in skills:
        target = target_root / skill_name(source)
        if target.exists() and not target.is_dir():
            print(f"ERROR    Target path is not a directory: {target.relative_to(ROOT)}")
            return False
        if directories_are_equal(source, target):
            print(f"UNCHANGED {skill_name(source)}")
            unchanged += 1
            continue
        print(f"SYNC     {relative_canonical_path(source)} -> {target.relative_to(ROOT)}")
        if not dry_run:
            try:
                target.parent.mkdir(parents=True, exist_ok=True)
                replace_generated_directory(source, target)
            except OSError as error:
                print(f"ERROR    Cannot safely replace generated Skill: {target.relative_to(ROOT)}")
                print(f"         {error}")
                print("         The previous projection was preserved; check that the target is writable and available locally.")
                return False
        synchronized += 1

    print(f"\n{len(skills)} Skills: {synchronized} synchronized, {unchanged} unchanged.")
    return True


def check_target(name: str, target_root: Path, skills: list[Path]) -> bool:
    print(f"\n== CHECK {name.upper()} ==")
    if not marker_matches(target_root, SKILL_MARKER_CONTENT):
        print(f"ERROR    Missing generated target: {target_root.relative_to(ROOT)}")
        return False
    expected = {skill_name(skill) for skill in skills}
    actual = {
        child.name for child in target_root.iterdir()
        if child.is_dir() and child.name != GENERATED_MARKER and (child / "SKILL.md").is_file()
    }
    valid = True
    for name_to_check in sorted(expected - actual):
        print(f"ERROR    Missing Skill: {name_to_check}")
        valid = False
    for name_to_check in sorted(actual - expected):
        print(f"ERROR    Unexpected Skill: {name_to_check}")
        valid = False
    for legacy in legacy_nested_dirs(target_root, skills):
        print(f"ERROR    Legacy nested Skill layout: {legacy.relative_to(ROOT)}")
        valid = False
    for source in skills:
        target = target_root / skill_name(source)
        if target.exists() and not directories_are_equal(source, target):
            print(f"ERROR    Out of sync: {skill_name(source)}")
            valid = False
    if valid:
        print(f"PASS     {len(skills)} Skills synchronized with flat discovery layout.")
    return valid


def clean_target(
    name: str, target_root: Path, marker_contents: str | tuple[str, ...]
) -> bool:
    print(f"\n== CLEAN {name.upper()} ==")
    if not remove_generated_directory(target_root, marker_contents):
        print(f"ERROR    Refusing to remove unmarked directory: {target_root.relative_to(ROOT)}")
        return False
    return True


def validate_prompt_target_root(target_root: Path) -> bool:
    if not target_root.exists():
        return True
    if target_root.is_symlink():
        print(f"ERROR    Refusing to modify linked prompt target: {target_root.relative_to(ROOT)}")
        return False
    if not target_root.is_dir():
        print(f"ERROR    Prompt target is not a directory: {target_root.relative_to(ROOT)}")
        return False
    if not marker_matches(target_root, (PROMPT_MARKER_CONTENT, LEGACY_PROMPT_MARKER_CONTENT)):
        print(f"ERROR    Refusing to modify unmarked prompt directory: {target_root.relative_to(ROOT)}")
        return False
    return True


def sync_prompt_target(name: str, target_root: Path, prompts: list[Path], dry_run: bool = False) -> bool:
    print(f"\n== SYNC {name.upper()} PROMPTS ==")
    print(f"Target: {target_root.relative_to(ROOT)}")
    if not validate_prompt_target_root(target_root):
        return False
    if not dry_run:
        target_root.mkdir(parents=True, exist_ok=True)
        write_prompt_marker(target_root)

    expected = {prompt_name(prompt, name) for prompt in prompts}
    existing = {
        path.name for path in target_root.iterdir()
        if path.is_file() and path.name != GENERATED_MARKER
    } if target_root.exists() else set()
    for stale in sorted(existing - expected):
        target = target_root / stale
        print(f"REMOVE   {target.relative_to(ROOT)}")
        if not dry_run:
            target.unlink()

    synchronized = unchanged = 0
    for source in prompts:
        target = target_root / prompt_name(source, name)
        expected_content = prompt_projection_content(source, name)
        if prompt_projection_is_valid(target, source, name):
            print(f"UNCHANGED {prompt_name(source, name)}")
            unchanged += 1
            continue
        print(f"SYNC     {relative_prompt_path(source)} -> {target.relative_to(ROOT)}")
        if not dry_run:
            atomic_write_text(target, expected_content)
        synchronized += 1

    print(f"\n{len(prompts)} prompts: {synchronized} synchronized, {unchanged} unchanged.")
    return True


def check_prompt_target(name: str, target_root: Path, prompts: list[Path]) -> bool:
    print(f"\n== CHECK {name.upper()} PROMPTS ==")
    if not target_root.exists() or not target_root.is_dir():
        print(f"ERROR    Missing prompt target: {target_root.relative_to(ROOT)}")
        return False
    if not marker_matches(target_root, PROMPT_MARKER_CONTENT):
        print(f"ERROR    Missing or invalid prompt marker: {target_root.relative_to(ROOT)}")
        return False
    expected = {prompt_name(prompt, name) for prompt in prompts}
    actual = {
        path.name for path in target_root.iterdir()
        if path.is_file() and path.name != GENERATED_MARKER
    }
    valid = True
    for missing in sorted(expected - actual):
        print(f"ERROR    Missing prompt: {missing}")
        valid = False
    for stale in sorted(actual - expected):
        print(f"ERROR    Unexpected prompt: {stale}")
        valid = False
    for source in prompts:
        target = target_root / prompt_name(source, name)
        if target.exists() and not prompt_projection_is_valid(target, source, name):
            print(f"ERROR    Out of sync: {target.relative_to(ROOT)}")
            valid = False
    if valid:
        print(f"PASS     {len(prompts)} prompts synchronized.")
    return valid


def main() -> int:
    parser = argparse.ArgumentParser(description="Synchronize canonical Skills and prompts with agent discovery directories.")
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--clean", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--agent", choices=["copilot", "claude", "codex", "all"], default="all")
    args = parser.parse_args()
    if args.check and args.clean or args.clean and args.dry_run:
        print("ERROR    Incompatible command-line options.")
        return 1
    skills = discover_skills()
    prompts = discover_prompts()
    if not validate_canonical_skills(skills) or not validate_skill_names(skills):
        return 1
    if not prompts:
        print("ERROR    No canonical prompts found.")
        return 1
    targets = TARGETS if args.agent == "all" else {args.agent: TARGETS[args.agent]}
    success = True
    for name, target in targets.items():
        if args.check:
            result = check_target(name, target, skills)
        elif args.clean:
            result = clean_target(name, target, SKILL_MARKER_CONTENT)
        else:
            result = sync_target(name, target, skills, args.dry_run)
        success = result and success
    prompt_targets = PROMPT_TARGETS if args.agent == "all" else {args.agent: PROMPT_TARGETS[args.agent]}
    for name, target in prompt_targets.items():
        if args.check:
            result = check_prompt_target(name, target, prompts)
        elif args.clean:
            result = clean_target(
                f"{name} prompts",
                target,
                (PROMPT_MARKER_CONTENT, LEGACY_PROMPT_MARKER_CONTENT),
            )
        else:
            result = sync_prompt_target(name, target, prompts, args.dry_run)
        success = result and success
    print("\n== RESULT ==")
    print("PASS     Synchronization completed successfully." if success else "ERROR    Synchronization failed.")
    return 0 if success else 1


if __name__ == "__main__":
    sys.exit(main())
