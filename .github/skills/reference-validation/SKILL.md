# Reference Validation

## Purpose

Perform an exhaustive bibliographic, documentary, and evidential audit of a document and its references.

The skill determines whether references exist, whether their bibliographic data and links are correct, whether sources are authoritative and appropriate, whether they actually support the claims for which they are cited, whether claims exceed the evidence, and where important externally verifiable claims lack adequate evidence.

The skill diagnoses before rewriting. It does not modify source material unless an explicit editing phase is authorized.

Fundamental distinction:

> existence of a source ≠ bibliographic correctness ≠ thematic relevance ≠ evidential support.

---

## Scope

This Skill may operate on:

- a passage;
- a section;
- a node or assemblage;
- a whole document;
- a bibliography/reference system.

It may identify cross-scope problems when required by the evidence, but such expansion must be explicit.

---

## Inputs

### Required

- the exact source material being audited;
- the requested scope, if narrower than the whole document.

### Optional

- repository and branch information;
- previous findings;
- audit state;
- constraints;
- decisions already established by the workflow.

The Skill must analyze the actual source when available. It must not silently substitute a translation, summary, reconstruction, or previous version.

---

## Dependencies

This Skill uses the principles established in:

```text
skills/_shared/evidence-and-citation.md
skills/_shared/analytical-discipline.md
skills/_shared/output-protocol.md
skills/_shared/language-agnostic-analysis.md
```

It does not depend on another analytical Skill for its core procedure.

---

## Core Distinction

For every important reference, distinguish:

1. **Existence** — does the cited work exist?
2. **Bibliographic correctness** — are its metadata accurate?
3. **Source quality** — is it authoritative and methodologically appropriate?
4. **Thematic relevance** — does it concern the subject?
5. **Evidential support** — does it actually establish the claim?
6. **Scope** — does it support the strength and breadth of the formulation?
7. **Currency** — is it still adequate for the temporal claim?

A source may pass one criterion and fail another.

---

## Exact Document Verification

When the source is in GitHub or another versioned repository, verify whenever possible:

- repository;
- exact path;
- branch;
- commit;
- blob/SHA;
- modification date;
- actual content.

If the requested version cannot be verified, state the limitation explicitly.

Never claim to have audited a version that was not actually retrieved.

Required identification:

```text
Document:
Repository:
Path:
Branch:
Commit:
Blob/SHA:
Modification date:
Verification status:
```

---

## Reference Inventory

Extract every citation appearing in the source and every bibliography entry.

For each reference identify:

- citation marker;
- location in the text;
- bibliography entry;
- claim or claims apparently supported;
- source type;
- URL;
- DOI;
- publication date;
- version/status.

Do not audit only references that initially appear problematic.

---

## Structural Reference Audit

Detect:

### Citation without bibliography

A citation occurs in the text but has no corresponding bibliography entry.

### Bibliography without citation

A bibliography entry exists but is never cited.

Classify whether it is legitimate, accidental, obsolete, or a candidate for removal.

### Malformed citation

Detect misplaced citations, broken Markdown, duplicated markers, missing syntax, incorrect numbering, or a citation attached to the wrong claim.

### Duplicate reference

Detect duplicate publications, duplicate DOIs, duplicate URLs, and cases where multiple entries represent different versions of the same work.

Do not delete a preprint/final pair automatically if their evidential status differs.

---

## Bibliographic Verification

Verify whenever possible:

- authors;
- title;
- year;
- journal/book/report;
- volume/issue/pages;
- publisher/institution;
- DOI;
- URL;
- edition;
- version;
- publication status;
- publication date.

Prioritize:

1. original publisher;
2. DOI registry;
3. original journal/conference;
4. official institution;
5. official court/government source;
6. recognized academic repository;
7. authoritative secondary source.

Classify each reference:

- Verified
- Verified with minor correction
- Partially verified
- Unverified
- Incorrect
- Obsolete version
- Duplicate

Never invent missing bibliographic information.

---

## Source-Type Verification

Identify whether the source is:

- peer-reviewed article;
- conference paper;
- book/book chapter;
- technical report;
- government publication;
- international organization;
- standards document;
- court decision;
- legislation/regulation;
- institutional webpage;
- preprint;
- dataset;
- technical documentation;
- company publication;
- journalism;
- commentary/blog;
- secondary source.

Evaluate whether the source type is appropriate for the claim.

Prefer primary technical/scientific evidence, official legal material, authoritative statistics, and original historical sources when available and appropriate.

---

## Evidential Support Test

This is the central procedure.

For every significant citation establish:

### What the text claims

Identify the precise proposition supported by the citation.

### What the source establishes

Inspect the source and summarize only the relevant evidence.

### Degree of correspondence

Classify the match as:

- Direct support
- Strong support
- Partial support
- Indirect support
- Weak support
- No support
- Contradictory support

Topic similarity is not evidential support.

---

## Overextension Test

Check whether the text is stronger than the source.

Pay special attention to:

