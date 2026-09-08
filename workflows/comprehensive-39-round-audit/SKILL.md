---
name: "comprehensive-39-round-audit"
description: "This workflow orchestrates a complete conceptual, philosophical, methodological, structural, argumentative, semantic, evidential, stylistic, phenomenological, and cartographic audit of a text through 39 consecutive rounds."
---

# Comprehensive 39-Round Audit Workflow

## Purpose

This workflow orchestrates a complete conceptual, philosophical, methodological, structural, argumentative, semantic, evidential, stylistic, phenomenological, and cartographic audit of a text through **39 consecutive rounds**.

It is designed for agentic environments such as Codex, Claude Code, and GitHub Copilot.

The workflow does not replace the individual Skills used during the audit. It coordinates them.

The governing principle is:

> **Analyze before intervening.**

The workflow must diagnose the existing work before proposing modifications. It must preserve what works, distinguish genuine problems from productive tensions, and prevent the audit from becoming an automatic rewriting process.

The final objective is not to make the text more orderly, more symmetrical, or more polished.

The objective is to determine whether the work's **cartographic precision can be improved without reducing the multiplicity and dynamism of the field it attempts to observe.**

---

# 1. Scope

This workflow applies to a complete work that may contain:

* a philosophical or theoretical argument;
* a personal or essayistic trajectory;
* a methodological framework;
* domains;
* assemblages;
* nodes;
* inter-stem nodes;
* connections;
* transformations;
* propagations;
* claims about AI, technology, science, society, cognition, knowledge, power, biology, geopolitics, or related fields;
* reflexive discussion of the author's own position;
* discussion of AI participation in the writing process.

The source may be:

* entirely in English;
* entirely in Spanish;
* multilingual;
* partially translated.

The workflow audits the **actual source text**, not an imagined translation.

---

# 2. Governing Principles

The workflow must preserve the following principles throughout all 39 rounds.

## 2.1 Analyze before rewriting

Do not rewrite passages during the audit unless a specific round explicitly requires examination of a possible reformulation.

The normal sequence is:

**observation → evidence → analysis → diagnosis → recommendation**

not:

**observation → correction**

---

## 2.2 Evidence before intervention

Every substantive finding must be traceable to:

* direct textual evidence;
* a clearly justified inference;
* convergent evidence from multiple passages;
* or reliable external evidence when external verification is genuinely required.

Never invent evidence.

Never attribute an intention to the author merely because a formulation could have that effect.

---

## 2.3 Preserve valid asymmetry

Do not normalize:

* unequal section lengths;
* unequal node development;
* different numbers of examples;
* different degrees of conceptual density;
* different numbers of connections;
* different levels of evidential support;

unless the asymmetry creates a genuine conceptual, structural, argumentative, or reader problem.

A map does not become more precise by making every region the same size.

---

## 2.4 Do not force categories

Never infer that something is a:

* node;
* inter-stem node;
* emergence;
* causal relation;
* propagation;
* contradiction;
* anthropomorphic formulation;
* technological-determinist claim;

merely because its title or vocabulary suggests it.

The category must be justified by the dynamics actually present in the text.

---

## 2.5 Preserve productive tensions

Not every unresolved opposition is a defect.

Distinguish:

* contradiction;
* tension;
* ambiguity;
* asymmetry;
* development;
* reflexivity;
* contextual variation;
* productive unresolvedness.

Do not resolve a productive tension merely because it looks untidy.

---

## 2.6 Do not anthropomorphize by grammar alone

Active verbs such as:

* produces;
* transforms;
* mediates;
* participates;
* reorganizes;
* modifies;

do not automatically attribute human-like mentality.

Anthropomorphism requires stronger evidence, such as attribution of:

* intention;
* desire;
* belief;
* consciousness;
* understanding;
* will;
* motives;
* autonomous mental agency.

---

## 2.7 Do not confuse causality with determinism

The workflow may identify genuine causal relations.

