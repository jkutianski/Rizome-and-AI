---
name: "Validate References"
description: "Perform a bibliographic, documentary, and evidential audit of a source and its references."
argument-hint: "Provide the source path or text, the audit scope, and any version or repository details."
agent: "agent"
---

Perform a complete reference-validation audit of the source provided by the user:

${input:source}

Use the following as the methodological authority:

- [AGENTS.md](../../AGENTS.md)
- [reference-validation Skill](../../skills/epistemic/reference-validation/SKILL.md)
- [evidence and citation protocol](../../skills/_shared/evidence-and-citation.md)
- [analytical discipline protocol](../../skills/_shared/analytical-discipline.md)
- [language-agnostic analysis protocol](../../skills/_shared/language-agnostic-analysis.md)
- [output protocol](../../skills/_shared/output-protocol.md)
- [finding schema](../../schemas/finding.md)
- [audit state schema](../../schemas/audit-state.md)

Before starting:

1. Identify the exact source version, language, requested scope, repository, branch, and commit when available.
2. Read the actual source and do not silently substitute a translation, summary, reconstruction, or previous version.
3. State which external verification was possible and which limitations remain.
4. Do not modify the source during the audit.

Build a complete reference inventory. Do not audit only references that initially appear problematic. For every in-text citation and bibliography entry, record when available:

- citation marker and source location;
- corresponding bibliography entry;
- claim or claims apparently supported;
- source type;
- URL, DOI, or other identifier;
- publication date, version, and status.

Assess every significant reference separately across these dimensions:

1. **Existence:** Does the cited work or document exist?
2. **Bibliographic correctness:** Are the authors, title, date, publication details, identifiers, and links accurate?
3. **Source quality:** Is the source authoritative and appropriate for the claim?
4. **Thematic relevance:** Does the source actually concern the subject at issue?
5. **Evidential support:** Does it establish the specific claim for which it is cited?
6. **Scope:** Does it support the strength and breadth of the formulation?
7. **Currency:** Is it adequate for the temporal claim being made?

Also audit the reference structure for:

- citations without bibliography entries;
- bibliography entries without citations;
- malformed, misplaced, duplicated, or incorrectly numbered citations;
- duplicate publications, DOIs, URLs, or versions;
- important externally verifiable claims that lack adequate evidence;
- claims that are stronger than the cited sources support.

For each reference, classify the result as one of: **Verified**, **Verified with Minor Correction**, **Partially Verified**, **Unverified**, **Incorrect**, **Obsolete Version**, or **Duplicate**. For evidential correspondence, use: **Direct Support**, **Strong Support**, **Partial Support**, **Indirect Support**, **Weak Support**, **No Support**, or **Contradictory Support**.

Deliver:

1. The document-verification record, including the source version and verification status.
2. The complete reference inventory.
3. A concise result for every reference with evidence, verification status, evidential correspondence, confidence, and limitations.
4. Structural citation findings and unsupported or overextended claims.
5. Findings using [schemas/finding.md](../../schemas/finding.md), clearly separated from recommendations or decisions.
6. A prioritized synthesis of necessary, advisable, optional, and not-recommended interventions.

Do not invent bibliographic data, links, quotations, source contents, or verification results. Distinguish source evidence, external evidence, analytical inference, and uncertainty. Existence of a source is not the same as bibliographic correctness, thematic relevance, or evidential support.