- universal claims;
- deterministic claims;
- causal claims;
- historical generalizations;
- quantitative claims;
- social effects;
- adoption claims;
- behavioral claims;
- future consequences.

Check transitions such as:

```text
can → does
may → will
associated with → causes
possible → demonstrated
technical capability → widespread adoption
specific context → universal conclusion
correlation → causation
```

Classify the problem as:

- source insufficient;
- formulation too strong;
- claim requires qualification;
- claim should be divided;
- additional source required.

Do not automatically rewrite the claim.

---

## Claims Without References

Identify externally verifiable claims lacking adequate citation, especially:

- dates;
- numbers/statistics;
- historical claims;
- scientific mechanisms;
- technical capabilities;
- economic claims;
- energy/water/emissions;
- infrastructure;
- semiconductors;
- employment;
- education;
- health/biology;
- AI adoption;
- bias/inequality;
- copyright;
- regulation;
- litigation;
- security;
- geopolitics.

Do not demand citations for every philosophical statement.

Distinguish factual external claims, author interpretation, philosophical argument, and inference.

---

## Evidence vs Interpretation

For important passages reconstruct:

```text
SOURCE / EVIDENCE
        ↓
EMPIRICAL FINDING
        ↓
INFERENCE
        ↓
AUTHOR'S INTERPRETATION
        ↓
PHILOSOPHICAL CONCLUSION
```

Determine whether each transition is justified.

Classify transitions as:

- legitimate inference;
- plausible interpretation;
- excessive inference;
- unsupported inference;
- category error.

Never present an author's interpretation as though it were established by the source.

---

## Source Quality

Evaluate:

### Authority

Who produced the source?

### Primariness

Is it original evidence or secondary commentary?

### Pertinence

Does it address the exact claim?

### Actuality

Is it current enough for the claim?

### Methodological quality

Is the evidence produced appropriately?

### Correspondence

Does it support the exact proposition?

Overall:

- Strong
- Acceptable
- Weak
- Inadequate

A prestigious source may still be inadequate for a particular claim.

---

## Currency Audit

Distinguish historical validity from current validity.

Re-check time-sensitive claims concerning:

- AI capabilities;
- legislation;
- regulation;
- court cases;
- standards;
- employment;
- energy;
- infrastructure;
- semiconductor markets;
- geopolitics;
- deployment/adoption;
- safety frameworks.

If a source has been superseded, identify the current status.

---

## Overloaded References

Detect references used to support many unrelated propositions.

If one source is used for technical, historical, social, and empirical claims simultaneously, determine whether it should be:

- retained;
- complemented;
- split across sources;
- replaced.

Do not multiply citations unnecessarily.

---

## Better-Source Detection

When an existing source is acceptable but a materially stronger source exists, identify it.

Prefer, when appropriate:

1. primary source;
2. original research;
3. official institutional source;
4. systematic/review literature;
5. authoritative secondary literature.

Do not replace a source merely because another source is newer.

---

## Multiple References

Determine whether multiple sources are:

- complementary;
- redundant;
- independent confirmations;
- different in scope;
- contradictory;
- jointly necessary.

Do not add citations merely to increase apparent authority.

---

## Contradictory Evidence

When sources disagree, compare:

- date;
- definitions;
- methodology;
- sample/population;
- geography;
- scope;
- assumptions.

Do not arbitrarily select the source that agrees with the text.

---

## Causality Audit

Audit causal language carefully.

Distinguish:

- correlation vs causation;
- association vs mechanism;
- possibility vs occurrence;
- capability vs deployment;
- deployment vs adoption;
- adoption vs impact;
- potential vs demonstrated effect;
- temporal succession vs causal relation.

Causal verbs trigger verification but are not automatically errors.

---

## Historical Claims

For historical statements verify chronology, attribution, original source, and historical context.

Do not use a contemporary technical source as the sole authority for a historical claim when a suitable primary historical source exists.

---

## Technical Claims

For claims involving AI and technology, verify specifically where relevant:

- architectures;
- algorithms;
- GPUs;
- TPUs;
- NPUs;
- neuromorphic computing;
- brain-computer interfaces;
- multimodal systems;
- in-memory computing;
- on-chip training;
- semiconductor technologies;
- data centers;
- networking;
- storage;
- compute;
- energy requirements.

A general AI source must not silently support a highly specific engineering claim.

---

## Scientific Claims

Verify mechanism, empirical basis, experimental context, scope, uncertainty, and whether the proposition is established or hypothetical.

Do not convert scientific possibility into scientific fact.

---

## Social Claims

For work, education, inequality, bias, culture, knowledge, authority, trust, institutions, and social behavior, verify whether the evidence actually studies the population and phenomenon being described.

Flag overgeneralization from a single country, institution, platform, occupational group, or experiment.

---

## Legal Claims

Verify:

- jurisdiction;
- court;
- case number;
- parties;
- date;
- document type;
- order/judgment status;
- settlement status;
- appeal status;
- later orders.

A news article describing a decision is not equivalent to the decision itself.

---

## URL and DOI Verification

Verify:

