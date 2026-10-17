Plain-language definitions of the terms used in the [conceptual model](conceptual-model.html) and [logic model](logic-model.html) tutorials, with longer explanations where novices most often get stuck.

## Research question

The single question your study is designed to answer. It is the anchor for everything that follows: your concepts, diagram, hypotheses, measures and analysis all have to answer it, so a vague question produces a vague model. Spend more time here than feels necessary.

**Check it against FINER** (Hulley and colleagues, *Designing Clinical Research*):

- **Feasible:** you can reach enough participants, data and time to answer it
- **Interesting:** it matters to you and to others in your field
- **Novel:** it confirms, extends or challenges what is known, rather than repeating it
- **Ethical:** answering it does not put people at undue risk
- **Relevant:** the answer could change practice, policy or future research

**Know what kind of question you are asking.** The verb signals the study you will need:

| Question type | Typical wording | What it needs |
| --- | --- | --- |
| Descriptive | "What is...?" "How common is...?" | A clear population and measure |
| Relational | "How does X relate to Y?" | Measures of both X and Y in the same people |
| Causal or comparative | "Does X cause, improve or reduce Y?" | A comparison group and control of confounders |

**Common novice mistakes:**

- **Too broad:** several outcomes or populations at once. Pick one of each.
- **Yes or no:** "Is sleep important?" invites a one-word answer. Ask *how* or *how much*.
- **Answer already known:** check the literature first; if it is settled, ask what is still uncertain.
- **Solution built in:** "How can we get students to sleep more?" assumes the answer. Study the relationship first.
- **Unmeasurable words:** "better", "quality" or "success" need a definition you can measure.

**Narrow it in stages:** topic (student health) → problem (exam scores drop in first year) → factor (sleep) → question (Among first-year health professions students, how does sleep duration relate to exam performance?).

**Self-test before moving on:** Can you name the single outcome? Could a friend outside your field restate the question? Could you sketch, roughly, the data that would answer it? If any answer is no, revise the question.

## Common theories and frameworks in health research

A theory gives your conceptual model a tested starting point: it tells you which concepts matter and which arrows earlier researchers have already justified. Choose the one whose core question is closest to yours, then adapt it.

