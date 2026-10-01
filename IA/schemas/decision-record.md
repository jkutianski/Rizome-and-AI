# Decision Record Schema

## Purpose

A **Decision Record** documents an explicit conclusion that changes, preserves, rejects, or constrains the architecture or methodology of the audit.

A Decision is not a Finding.

A Finding describes what the audit observes or diagnoses.

A Decision determines what the audit will preserve, reject, separate, merge, reopen, or otherwise treat as operative.

---

## Core Principle

> Findings describe the state of the investigation. Decisions establish the consequences of that investigation.

A decision must therefore be traceable to findings, evidence, reasoning, or explicit methodological rules.

---

## Core Structure

```text
Decision Record
├── id
├── decision
├── basis
├── evidence
├── affected_components
├── alternatives_considered
├── rationale
├── confidence
├── status
└── reversal_condition
```

---

## `id`

Stable unique identifier.

Example:

```text
D-0014
```

---

## `decision`

The actual decision.

It should be stated directly and unambiguously.

Examples:

```text
Do not classify AI + Identity as an autonomous inter-stem node.
```

```text
Keep Nodes D and E distinct.
```

```text
Treat A–E as parallel concentrations rather than a causal sequence.
```

```text
Preserve the distinction between relevance, authority, legitimacy, and truth.
```

---

## `basis`

Why the decision is being considered.

This may reference:

* a Finding;
* several converging Findings;
* a methodological rule;
* a transversal review;
* a direct textual constraint;
* an architectural requirement.

Example:

```text
The transversal review found no distinct transformation that justifies
AI + Identity as an autonomous concentration.
```

---

## `evidence`

Evidence supporting the decision.

Evidence may include:

```text
finding IDs
source locations
direct textual evidence
cross-node evidence
architectural evidence
methodological constraints
external evidence
```

The decision must not claim stronger evidence than the audit actually possesses.

---

## `affected_components`

Components changed or constrained by the decision.

Examples:

```text
Node D
Node E
Inter-stem architecture
39-round audit state
```

---

## `alternatives_considered`

Relevant alternatives considered before deciding.

Examples:

```text
Create autonomous node
Merge into Node D
Merge into Node E
Redistribute content
Leave content embedded in existing nodes
```

Rejected alternatives should be recorded rather than forgotten.

---

## `rationale`

The reasoning connecting evidence to decision.

The rationale should answer:

```text
Why does this evidence justify this decision?
```

It must not simply repeat the decision.

Example:

```text
The proposed Identity material does not generate a distinct relational
concentration whose tensions and transformation differ sufficiently from
existing nodes. Creating a separate node would therefore organize a theme
rather than identify a new dynamic.
```

---

## `confidence`

Confidence in the decision:

```text
High
Medium
Low
```

Confidence should reflect the strength of the basis, not personal certainty alone.

A low-confidence decision may remain operational if the workflow requires temporary closure, but it should normally include an explicit reversal condition.

---

## `status`

Allowed values:

```text
active
superseded
reopened
rejected
```

### `active`

The decision currently governs the audit.

### `superseded`

A later decision replaced it.

### `reopened`

New evidence caused the decision to be reconsidered.

### `rejected`

The proposed decision itself was not accepted.

Historical records must remain intact.

---

## `reversal_condition`

Defines what would justify reopening the decision.

This field is especially important for closed conceptual or architectural decisions.

Examples:

```text
Reopen only if new textual evidence demonstrates a distinct transformation
between assemblages that is not accounted for elsewhere in the architecture.
```

```text
Reopen if the source explicitly establishes a causal dependency between
D and E that changes their current functional distinction.
```

A reversal condition prevents decisions from becoming dogmatic while preventing arbitrary reopening.

---

## Decision Types

A Decision Record may be classified as:

```text
conceptual
structural
methodological
cartographic
causal
epistemic
reader
authorship
workflow
preservation
```

---

## Finding vs Decision

### Finding

```text
Finding:
The material associated with AI + Identity overlaps substantially with
existing relational concentrations.
```

### Decision

```text
Decision:
Do not create AI + Identity as an autonomous node.
```

The finding does not automatically determine the decision.

The decision records the reason why the audit acts on the finding in a particular way.

---

## Closed Decisions That Must Be Preserved

The current project contains several decisions that should remain explicitly represented in the shared state.

Examples include:

```text
AI ≠ rhizome
```

```text
Map ≠ territory
```

```text
Classification belongs to the map, not necessarily to the territory.
```

```text
A node is not a theme.
```

```text
A node is not an element.
```

```text
An inter-stem node is not merely interdisciplinary.
```

```text
Connection ≠ propagation.
```

```text
Propagation ≠ linear causality.
```

```text
Causal participation ≠ intention.
```

```text
Complexity ≠ emergence.
```

```text
Multiplicity ≠ horizontality.
```

```text
Technical possibility ≠ historical inevitability.
```

```text
Production ≠ knowledge.
```

```text
Production ≠ evidence.
```

```text
Relevance ≠ authority.
```

```text
Authority ≠ truth.
```

```text
Understanding ≠ functional behavior.
```

```text
Openness ≠ sovereignty.
```

These should be encoded as active Decision Records when they function as methodological constraints on subsequent agents.

---

## Structural Decision Example

```text
id:
D-0008

decision:
Keep Nodes D and E distinct.

basis:
The transversal review identified overlap but also distinct transformations.

evidence:
F-0041
F-0047
F-0063

affected_components:
Node D
Node E
Inter-stem architecture

alternatives_considered:
Merge D and E
Redistribute E into D
Keep D and E distinct

rationale:
D centers on mediation, relevance, authority, and power, while E centers on
production, evaluation, evidence, and attribution. Their adjacency does not
erase the difference in the transformations they make visible.

confidence:
High

status:
active

reversal_condition:
Reopen only if later evidence demonstrates that the two sections perform
the same relational function and that their distinction produces no
meaningful analytical gain.
```

---

## Negative Structural Decision Example

```text
decision:
Do not add a new node.

basis:
The transversal review found that the proposed material is already
functionally represented elsewhere.

rationale:
Adding a node would increase taxonomy without increasing cartographic
visibility.

status:
active
```

Negative decisions are important.

A decision **not to add**, **not to merge**, **not to rewrite**, or **not to classify** is still a decision.

---

## Decision Precedence

When decisions conflict, the audit should resolve them through explicit state transition rather than silent replacement.

Preferred sequence:

```text
Existing Decision
      ↓
New Evidence
      ↓
Finding
      ↓
Reassessment
      ↓
New Decision
      ↓
Old Decision → superseded / reopened
```

Never:

```text
Old Decision
      ↓
silent overwrite
```

---

## Governing Principle

> A decision closes a question provisionally without pretending that the question can never be reopened.

A good Decision Record therefore performs two functions simultaneously:

1. it prevents methodological drift and accidental regression;
2. it preserves the conditions under which reconsideration would be legitimate.

The purpose is not to make the architecture immutable.

It is to make change accountable.
