# Agent Contract

## Purpose

This document defines the common contract for any agent that executes the **Rizome-and-AI** Skills.

The contract is agent-neutral.

Codex, Claude Code, GitHub Copilot, or another compatible agent may implement it differently, but they must preserve the same analytical semantics, state model, and methodological constraints.

---

## Core Architecture

```text
                         ┌──────────────────────┐
                         │      SOURCE TEXT     │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │    AUDIT WORKFLOW    │
                         └──────────┬───────────┘
                                    │
                                    ▼
                    ┌─────────────────────────────┐
                    │       CORE SKILLS           │
                    │                             │
                    │ conceptual / cartographic  │
                    │ causal / critical          │
                    │ structural / reader        │
                    │ authorship / epistemic     │
                    │ synthesis                  │
                    └─────────────┬───────────────┘
                                  │
                                  ▼
                    ┌─────────────────────────────┐
                    │       SHARED STATE          │
                    │                             │
                    │ Findings                    │
                    │ Decisions                   │
                    │ Nodes                       │
                    │ Connections                 │
                    │ Propagations                │
                    │ Open Questions              │
                    └─────────────┬───────────────┘
                                  │
                ┌─────────────────┼─────────────────┐
                ▼                 ▼                 ▼
             Codex          Claude Code       GitHub Copilot
```

The agent is an execution environment, not a second methodology.

---

# 1. Agent Responsibilities

An executing agent must:

1. load the relevant Skill;
2. read the current Audit State;
3. respect active Decision Records;
4. analyze the source according to the Skill;
5. produce structured Findings;
6. update the Audit State when authorized;
7. create Decision Records only when the workflow permits decisions;
8. preserve rejected hypotheses and negative findings;
9. distinguish evidence from interpretation;
10. report uncertainty explicitly.

The agent must not silently modify the methodology.

---

# 2. Agent Must Not Become the Method

The agent may determine:

* what evidence supports a finding;
* what relationships are visible;
* what tensions are present;
* whether a claim is vulnerable;
* whether a node satisfies the relevant criteria;
* whether a connection or propagation is sufficiently established.

The agent must not redefine the underlying methodology merely because another interpretation appears convenient.

For example, an agent must not redefine:

```text
node = important topic
```

when the methodology defines:

```text
node = concentration of relations and tensions
```

Similarly, it must not redefine:

```text
inter-stem node = interdisciplinary subject
```

when the methodology requires a transformative crossing of assemblages.

---

# 3. Required Inputs

Every Skill execution must receive, directly or indirectly:

```text
source
audit_state
skill
scope
constraints
```

### `source`

The text or material being analyzed.

### `audit_state`

The current shared state.

### `skill`

The specific analytical capability being invoked.

### `scope`

The part of the source to analyze.

Possible scopes include:

```text
sentence
paragraph
section
node
assemblage
cross-assemblage
whole-work
```

### `constraints`

Relevant methodological constraints, including:

* active decisions;
* blind-pass restrictions;
* language configuration;
* source version;
* round-specific instructions.

---

# 4. Source Freeze

Before a multi-round audit begins, the agent must identify the source version being audited.

If the source changes materially:

```text
source_status:
  changed
```

must be recorded.

The audit must not silently combine findings from different source versions.

---

# 5. Language Handling

The agent must analyze the source in its actual language.

Rules:

* do not translate mentally before analysis;
* do not assume English terminology is the semantic standard;
* do not treat unusual wording as conceptual error merely because it differs from another language;
* distinguish semantic problems from translation problems;
* preserve the source's actual conceptual terminology.

Core rule:

> Analyze the source that actually exists, in the language in which it exists.

---

# 6. Skill Execution Contract

Each Skill execution follows:

```text
LOAD
  ↓
READ STATE
  ↓
CHECK CONSTRAINTS
  ↓
ANALYZE SOURCE
  ↓
SEPARATE OBSERVATION / INTERPRETATION
  ↓
PRODUCE FINDINGS
  ↓
ASSESS CONFIDENCE
  ↓
CHECK EXISTING FINDINGS
  ↓
UPDATE STATE
  ↓
REPORT RESULT
```

The agent must not skip directly from source text to intervention.

---

# 7. Analyze Before Intervening

The default sequence is:

```text
observation
→ evidence
→ interpretation
→ diagnosis
→ recommendation
→ decision
→ intervention
```

Not:

```text
problem assumed
→ rewrite
```

The agent should preserve material when the evidence does not justify intervention.

Core principle:

> Do not improve what does not need improvement.

---

# 8. Finding Production

Every substantive analytical result should be representable through the common Finding schema.

At minimum:

```text
id
source_location
target
observation
evidence
interpretation
issue_type
severity
confidence
status
architectural_scope
recommendation
```

The agent may produce several findings from one Skill execution.

