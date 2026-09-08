# Skill Contract

## Purpose

This document defines the common structural contract for every analytical Skill in the Rizome-and-AI repository.

The contract is **agent-neutral**.

A Skill may be executed by Codex, Claude Code, GitHub Copilot, or another compatible agent without changing its analytical methodology.

The purpose of this contract is interoperability, not methodological standardization beyond the requirements necessary for consistent execution.

---

## 1. Skill Identity

Every Skill must have:

* a unique directory;
* a `SKILL.md` file;
* a clear analytical purpose;
* a defined scope;
* explicit inputs;
* explicit outputs;
* stated dependencies when applicable.

The Skill name should identify the analytical capability rather than a particular text, author, agent, or project phase.

---

## 2. Purpose

Each Skill must state what it is designed to analyze.

The purpose should answer:

> What analytical problem does this Skill address?

A Skill should perform one coherent analytical function.

It should not become a general-purpose audit containing unrelated capabilities.

---

## 3. Scope

Each Skill must define its analytical scope.

Scope may be:

* passage;
* section;
* node;
* assemblage;
* inter-stem relation;
* whole work;
* workflow;
* methodology.

The Skill must not silently expand beyond its declared scope.

Cross-scope findings are permitted when the evidence requires them, but the expansion must be made explicit.

---

## 4. Inputs

A Skill may receive:

```text
source
scope
audit_state
constraints
previous_findings
relevant_decisions
```

Not every Skill requires every input.

The Skill must state which inputs are:

* required;
* optional;
* prohibited or irrelevant.

### Minimum conceptual input

Every analytical Skill requires access to the source material relevant to its scope.

A Skill must not analyze an imagined, translated, summarized, or reconstructed version of the source when the actual source is available.

---

## 5. Shared Protocols

Skills should load only the shared protocols relevant to their task.

Available shared protocols are:

```text
skills/_shared/
├── analytical-discipline.md
├── evidence-and-citation.md
├── language-agnostic-analysis.md
└── output-protocol.md
```

Shared protocols define cross-Skill behavior.

They do not replace the analytical procedure of an individual Skill.

---

## 6. Dependencies

When a Skill depends conceptually or procedurally on another Skill, the dependency should be explicit.

Example:

```text
inter-stem-validation
    depends on
node-validation
```

A dependency does not mean that the dependent Skill must mechanically execute the other Skill.

It means that its analysis presupposes concepts, distinctions, or findings established there.

Dependencies should be kept minimal.

Circular dependencies should be avoided.

---

## 7. Analytical Procedure

Every Skill must define how the analysis is performed.

The procedure should distinguish, where applicable:

```text
observation
    ↓
evidence
    ↓
interpretation
    ↓
diagnosis
    ↓
recommendation
```

The procedure must not require a predetermined conclusion.

A Skill evaluates whether its target condition is present.

It does not assume that the condition exists merely because the Skill was invoked.

---

## 8. Findings

A Skill produces analytical findings using the common Finding contract:

```text
schemas/finding.md
```

A finding should distinguish:

* observation;
* evidence;
* interpretation;
* issue type;
* severity;
* confidence;
* architectural scope;
* recommendation.

A Skill must not encode a final methodological decision as though it were merely a finding.

---

## 9. Decisions

A Skill may provide evidence relevant to a decision.

It should not silently convert its own finding into a repository-wide decision.

Decisions are represented by:

```text
schemas/decision-record.md
```

Examples include:

* preserve;
* merge;
* eliminate;
* reformulate;
* reject;
* reopen;
* defer.

When a decision is required, its basis must remain traceable to findings and evidence.

---

## 10. Audit State

When executed within an ongoing audit, a Skill reads and updates:

```text
schemas/audit-state.md
```

The Skill must preserve:

* previous findings;
* unresolved questions;
* rejected hypotheses;
* preserved decisions;
* validated structures;
* candidate structures.

A Skill must not silently erase previous analytical history.

---

## 11. Negative Findings

A Skill must be capable of producing a negative result.

Examples:

```text
No contradiction identified.
No propagation demonstrated.
No inter-stem transformation established.
No sufficient evidence for emergence.
No conceptual inconsistency detected.
```

Negative findings are valid analytical outputs.

The absence of a finding is not evidence that the Skill failed.

---

## 12. Uncertainty

Every substantive finding should carry an explicit confidence level:

```text
High
Medium
Low
```

Confidence refers to the strength of the analytical basis, not the importance of the finding.

A high-severity finding may have low confidence.

A low-severity finding may have high confidence.

