# Rizome-and-AI

## A reusable methodology for analyzing technology, AI, and philosophical texts through a rhizomatic cartography

**Rizome-and-AI** is a modular, agent-neutral methodology for analyzing complex philosophical, conceptual, technological, and sociotechnical texts.

It uses the **rhizome as a way of observing relations**, not as a claim that AI, technology, or society *is* a rhizome.

The repository is designed to work across **Codex, Claude Code, and GitHub Copilot** while keeping the analytical methodology independent from any particular agent.

---

## What This Repository Does

The methodology provides tools for examining:

* concepts and their consistency;
* elements, relations, tensions, and transformations;
* assemblages and their internal dynamics;
* nodes as concentrations of relations and tensions;
* inter-stem nodes across assemblages;
* connections and propagation;
* causality and non-linear dynamics;
* emergence;
* scale;
* technology and material substrate;
* power, mediation, relevance, authority, and truth;
* knowledge, evidence, production, and attribution;
* technological determinism;
* anthropomorphism;
* philosophical claims;
* structural redundancy and necessity;
* contradictions and tensions;
* authorship and observer implication;
* AI-assisted writing;
* phenomenological reading;
* voice, style, and rhythm;
* originality and ending;
* whole-work coherence.

The methodology is intended to **analyze before intervening**.

It does not assume that every text needs correction, restructuring, simplification, or expansion.

---

## The Central Perspective

The project distinguishes between the **rhizome** and the **map**.

The rhizome is understood as a dynamic field of relations, tensions, transformations, connections, dependencies, and possibilities.

The map is a provisional construction made by an observer. It selects, separates, groups, classifies, and temporarily stabilizes aspects of that dynamic field so that certain relations become visible.

Therefore:

> **The map is not the territory.**

And:

> **Classification belongs to the map, not necessarily to the territory.**

A stable map does not imply a stable rhizome.

The purpose of the methodology is not to reproduce the rhizome completely, which would be impossible, but to construct useful cartographic cuts without confusing those cuts with the dynamics they attempt to render visible.

---

## Cartographic Architecture

The methodology uses the following orientation:

```text
Rhizome
   │
   ▼
General Domains
Science · Technology · Society
   │
   ▼
Assemblages
   │
   ▼
Concentrations of relations and tensions
   │
   ▼
Nodes
   │
   ▼
Inter-stem nodes
```

This is a **cartographic architecture, not a hierarchy of reality**.

### Domains

Science, Technology, and Society function as provisional cartographic orientations.

They are not necessarily separate ontological territories.

### Assemblages

Assemblages are relatively stable configurations of relations and tensions.

They are porous and dynamic rather than closed containers.

### Nodes

A node is not simply an important element or an interesting topic.

A node is a **concentration of relations and tensions that acquires a recognizable dynamic**.

### Inter-stem Nodes

An inter-stem node is not merely an interdisciplinary topic or an `AI + X` combination.

It requires a demonstrated dynamic crossing assemblages or domains and modifying their conditions of functioning.

The basic analytical sequence is:

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

A title alone is never sufficient to establish an inter-stem node.

---

## Fundamental Distinctions

The methodology protects several distinctions that prevent conceptual collapse:

| Distinction                     | Principle                                                          |
| ------------------------------- | ------------------------------------------------------------------ |
| AI / rhizome                    | AI is not the rhizome                                              |
| map / territory                 | The map is a provisional construction                              |
| node / topic                    | A node requires relational concentration                           |
| node / element                  | A node is not an element                                           |
| connection / causality          | Connection does not automatically imply causality                  |
| connection / propagation        | Connection does not automatically propagate                        |
| propagation / linear causality  | Propagation does not require a linear chain                        |
| complexity / emergence          | Complexity is not automatically emergence                          |
| multiplicity / horizontality    | Multiplicity does not imply equality or horizontality              |
| possibility / inevitability     | Technical possibility does not imply historical inevitability      |
| participation / intention       | Causal participation does not imply intention                      |
| behavior / understanding        | Functional behavior does not automatically establish understanding |
| production / knowledge          | Production does not establish knowledge                            |
| production / evidence           | Production does not constitute evidence by itself                  |
| relevance / authority           | Relevance does not establish authority                             |
| authority / truth               | Authority does not establish truth                                 |
| evaluation / philosophy of mind | Evaluation is not equivalent to understanding or consciousness     |
| evaluation / power              | Evaluation and power must remain analytically distinguishable      |
| openness / sovereignty          | Openness does not imply sovereignty                                |