It must distinguish:

* causal influence from determination;
* contribution from sufficiency;
* enablement from necessity;
* constraint from inevitability;
* technical possibility from historical inevitability;
* causal participation from intentional agency.

A rhizomatic analysis does not require abandoning causality.

---

## 2.8 Do not confuse the map with the territory

The map is a relatively stable construction produced by an observer.

The rhizome remains dynamic.

The stability of the map does not imply the stability of the territory.

Classification belongs to the cartographic operation and must not automatically be treated as an ontological property of the field being mapped.

---

# 3. Source Freeze

Before beginning Round 1:

1. Identify the exact source version being audited.
2. Treat that version as frozen.
3. Record the source language or languages.
4. Record any explicit scope restrictions.
5. Record whether external evidence is permitted.
6. Record any previously closed architectural decisions that must be preserved.
7. Do not silently incorporate material from earlier drafts.
8. Do not modify the source during the audit.

If a new source version is introduced, treat it as a new audit input unless the user explicitly requests continuation or comparison.

---

# 4. Audit State

Maintain an audit ledger throughout the workflow.

Each finding should contain, where applicable:

* `Finding ID`
* `Round`
* `Location`
* `Evidence`
* `Issue Type`
* `Diagnosis`
* `Severity`
* `Confidence`
* `Architectural Scope`
* `Related Findings`
* `Root Issue`
* `Recommendation`
* `Status`

### Severity

* **A — Critical:** compromises a fundamental claim or architectural operation.
* **B — Important:** significantly affects conceptual, methodological, structural, or argumentative precision.
* **C — Local:** localized problem with limited architectural consequences.
* **D — Stylistic:** primarily affects form, rhythm, or presentation.
* **E — Non-problematic:** unusual, asymmetric, difficult, or unconventional but valid.

### Confidence

* High
* Medium
* Low

### Recommendation

* Necessary
* Advisable
* Optional
* Not Recommended
* Leave Unchanged

Do not treat the severity scale as a numerical score.

---

# 5. Round / Skill Relationship

A **round is not a Skill**.

One round may invoke several Skills.

One Skill may be invoked in several rounds.

The workflow must therefore distinguish:

* **methodological round** — what question is being audited;
* **Skill** — which analytical capability performs the work;
* **finding** — what the analysis discovers;
* **synthesis** — how findings interact across rounds.

Never duplicate an individual Skill's complete methodology inside a round. Invoke or apply the relevant Skill.

---

# 6. Language-Agnostic Protocol

Apply:

`skills/_shared/language-agnostic-analysis.md`

before and throughout the workflow.

The source may be written in any language.

Analyze:

* conceptual meaning in the original language;
* semantic scope in the original formulation;
* terminology in context;
* multilingual transitions where relevant.

Do not translate the source mentally into English before analyzing it.

When a finding depends on exact wording, preserve the original wording.

If the user specifies an output language, use it.

Otherwise, use the language requested by the user or the predominant language of the source.

---

# 7. Shared Analytical Protocols

The workflow must use the following shared protocols:

* `skills/_shared/language-agnostic-analysis.md`
* `skills/_shared/evidence-and-citation.md`
* `skills/_shared/analytical-discipline.md`
* `skills/_shared/output-protocol.md`

These protocols govern every round.

---

# 8. The 39 Rounds

## Round 1 — Strict Validation of A–E

### Objective

Validate each proposed inter-stem node independently.

### Apply

* `node-validation`
* `inter-stem-validation`
* `element-relation-tension`

### Test

For each node:

**assemblages → relations → tensions → concentration → modification of conditions → transformation → possible propagation**

Validate:

* assemblages;
* elements;
* relations;
* tensions;
* concentration;
* reciprocal modification;
* transformation;
* propagation;
* distinct function.

Do not infer validity from the title.

---

## Round 2 — Elements, Relations, Tensions, Transformations

### Objective

