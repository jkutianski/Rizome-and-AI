# Rizome-and-AI — Repository Instructions

## Purpose

This repository contains a reusable, agent-neutral analytical methodology for auditing philosophical and conceptual texts through a rhizomatic and cartographic framework.

The methodology is designed to operate across **Codex, Claude Code, and GitHub Copilot**.

The repository itself is the methodological source of truth.

## Source of Truth

Before performing substantive analytical work:

1. Read this file.
2. Identify the applicable Skill in `skills/`.
3. Load the relevant shared protocols from `skills/_shared/`.
4. If executing the complete audit, use `workflows/comprehensive-39-round-audit/SKILL.md`.
5. Use the schemas in `schemas/` for findings, audit state, and decisions.
6. Consult the appropriate adapter in `agents/` when working in a specific agent environment.

Do not duplicate detailed methodology from these files into this document.

## Core Rule

**Analyze before intervening.**

Do not rewrite, improve, restructure, merge, eliminate, or create material until the relevant analytical work has established that an intervention is warranted.

Do not manufacture problems merely because an alternative formulation seems preferable.

## Non-Negotiable Conceptual Distinctions

Preserve the following distinctions unless concrete evidence from the source requires reopening them:

* AI is not the rhizome.
* Map is not territory.
* The rhizome is dynamic; the map is a provisional stabilization of observation.
* Classification belongs to the map, not necessarily to the territory.
* A node is a concentration of relations and tensions, not an element or topic.
* A connection is not automatically causality.
* Connection is not propagation.
* Propagation is not linear causality.
* An inter-stem node is not merely interdisciplinarity or an `AI + X` topic.
* Complexity is not automatically emergence.
* Multiplicity is not horizontality.
* Technical possibility is not historical inevitability.
* Causal participation is not intention.
* Functional behavior is not automatically understanding.
* Production is not knowledge.
* Production is not evidence.
* Relevance is not authority.
* Authority is not truth.
* Evaluation is not philosophy of mind.
* Evaluation is not power.
* Openness is not sovereignty.
* AI must not be anthropomorphized without argument.

## Node and Inter-Stem Discipline

Never infer a node or inter-stem node from its title alone.

For inter-stem analysis, reconstruct the sequence:

**assemblages → relations → tensions → concentration → modification of conditions → transformation → possible propagation**

If the evidence does not support this structure, do not force the category.

## Language and Evidence

Analyze the source in the language in which it actually exists.

Do not analyze an imagined translation.

Distinguish conceptual, semantic, stylistic, evidential, and methodological problems.

Do not invent evidence, sources, citations, intentions, or arguments.

Distinguish source evidence from analytical inference and external evidence.

## Audit State

Treat `schemas/audit-state.md` as persistent investigation memory.

Do not silently delete previous findings, rejected hypotheses, decisions, or unresolved questions.

A rejected hypothesis remains part of the audit history and must not be silently resurrected.

Findings and decisions are distinct objects.

## Structural Restraint

Before proposing a new node, merger, elimination, or major restructuring, perform the required transversal review.

Ask:

* What is already conceptually solid?
* Is the proposed category genuinely necessary?
* Is there redundancy?
* Does the proposed node perform a unique function?
* Does the architecture remain cartographic rather than becoming a conventional taxonomy?
* Does the intervention improve the argument, or merely make the structure look cleaner?

## Blind Analysis

Rounds explicitly designated as blind must be conducted without importing conclusions from previous analytical passes.

In particular, preserve the isolation requirements of the comprehensive 39-round workflow.

## Editing

Analysis and editing are separate phases.

Do not modify source material during an audit unless the user explicitly requests an intervention or the applicable workflow explicitly authorizes it.

When editing is authorized, preserve the author's conceptual ownership, voice, asymmetries, and productive tensions.

## Agent Interoperability

The conceptual methodology is shared across agents.

Agent-specific files in `agents/` define execution adaptations only.

**The agent is interchangeable; the methodology is not.**

## Repository Map

```text
skills/
    _shared/       Shared analytical protocols
    conceptual/    Conceptual and philosophical analysis
    cartographic/  Map, nodes, connections, propagation
    causal/        Causality, scale, emergence
    critical/      Critical and adversarial analysis
    structural/    Architecture, redundancy, contradiction
    reader/        Reader-oriented analysis
    authorship/    Observer, authorship, voice, phenomenology
    epistemic/     Knowledge, evidence, power, authority
    synthesis/     Originality, ending, integrated audit

workflows/
    comprehensive-39-round-audit/
                   Complete 39-round audit orchestration

schemas/
    finding.md
    audit-state.md
    decision-record.md

agents/
    agent-contract.md
    codex.md
    claude-code.md
    github-copilot.md
```

## Final Principle

The purpose of the repository is not to make every text cleaner, more symmetrical, or more conventional.

Its purpose is to make relations, tensions, transformations, limits, and concentrations visible without confusing the map with the rhizome.