These distinctions are methodological constraints, not conclusions that every text must affirm.

---

## Repository Structure

```text
Rizome-and-AI/
│
├── skills/
│   ├── _shared/
│   ├── conceptual/
│   ├── cartographic/
│   ├── causal/
│   ├── critical/
│   ├── structural/
│   ├── reader/
│   ├── authorship/
│   ├── epistemic/
│   └── synthesis/
│
├── workflows/
│   └── comprehensive-39-round-audit/
│
├── schemas/
│   ├── finding.md
│   ├── audit-state.md
│   └── decision-record.md
│
├── agents/
│   ├── agent-contract.md
│   ├── codex.md
│   ├── claude-code.md
│   └── github-copilot.md
│
├── prompts/
│   └── canonical cross-agent prompt definitions
│
├── AGENTS.md
├── CLAUDE.md
├── README.md
└── .github/
    ├── copilot-instructions.md
    └── prompts/             Visual Studio Code projections
```

Prompt projections are also exposed through `.codex/prompts/` for Codex and
`.claude/commands/` for Claude Code. The canonical prompt definitions remain in
`prompts/` so the three environments execute the same analytical instructions.

---

## Skills

The analytical capabilities are divided into functional families.

### Conceptual

Analyze conceptual consistency, elements, relations, tensions, semantic precision, and philosophical claims.

### Cartographic

Analyze map/territory relations, nodes, connections, propagation, inter-stem structures, and rhizomatic cartography.

### Causal

Analyze causality, propagation, scale, and emergence.

### Critical

Test anthropomorphism, technological determinism, vulnerability, falsifiability, and strong objections.

### Structural

Analyze architecture, necessity, redundancy, contradiction, tension, and asymmetry.

### Reader

Examine the work as a whole, perform blind external readings, and test accessibility to non-specialist readers.

### Authorship

Analyze observer implication, AI-assisted writing, voice, style, rhythm, and phenomenological reading.

### Epistemic

Analyze power, mediation, relevance, authority, knowledge, evidence, production, and attribution.

### Synthesis

Integrate findings, examine originality, evaluate the ending, and produce a final audit.

---

## Shared Protocols

The Skills use shared methodological protocols in:

```text
skills/_shared/
```

These establish common rules for:

* language-agnostic analysis;
* evidence and citation;
* analytical discipline;
* output structure.

This prevents individual Skills from silently developing incompatible methodologies.

---

## Complete 39-Round Audit

The repository includes a comprehensive workflow:

```text
workflows/comprehensive-39-round-audit/SKILL.md
```

The workflow orchestrates **39 consecutive analytical rounds** covering:

1. individual node validation;
2. elements and relations;
3. concentrations;
4. transversal architecture;
5. rhizomatic visibility;
6. territorial transitions;
7. internal tensions;
8. power/relevance/authority;
9. whole-work reading;
10. blind external reading;
11. philosophical claims;
12. conceptual consistency;
13. hostile reading;
14. originality;
15. necessity;
16. phenomenological reading;
17. voice and style;
18. authorship and observer;
19. structural necessity;
20. second blind reading;
21. Deleuze & Guattari challenge;
22. vulnerability;
23. dangerous words;
24. systemic reading;
25. autonomy;
26. second hostile reading;
27. reduction;
28. integrity;
29. non-specialist reading;
30. rhythm;
31. semantic precision;
32. invisible redundancy;
33. connectors;
34. contradictions;
35. scale;
36. causality and propagation;
37. exteriority and interiority;
38. ending and openness;
39. final integrated audit.

The workflow is an orchestrator. It does not replace the individual Skills.

---

## Findings, State, and Decisions

The repository separates three things that are often confused:

### Finding

An analytical result about something observed in the source.

### Audit State

Persistent investigation memory containing findings, hypotheses, questions, validated structures, rejected structures, and ongoing analysis.

### Decision

A methodological or structural determination based on findings.

This distinction allows the system to preserve uncertainty, disagreement, rejected alternatives, and later reversals.

See:

```text
schemas/finding.md
schemas/audit-state.md
schemas/decision-record.md
```

---

## Agent Interoperability

The methodology is deliberately **agent-neutral**.

```text
                 METHODOLOGICAL CORE
                         │
          ┌──────────────┼──────────────┐
          │              │              │
        Codex       Claude Code    GitHub Copilot
          │              │              │
       adapter         adapter         adapter
          │              │              │
          └──────────────┼──────────────┘
                         │
                 Shared Skills
                 Shared Schemas
                 Shared Workflows
```