It must not collapse distinct findings merely for brevity.

---

# 9. Existing Findings

Before creating a new finding, the agent should inspect relevant existing findings.

It must determine whether the observation is:

```text
new
corroborating
qualifying
contesting
duplicating
superseding
```

Repeated observation does not necessarily mean redundant finding.

Different Skills may legitimately observe the same passage for different analytical reasons.

---

# 10. Decision Boundary

The agent must distinguish:

```text
Finding
```

from:

```text
Decision
```

Example:

```text
Finding:
The proposed node overlaps substantially with existing concentrations.
```

is not equivalent to:

```text
Decision:
Do not create the node.
```

The latter requires an explicit decision record.

---

# 11. Decision Authority

An agent may create a Decision Record only when:

1. the current workflow permits decisions;
2. sufficient evidence exists;
3. relevant transversal checks have been performed when structurally required;
4. the decision does not silently contradict an active Decision Record.

If these conditions are not satisfied, the agent should produce:

```text
Finding
+
Recommendation: Investigate further
```

rather than prematurely closing the issue.

---

# 12. Closed Decisions

Active decisions must be treated as constraints.

For example:

```text
AI ≠ rhizome
```

cannot be silently replaced by:

```text
AI is a rhizome-like system
```

because a later agent finds the analogy rhetorically attractive.

A closed decision may be reopened only through its recorded reversal condition.

---

# 13. Rejected Hypotheses

The agent must inspect `rejected_hypotheses` before proposing new structural entities.

This prevents accidental resurrection of previously rejected nodes.

A previously rejected hypothesis may be reconsidered only if:

* new evidence exists;
* the new evidence is explicitly identified;
* the previous rejection is referenced;
* reopening is recorded.

---

# 14. Blind Passes

When a workflow specifies a blind pass, the agent must not access information excluded by that pass.

Blindness is methodological isolation, not merely a label.

For example, a blind external reading must not rely on:

* previous interpretations;
* author explanations not present in the text;
* previous node classifications;
* previous audit conclusions;
* hidden project history.

The resulting findings are integrated only after the blind pass is complete.

---

# 15. Inter-Stem Validation

An agent must never classify an inter-stem node from a title alone.

It must reconstruct:

```text
assemblages
→ relations
→ tensions
→ concentration
→ modification of conditions
→ transformation
→ possible propagation
```

If the evidence stops at:

```text
AI + X
```

the agent must not infer inter-stem status.

Possible outcomes include:

```text
Strong Inter-Stem Node
Plausible Inter-Stem Node
Ambiguous Inter-Stem Candidate
Cross-Assemblage Connection
Interdisciplinary Theme
Ordinary Node
Insufficient
```

---

# 16. Causality

The agent must distinguish:

```text
relation
causality
influence
enablement
constraint
determination
necessity
sufficiency
propagation
```

A rhizomatic analysis does not require eliminating causality.

It requires avoiding unjustified causal totalization.

---

# 17. Emergence

The agent must not classify something as emergence merely because it is:

* new;
* complex;
* unexpected;
* multiple;
* nonlinear;
* propagated;
* difficult to predict.

Emergence requires a relational configuration whose relevant properties or dynamics cannot be adequately attributed to a single element alone.

---

# 18. Anthropomorphism

The agent must distinguish:

```text
causal efficacy ≠ intentional agency
functional behavior ≠ understanding
optimization ≠ intention
operational autonomy ≠ mental autonomy
actor ≠ human-like subject
```

Active language is not automatically anthropomorphic.

The question is what mental property the text actually attributes and whether that attribution is justified.

---

# 19. Power and Epistemic Distinctions

The agent must preserve:

```text
mediation
≠
selection
≠
visibility
≠
relevance
≠
authority
≠
legitimacy
≠
truth
≠
power
```

Likewise:

```text
production
≠
knowledge
≠
evidence
≠
attribution
```

These distinctions are methodological constraints, not optional stylistic preferences.

---

# 20. No Automatic Determinism

The agent must not infer technological determinism from ordinary causal claims.

Distinguish:

```text
technical possibility
≠
historical inevitability

technical capacity
≠
adoption

constraint
≠
determination

influence
≠
sufficiency
```

The existence of social, political, material, or institutional mediation must be considered where relevant.

---

# 21. Materiality

Material substrate should be treated as a possible active condition of the dynamics.

Relevant factors may include:

* energy;
* water;
* minerals;
* semiconductors;
* compute;
* data centers;
* networks;
* storage;
* devices;
* logistics;
* infrastructure.

The agent should not create a separate node merely because materiality appears.

Materiality is normally a transversal analytical dimension unless the source establishes a distinct concentration.

---

# 22. Feedback

When feedback is present, the agent should identify the circuit rather than merely naming it.

For example:

