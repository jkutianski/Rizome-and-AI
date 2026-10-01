# GitHub Copilot Adapter

## Purpose

This adapter defines how **GitHub Copilot** executes the agent-neutral Rizome-and-AI methodology.

Copilot must use the same core Skills, workflows, schemas, and methodological constraints as every other compatible agent.

This adapter does not create a separate Copilot methodology.

---

## Architecture

```text id="v6p1q8"
GitHub Copilot
       │
       ├── Repository instructions
       │
       ├── workflows/
       │
       ├── skills/
       │
       └── schemas/
```

The repository is the shared source of truth.

---

# 1. Initialization

Before analytical execution:

1. load applicable repository instructions;
2. identify the source;
3. identify source version;
4. locate the requested Skill or workflow;
5. load required shared protocols;
6. inspect Audit State;
7. inspect active Decision Records;
8. inspect rejected hypotheses;
9. establish scope.

---

# 2. Instruction Hierarchy

Copilot-specific instructions must not override the conceptual methodology.

The effective hierarchy is:

```text id="2o9r8f"
Platform constraints
        ↓
Repository methodology
        ↓
Workflow
        ↓
Skill
        ↓
Task-specific request
```

A task request cannot silently redefine a core methodological distinction.

---

# 3. Skill Execution

Use the repository Skills as analytical units.

Examples:

```text id="j7d6m3"
skills/conceptual/semantic-precision/
```

```text id="x1y5m0"
skills/cartographic/propagation-analysis/
```

```text id="q8w3p2"
skills/epistemic/power-mediation-authority/
```

```text id="a9r6f1"
workflows/comprehensive-39-round-audit/
```

Do not duplicate Skill contents inside Copilot-specific instructions.

---

# 4. Shared Schemas

Findings must follow:

```text id="3uk7dn"
schemas/finding.md
```

Audit persistence must follow:

```text id="v4s1x8"
schemas/audit-state.md
```

Decisions must follow:

```text id="2m7b5j"
schemas/decision-record.md
```

These schemas guarantee interoperability with other agents.

---

# 5. Repository-Centered State

Important analytical state should be represented explicitly in repository artifacts when persistence is required.

Do not assume that a future Copilot session will reconstruct the complete reasoning from conversational context.

Persist:

* findings;
* decisions;
* rejected hypotheses;
* unresolved questions;
* node classifications;
* inter-stem classifications;
* source version;
* final synthesis.

---

# 6. Code-Oriented Environment

Copilot may naturally encounter the methodology while editing or reviewing repository files.

Code-oriented context does not change the nature of the task.

For example, if a Skill file is being reviewed, the agent must distinguish:

```text id="h1v3x0"
file syntax
```

from:

```text id="b6z8r2"
methodological semantics
```

A syntactically valid Skill may still contain methodological problems.

A philosophically unusual formulation is not necessarily a syntax problem.

---

# 7. Editing Discipline

When asked to modify Skills or schemas:

1. inspect neighboring files;
2. preserve shared conventions;
3. avoid duplicating existing capabilities;
4. verify cross-file terminology;
5. check active decisions;
6. make the smallest justified modification;
7. inspect the resulting architecture.

Do not create a new Skill merely to solve a problem already covered by an existing one.

---

# 8. Pull Request / Diff Awareness

When reviewing repository changes, Copilot should distinguish:

```text id="8h9t2u"
new capability
refinement
duplication
regression
terminological drift
architectural change
```

A smaller diff is not automatically a better change.

The criterion is preservation of methodological and architectural integrity.

---

# 9. Blind Passes

If the workflow specifies a blind pass, Copilot must respect the corresponding information boundary.

Repository visibility does not automatically authorize use of every file.

The workflow determines which information is methodologically admissible.

---

# 10. Findings and Decisions

Copilot must preserve:

```text id="m0w8p5"
Finding ≠ Decision
```

For example:

```text id="w3c6v1"
Finding:
The proposed section overlaps with an existing node.
```

does not automatically become:

```text id="r8q1z4"
Decision:
Delete the section.
```

The second requires explicit decision authority and sufficient evidence.

---

# 11. Structural Constraints

Copilot must respect the project's structural distinctions:

```text id="j9p0e2"
Science / Technology / Society
    ↓
Assemblages
    ↓
Nodes
    ↓
Inter-Stem Nodes
```

This is a cartographic architecture, not a rigid hierarchy.

The agent must not convert it into a conventional taxonomy merely to make the repository easier to organize.

---

# 12. Final Output

Standard analytical output:

```text id="0k2g4v"
Skill
Scope
Findings
Decisions
State Changes
Unresolved Questions
Recommendations
Confidence
```

Complete audits must follow the workflow's mandatory final report.

---

# 13. Copilot-Specific Principle

Copilot's strongest contribution may occur inside the repository itself, where it can inspect, compare, modify, and review the Skill architecture.

That repository awareness must increase traceability, not introduce a second conceptual system.

> Copilot adapts the repository interaction layer; the Skills remain the shared analytical core.