Reconstruct the relational material of the work.

### Apply

* `element-relation-tension`

Identify:

* elements;
* relations;
* tensions;
* transformations;
* feedback;
* level confusions;
* material conditions;
* infrastructural conditions.

Determine whether the text confuses:

* element with relation;
* relation with tension;
* tension with node;
* example with structural component.

---

## Round 3 — Concentrations

### Objective

Determine whether apparent nodes are genuine concentrations rather than themes.

### Apply

* `node-validation`
* `element-relation-tension`

Test:

* relational density;
* tension;
* concentration;
* recognizable dynamic;
* transformation;
* unique function.

A topic is not a node merely because it receives substantial discussion.

---

## Round 4 — Transversal Architecture

### Objective

Audit the complete architecture.

### Apply

* `structural-architecture`
* `necessity-redundancy`

Check:

* domains;
* assemblages;
* nodes;
* inter-stem nodes;
* duplications;
* absorption possibilities;
* hidden hierarchy;
* category capture;
* cartographic character;
* structural dependencies.

Do not equate organization with hierarchy.

---

## Round 5 — Rhizomatic Visibility

### Objective

Determine whether the work actually makes relational multiplicity visible.

### Apply

* `rhizomatic-cartography`
* `map-territory`
* `connection-analysis`

Test whether the text makes visible:

* relations;
* displacements;
* tensions;
* transformations;
* feedback;
* multiple connections;
* uneven connectivity;
* contingent trajectories;

rather than merely presenting a classification of themes.

---

## Round 6 — Transitions Between Territories

### Objective

Audit transitions between assemblages and domains.

### Apply

* `connection-analysis`
* `inter-stem-validation`

Classify transitions as:

* necessary;
* legitimate;
* weak;
* declarative;
* artificial;
* unsupported.

Unequal connectivity may itself be analytically significant.

---

## Round 7 — Internal Tensions

### Objective

Audit tensions within each node and assemblage.

### Apply

* `element-relation-tension`
* `contradiction-tension`

Identify:

* competing forces;
* incompatibilities;
* dependencies;
* asymmetries;
* unresolved tensions;
* productive contradictions.

Do not manufacture tensions merely to make a node appear complex.

---

## Round 8 — Power, Relevance, Authority

### Objective

Perform the specialized audit of D.

### Apply

* `power-mediation-authority`

Maintain the distinction:

**mediation → selection → visibility → relevance → authority → power**

Audit separately:

* relevance;
* authority;
* legitimacy;
* truth;
* auditability;
* power.

Truth production must not become the conceptual center merely because the word "truth" appears.

---

## Round 9 — Read the Text as a Work

### Objective

Determine whether the text functions as a coherent work rather than a collection of sections.

### Apply

* `whole-work-reading`

Reconstruct:

**personal experience → observer → map → rhizome → assemblages → nodes → inter-stem → transformations/propagations → closure**

Treat this as a diagnostic trajectory, not a mandatory formula.

---

## Round 10 — First Blind External Reading

### Objective

Read the work as if encountering it for the first time.

### Apply

* `blind-external-reading`

Do not rely on:

* previous discussions;
* hidden methodology;
* author explanations;
* prior audit conclusions.

Determine what the text itself allows a reader to reconstruct.

---

## Round 11 — Philosophical Claims

### Objective

Audit major philosophical claims.

### Apply

* `philosophical-claims`
* `conceptual-consistency`
* `semantic-precision`

Pay particular attention to:

* consciousness;
* understanding;
* agency;
* extended cognition;
* knowledge;
* authority;
* power;
* emergence;
* intervention;
* representation.

---

## Round 12 — Conceptual Consistency

### Objective

Test whether major concepts retain coherent functions across the entire work.

### Apply

* `conceptual-consistency`

Audit:

* rhizome;
* map;
* territory;
* assemblage;
* node;
* inter-stem;
* substrate;
* tension;
* transformation;
* propagation;
* emergence;
* agency;
* knowledge;
* authority.

