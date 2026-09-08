from pathlib import Path
import filecmp
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
CANONICAL_SKILLS = ROOT / "skills"
GENERATED_MARKER = ".generated-by-rizome-sync"
AGENT_SKILL_ROOTS = {
    "copilot": ROOT / ".github" / "skills",
    "claude": ROOT / ".claude" / "skills",
    "codex": ROOT / ".agents" / "skills",
}


REQUIRED_FILES = [
    "AGENTS.md",
    "CLAUDE.md",
    "README.md",
    ".github/copilot-instructions.md",
    "workflows/comprehensive-39-round-audit/SKILL.md",
    "schemas/finding.md",
    "schemas/audit-state.md",
    "schemas/decision-record.md",
    "agents/agent-contract.md",
    "agents/codex.md",
    "agents/claude-code.md",
    "agents/github-copilot.md",
]


EXPECTED_SKILLS = {
    "skills/conceptual/conceptual-consistency/SKILL.md",
    "skills/conceptual/element-relation-tension/SKILL.md",
    "skills/conceptual/semantic-precision/SKILL.md",
    "skills/conceptual/philosophical-claims/SKILL.md",
    "skills/cartographic/map-territory/SKILL.md",
    "skills/cartographic/connection-analysis/SKILL.md",
    "skills/cartographic/propagation-analysis/SKILL.md",
    "skills/cartographic/node-validation/SKILL.md",
    "skills/cartographic/inter-stem-validation/SKILL.md",
    "skills/cartographic/rhizomatic-cartography/SKILL.md",
    "skills/causal/causality-propagation/SKILL.md",
    "skills/causal/scale-analysis/SKILL.md",
    "skills/causal/emergence-analysis/SKILL.md",
    "skills/critical/anthropomorphism-audit/SKILL.md",
    "skills/critical/technological-determinism/SKILL.md",
    "skills/critical/falsifiability-vulnerability/SKILL.md",
    "skills/critical/hostile-reader/SKILL.md",
    "skills/structural/structural-architecture/SKILL.md",
    "skills/structural/necessity-redundancy/SKILL.md",
    "skills/structural/contradiction-tension/SKILL.md",
    "skills/structural/asymmetry-analysis/SKILL.md",
    "skills/reader/whole-work-reading/SKILL.md",
    "skills/reader/blind-external-reading/SKILL.md",
    "skills/reader/non-specialist-reader/SKILL.md",
    "skills/authorship/observer-implication/SKILL.md",
    "skills/authorship/ai-writing-reflexivity/SKILL.md",
    "skills/authorship/voice-style-rhythm/SKILL.md",
    "skills/authorship/phenomenological-reading/SKILL.md",
    "skills/epistemic/power-mediation-authority/SKILL.md",
    "skills/epistemic/knowledge-evidence-production/SKILL.md",
    "skills/epistemic/reference-validation/SKILL.md",
    "skills/synthesis/originality-analysis/SKILL.md",
    "skills/synthesis/ending-openness/SKILL.md",
    "skills/synthesis/integrated-audit/SKILL.md",
}


SHARED_PROTOCOLS = {
    "skills/_shared/language-agnostic-analysis.md",
    "skills/_shared/evidence-and-citation.md",
    "skills/_shared/analytical-discipline.md",
    "skills/_shared/output-protocol.md",
}


errors = []
warnings = []


def check_exists(relative_path):
    path = ROOT / relative_path
    if path.exists():
        print(f"PASS     {relative_path}")
        return True
    print(f"ERROR    Missing: {relative_path}")
    errors.append(relative_path)
    return False


def canonical_skill_inventory():
    if not CANONICAL_SKILLS.exists():
        return set()
    return {
        path
        for path in CANONICAL_SKILLS.rglob("SKILL.md")
        if "_shared" not in path.relative_to(CANONICAL_SKILLS).parts
    }


def canonical_skill_names():
    return {path.parent.name for path in canonical_skill_inventory()}


def relative_files(directory, exclude_marker=False):
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


def directories_are_equal(source, target):
    if not source.is_dir() or not target.is_dir():
        return False
    source_files = relative_files(source)
    target_files = relative_files(target, exclude_marker=True)
    if source_files != target_files:
        return False
    return all(
        filecmp.cmp(source / relative, target / relative, shallow=False)
        for relative in source_files
    )


def check_required_files():
    print("\n== Required files ==")
    for path in REQUIRED_FILES:
        check_exists(path)


def check_skills():
    print("\n== Canonical Skills ==")
    for path in sorted(EXPECTED_SKILLS):
        check_exists(path)
    actual = {
        str(path.relative_to(ROOT)).replace("\\", "/")
        for path in canonical_skill_inventory()
    }
    unexpected = actual - EXPECTED_SKILLS
    missing = EXPECTED_SKILLS - actual
    if not unexpected and not missing:
        print("PASS     Skill inventory matches expected architecture")
    for path in sorted(unexpected):
        print(f"WARNING  Unexpected Skill: {path}")
        warnings.append(path)
    for path in sorted(missing):
        if path not in errors:
            print(f"ERROR    Missing Skill: {path}")
            errors.append(path)


