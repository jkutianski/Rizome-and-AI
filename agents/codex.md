# Codex Adapter

## Purpose

This adapter defines how **Codex** executes the agent-neutral Rizome-and-AI methodology.

Codex must use the existing Skills, workflows, schemas, and shared protocols.

This file does not redefine the methodology.

---

## Architecture

```text
Codex
  │
  ├── AGENTS.md
  │
  ├── workflows/
  │     └── comprehensive-39-round-audit/
  │
  ├── skills/
  │     ├── _shared/
  │     ├── conceptual/
  │     ├── cartographic/
  │     ├── causal/
  │     ├── critical/
  │     ├── structural/
  │     ├── reader/
  │     ├── authorship/
  │     ├── epistemic/
  │     └── synthesis/
  │
  └── schemas/
        ├── finding.md
        ├── audit-state.md
        └── decision-record.md
```

Codex is the execution layer over this structure.

---

# 1. Initialization

Before beginning an audit:

1. identify the source;
2. establish the source version;
3. freeze the source when appropriate;
4. locate the relevant workflow or Skill;
5. read the relevant shared protocols;
6. read the current Audit State, if one exists;
7. identify active Decision Records;
8. identify rejected hypotheses;
9. determine the permitted scope.

Do not begin structural analysis before establishing these constraints.

---

# 2. Repository Discovery

When operating inside the repository, inspect the relevant files rather than assuming their contents.

Prefer:

```text id="0l7f9e"
AGENTS.md
workflows/
skills/
schemas/
```

as the primary methodological sources.

Do not infer repository conventions from filenames alone.

---

# 3. Skill Selection

Use the smallest Skill or combination of Skills capable of answering the requested analytical question.

Do not invoke the entire methodology when a focused Skill is sufficient.

Examples:

```text id="0h8b8d"
"Is this really an inter-stem node?"
→ cartographic/inter-stem-validation
```

```text id="7c1v3n"
"Does this passage imply technological determinism?"
→ critical/technological-determinism
```

```text id="l4wh4v"
"Is this repeated idea redundant?"
→ structural/necessity-redundancy
```

---

# 4. Workflow Execution

For the complete 39-round audit, execute:

```text id="1f0b8a"
workflows/comprehensive-39-round-audit/
```

The workflow is authoritative regarding:

* round order;
* blind-pass conditions;
* transversal review;
* intervention thresholds;
* synthesis;
* completion.

Do not replace the workflow with an improvised sequence.

---

# 5. Context Management

Codex should maintain the distinction between:

```text id="4o2z2u"
source context
methodological context
audit-state context
current Skill context
```

Do not allow accumulated context to silently alter blind-pass conditions.

When context becomes too large, preserve state through explicit records rather than relying on conversational memory.

---

# 6. State Persistence

When a persistent audit state is available, update it according to:

```text id="7n0v7b"
schemas/audit-state.md
```

Findings must conform to:

```text id="9xy9wt"
schemas/finding.md
```

Decisions must conform to:

```text id="8nd6rq"
schemas/decision-record.md
```

Never store a decision as if it were merely a finding.

---

# 7. File Operations

When modifying repository files:

* preserve existing directory structure;
* avoid unrelated modifications;
* do not overwrite source material unless explicitly authorized;
* keep generated artifacts separate from source material;
* preserve audit history.

A methodological audit must not accidentally become a source-editing operation.

---

# 8. Analysis Before Editing

Default Codex behavior:

```text id="f6n0xe"
READ
→ ANALYZE
→ RECORD
→ RECOMMEND
→ DECIDE
→ EDIT
```

Editing should occur only when explicitly authorized or when the workflow enters an intervention phase.

Do not rewrite a passage merely because a cleaner formulation is possible.

---

# 9. Blind Passes

For blind rounds:

```text id="q2h6x7"
Do not consult:
- previous interpretations
- previous findings
- author explanations
- hidden project history
- prior node classifications
```

Use only the information permitted by the workflow.

After the blind pass, integrate its results into the shared state.

---

# 10. Repository Safety

Before structural changes:

1. inspect current state;
2. identify affected files;
3. check whether a Decision Record already governs the issue;
4. preserve previous state;
5. make the smallest justified change.

Do not create new Skills or nodes simply because an analytical gap feels inconvenient.

---

# 11. Final Reporting

Codex should report results in a form compatible with the common schemas.

At minimum:

```text id="r4ymk1"
Skill
Scope
Findings
Decisions
State Changes
Unresolved Questions
Recommendations
Confidence
```

For complete audits, use the mandatory 14-part final report defined by the workflow.

---

# 12. Codex-Specific Principle

Codex may use repository inspection, file operations, version control, and other execution capabilities to improve traceability.

Those capabilities do not authorize methodological changes.

> Codex adapts the execution environment; it does not adapt the conceptual framework.