- URL accessibility;
- correct destination;
- DOI validity;
- DOI correspondence;
- correct version;
- redirects or migrations.

If the source can be verified independently but its URL is inaccessible, separate source verification from link verification.

---

## No Fabrication

Never invent:

- authors;
- titles;
- dates;
- DOI;
- URLs;
- publication details;
- quotations;
- findings;
- legal status.

If verification fails, mark the source as unverified.

---

## Insertion Criterion

Do not add citations merely to make a text appear academic.

Recommend a new source only when:

1. the claim is externally verifiable;
2. evidence materially strengthens the claim;
3. the proposed source directly or substantially supports it.

Do not cite metaphors, personal reflections, conceptual transitions, or philosophical interpretations merely because they sound theoretical.

---

## Authorial Voice

The audit must not transform the document into:

- an academic paper;
- a literature review;
- a conventional introduction to AI;
- a corporate document;
- a technical report;
- a Deleuze & Guattari exegesis.

Preserve the distinction between evidence, interpretation, philosophical argument, and methodological proposal.

---

## Analytical Procedure

Execute the following sequence:

1. Verify the exact document.
2. Inventory citations and bibliography.
3. Detect orphaned, malformed, and duplicate references.
4. Verify bibliographic metadata.
5. Verify source type and authority.
6. Map each important citation to its claim.
7. Inspect the cited source.
8. Compare claim and evidence.
9. Test for overextension.
10. Detect unsupported external claims.
11. Audit causal language.
12. Audit currency.
13. Identify overloaded or weak references.
14. Search for materially better sources when necessary.
15. Record findings with confidence.
16. Recommend actions without automatically editing the source.

The procedure must remain open to a negative result.

---

## Findings

Substantive findings should be representable through `schemas/finding.md` and should distinguish:

- observation;
- evidence;
- interpretation;
- issue type;
- severity;
- confidence;
- architectural scope;
- recommendation.

Recommended issue types include:

- bibliographic-error;
- missing-reference;
- orphan-reference;
- malformed-citation;
- duplicate-reference;
- weak-source;
- outdated-source;
- insufficient-support;
- overextended-claim;
- causal-overclaim;
- unsupported-inference;
- overloaded-reference;
- broken-link;
- incorrect-doi;
- legal-status-outdated;
- source-claim-mismatch.

Confidence must be:

- High
- Medium
- Low

Severity and confidence are separate dimensions.

---

## Recommendations

Use one of:

- Necessary
- Advisable
- Optional
- Not recommended
- Leave unchanged
- Investigate further

Recommended reference actions:

- Keep
- Keep + correct
- Keep + qualify claim
- Complement
- Replace
- Split
- Remove
- Verify manually

Do not treat intervention as inherently preferable.

---

## Output

Always produce:

### 1. Exact document verification

```text
Document:
Repository:
Path:
Branch:
Commit:
Blob/SHA:
Modification date:
Verification status:
```

### 2. Executive diagnosis

State:

- overall reference quality;
- principal strengths;
- principal weaknesses;
- most important evidential risks;
- final A/B/C/D classification.

### 3. Complete reference inventory

List every reference and status.

### 4. Reference-by-reference audit

For each significant reference:

```text
Reference:
Bibliographic status:
Source type:
Authority:
Current status:
Claim supported:
What the source establishes:
Evidential correspondence:
Overextension:
Quality:
Problems:
Recommended action:
Confidence:
```

### 5. Missing references

Identify unsupported externally verifiable claims and assign priority:

- Critical
- High
- Medium
- Low

### 6. Weak references

Identify sources requiring correction, qualification, supplementation, replacement, or removal.

### 7. Orphan references

Separate:

- cited without bibliography;
- bibliography without citation;
- malformed;
- duplicated;
- suspicious/ambiguous.

### 8. Overloaded references

Identify references supporting too many unrelated claims.

### 9. Causal-language audit

Identify claims whose causal strength exceeds their evidence.

### 10. Current-status audit

Especially for law, litigation, regulation, AI capabilities, infrastructure, employment, energy, and geopolitics.

### 11. Evidence coverage map

Classify document claims as:

- strongly supported;
- adequately supported;
- partially supported;
- weakly supported;
- unsupported;
- philosophical/interpretive.

### 12. Recommended actions

Separate:

- Must fix
- Should fix
- Optional improvement

### 13. Final classification

Use:

**A — Reference architecture is robust**

**B — Minor corrections required**

**C — Significant evidential revision required**

**D — Major reference reconstruction required**

Explain the classification.

---

## Final Integrity Rule

The purpose of this Skill is not to maximize the number of references.

Its purpose is to maximize the correspondence between:

> **claim → evidence → source → interpretation**

while preserving the distinction between:

> **what the source establishes**

and

> **what the author argues from it.**

When uncertainty remains, preserve the uncertainty.

When evidence is insufficient, say so.

When the source is strong, say so.

When the author's argument goes beyond the evidence, identify the precise point where it does so.

Do not hide weaknesses behind citations.