def check_generated_agent_skills():
    print("\n== Generated agent Skill projections ==")
    expected_names = canonical_skill_names()
    valid = True
    for agent, target_root in AGENT_SKILL_ROOTS.items():
        label = target_root.relative_to(ROOT)
        print(f"\n-- {agent.upper()}: {label} --")
        if not target_root.exists():
            print(f"ERROR    Missing generated Skill root: {label}")
            errors.append(str(label))
            valid = False
            continue
        if not target_root.is_dir():
            print(f"ERROR    Skill root is not a directory: {label}")
            errors.append(str(label))
            valid = False
            continue
        marker = target_root / GENERATED_MARKER
        if not marker.is_file():
            print(f"ERROR    Missing generation marker: {label}/{GENERATED_MARKER}")
            errors.append(str(marker.relative_to(ROOT)))
            valid = False
        direct_skills = {
            child.name
            for child in target_root.iterdir()
            if child.is_dir()
            and child.name != GENERATED_MARKER
            and (child / "SKILL.md").is_file()
        }
        nested_skill_files = []
        for path in target_root.rglob("SKILL.md"):
            relative = path.relative_to(target_root)
            if len(relative.parts) > 2:
                nested_skill_files.append(relative)
        if nested_skill_files:
            for path in sorted(nested_skill_files):
                print(f"ERROR    Nested Skill layout: {label}/{path}")
                errors.append(str(label / path))
            valid = False
        missing = expected_names - direct_skills
        stale = direct_skills - expected_names
        for name in sorted(missing):
            print(f"ERROR    {agent}: missing Skill projection: {name}")
            errors.append(f"{label}/{name}/SKILL.md")
            valid = False
        for name in sorted(stale):
            print(f"ERROR    {agent}: unexpected Skill projection: {name}")
            errors.append(f"{label}/{name}/SKILL.md")
            valid = False
        for source_file in sorted(canonical_skill_inventory()):
            source = source_file.parent
            name = source.name
            target = target_root / name
            if not target.is_dir():
                continue
            if not directories_are_equal(source, target):
                print(f"ERROR    {agent}: out of sync: {name}")
                errors.append(f"{label}/{name}")
                valid = False
        unexpected_root_files = {
            path.relative_to(target_root)
            for path in target_root.iterdir()
            if path.is_file() and path.name != GENERATED_MARKER
        }
        if unexpected_root_files:
            for path in sorted(unexpected_root_files):
                print(f"ERROR    {agent}: unexpected root file: {label}/{path}")
                errors.append(str(label / path))
            valid = False
        if valid:
            print(f"PASS     {agent}: {len(expected_names)} flat Skill projections synchronized")


def check_shared_protocols():
    print("\n== Shared protocols ==")
    for path in sorted(SHARED_PROTOCOLS):
        check_exists(path)


def extract_relative_references(path):
    text = path.read_text(encoding="utf-8")
    return re.findall(
        r'(?<!https://)(?<!http://)(?:skills|schemas|agents|workflows|\.github|\.claude|\.agents)/[A-Za-z0-9_./-]+',
        text,
    )


def check_internal_references():
    print("\n== Internal references ==")
    checked = set()
    candidates = [
        ROOT / "AGENTS.md",
        ROOT / "CLAUDE.md",
        ROOT / "README.md",
        ROOT / ".github" / "copilot-instructions.md",
        ROOT / "agents",
        ROOT / "skills",
        ROOT / "workflows",
        ROOT / "schemas",
    ]
    files = []
    for candidate in candidates:
        if candidate.is_file():
            files.append(candidate)
        elif candidate.is_dir():
            files.extend(candidate.rglob("*.md"))
    for file in files:
        for reference in extract_relative_references(file):
            reference = reference.rstrip("`),.;:")
            target = ROOT / reference
            if reference in checked:
                continue
            checked.add(reference)
            if target.exists():
                continue
            print(f"WARNING  Unresolved reference: {reference} (from {file.relative_to(ROOT)})")
            warnings.append(reference)


def check_adapter_size():
    print("\n== Agent adapter duplication check ==")
    adapters = [
        ROOT / "AGENTS.md",
        ROOT / "CLAUDE.md",
        ROOT / ".github" / "copilot-instructions.md",
    ]
    for path in adapters:
        if not path.exists():
            continue
        lines = path.read_text(encoding="utf-8").splitlines()
        if len(lines) > 120:
            print(f"WARNING  {path.relative_to(ROOT)} contains {len(lines)} lines")
            warnings.append(str(path))
        else:
            print(f"PASS     {path.relative_to(ROOT)} ({len(lines)} lines)")


def main():
    print("Rizome-and-AI Repository Integrity Validator")
    print(f"Repository: {ROOT}")
    check_required_files()
    check_skills()
    check_generated_agent_skills()
    check_shared_protocols()
    check_internal_references()
    check_adapter_size()
    print("\n== Result ==")
    if errors:
        print(f"ERRORS:   {len(errors)}")
    if warnings:
        print(f"WARNINGS: {len(warnings)}")
    if not errors and not warnings:
        print("PASS     Repository integrity verified")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
