---
name: "Complete 39-Round Audit"
description: "Run the complete 39-round conceptual and cartographic audit workflow on a specified source."
argument-hint: "Provide the source path, the text to analyze, and the output language."
agent: "agent"
---

Run a complete 39-round audit of the source provided by the user:

${input:source}

Use the following as the methodological authority:

- [AGENTS.md](../../AGENTS.md)
- [39-round audit workflow](../../workflows/comprehensive-39-round-audit/SKILL.md)
- [shared protocols](../../skills/_shared/)
- [finding schema](../../schemas/finding.md)
- [audit state schema](../../schemas/audit-state.md)
- [decision record schema](../../schemas/decision-record.md)

Before starting:

1. Identify and freeze the exact source version.
2. Record the source language or languages and analyze the original formulation.
3. Read the existing audit state, active decisions, and rejected hypotheses, if they exist.
4. Do not modify the source during the audit.

During execution:

- Complete all 39 rounds in the order defined by the workflow.
- Respect blind rounds and their information boundaries.
- Apply the Skills specified by each round without duplicating their methodology.
- Distinguish observation, evidence, interpretation, diagnosis, recommendation, and decision.
- Record each finding using the common schema, including location, severity, confidence, and architectural scope.
- Do not turn connections into causality or propagation without sufficient evidence.
- Do not infer nodes, inter-stem nodes, emergence, anthropomorphism, or determinism from titles or vocabulary alone.
- Preserve asymmetries and productive tensions when there is no evidence of a problem.

Deliver:

1. The updated audit state, preserving the previous history.
2. New, corroborated, qualified, contested, or superseded findings, separated from decisions.
3. Explicit decisions with their basis, alternatives considered, and reversal conditions.
4. Unresolved questions, evidential limits, and interpretive risks.
5. A final synthesis stating what should be preserved, what requires intervention, and what should remain unchanged.

Do not rewrite the source or propose structural changes before the evidence from the rounds and the transversal review justifies them. If the source, its version, or the state required to continue is missing, request only that information before beginning the analysis.