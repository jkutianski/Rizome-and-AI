---
name: "Validate Node in Seven Steps"
description: "Validate a proposed or existing node through the repository's seven-step relational sequence."
argument-hint: "Provide the source, the candidate node, and its location."
agent: "agent"
---

Validate the proposed or existing node described by the user:

${input:node}

Use the following as the methodological authority:

- [AGENTS.md](../../AGENTS.md)
- [node-validation Skill](../../skills/cartographic/node-validation/SKILL.md)
- [finding schema](../../schemas/finding.md)
- [audit state schema](../../schemas/audit-state.md)
- [decision record schema](../../schemas/decision-record.md)

Read the source passage and the relevant surrounding context before assessing the candidate. Analyze the source in its original language and do not infer node status from the title, importance, length, or thematic visibility alone.

Evaluate the candidate in this exact order:

1. **Elements:** What participates in the candidate dynamic?
2. **Relations:** How are those elements connected or mutually involved?
3. **Tensions:** What conflicts, dependencies, asymmetries, incompatibilities, or competing forces make the relations dynamically significant?
4. **Concentration:** Why do these relations and tensions belong together as a recognizable concentration rather than a loose theme or list?
5. **Dynamic:** What recognizable process or configuration emerges from the concentration?
6. **Transformation:** What changes because of this dynamic, and what consequence does it produce within the map?
7. **Distinct Function:** What does this candidate make visible that another node does not?

For each step, provide:

- the direct textual evidence or a clearly marked inference;
- the analytical assessment;
- confidence: High, Medium, or Low;
- whether the step is satisfied, partial, unsupported, or unresolved.

Then provide:

1. A final classification: **Validated Node**, **Partially Developed Node**, **Candidate Node**, **Thematic Grouping**, **Ordinary Relation**, or **Insufficient Evidence**.
2. A structured finding using [schemas/finding.md](../../schemas/finding.md), separated from any decision.
3. The candidate's strongest supporting evidence and its strongest weakness.
4. Its overlap or distinction relative to nearby nodes, if that can be established from the source.
5. A recommendation: **Necessary**, **Advisable**, **Optional**, **Not Recommended**, or **Leave Unchanged**.

Do not upgrade the candidate to an inter-stem node through this command alone. If the evidence suggests cross-assemblage status, record that as a separate question and recommend the [inter-stem-validation Skill](../../skills/cartographic/inter-stem-validation/SKILL.md). Do not invent missing relations, tensions, transformations, or evidence.