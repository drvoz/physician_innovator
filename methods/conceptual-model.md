## Overview

In seven steps you will build a conceptual model: a diagram, with a short narrative, that shows the key concepts in your research question and how you believe they relate. It becomes the backbone of your literature review, hypotheses, measures and analysis plan.

**A conceptual model** is a simplified picture of how part of the world works, drawn from theory and evidence. Boxes are concepts; arrows are the relationships you propose.

| Tool | What it shows | Main question it answers |
| --- | --- | --- |
| Theory | General explanation of a phenomenon, tested across many studies | Why does this happen in general? |
| Conceptual model | The specific concepts and relationships in *your* study, informed by theory | What do I think is going on, and what will I test? |
| [Logic model](logic-model.html) | How a program's resources and activities lead to its outcomes | How will this project produce results? |

**What you will produce:**

- A one-sentence research question
- A table of defined concepts
- A labeled diagram of concepts and relationships
- A list of testable hypotheses
- A measurement plan linking each concept to a measure

**The seven steps:**

1. Define the research question and the outcome
2. Review the literature and choose a guiding theory or framework
3. Identify and define the key concepts
4. Map the relationships between concepts
5. Draw the model and state hypotheses
6. Operationalize each concept into measures
7. Critique and revise

## Step 1: Define the research question and the outcome

**Goal:** a focused question with one clearly named outcome. The outcome is the box your whole model points toward.

1. Write down the problem that interests you in plain language.
2. Name the **outcome**: the condition, behavior or result you want to explain or change.
3. Name the **population** and **setting** you care about.
4. Name the main **factor** you think influences the outcome (an exposure, characteristic or intervention).
5. Combine them into one question. Use a structure such as PICO (population, intervention or exposure, comparison, outcome) to check that nothing is missing.
6. Narrow it until it could be answered in a single study.

**Template:** Among [population] in [setting], how does [factor] relate to [outcome]?

**Too broad:** "What affects student wellbeing?" **Focused:** "Among first-year health professions students, how does sleep duration relate to exam performance?"