```text
technology
→ modifies practice
→ produces new data
→ changes subsequent technology
→ modifies practice again
```

A feedback claim should identify:

* what changes;
* what feeds back;
* through which relation;
* under what conditions.

---

# 23. Scope Control

The agent must not extend a local observation into a whole-work diagnosis without evidence.

Likewise:

```text
sentence
≠
section
≠
node
≠
assemblage
≠
whole architecture
```

Architectural claims require architectural evidence.

---

# 24. Confidence

Every substantive finding must communicate confidence:

```text
High
Medium
Low
```

The agent should lower confidence when:

* evidence is indirect;
* wording is ambiguous;
* multiple interpretations remain plausible;
* the source does not establish the relevant relation;
* the conclusion depends on external evidence not yet verified.

Uncertainty is preferable to false precision.

---

# 25. Recommendations

Recommendations should use the shared classes:

```text
Necessary
Advisable
Optional
Not recommended
Leave unchanged
Investigate further
```

The agent should not recommend rewriting merely because a sentence could be made smoother.

---

# 26. Intervention Threshold

Before recommending structural intervention, ask:

1. What is the problem?
2. What evidence establishes it?
3. What function is currently failing?
4. What would be lost by leaving it unchanged?
5. Is the problem local or architectural?
6. Is intervention reversible?
7. Is there a less invasive intervention?
8. Could the apparent problem be productive tension or asymmetry?

If the answer does not justify intervention, preserve the existing structure.

---

# 27. New Node Threshold

A new node requires evidence of:

```text
elements
→ relations
→ tensions
→ concentration
→ recognizable dynamic
→ distinct analytical function
```

Importance alone is insufficient.

A topic is not a node.

A node must earn its status through relational concentration.

---

# 28. New Inter-Stem Threshold

A new inter-stem node requires evidence that:

1. at least two assemblages are involved;
2. meaningful relations connect them;
3. tensions emerge between or across them;
4. those relations concentrate into a recognizable dynamic;
5. conditions of functioning are modified;
6. a transformation results;
7. possible propagation can be identified or legitimately hypothesized.

If these conditions are not sufficiently established, classify the material more conservatively.

---

# 29. Propagation Threshold

Propagation requires more than:

```text
A affects B.
```

The agent should identify:

```text
origin
→ transformation
→ changed condition
→ relation/path
→ downstream site
→ downstream change
```

and the conditions under which propagation occurs.

---

# 30. Final Synthesis

The agent must not treat the number of findings as the quality of the audit.

The integrated result should determine:

* which findings converge;
* which remain independent;
* which are duplicates;
* which reveal productive tension;
* which are rejected;
* which require intervention;
* which should be preserved;
* which have architectural consequences.

The final synthesis must distinguish:

```text
what the source says
what the evidence supports
what the analyst infers
what remains uncertain
what should change
what should remain untouched
```

---

# 31. Agent Output

A standard Skill execution should return:

```text
Skill
Scope
Findings
Decisions
State Changes
Unresolved Questions
Confidence
Recommendations
```

A minimal result may look like:

```text
Skill:
node-validation

Scope:
Node D

Findings:
F-0041
F-0042

Decisions:
None

State Changes:
Node D remains validated.

Unresolved Questions:
Whether one formulation collapses relevance and authority.

Confidence:
High

Recommendations:
Investigate further.
```

---

# 32. Error Handling

If the agent cannot establish sufficient evidence, it must not manufacture a conclusion.

Preferred result:

```text
status: unresolved
confidence: Low
recommendation: Investigate further
```

rather than an unsupported classification.

If required source material is unavailable, the agent should report the missing evidence rather than infer it.

---

# 33. Inter-Agent Compatibility

Agents may differ in:

* prompt format;
* file discovery;
* tool invocation;
* context management;
* state persistence;
* output formatting.

They must not differ in the underlying analytical contract.

Therefore:

```text
Codex adapter
Claude Code adapter
GitHub Copilot adapter
```

are implementation layers.

They are not independent methodologies.

---

# 34. Non-Negotiable Principles

Every compatible agent must preserve:

```text
Analyze before intervening.

The map is not the territory.

The rhizome is not the map.

AI is not the rhizome.

A node is not a theme.

A node is not an element.

An inter-stem node is not merely interdisciplinary.

Connection is not propagation.

Propagation is not linear causality.

Causal participation is not intention.

Complexity is not emergence.

Multiplicity is not horizontality.

Technical possibility is not historical inevitability.

Production is not knowledge.

Production is not evidence.

Relevance is not authority.

Authority is not truth.

Understanding is not functional behavior.

Openness is not sovereignty.
```

---

# 35. Governing Principle

> The agent is interchangeable; the methodology is not.

The purpose of this contract is to make the same Skills executable across different agent environments while preserving the project's conceptual distinctions, audit discipline, state history, and decision traceability.