Conceptual variation is not automatically conceptual inconsistency.

---

## Round 13 — Philosophically Hostile Reading

### Objective

Attack the strongest vulnerable assumptions.

### Apply

* `hostile-reader`
* `anthropomorphism-audit`
* `technological-determinism`

Test objections concerning:

* instrumentalism;
* anthropomorphism;
* determinism;
* AI agency;
* AI understanding;
* AI consciousness;
* arbitrary nodes;
* decorative use of rhizome;
* conventional network architecture;
* inevitability;
* insufficient evidence.

---

## Round 14 — Originality

### Objective

Determine where the work performs an original conceptual or methodological operation.

### Apply

* `originality-analysis`

Test originality at the level of:

* question;
* perspective;
* conceptual operation;
* methodological operation;
* cartographic construction;
* node architecture;
* inter-stem criterion;
* observer implication;
* AI-writing reflexivity.

Do not claim absolute historical novelty without evidence.

---

## Round 15 — Structural Necessity

### Objective

Determine which structural components are necessary.

### Apply

* `necessity-redundancy`
* `structural-architecture`

Ask:

> What meaningful conceptual or architectural function would be lost if this component disappeared?

Do not reduce for aesthetic reasons.

---

## Round 16 — Phenomenological Trajectory

### Objective

Read the work as an experience of movement.

### Apply

* `phenomenological-reading`

Analyze:

* orientation;
* disorientation;
* rhythm;
* accumulation;
* transitions;
* scale changes;
* returns;
* interruptions;
* density;
* breathing;
* closure.

Do not psychoanalyze the author.

---

## Round 17 — Voice, Style, Rhythm

### Objective

Determine whether form preserves the author's recognizable voice.

### Apply

* `voice-style-rhythm`

Audit:

* personal voice;
* essayistic character;
* rhythm;
* cadence;
* sentence density;
* paragraph density;
* enumeration;
* transitions;
* academicization;
* corporate tone;
* artificial smoothing.

Do not equate polish with improvement.

---

## Round 18 — Observer and AI Writing

### Objective

Audit the observer's implication and the reflexive role of AI in writing.

### Apply

* `observer-implication`
* `ai-writing-reflexivity`

Test:

* situated observation;
* selection;
* classification;
* observer/map relation;
* author/AI relation;
* cognitive support;
* epistemic mediation;
* authorship;
* responsibility;
* reflexive loops.

Do not infer AI authorship from AI participation.

---

## Round 19 — Second Structural Necessity Pass

### Objective

Revisit structural necessity after the conceptual and philosophical audits.

### Apply

* `necessity-redundancy`
* `structural-architecture`

Determine whether earlier diagnoses change when the whole relational architecture is considered.

Do not double-count identical findings.

---

## Round 20 — Second Blind Reading

### Objective

Perform a fresh independent external reading.

### Apply

* `blind-external-reading`

This pass must be analytically isolated from the conclusions of Round 10.

Do not feed prior diagnoses into the reader model.

Compare the two blind readings only afterward.

---

## Round 21 — Deleuze & Guattari Attack

### Objective

Test the architecture against a demanding rhizomatic critique.

### Apply

* `hostile-reader`
* `rhizomatic-cartography`
* `map-territory`

Test:

* classification;
* map stability;
* hidden hierarchy;
* nodes as centers;
* A–E capture;
* network conventionality;
* multiplicity;
* stability;
* territorialization.

Do not assume that any classification is automatically anti-rhizomatic.

---

## Round 22 — Falsifiability and Vulnerability

### Objective

Identify claims vulnerable to empirical, conceptual, evidential, or scope-based challenge.

### Apply

* `falsifiability-vulnerability`

Determine:

* what could challenge the claim;
* whether evidence supports its strength;
* whether modality exceeds support;
* whether counterexamples matter;
* whether external verification is required.