**New to research questions?** See the [deeper explanation](terms.html#research-question): what makes a good question, question types, common mistakes and a self-test.

**Output:** a one-sentence research question with a named outcome.

## Step 2: Review the literature and choose a guiding theory or framework

**Goal:** ground your model in what is already known, so your arrows are justified rather than guessed.

1. Search for studies on your outcome and your main factor. Look first for systematic reviews.
2. As you read, keep a log of the concepts each study used and the relationships it found, with the direction and strength of each.
3. Note which existing theories or frameworks the studies cite. Common examples in health research include the Social Ecological Model, Health Belief Model, Theory of Planned Behavior, Social Cognitive Theory and Andersen's Behavioral Model of Health Services Use.
4. Choose one theory or framework that best fits your question. You may adapt it, but say what you changed and why.
5. Identify gaps: relationships that are untested, contested or unstudied in your population. Those gaps are where your study adds value.

**New to these theories?** [Brief guides to each](terms.html#common-theories-and-frameworks-in-health-research), with examples and a short how-to-choose.

**Template: literature log**

| Source | Concepts studied | Relationship found (direction, strength) | Population | Theory used | Notes or gaps |
| --- | --- | --- | --- | --- | --- |
| &nbsp; | | | | | |
| &nbsp; | | | | | |

**Output:** a literature log, a chosen theory or framework, and a short list of gaps.

## Step 3: Identify and define the key concepts

**Goal:** a short list of clearly defined concepts, each with a role in the model.

1. From your literature log, list every concept that plausibly affects your outcome.
2. Keep the ones that matter most for your question and that the theory highlights. Aim for five to nine; more becomes hard to study and to read.
3. Write a **conceptual definition** for each: what it means in words, citing a source where possible.
4. Assign each concept a role:
    - **Exposure or independent variable:** the main factor you study
    - **Outcome or dependent variable:** what you explain
    - **Mediator:** the pathway through which the exposure affects the outcome
    - **Moderator:** something that changes the strength or direction of a relationship
    - **Confounder:** something that affects both exposure and outcome and could create a false link
5. Group related concepts by level if your theory uses levels (individual, interpersonal, organizational, community, policy).

<div class="rolekey" aria-label="Role colors used in every diagram">
<span class="role r-exp">Exposure</span>
<span class="role r-med">Mediator</span>
<span class="role r-mod">Moderator</span>
<span class="role r-conf">Confounder</span>
<span class="role r-out">Outcome</span>
</div>

These five colors mark the same roles in every diagram on these pages. Use them for your Mural sticky notes too, so a role looks the same on the page and on the board.

**Template: concept table**

| Concept | Conceptual definition | Role in model | Level | Source |
| --- | --- | --- | --- | --- |
| &nbsp; | | | | |
| &nbsp; | | | | |
| &nbsp; | | | | |

**Output:** a concept table with definitions and roles.

## Step 4: Map the relationships between concepts

**Goal:** decide which concepts influence which, in what direction, and through what pathway.

Most conceptual models are built from the same five roles. The generic model below shows how they connect.

<figure class="dia">
<svg viewBox="0 0 760 416" role="img" aria-label="Arrows run from causes toward the outcome you explain">
<defs><marker id="cm-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path class="arr" d="M0 0L10 5L0 10z"/></marker></defs>
<text class="t ttl" x="24" y="28">Arrows run from causes toward the outcome you explain</text>
<g class="ln dash">
<path d="M300 112V144H128V176" marker-end="url(#cm-arrow)"/>
<path d="M460 112V144H632V176" marker-end="url(#cm-arrow)"/>
</g>
<g class="ln">
<path d="M220 204H288" marker-end="url(#cm-arrow)"/>
<path d="M472 204H540" marker-end="url(#cm-arrow)"/>
<path d="M128 232V290H632V232" marker-end="url(#cm-arrow)"/>
<path d="M380 336V294" marker-end="url(#cm-arrow)"/>
</g>
<rect class="box r-conf" x="264" y="56" width="232" height="56" rx="8"/>
<text class="t n" x="380" y="80" text-anchor="middle">Confounder</text>
<text class="t q" x="380" y="98" text-anchor="middle">affects both; control for it</text>
<rect class="box r-exp" x="36" y="176" width="184" height="56" rx="8"/>
<text class="t n" x="128" y="200" text-anchor="middle">Exposure</text>
<text class="t q" x="128" y="218" text-anchor="middle">main factor you study</text>
<rect class="box r-med" x="288" y="176" width="184" height="56" rx="8"/>
<text class="t n" x="380" y="200" text-anchor="middle">Mediator</text>
<text class="t q" x="380" y="218" text-anchor="middle">the pathway: how it works</text>
<rect class="box r-out" x="540" y="176" width="184" height="56" rx="8"/>
<text class="t n" x="632" y="200" text-anchor="middle">Outcome</text>
<text class="t" x="632" y="218" text-anchor="middle">what you want to explain</text>
<rect class="box r-mod" x="264" y="336" width="232" height="56" rx="8"/>
<text class="t n" x="380" y="360" text-anchor="middle">Moderator</text>
<text class="t q" x="380" y="378" text-anchor="middle">changes the strength of a link</text>
<text class="t q" x="214" y="136" text-anchor="middle">controlled for</text>
<text class="t q" x="546" y="136" text-anchor="middle">controlled for</text>
<text class="t n" x="254" y="196" text-anchor="middle">+</text>
<text class="t n" x="506" y="196" text-anchor="middle">+</text>
<text class="t q" x="254" y="282" text-anchor="middle">direct effect</text>
<text class="t q" x="380" y="160" text-anchor="middle">indirect effect</text>
<text class="t q" x="392" y="318">modifies the direct effect</text>
</svg>
</figure>

Read it left to right: the exposure affects the outcome directly and through the mediator; the moderator changes how strong that effect is; the confounder is measured and adjusted for.

**Example using the Step 1 question** (sleep and exam performance):

- **Exposure:** sleep duration
- **Mediator:** attention and memory consolidation
- **Moderator:** study habits, which may make sleep matter more or less
- **Confounder:** workload or stress, which can shorten sleep and lower scores at the same time
- **Outcome:** exam performance

**How to map:**

1. Write each concept from Step 3 on a sticky note or card.
2. Place the outcome on the right and the exposure on the left.
3. For each other concept ask: does it sit between them (mediator), change their link (moderator), or affect both (confounder)?
4. Draw an arrow only where theory or evidence supports a relationship. Cite the source for each.
5. Note the expected direction of each arrow: positive (+) or negative (−).
6. Remove concepts with no arrows; they do not belong in this model.

**Output:** a draft map with every arrow justified.

## Step 5: Draw the model and state hypotheses

**Goal:** a clean, readable diagram and a matching list of testable statements.

**Drawing conventions:**

- Boxes for concepts, one concept per box, with a short label.
- Arrows for proposed effects, pointing from cause to effect.
- Read left to right: background factors and exposure on the left, outcome on the right.
- A moderator's arrow points at the arrow it changes, not at a box.
- Mark expected direction on each arrow with **+** or **−**.
- Use a dashed line for a relationship you will control for but not test.
- Group concepts by level with a shaded band if your theory uses levels.
- Fit it on one page; if it does not fit, it is probably too complex for one study.

**Tools:** Mural is the default for this course: use sticky notes for concepts during mapping, then tidy them into boxes and connectors for the final diagram, and share the board with your peer reviewer for comments. Kumu suits more complex models: many concepts, feedback loops, or causal loop diagrams where you want each arrow to carry its evidence. PowerPoint, Google Drawings or draw.io work for a simple final version.

**Turn every arrow into a hypothesis:**

1. Write one statement per arrow you will test.
2. Include the direction of the expected effect.
3. Make it falsifiable: it must be possible for data to show you wrong.

**Template:** H[n]: Among [population], higher [concept A] will be associated with [higher / lower] [concept B]. For a moderator: the relationship between [A] and [B] will be [stronger / weaker] when [moderator] is [high / present].

**Write a short narrative** (one or two paragraphs) that walks the reader through the model left to right, citing the evidence behind each arrow.

**Output:** a labeled diagram, a numbered list of hypotheses and a narrative paragraph.

## Step 6: Operationalize each concept into measures

**Goal:** every box in your model can be measured, so every hypothesis can be tested.

1. For each concept, write an **operational definition**: exactly how you will observe or measure it in your study.
2. Prefer validated instruments (published scales or standard measures) over questions you write yourself. Note their reliability and validity evidence.
3. Record the data source: survey, interview, observation, medical record, administrative data or a device.
4. Record the level of measurement (categorical, ordinal, continuous), since it shapes your analysis.
5. Check the fit: does the measure capture the concept as you defined it in Step 3? If not, change the measure or narrow the definition.
6. Match each hypothesis to the measures and the planned analysis.

**Template: measurement plan**

| Concept | Operational definition | Instrument or measure | Data source | Level of measurement | Hypotheses it serves |
| --- | --- | --- | --- | --- | --- |
| &nbsp; | | | | | |
| &nbsp; | | | | | |
| &nbsp; | | | | | |

**Output:** a measurement plan covering every concept in the model.

## Step 7: Critique and revise

**Goal:** a model that a skeptical reader would accept as clear, justified and testable.

1. Explain your model aloud to a classmate in two minutes without notes. Where you stumble, the model is unclear.
2. Ask a peer to review it with the checklist below, then swap.
3. Share it with your advisor or a content expert and ask: "What is missing, and what would you remove?"
4. Revise, and keep each version so you can show how the model evolved.
5. Return to the model after data collection to compare what you expected with what you found.

**Review checklist:**

- [ ] The research question names one population, one main factor and one outcome
- [ ] Every concept has a conceptual and an operational definition
- [ ] Every arrow is supported by theory or cited evidence
- [ ] The guiding theory or framework is named, and any changes are explained
- [ ] Mediators, moderators and confounders are labeled correctly
- [ ] Arrows show direction, and expected signs (+ or −) are marked
- [ ] Every tested arrow has a matching hypothesis
- [ ] Every concept has a feasible measure
- [ ] The diagram fits on one page and reads left to right
- [ ] A reader new to the topic can follow it with the narrative alone

**Practice exercise (about 60 minutes):**

1. Pick a topic from your field and write a research question using the Step 1 template (10 min).
2. List six to eight concepts and assign each a role (15 min).
3. Sketch the model on paper using the Step 5 conventions (15 min).
4. Write three hypotheses (10 min).
5. Swap with a partner and review each other's work with the checklist (10 min).

**Facilitated version with synthetic rural data:** [Sheffield practice exercise](sheffield-exercise.html) (20 minutes).
