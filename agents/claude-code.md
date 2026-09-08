# Claude Code Adapter

## Purpose

This adapter defines how **Claude Code** executes the agent-neutral Rizome-and-AI methodology.

Claude Code must consume the same Skills, workflows, schemas, and shared protocols used by every other compatible agent.

This file does not duplicate or reinterpret those Skills.

---

## Architecture

```text id="c6m5ik"
Claude Code
     │
     ├── CLAUDE.md
     │
     ├── workflows/
     │
     ├── skills/
     │
     └── schemas/
```

The repository remains the source of methodological truth.

---

# 1. Initialization

At the beginning of an audit:

1. read the applicable `CLAUDE.md`;
2. identify the source;
3. establish source version;
4. locate the relevant workflow or Skill;
5. load required shared protocols;
6. read current Audit State;
7. read active Decision Records;
8. identify rejected hypotheses;
9. establish scope and constraints.

Do not begin analysis from conversational assumptions when repository state is available.

---

# 2. Skill Loading

Claude Code should load only the Skills required for the task.

Examples:

```text id="04qj8k"
Node classification
→ skills/cartographic/node-validation/SKILL.md
```

```text id="qz0z0a"
Causal claim audit
→ skills/causal/causality-propagation/SKILL.md
```

```text id="k1p4x9"
Complete audit
→ workflows/comprehensive-39-round-audit/SKILL.md
```

Skills remain the analytical units.

Claude Code is only their execution environment.

---

# 3. Shared Protocols

When a Skill requires them, load:

```text id="u1yd7s"
skills/_shared/language-agnostic-analysis.md
skills/_shared/evidence-and-citation.md
skills/_shared/analytical-discipline.md
skills/_shared/output-protocol.md
```

Do not substitute personal reasoning conventions for these shared protocols.

---

# 4. State

Use:

```text id="55h2q0"
schemas/audit-state.md
```

as the state contract.

Use:

```text id="m5x9pk"
schemas/finding.md
```

for analytical findings.

Use:

```text id="g0v2b7"
schemas/decision-record.md
```

for explicit decisions.

State must remain recoverable across sessions whenever the audit is intended to persist.

---

# 5. Conversation vs Repository State

Conversational context may assist analysis.

It must not replace explicit repository state when persistence matters.

If a conclusion is important enough to constrain future analysis, record it in the appropriate state or Decision Record.

Do not rely on:

```text id="a7l0xk"
"I remember that we decided..."
```

when the decision should be persistent.

---

# 6. Analyze Before Editing

Claude Code must distinguish analytical work from source modification.

Default sequence:

```text id="g0h4f2"
Analyze
   ↓
Findings
   ↓
Recommendation
   ↓
Decision
   ↓
Authorized modification
```

Do not silently rewrite the source during an audit.

---

# 7. Structural Intervention

Before modifying:

* nodes;
* assemblages;
* inter-stem classifications;
* architecture;
* substantial passages;

perform the required transversal review.

Check existing decisions and rejected hypotheses first.

A structural intervention without this check risks creating local improvements that damage the global map.

---

# 8. Blind Reading

Claude Code must respect the information boundary of blind rounds.

If previous findings are available in repository state but the current round is blind, those findings must not be used.

The isolation is part of the methodology.

---

# 9. Evidence Discipline

When a conclusion depends on external evidence, identify that dependency explicitly.

Do not use external knowledge to silently repair an unsupported claim.

The distinction must remain visible between:

```text id="b4s4u5"
source evidence
analytical inference
external evidence
```

---

# 10. Parallel Analysis

Claude Code may perform multiple analytical passes when useful.

However, parallel Skills must produce independent Findings before integration.

Do not prematurely collapse them into a single conclusion.

Example:

```text id="0tr8d8"
Node validation
       +
Causality analysis
       +
Hostile reading
       ↓
Independent Findings
       ↓
Integrated diagnosis
```

---

# 11. No Methodological Drift

Claude Code must preserve the project's closed distinctions, including:

```text id="3ij6ki"
AI ≠ rhizome
map ≠ territory
node ≠ theme
inter-stem ≠ interdisciplinarity
connection ≠ propagation
causal participation ≠ intention
complexity ≠ emergence
production ≠ evidence
relevance ≠ authority
authority ≠ truth
```

A new interpretation may challenge a decision only through explicit reopening.

---

# 12. Final Output

A Skill result should conform to:

```text id="mb7h1q"
Skill
Scope
Findings
Decisions
State Changes
Unresolved Questions
Recommendations
Confidence
```

The complete 39-round audit must use the final report specified in the workflow.

---

# 13. Claude Code-Specific Principle

Claude Code may use its conversational reasoning and repository capabilities to maintain continuity and perform complex multi-pass analysis.

Those capabilities must remain subordinate to the shared methodology.

> Claude Code provides the working context; the repository provides the methodological contract.