Do not force interpretive or philosophical claims into scientific falsifiability.

---

## Round 23 — Dangerous Words

### Objective

Audit semantically high-risk vocabulary.

### Apply

* `semantic-precision`

Prioritize:

* agency;
* autonomy;
* understanding;
* consciousness;
* knowledge;
* authority;
* legitimacy;
* relevance;
* production;
* representation;
* intervention;
* capacity;
* transformation;
* emergence;
* power;
* mediation;
* conditions.

---

## Round 24 — Whole-Work System

### Objective

Determine whether the work has an invisible thread and unity without becoming totalizing.

### Apply

* `whole-work-reading`
* `conceptual-consistency`

Test:

* general problem;
* trajectory;
* invisible thread;
* cumulative development;
* recurrence;
* observer;
* A–E relation;
* opening/ending relation.

---

## Round 25 — Autonomy of the Work

### Objective

Determine whether the work can stand without the history of its creation.

### Apply

* `blind-external-reading`

Ask:

> Can the reader reconstruct the conceptual operation without knowing the conversations, drafts, prompts, or methodology that produced it?

---

## Round 26 — Second Hostile Reader

### Objective

Identify the strongest concrete objections remaining after previous rounds.

### Apply

* `hostile-reader`

Focus on objections to:

* A;
* B;
* C;
* D;
* E;
* their differentiation;
* their necessity;
* their evidence;
* their relation to one another.

Do not manufacture objections where the text already answers them.

---

## Round 27 — Reduction and Pruning

### Objective

Determine what can be removed, compressed, absorbed, or merged without meaningful conceptual loss.

### Apply

* `necessity-redundancy`

Use:

* removal test;
* absorption test;
* merge test;
* relocation test;
* compression test.

Do not optimize for minimum length.

---

## Round 28 — Structural Integrity

### Objective

Verify that closed architectural decisions remain intact.

### Apply

* `structural-architecture`
* `integrated-audit` as an integrity checkpoint where supported

Preserve, unless concrete textual evidence requires reconsideration:

* AI ≠ rhizome;
* map ≠ territory;
* dynamic rhizome / relatively stable map;
* classification belongs to the map;
* A–E differentiation;
* eliminated autonomous nodes;
* materiality;
* contingency;
* absence of a forced global-connections section;
* absence of an independent feedback section;
* latent BCI material where appropriate.

Do not reopen closed decisions merely because an alternative architecture would look cleaner.

---

## Round 29 — Non-Specialist Reader

### Objective

Determine whether conceptual difficulty belongs to the thought rather than avoidable opacity.

### Apply

* `non-specialist-reader`

Test:

* terminology;
* references;
* abstraction;
* examples;
* transitions;
* density;
* assumptions;
* AI-related concepts;
* causal claims;
* philosophical claims.

Do not simplify the work merely to make it easier.

---

## Round 30 — Breathing and Rhythm

### Objective

Revisit reader movement and prose rhythm.

### Apply

* `voice-style-rhythm`
* `phenomenological-reading`

Audit:

* paragraph length;
* conceptual accumulation;
* abstraction/example balance;
* pauses;
* transitions;
* repeated formulations;
* density;
* reader fatigue;
* recovery points.

---

## Round 31 — Semantic Precision

### Objective

Perform the final detailed semantic audit.

### Apply

* `semantic-precision`

Prioritize formulations concerning:

* AI modifies;
* AI participates;
* AI intervenes;
* AI produces;
* authority;
* legitimacy;
* relevance;
* conditions;
* design;
* sovereignty;
* emergence;
* agency;
* understanding.

Check quantifiers, modality, attribution, scope, and semantic drift.

---

## Round 32 — Invisible Redundancy

### Objective

Identify redundancies that are functional rather than lexical.

### Apply

* `necessity-redundancy`
* `structural-architecture`

Compare:

* functions;
* tensions;
* transformations;
* examples;
* propagations;
* conclusions.