These dimensions must remain separate.

---

## 13. Language

Skills are language-agnostic unless explicitly specified otherwise.

The source may be:

* English;
* Spanish;
* another language;
* multilingual.

The Skill must analyze the source in the language in which it exists.

It must not:

* silently translate the source;
* judge a formulation by how it would sound in another language;
* infer conceptual weakness from linguistic unfamiliarity.

When wording is analytically relevant, preserve the original wording.

---

## 14. Evidence

A Skill must distinguish among:

```text
source evidence
analytical inference
external evidence
```

External evidence should be introduced only when required by the analytical task.

A Skill must not:

* invent citations;
* invent sources;
* fabricate empirical support;
* attribute intentions without evidence;
* convert inference into source evidence.

See:

```text
skills/_shared/evidence-and-citation.md
```

---

## 15. Conceptual Restraint

A Skill must not infer categories solely from:

* titles;
* headings;
* keywords;
* adjacency;
* disciplinary labels;
* the presence of AI;
* apparent conceptual similarity.

For example:

```text
AI + X
```

does not by itself establish:

* an inter-stem node;
* a causal relation;
* propagation;
* emergence;
* a new assemblage.

The analytical procedure must establish the relevant relational structure.

---

## 16. Editing Boundary

A Skill is analytical unless explicitly designated otherwise.

Analytical Skills must not modify source material.

They may recommend:

* clarification;
* restructuring;
* deletion;
* preservation;
* expansion;
* qualification;
* reformulation.

Actual editing belongs to a separate authorized phase.

---

## 17. Agent Independence

A Skill must not contain instructions specific to:

* Codex;
* Claude Code;
* GitHub Copilot;
* a particular model;
* a particular API;
* a particular operating system.

Agent-specific behavior belongs in:

```text
agents/
```

and repository execution instructions.

The Skill defines **what analysis to perform**.

The agent adapter defines **how that analysis is executed in a particular environment**.

---

## 18. Workflow Independence

A Skill must not assume that it is always executed as part of the 39-round audit.

It must be usable independently when its required inputs are available.

The comprehensive workflow determines:

* when the Skill is invoked;
* what precedes it;
* what follows it;
* how its findings contribute to the whole audit.

Therefore:

```text
Skill
=
analytical capability

Workflow
=
orchestration
```

---

## 19. Blind Analysis

When a Skill is invoked as part of a designated blind pass, it must respect the isolation conditions established by the workflow.

It must not import conclusions from previous rounds merely because those conclusions are available in persistent state.

Blind analysis may produce new findings that later become part of the integrated state.

---

## 20. Structural Intervention Threshold

A Skill should recommend structural intervention only when the evidence supports it.

Possible recommendations include:

```text
Necessary
Advisable
Optional
Not recommended
Leave unchanged
Investigate further
```

The Skill must not treat structural change as inherently preferable.

---

## 21. Compatibility with the Finding Contract

Every substantive analytical output must be representable through:

```text
schemas/finding.md
```

At minimum:

```text
finding_id
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

If a Skill produces information that cannot be represented by this contract, the Skill must explicitly document why.

---

## 22. Compatibility with Audit State

A Skill operating inside an audit should make clear which state components it may:

* read;
* add;
* modify;
* qualify;
* mark as unresolved;
* mark as rejected;
* supersede.

It must not silently rewrite the history of the investigation.

---

## 23. Compatibility with Decision Records

When a Skill contributes to a methodological or structural decision, the relationship should remain traceable:

```text
source
  ↓
finding
  ↓
synthesis
  ↓
decision
```

The inverse must also be possible:

```text
decision
  ↓
basis
  ↓
findings
  ↓
source evidence
```

This creates an auditable chain between evidence and structural decisions.

---

## 24. Completion Condition

A Skill execution is complete when:

1. the declared scope has been analyzed;
2. relevant evidence has been identified;
3. observations and interpretations have been separated;
4. findings have been classified;
5. confidence has been assessed;
6. relevant existing findings have been considered;
7. required state updates have been identified;
8. recommendations, if any, have been stated;
9. no unsupported conclusion has been introduced.

Completion does not require finding a problem.

A valid result may be:

> No intervention warranted.

---

## 25. Interoperability Principle

All Skills should conform to the same basic contract while remaining analytically distinct.

The goal is not to make every Skill structurally identical in content.

The goal is to make their **inputs, outputs, evidence discipline, state interaction, and agent boundaries mutually intelligible**.

> **Different analytical capabilities; one interoperable methodological language.**
