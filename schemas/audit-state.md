# Audit State Schema

## Purpose

The **Audit State** is the persistent state of an ongoing audit.

It allows multiple Skills, rounds, and agents to work on the same source without losing previous findings, decisions, rejected hypotheses, unresolved questions, or architectural history.

The Audit State is **not a final conclusion**.

It is the current state of the investigation.

---

## Core Principle

> The audit state records what has been examined, what has been established, what remains uncertain, and what has been decided without pretending that the investigation has stopped changing.

Later rounds may qualify earlier findings.

They must not silently erase audit history.

---

## Core Structure

```text
Audit State
├── source
├── language
├── source_status
├── current_round
├── completed_rounds
├── findings
├── unresolved_questions
├── validated_nodes
├── candidate_nodes
├── inter_stem_candidates
├── connections
├── propagations
├── contradictions
├── preserved_decisions
├── rejected_hypotheses
├── intervention_candidates
└── final_synthesis
```

---

## `source`

Identifies the source being audited.

May include:

```text
name
version
path
hash
date
```

The source should be frozen before the 39-round audit begins.

---

## `language`

Records the language configuration of the source.

Examples:

```text
English
```

```text
Spanish
```

```text
Mixed: Spanish / English
```

The audit must analyze the source in the language in which it actually exists.

> Analyze the source that actually exists, in the language in which it exists. Do not analyze an imagined translation.

---

## `source_status`

Allowed values:

```text
unfrozen
frozen
changed
refrozen
```

If the source changes during an audit, the change must be recorded.

A new source version should not silently inherit conclusions from an earlier source.

---

## `current_round`

The current audit round.

Example:

```text
17
```

The 39-round workflow must preserve the distinction between:

* round number;
* Skill used;
* findings generated;
* decisions produced.

A round is a methodological stage, not necessarily a single Skill.

---

## `completed_rounds`

List of completed rounds.

Example:

```text
1
2
3
4
5
```

Completion should mean that the round's required analytical task was actually performed.

---

## `findings`

Registry of Finding objects.

Example:

```text
F-0001
F-0002
F-0003
```

The full Finding data should remain accessible through the common Finding schema.

Findings may be:

```text
open
corroborated
contested
qualified
rejected
unresolved
superseded
```

Do not delete rejected or superseded findings from the history.

---

## `unresolved_questions`

Questions that remain genuinely open.

Examples:

```text
Does the transition between Nodes D and E establish a new relation
or repeat an existing epistemic distinction?
```

```text
Is the transformation identified in Node B sufficient to justify
inter-stem status?
```

Unresolved questions are not failures.

They are part of the audit state when the evidence is insufficient for closure.

---

## `validated_nodes`

Nodes that have passed the relevant validation threshold.

For each node, preserve at least:

```text
node_id
name
assemblage
relational concentration
core tensions
distinct function
validation_basis
confidence
```

A node should not be considered validated merely because it has a section title.

---

## `candidate_nodes`

Potential nodes that have not yet passed the validation threshold.

Examples:

```text
candidate
ambiguous
needs_transversal_review
```

Candidate status prevents premature architectural expansion.

---

## `inter_stem_candidates`

Potential inter-stem nodes.

Each candidate should record the strict sequence:

```text
assemblages
↓
relations
↓
tensions
↓
concentration
↓
modification of conditions
↓
transformation
↓
possible propagation
```

Allowed status:

```text
Strong Inter-Stem Node
Plausible Inter-Stem Node
Ambiguous Inter-Stem Candidate
Cross-Assemblage Connection
Interdisciplinary Theme
Ordinary Node
Insufficient
```

Titles alone cannot promote a candidate to inter-stem status.

---

## `connections`

Validated or proposed relations between components.

A connection should identify:

```text
source
target
relation
evidence
function
confidence
status
```

Possible relations include:

```text
dependency
cooperation
competition
transfer
reuse
adaptation
conflict
complementarity
substitution
restriction
feedback
transformation
```

A connection is not automatically causal.

---

## `propagations`

Records transformations that extend through relations.

Each propagation should identify:

```text
origin
transformation
changed_condition
path_or_relation
downstream_site
downstream_change
conditions
confidence
status
```

A statement that "AI affects X" is not sufficient to establish propagation.

---

## `contradictions`

Records possible contradictions.

Each should distinguish:

```text
logical contradiction
conceptual contradiction
methodological contradiction
structural contradiction
argumentative contradiction
semantic contradiction
productive tension
contextual difference
development
```

Not every tension is a contradiction.

---

## `preserved_decisions`

Records decisions that must remain active throughout the audit.

Examples:

```text
AI is not the rhizome.
```

```text
The map is not the territory.
```

```text
D and E remain distinct.
```

```text
A–E do not constitute a causal sequence.
```

Preserved decisions act as constraints against accidental conceptual regression.

---

## `rejected_hypotheses`

Records hypotheses explicitly tested and rejected.

Examples:

```text
AI + Identity as autonomous node
```

```text
AI + Social Acceleration as autonomous node
```

```text
AI + Desires and Aspirations as autonomous node
```

```text
D and E should be merged
```

Rejected hypotheses must remain visible.

This is essential because a later agent must not interpret absence as unfinished work and resurrect an already rejected structure without new evidence.

---

## `intervention_candidates`

Potential changes to the source.

Each candidate should record:

```text
target
problem
proposed intervention
basis
severity
confidence
reversibility
status
```

Possible statuses:

```text
candidate
accepted
rejected
deferred
implemented
```

No intervention should be implemented merely because it appears in this field.

---

## `final_synthesis`

Produced only during the integrated synthesis phase.

It should summarize:

```text
general_diagnosis
current_architecture
structural_strengths
real_problems
redundancies
nodes
connections
propagations
contradictions
philosophical_risks
semantic_and_stylistic_risks
decisions_to_preserve
recommended_interventions
final_verdict
```

The final synthesis integrates the state.

It does not replace the state.

---

## State Transition Principle

The Audit State evolves monotonically in **history**, not necessarily in **conclusion**.

For example:

```text
Candidate Node
      ↓
Validated Node
      ↓
Qualified
      ↓
Rejected
```

The previous states remain historically recoverable.

Similarly:

```text
Finding
   ↓
Corroborated
   ↓
Qualified
```

does not mean the original finding disappears.

---

## Multi-Agent Rule

When multiple agents operate on the same audit:

```text
Agent A
   ↓
Finding / Decision
   ↓
Shared Audit State
   ↓
Agent B
   ↓
Finding / Qualification
   ↓
Shared Audit State
```

Agents must read relevant existing state before producing new structural conclusions.

They must not behave as if they are conducting a completely independent audit unless the workflow explicitly requests a blind pass.

---

## Blind-Pass Exception

Rounds explicitly designated as blind must receive only the information allowed by the workflow.

For the 39-round audit, blind passes include:

```text
Round 10
Round 20
Round 25
```

Their isolation is methodological.

Their results are integrated afterward.

---

## No Silent Deletion

The following must never be silently deleted:

* findings;
* rejected hypotheses;
* preserved decisions;
* unresolved questions;
* previous node classifications;
* previous inter-stem classifications;
* source versions.

If something changes, record the transition.

---

## Governing Principle

> The Audit State is the memory of the investigation.

It prevents the audit from repeatedly rediscovering the same questions, silently reversing decisions, resurrecting rejected structures, or confusing a later qualification with the disappearance of an earlier observation.