Repeated language is not enough to establish redundancy.

---

## Round 33 — Connectors

### Objective

Audit conceptual transitions between sections and territories.

### Apply

* `connection-analysis`

Distinguish:

* conceptual connection;
* rhetorical signposting;
* thematic adjacency;
* causal relation;
* transformation;
* propagation.

A connector does not need to connect everything to everything else.

---

## Round 34 — Contradictions

### Objective

Perform the final contradiction/tension audit.

### Apply

* `contradiction-tension`

Use the same-conditions test.

Check:

* scope;
* time;
* scale;
* modality;
* conceptual meaning;
* conditions.

Preserve genuine productive tensions.

---

## Round 35 — Scale

### Objective

Audit micro/meso/macro transitions.

### Apply

* `scale-analysis`

Test:

* scale transitions;
* aggregation;
* downward effects;
* meso configurations;
* mechanisms;
* generalization;
* temporal scale;
* power;
* materiality.

Do not infer macro transformation directly from micro evidence without an adequate transition.

---

## Round 36 — Causality and Propagation

### Objective

Perform the final audit of causal dynamics.

### Apply

* `causality-propagation`
* `propagation-analysis`

Test:

* causal claims;
* enabling conditions;
* distributed causality;
* feedback;
* transformation;
* propagation;
* interruption;
* attenuation;
* amplification;
* contingency.

Do not convert propagation into a hidden linear chain.

---

## Round 37 — Exteriority / Interiority

### Objective

Determine whether the observer and AI-writing process are genuinely implicated in the analytical field.

### Apply

* `observer-implication`
* `ai-writing-reflexivity`

Test the reflexive loop:

**AI participates in constructing the map → the map analyzes AI → this participation becomes part of the object of analysis → the analysis changes the observer's position**

Do not collapse observer and observed.

---

## Round 38 — Ending and Openness

### Objective

Determine whether the ending closes the work without pretending to close the rhizome.

### Apply

* `ending-openness`
* `whole-work-reading`

Test:

* relation to opening;
* synthesis;
* trajectory;
* remaining openness;
* contingency;
* observer position;
* Node E's role;
* absence of hierarchy;
* absence of totalizing conclusion.

Core test:

> Does the work end, while the field it maps remains capable of changing?

---

# 9. Round 39 — Integrated Audit

### Objective

Produce the final diagnosis of the complete work.

### Apply

* `integrated-audit`

Round 39 must not simply repeat all previous findings.

It must synthesize them.

It must:

1. identify convergent findings;
2. identify independent findings;
3. collapse duplicate findings;
4. identify root problems;
5. distinguish local from architectural consequences;
6. preserve productive tensions;
7. reconstruct the final architecture;
8. validate A–E;
9. validate connections;
10. validate propagations;
11. assess causality;
12. assess emergence;
13. assess materiality;
14. assess power;
15. assess contingency;
16. assess map/territory;
17. assess observer implication;
18. assess AI-writing reflexivity;
19. assess philosophical vulnerabilities;
20. assess semantic precision;
21. assess redundancy;
22. assess asymmetry;
23. assess contradictions;
24. assess reader autonomy;
25. assess voice and rhythm;
26. assess originality;
27. assess ending openness.

---

# 10. Mandatory Final Report

The final output of Round 39 must contain:

## 1. General Diagnosis

State the overall condition of the work.

Distinguish:

* structural solidity;
* conceptual solidity;
* real vulnerabilities;
* unresolved but productive tensions;
* areas requiring intervention;
* areas that should remain untouched.

---

## 2. Current Architecture

Represent the architecture as:

**Rhizome → General Domains → Assemblages → Nodes → Inter-Stem Nodes → Transformations / Propagations**

Do not represent A–E as a causal or hierarchical sequence.

---

## 3. Structural Strengths

Identify what is already working.

Include negative findings such as:

* no significant redundancy detected;
* no relevant anthropomorphism detected;
* no structural hierarchy detected;
* no determinist formulation detected.

---

## 4. Real Problems

List only findings that justify intervention.

Group related findings by root issue.

---

## 5. Redundancies

Distinguish:

* necessary recurrence;
* productive overlap;
* partial redundancy;
* genuine redundancy.

---

## 6. Nodes

For each node:

* function;
* relational concentration;
* tensions;
* transformation;
* differentiation;
* status.

---

## 7. Connections

Identify significant connections between:

* assemblages;
* nodes;
* inter-stem nodes;
* scales;
* domains.

Do not demand complete connectivity.

---

## 8. Propagations

For each genuine propagation identify:

* initial transformation;
* pathway;
* receiving site;
* changed condition;
* transformation at receiving site;
* contingencies;
* interruption or modification;
* possible feedback.

---

## 9. Contradictions

Distinguish:

* genuine contradictions;
* productive tensions;
* contextual differences;
* apparent contradictions;
* unresolved ambiguities.

---

## 10. Philosophical Risks

Address, where relevant:

* anthropomorphism;
* technological determinism;
* unjustified emergence;
* consciousness claims;
* understanding claims;
* agency;
* extended cognition;
* knowledge;
* authority;
* truth;
* power.

---

## 11. Semantic and Stylistic Risks

Identify only meaningful issues involving:

* semantic scope;
* modality;
* attribution;
* terminology;
* ambiguity;
* voice;
* rhythm;
* density;
* artificial smoothing;
* unnecessary academicization.

---

## 12. Decisions to Preserve

Explicitly list architectural decisions that should **not** be reopened.

This section is mandatory.

---

## 13. Recommended Interventions

Divide recommendations into:

### Necessary

Changes required to prevent a significant conceptual, structural, methodological, or argumentative problem.

### Advisable

Changes that materially improve precision or architecture but are not strictly necessary.

### Optional

Changes that may improve presentation without significant architectural effect.

### Not Recommended

Changes that would make the text more orderly but would reduce its conceptual or cartographic integrity.

### Leave Unchanged

Elements that work adequately and should not be modified.

---

## 14. Final Verdict

Answer:

> **Is the architecture sufficiently consolidated for final editing?**

The answer must not be based on a numerical score.

It should state:

* what remains unresolved;
* whether unresolved issues are structural or local;
* whether the A–E architecture is stable;
* whether inter-stem nodes are sufficiently justified;
* whether the text can proceed to final editing;
* what must happen before editing, if anything.

---

# 11. Cross-Round Dependency Rules

Later rounds may use findings from earlier rounds, but must not mechanically inherit their conclusions.

A later Skill may:

* confirm;
* refine;
* qualify;
* contradict;
* absorb;
* downgrade;
* upgrade;

an earlier finding.

When findings conflict, return to:

1. source evidence;
2. exact location;
3. conceptual dimension;
4. scope;
5. confidence;
6. whether the apparent conflict is actually a productive tension.

---

# 12. Blind-Pass Isolation

Rounds 10, 20, and 25 must be treated as distinct reader experiments.

For each blind pass:

* suppress previous diagnoses;
* do not reveal intended architecture;
* do not instruct the reader what the nodes are;
* do not tell the reader what they should notice;
* use only the source and the reader model.

Afterward, compare the results.

The purpose is not to make all blind readings agree.

Divergence can reveal:

* ambiguity;
* productive multiplicity;
* local opacity;
* structural weakness;
* reader-dependent interpretation.

---

# 13. Transversal Review Before Structural Intervention

Before recommending:

* creation of a node;
* elimination of a node;
* merging nodes;
* splitting a node;
* creating an inter-stem node;
* changing the architecture;
* adding a major section;

perform a transversal review.

Ask:

1. Does the problem actually originate here?
2. Is the proposed component already represented elsewhere?
3. Can the function be absorbed?
4. Would the modification create redundancy?
5. Would it create artificial symmetry?
6. Would it create a hidden hierarchy?
7. Would it convert a relational map into a conventional taxonomy?
8. Would it obscure an existing connection?
9. Would it reduce productive asymmetry?
10. Does it increase cartographic precision?

A new node requires strong evidence.

---

# 14. New Node Threshold

A new node must not be created merely because an important topic is missing.

Require evidence of:

* distinct relations;
* identifiable tensions;
* concentration;
* recognizable dynamic;
* transformation;
* unique function;
* sufficient development;
* architectural necessity;
* transversal differentiation from existing nodes.

If these conditions are not met:

* absorb;
* relocate;
* reformulate;
* compress;
* or leave the material distributed.

Do not create a node to achieve symmetry.

---

# 15. Inter-Stem Threshold

An inter-stem node must satisfy:

**Assemblages → Relations → Tensions → Concentration → Modification of Conditions → Transformation → Possible Propagation**

The following are insufficient by themselves:

* interdisciplinary relevance;
* importance;
* thematic overlap;
* “AI + X”;
* two-way influence;
* adjacency;
* shared vocabulary.

The title cannot establish inter-stem status.

---

# 16. Propagation Threshold

A propagation requires:

1. an identifiable transformation;
2. a pathway or relational mechanism;
3. another site or configuration;
4. a changed condition there;
5. a resulting transformation or dynamic.

If the only evidence is that "AI affects X," do not classify the relation as propagation.

---

# 17. Emergence Threshold

Do not classify a phenomenon as emergent merely because it is:

* new;
* complex;
* unexpected;
* nonlinear;
* large-scale;
* difficult to predict;
* distributed;
* produced by many elements.

Require a relational configuration whose properties cannot adequately be attributed to a single element alone.

---

# 18. External Evidence

External evidence should be introduced only when required by the analytical task.

Examples:

* empirical verification;
* factual correction;
* historical claim;
* technical claim;
* current institutional information;
* comparison requiring external evidence.

External evidence must remain distinguishable from:

* source evidence;
* analytical inference;
* interpretation.

Do not add citations merely to make philosophical prose appear authoritative.

---

# 19. No Automatic Rewrite Phase

The 39-round audit is an **analysis workflow**.

It does not automatically rewrite the source.

After Round 39, the user may request a separate editing phase.

That editing phase must use the final audit as a diagnostic basis and must preserve:

* authorial voice;
* conceptual distinctions;
* productive tensions;
* meaningful asymmetries;
* open-endedness;
* cartographic character.

---

# 20. Final Intervention Test

Before any recommended modification, ask:

> **Does this change increase cartographic precision, or does it merely increase order?**

Reject modifications whose primary justification is:

* symmetry;
* tidiness;
* conventional academic structure;
* stylistic uniformity;
* maximum compression;
* complete connectivity;
* exhaustive categorization.

---

# 21. Completion Condition

The workflow is complete only when:

* all 39 rounds have been executed;
* findings have been recorded;
* duplicate findings have been consolidated;
* architectural findings have been separated from local findings;
* productive tensions have been preserved;
* closed decisions have been checked;
* A–E have been evaluated;
* connections and propagations have been distinguished;
* philosophical and semantic risks have been assessed;
* reader and voice audits have been incorporated;
* Round 39 has produced the integrated diagnosis.

The final audit must make clear:

**what must change, what may change, what should not change, and why.**

---

# 22. Core Operating Principle

The workflow must never optimize the text simply for order.

Its governing question is:

> **Does the proposed intervention make the relational field more visible without pretending that the map exhausts the rhizome?**

The final methodological principle is:

> **A more orderly text is not necessarily a better map.**

> **A larger architecture is not necessarily a more complex architecture.**

> **A more polished formulation is not necessarily a more precise formulation.**

> **The map stabilizes the gaze. The rhizome remains in motion. Cartography attempts to keep that difference visible.**
