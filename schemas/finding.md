# Finding Schema

## Purpose

A **Finding** records an observation or diagnosis produced during an audit.

The Finding schema is agent-neutral. It must be usable by Codex, Claude Code, GitHub Copilot, or another compatible agent without changing its conceptual meaning.

A Finding is **not a decision**.

A Finding describes something the audit has observed, inferred, or diagnosed. A later Decision may accept, qualify, reject, preserve, merge, separate, or act upon that finding.

---

## Core Principle

> A finding records what the audit has established or made visible; it does not silently decide what should be done about it.

The distinction between **observation**, **interpretation**, and **decision** must remain explicit.

---

## Required Structure

```text
Finding
├── id
├── source_location
├── target
├── observation
├── evidence
├── interpretation
├── issue_type
├── severity
├── confidence
├── status
├── architectural_scope
└── recommendation
```

---

## Fields

### `id`

Unique identifier for the finding.

Format is implementation-dependent, but it must remain stable across rounds and agents.

Example:

```text
F-0037
```

---

### `source_location`

Where in the source the finding originates.

May contain:

* section;
* paragraph;
* heading;
* sentence;
* node;
* assemblage;
* round;
* file and line range, when available.

Example:

```text
Node D — paragraph 4
```

A finding should be traceable to its evidential basis whenever possible.

---

### `target`

The specific object being evaluated.

Examples:

```text
Node D
```

```text
The claim that relevance produces authority
```

```text
Transition between assemblages
```

```text
Ending section
```

---

### `observation`

What is directly observable in the source.

This field must avoid unnecessary interpretation.

Example:

```text
The text moves from visibility to relevance and then immediately describes the resulting condition as authority.
```

---

### `evidence`

The evidence supporting the finding.

Evidence may be:

* direct textual evidence;
* structural evidence;
* cross-sectional evidence;
* methodological evidence;
* external evidence, when permitted by the audit protocol.

When possible, include the relevant quotation, location, or reference.

Do not invent evidence.

Evidence strength should be distinguished where useful:

```text
Direct
Strong inferential
Weak inferential
Insufficient
```

---

### `interpretation`

The analytical meaning assigned to the observation.

Example:

```text
The formulation risks collapsing relevance and authority unless the transition between them is explicitly relational rather than automatic.
```

Interpretation is not equivalent to observation.

---

### `issue_type`

The primary type of issue.

Allowed values:

```text
conceptual
methodological
structural
argumentative
semantic
evidential
stylistic
cartographic
causal
epistemic
authorship
reader
none
```

Multiple types may be recorded when necessary, but a primary type should be identifiable.

---

### `severity`

Use the common audit severity scale:

```text
A — Critical
B — Major
C — Moderate
D — Minor
E — Non-problematic / observation only
```

Interpretation:

* **A — Critical:** threatens the coherence or validity of a central part of the work.
* **B — Major:** materially affects an important claim, node, relation, or structural function.
* **C — Moderate:** meaningful issue with limited architectural consequences.
* **D — Minor:** localized issue that does not materially threaten the argument.
* **E — Non-problematic / observation only:** useful observation, productive tension, or issue that does not require intervention.

Severity must not be inflated merely because a finding is interesting.

---

### `confidence`

Confidence in the finding:

```text
High
Medium
Low
```

Confidence concerns the analyst's basis for the finding, not the severity of the underlying issue.

A low-confidence finding may still be important enough to investigate.

---

### `status`

Current epistemic status of the finding.

Allowed values:

```text
open
corroborated
contested
qualified
rejected
unresolved
superseded
```

Status changes must not erase the previous state.

---

### `architectural_scope`

Where the finding operates.

Allowed values:

```text
local
node
inter-stem
assemblage
cross-assemblage
whole-work
methodology
workflow
```

A finding may have more than one scope when explicitly justified.

---

### `recommendation`

Recommended action, if any.

Allowed values:

```text
Necessary
Advisable
Optional
Not recommended
Leave unchanged
Investigate further
```

A recommendation is not itself a decision.

For example:

```text
Finding:
Node D risks collapsing relevance and authority.

Recommendation:
Investigate further.
```

A later decision may be:

```text
Decision:
Do not merge relevance and authority; preserve the distinction.
```

---

## Finding Lifecycle

A finding may evolve through the audit:

```text
observed
    ↓
interpreted
    ↓
corroborated / contested
    ↓
qualified / rejected / unresolved
    ↓
integrated into decision or synthesis
```

A later round may qualify an earlier finding without invalidating the fact that the earlier observation occurred.

---

## Cross-Agent Rule

Different agents may produce different findings about the same source.

They must not silently overwrite one another.

Instead:

```text
F-0012
F-0048
F-0071
```

may all refer to the same target while preserving their independent evidence and interpretations.

The integrated audit determines whether they represent:

* independent problems;
* different manifestations of one problem;
* productive tension;
* redundancy;
* contradictory interpretations;
* or no actual problem.

---

## Negative Findings

The absence of a problem is also meaningful.

Examples:

```text
No evidence that Node C is being treated as technologically deterministic.
```

```text
The transition between D and E does not establish conceptual equivalence.
```

```text
The text does not provide sufficient evidence to classify this section as an inter-stem node.
```

Negative findings should be recorded when they prevent later agents from incorrectly reopening settled questions.

---

## What a Finding Must Not Do

A Finding must not:

* silently rewrite the source;
* invent evidence;
* infer an inter-stem node from a title alone;
* treat importance as proof of node status;
* convert every connection into causality;
* convert every novelty into emergence;
* convert every AI action into intention;
* treat disagreement as contradiction;
* turn stylistic preference into conceptual criticism;
* turn language difference into philosophical error;
* silently make a structural decision.

---

## Minimal Example

```text
id: F-0017

source_location:
  Node D, paragraph 3

target:
  Relation between relevance and authority

observation:
  The text places relevance immediately before authority without explicitly
  distinguishing the mechanisms connecting them.

evidence:
  Direct textual evidence.

interpretation:
  The passage may be read as implying that relevance automatically produces
  authority.

issue_type:
  conceptual

severity:
  C — Moderate

confidence:
  Medium

status:
  open

architectural_scope:
  node

recommendation:
  Investigate further
```

---

## Governing Principle

> The Finding makes the audit traceable. It records what was seen, what supports the observation, what was inferred, and how certain that inference is.

It must never conceal the transition from evidence to interpretation.