The agents provide different execution environments.

They do not provide different methodologies.

> **The agent is interchangeable; the methodology is not.**

---

## How to Use the Repository

### For a single analytical task

1. Identify the question or problem.
2. Select the relevant Skill.
3. Load the required shared protocols.
4. Analyze the source.
5. Record findings using the common schema.
6. Distinguish findings from decisions.
7. Intervene only if the evidence warrants intervention.

### For a complete audit

Use:

```text
workflows/comprehensive-39-round-audit/SKILL.md
```

The workflow defines the order, state management, blind-pass restrictions, thresholds, and final synthesis.

### For a specific agent

Use the corresponding adapter:

```text
agents/codex.md
agents/claude-code.md
agents/github-copilot.md
```

The adapters explain how the same methodology is executed within each environment.

### Commands

The canonical command definitions are stored in:

```text
prompts/
```

The repository currently provides three commands:

| Command | Purpose |
| --- | --- |
| `complete-39-round-audit` | Run the complete 39-round audit workflow. |
| `validate-node-seven-steps` | Validate a node through Elements, Relations, Tensions, Concentration, Dynamic, Transformation, and Distinct Function. |
| `validate-references` | Audit the existence, bibliographic correctness, relevance, evidential support, scope, and currency of references. |

#### Visual Studio Code

The commands are exposed as prompt files in `.github/prompts/`. In Copilot Chat, type `/` and select the command, or use **Chat: Run Prompt**. Provide the source, node, or scope requested by the command.

Examples:

```text
/complete-39-round-audit
/validate-node-seven-steps
/validate-references
```

#### Codex

Codex projections are stored in `.codex/prompts/`. Invoke them through the Codex prompt command using the projection name, for example:

```text
/prompts:complete-39-round-audit
/prompts:validate-node-seven-steps
/prompts:validate-references
```

Pass the source or candidate node in the same request when the prompt requires an input.

#### Claude Code

Claude Code command projections are stored in `.claude/commands/` and are invoked with `/`:

```text
/complete-39-round-audit documents/English.md
/validate-node-seven-steps documents/English.md -- node candidate
/validate-references documents/English.md
```

Claude command projections receive their request through `$ARGUMENTS` and load the canonical prompt from `prompts/`.

#### Synchronization

After adding or changing a canonical prompt, synchronize all projections with:

```text
python scripts/sync-agent-skills.py
```

Check synchronization without modifying files:

```text
python scripts/sync-agent-skills.py --check
```

The repository validator also checks the prompt projections:

```text
python scripts/validate-repository.py
```

---

## Design Principles

The repository follows several general principles:

1. **Analyze before intervening.**
2. **Do not manufacture problems.**
3. **Preserve productive difficulty.**
4. **Do not infer categories from titles alone.**
5. **Do not confuse elements with relations or nodes.**
6. **Do not reduce propagation to linear causality.**
7. **Do not treat technical possibility as inevitability.**
8. **Do not anthropomorphize AI without argument.**
9. **Keep evidence, inference, and interpretation distinct.**
10. **Respect the language of the source.**
11. **Preserve rejected hypotheses and previous decisions.**
12. **Perform transversal review before major structural intervention.**
13. **Protect authorial voice when editing is authorized.**
14. **Keep the map provisional and partial.**

---

## What This Repository Is Not

It is not:

* a conventional AI taxonomy;
* a Deleuze & Guattari exegesis;
* a generic academic writing framework;
* a proofreading system;
* an automatic rewriting engine;
* a system that assumes every text requires improvement;
* a claim that AI itself constitutes a rhizome;
* a fixed classification of reality.

Its purpose is narrower and more demanding:

> **To provide a disciplined way of making relations, tensions, transformations, concentrations, limits, and crossings visible without confusing the analytical map with the dynamic field it attempts to observe.**

---

## Status

The repository currently contains:

* a complete modular Skill inventory;
* shared analytical protocols;
* a 39-round comprehensive audit workflow;
* common schemas for findings, state, and decisions;
* agent-neutral interoperability rules;
* adapters for Codex, Claude Code, and GitHub Copilot.

The methodology should be treated as a **living analytical system**. Changes should preserve interoperability and should not silently overturn established methodological decisions.

---

## License

License information will be added when the repository's licensing decision is finalized.