| Theory or framework | Level it focuses on | Best when your question is about |
| --- | --- | --- |
| [Social Ecological Model](#social-ecological-model) | Many levels, individual to policy | How surroundings, not just individuals, shape health |
| [Health Belief Model](#health-belief-model) | Individual | Why people do or don't take a preventive or screening action |
| [Theory of Planned Behavior](#theory-of-planned-behavior) | Individual, with social norms | Predicting a specific behavior from intentions |
| [Social Cognitive Theory](#social-cognitive-theory) | Person, behavior and environment together | Learning and maintaining behaviors; building confidence |
| [Andersen's Behavioral Model](#andersens-behavioral-model-of-health-services-use) | Individual and health system | Who uses health services, and why |

### Social Ecological Model

<figure class="dia">
<svg viewBox="0 0 760 428" role="img" aria-label="Influences on health sit in nested layers">
<text class="t ttl" x="24" y="24">Influences on health sit in nested layers</text>
<ellipse class="box" cx="380" cy="230" rx="350" ry="180"/>
<ellipse class="box" cx="380" cy="230" rx="280" ry="144"/>
<ellipse class="box" cx="380" cy="230" rx="210" ry="108"/>
<ellipse class="box" cx="380" cy="230" rx="140" ry="72"/>
<ellipse class="box r-out" cx="380" cy="230" rx="76" ry="36"/>
<text class="t n" x="380" y="66" text-anchor="middle">Public policy</text>
<text class="t q" x="380" y="80" text-anchor="middle">laws, regulations, funding</text>
<text class="t n" x="380" y="102" text-anchor="middle">Community</text>
<text class="t q" x="380" y="116" text-anchor="middle">neighborhoods, norms, resources</text>
<text class="t n" x="380" y="138" text-anchor="middle">Organizational</text>
<text class="t q" x="380" y="152" text-anchor="middle">schools, workplaces, clinics</text>
<text class="t n" x="380" y="174" text-anchor="middle">Interpersonal</text>
<text class="t q" x="380" y="188" text-anchor="middle">family, friends, peers</text>
<text class="t n" x="380" y="228" text-anchor="middle">Individual</text>
<text class="t q" x="380" y="243" text-anchor="middle">beliefs, biology</text>
</svg>
</figure>

**Core idea:** health is shaped by nested layers of influence, not by individual choice alone. It grew from Bronfenbrenner's ecological systems theory and was adapted for health promotion by McLeroy and colleagues in 1988.

**Key levels:** individual (knowledge, attitudes, biology) · interpersonal (family, friends, peers) · organizational (schools, workplaces, clinics) · community (neighborhoods, norms, resources) · public policy (laws, regulations, funding).

**How it shapes your model:** group your concepts into bands by level, and ask whether factors at higher levels affect the outcome directly or through individual factors.

**Example:** campus food environment (community) → healthy eating habits (individual) → student BMI.

**Watch out:** it is a broad organizing framework rather than a predictive theory, so you still need evidence for each arrow. Studying every level at once is rarely feasible.

### Health Belief Model

<figure class="dia">
<svg viewBox="0 0 760 326" role="img" aria-label="Beliefs about risk and payoff drive the decision to act">
<text class="t ttl" x="24" y="24">Beliefs about risk and payoff drive the decision to act</text>
<defs><marker id="hbm-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path class="arr" d="M0 0L10 5L0 10z"/></marker></defs>
<g class="ln">
<path d="M244 76H284M244 124H284M244 172H284M244 220H284M244 268H284M284 76V268"/>
<path d="M284 172H330" marker-end="url(#hbm-arrow)"/>
<path d="M420 96V142" marker-end="url(#hbm-arrow)"/>
<path d="M510 172H566" marker-end="url(#hbm-arrow)"/>
</g>
<rect class="box" x="24" y="56" width="220" height="40" rx="8"/>
<rect class="box" x="24" y="104" width="220" height="40" rx="8"/>
<rect class="box" x="24" y="152" width="220" height="40" rx="8"/>
<rect class="box" x="24" y="200" width="220" height="40" rx="8"/>
<rect class="box" x="24" y="248" width="220" height="40" rx="8"/>
<text class="t n" x="134" y="80" text-anchor="middle">Perceived susceptibility</text>
<text class="t n" x="134" y="128" text-anchor="middle">Perceived severity</text>
<text class="t n" x="134" y="176" text-anchor="middle">Perceived benefits (+)</text>
<text class="t n" x="134" y="224" text-anchor="middle">Perceived barriers (−)</text>
<text class="t n" x="134" y="272" text-anchor="middle">Self-efficacy</text>
<rect class="box" x="330" y="56" width="180" height="40" rx="8"/>
<text class="t n" x="420" y="80" text-anchor="middle">Cues to action</text>
<rect class="box" x="330" y="142" width="180" height="60" rx="8"/>
<text class="t n" x="420" y="168" text-anchor="middle">Likelihood of</text>
<text class="t n" x="420" y="184" text-anchor="middle">taking action</text>
<rect class="box r-out" x="566" y="142" width="170" height="60" rx="8"/>
<text class="t n" x="651" y="168" text-anchor="middle">Health behavior</text>
<text class="t" x="651" y="186" text-anchor="middle">e.g. getting screened</text>
<text class="t q" x="24" y="312">Background factors such as age, education and culture shape every belief.</text>
</svg>
</figure>

**Core idea:** people take a health action when they believe they are at risk, that the problem is serious, and that acting will help more than it costs. It was developed in the 1950s by social psychologists in the US Public Health Service to understand low uptake of tuberculosis screening.

**Key constructs:** perceived susceptibility · perceived severity · perceived benefits · perceived barriers · cues to action · self-efficacy (added later).

**How it shapes your model:** the perceptions sit on the left as predictors of a single health behavior on the right; demographics often act as background or moderating factors.

**Example:** perceived barriers (cost, time) → flu vaccination among nursing students.

**Watch out:** it focuses on individual beliefs and gives little weight to social, economic or environmental conditions, or to habits and emotion.

### Theory of Planned Behavior

<figure class="dia">
<svg viewBox="0 0 760 320" role="img" aria-label="Intention carries beliefs into behavior">
<text class="t ttl" x="24" y="24">Intention carries beliefs into behavior</text>
<defs><marker id="tpb-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path class="arr" d="M0 0L10 5L0 10z"/></marker></defs>
<g class="ln">
<path d="M254 80H292M254 160H292M254 240H292M292 80V240"/>
<path d="M292 160H330" marker-end="url(#tpb-arrow)"/>
<path d="M490 160H566" marker-end="url(#tpb-arrow)"/>
<path d="M139 264V300H651V184" marker-end="url(#tpb-arrow)"/>
</g>
<rect class="box" x="24" y="56" width="230" height="48" rx="8"/>
<text class="t n" x="40" y="76">Attitude</text>
<text class="t q" x="40" y="94">is it good or bad?</text>
<rect class="box" x="24" y="136" width="230" height="48" rx="8"/>
<text class="t n" x="40" y="156">Subjective norms</text>
<text class="t q" x="40" y="174">do others want me to?</text>
<rect class="box" x="24" y="216" width="230" height="48" rx="8"/>
<text class="t n" x="40" y="236">Perceived behavioral control</text>
<text class="t q" x="40" y="254">can I do it?</text>
<rect class="box r-med" x="330" y="136" width="160" height="48" rx="8"/>
<text class="t n" x="410" y="156" text-anchor="middle">Intention</text>
<text class="t q" x="410" y="174" text-anchor="middle">the built-in mediator</text>
<rect class="box r-out" x="566" y="136" width="170" height="48" rx="8"/>
<text class="t n" x="651" y="164" text-anchor="middle">Behavior</text>
<text class="t q" x="395" y="292" text-anchor="middle">control can also act on behavior directly</text>
</svg>
</figure>

**Core idea:** the best predictor of a behavior is the intention to perform it, and intention is shaped by three things. Developed by Icek Ajzen, published in full in 1991.

**Key constructs:** attitude toward the behavior (is it good or bad?) · subjective norms (do important others want me to?) · perceived behavioral control (can I do it?) → intention → behavior. Perceived control can also affect behavior directly.

**How it shapes your model:** intention is a built-in mediator between the three beliefs and the behavior.

**Example:** subjective norms among classmates → intention to use a study planner → study planner use.

**Watch out:** people do not always act on intentions (the intention–behavior gap), and the theory says little about habit or environment.

### Social Cognitive Theory

<figure class="dia">
<svg viewBox="0 0 760 340" role="img" aria-label="Person, behavior and environment shape one another">
<text class="t ttl" x="24" y="24">Person, behavior and environment shape one another</text>
<defs><marker id="sct-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path class="arr" d="M0 0L10 5L0 10z"/></marker></defs>
<g class="ln">
<path d="M300 124L180 244" marker-start="url(#sct-arrow)" marker-end="url(#sct-arrow)"/>
<path d="M460 124L580 244" marker-start="url(#sct-arrow)" marker-end="url(#sct-arrow)"/>
<path d="M260 280H500" marker-start="url(#sct-arrow)" marker-end="url(#sct-arrow)"/>
</g>
<rect class="box r-med" x="270" y="52" width="220" height="72" rx="8"/>
<text class="t n" x="380" y="76" text-anchor="middle">Person</text>
<text class="t q" x="380" y="96" text-anchor="middle">self-efficacy, outcome</text>
<text class="t q" x="380" y="112" text-anchor="middle">expectations, knowledge</text>
<rect class="box r-out" x="40" y="244" width="220" height="72" rx="8"/>
<text class="t n" x="150" y="272" text-anchor="middle">Behavior</text>
<text class="t q" x="150" y="292" text-anchor="middle">skills, practice, habits</text>
<rect class="box" x="500" y="244" width="220" height="72" rx="8"/>
<text class="t n" x="610" y="272" text-anchor="middle">Environment</text>
<text class="t q" x="610" y="292" text-anchor="middle">role models, support, barriers</text>
<text class="t q" x="380" y="200" text-anchor="middle">reciprocal determinism</text>
</svg>
</figure>

**Core idea:** behavior, personal factors and the environment continually influence one another, a process Bandura called reciprocal determinism. People learn by doing and by watching others. Developed by Albert Bandura, named in 1986.

**Key constructs:** self-efficacy (confidence you can do it) · outcome expectations · observational learning (modeling) · behavioral capability (knowledge and skill) · reinforcement · environment.

**How it shapes your model:** self-efficacy is often the central mediator; the environment and role models feed into it, and feedback loops show behavior changing the person and environment in turn.

**Example:** simulation practice (skill) → self-efficacy → performance in a real clinical event.

**Watch out:** it has many constructs and loose boundaries, so pick the few that fit your question rather than drawing all of them. Two-way arrows are hard to test in a single study.

### Andersen's Behavioral Model of Health Services Use

<figure class="dia">
<svg viewBox="0 0 760 340" role="img" aria-label="Predisposing, enabling and need factors drive use of care">
<text class="t ttl" x="24" y="24">Predisposing, enabling and need factors drive use of care</text>
<defs><marker id="and-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path class="arr" d="M0 0L10 5L0 10z"/></marker></defs>
<g class="ln">
<path d="M264 82H296M264 154H296M264 226H296M296 82V226"/>
<path d="M296 154H330" marker-end="url(#and-arrow)"/>
<path d="M510 154H560" marker-end="url(#and-arrow)"/>
</g>
<g class="ln dash"><path d="M420 284V184" marker-end="url(#and-arrow)"/></g>
<rect class="box" x="24" y="52" width="240" height="60" rx="8"/>
<text class="t n" x="40" y="76">Predisposing</text>
<text class="t q" x="40" y="94">age, education, health beliefs</text>
<rect class="box" x="24" y="124" width="240" height="60" rx="8"/>
<text class="t n" x="40" y="148">Enabling</text>
<text class="t q" x="40" y="166">insurance, income, transport</text>
<rect class="box" x="24" y="196" width="240" height="60" rx="8"/>
<text class="t n" x="40" y="220">Need</text>
<text class="t q" x="40" y="238">perceived and evaluated health</text>
<rect class="box r-med" x="330" y="124" width="180" height="60" rx="8"/>
<text class="t n" x="420" y="150" text-anchor="middle">Use of health</text>
<text class="t n" x="420" y="168" text-anchor="middle">services</text>
<rect class="box r-out" x="560" y="124" width="176" height="60" rx="8"/>
<text class="t n" x="648" y="150" text-anchor="middle">Health outcomes</text>
<text class="t q" x="648" y="168" text-anchor="middle">status, satisfaction</text>
<rect class="band" x="24" y="284" width="712" height="40" rx="8"/>
<text class="t" x="40" y="308">Later versions add the health system and contextual factors</text>
</svg>
</figure>

**Core idea:** whether people use health services depends on what predisposes them, what enables or blocks them, and how much they need care. Developed by Ronald Andersen in 1968 and revised several times since.

**Key constructs:** predisposing factors (age, education, health beliefs) · enabling factors (insurance, income, transport, a regular source of care) · need factors (perceived and evaluated health status) → use of health services → health outcomes. Later versions add the health system and contextual factors.

**How it shapes your model:** sort concepts into the three columns; health services use usually sits as the outcome or as a mediator before health outcomes.

**Example:** transportation access (enabling) → prenatal visit attendance → birth outcomes.

**Watch out:** it describes access well but explains less about the quality of care once received, or the decision-making inside a visit.

### Choosing among them

1. Name your outcome. Is it a behavior, a decision, use of a service, or a health status?
2. Ask where you think the main influences sit: in the person's beliefs, their social world, their environment, or the health system.
3. Pick the theory whose concepts best match those influences, and see which ones prior studies on your topic used.
4. It is fine to combine: for example, use the Social Ecological Model for the levels and the Health Belief Model for the individual-level concepts. Say clearly which parts come from which source.

## Other key terms

| Term | Meaning |
| --- | --- |
| Concept (construct) | An idea your study is about, such as stress or adherence, defined in words |
| Conceptual definition | What a concept means, in words, usually drawn from theory or prior research |
| Operational definition | Exactly how a concept will be observed or measured in your study |
| Exposure (independent variable) | The main factor you think influences the outcome |
| Outcome (dependent variable) | The condition, behavior or result you want to explain |
| Mediator | The pathway through which the exposure affects the outcome |
| Moderator | A factor that changes the strength or direction of a relationship |
| Confounder | A factor that affects both exposure and outcome and could create a false link |
| Hypothesis | A testable, directional prediction about a relationship in your model |
| Theory | A general explanation of why something happens, tested across many studies |
| Framework | An organizing structure of concepts, often drawn from one or more theories |
| Logic model | A one-page picture of how a program's inputs and activities lead to its outcomes |
| RE-AIM | A framework for judging impact: Reach, Effectiveness, Adoption, Implementation, Maintenance |
| RACI | A roles chart: Responsible, Accountable, Consulted, Informed |
| ERIC | Expert Recommendations for Implementing Change: a list of 73 named implementation strategies |
