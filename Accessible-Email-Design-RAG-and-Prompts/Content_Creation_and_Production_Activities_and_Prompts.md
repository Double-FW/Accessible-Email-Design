# Accessible Email Design: human-managed content creation and production activities and prompts

**Prepared:** 8 November 2026 · **Source revision:** `9073de0460c4c078a4aa19a4a87c190243da984d`  
**Source:** [Double-FW/Accessible-Email-Design](https://github.com/Double-FW/Accessible-Email-Design/tree/9073de0460c4c078a4aa19a4a87c190243da984d)  
**Audience:** authors, editors, designers, publishers, communication teams, producers, commissioners, access-service practitioners and technical/quality partners.

## Where the repository is useful

Use this compact guide to plan, draft, inspect and revise emails and newsletters so that meaning, sequence and actions survive visual, nonvisual, mobile and plain-text reading. The current AGENTS file provides a useful prepare/review/repair workflow while explicitly distinguishing content inspection from actual client testing.

The repository contains guidance, not an email validator, client test matrix or delivery system. Its 14pt minimum is a source-guide rule, not a universal WCAG threshold; any reconciliation with other profiles must be explicit. “Ragged-right” means left-aligned prose with uneven right edges in the guide’s Latin-script examples, not right-aligned text or a rule overriding other scripts. Preparation or review does not authorise sending or scheduling an email.

The activities below are an editorial application of the repository, not a claim that it already contains a complete organisational process. AI can organise material, draft options and scripts, identify inconsistencies and prepare specifications or evidence summaries. Authors and editors preserve factual meaning and editorial intent. Designers and technical practitioners implement and verify delivered formats. Qualified access-service specialists review their work, and affected audiences inform the experience. Accountable publishers/producers retain creative, acceptance, rights and release decisions. Assign these responsibilities to actual people locally; the examples do not establish a new team or approval body.

## How to use the prompts

1. Attach [RAG_Reference.md](RAG_Reference.md). For selective retrieval, use the source routes below and [Source_Coverage.md](Source_Coverage.md).
2. Replace bracketed inputs with the actual project brief, artefacts and evidence. Supply the target task, audience, platform/setting, constraints and intended decision. Treat missing information as unknown.
3. Use either example prompt for the activity. Both refer to this folder’s reference. Supply only appropriate project information; use anonymised research findings where possible.
4. Require source ID, filename and original section citations; distinguish source guidance, local proposal, observed result and uncertainty. Ask for evidence requests where an artefact cannot be inspected.
5. Review the result with the named human roles and record decisions. A prompt output is a draft editorial/production aid, not implementation or evidence that a test ran. Do not defer disabled people’s involvement until final testing.

**Reusable response contract:** “Use the attached RAG_Reference.md as the knowledge source. Cite source IDs, files and sections. Distinguish source statements, project evidence, recommendations and unknowns. Preserve applicable source identifiers. Do not invent research, capability, approvals or test results. Give a concrete content/production artefact, trade-offs, evidence requests and decisions for the human team.”

## Activity map

| Activity | Production stage | Expected output |
| --- | --- | --- |
| 1. Frame an email’s purpose, facts and actions | Communication commissioning | A communication brief and fact/action checklist. |
| 2. Structure concise, navigable email content | Copywriting and editorial design | A revised content outline and draft message structure. |
| 3. Specify semantic, maintainable email templates | Template production and implementation handoff | A template specification or annotated HTML-review brief. |
| 4. Apply readable typography, colour and alignment | Visual email design | A style/contrast review and proposed design revisions. |
| 5. Create purpose-based images and meaningful links | Asset production and content review | An image/alternative-text inventory and revised link labels. |
| 6. Plan responsive and client-dependent presentation | Responsive design and test commissioning | A client/environment test brief and responsive repair list. |
| 7. Maintain an equivalent plain-text version | Multi-representation publishing | A plain-text content specification and HTML/text parity review. |
| 8. Review, repair and re-review the final email | Pre-send QA and controlled reuse | A scoped review report, repaired draft and outstanding checks. |

## 1. Frame an email’s purpose, facts and actions

**Production stage:** Communication commissioning

**Retrieve:** [S001 — Email_Accessibility.md](RAG_Reference.md#s001); [S003 — AGENTS.md](RAG_Reference.md#s003).

**Relevant source sections:** Sections 1–2; AGENTS: Establish the request.

### Tasks the repository can support

- Define audience, purpose, tone and required reader action.
- Inventory trusted facts, destinations and supplied assets.
- Identify essential unknowns without adding invented content.

**Expected output:** A communication brief and fact/action checklist.

**Human review:** The communication owner confirms facts and destinations; preparation remains separate from dispatch.

### Example prompt 1

> Use the attached RAG to brief [email or newsletter]. Identify audience, required facts, intended action, language, tone, template and constraints. List supplied destinations and missing information rather than inventing links. Produce a content plan and source-grounded accessibility considerations, without sending or scheduling anything.

### Example prompt 2

> Challenge [email brief] against the RAG. Find competing actions, assumed audience knowledge, unverified destinations and essential information hidden in images. Propose a simpler brief while preserving required facts.

## 2. Structure concise, navigable email content

**Production stage:** Copywriting and editorial design

**Retrieve:** [S001 — Email_Accessibility.md](RAG_Reference.md#s001).

**Relevant source sections:** Sections 3–4 and 13–15.

### Tasks the repository can support

- Put facts and actions in a logical reading sequence.
- Use meaningful headings only where the message needs them.
- Edit for clarity without deleting necessary qualifications.

**Expected output:** A revised content outline and draft message structure.

**Human review:** The editor confirms meaning and action order before styling or implementation.

### Example prompt 1

> Using the RAG, restructure [email copy] for clear visual and screen-reader reading. Create only necessary headings, logical sections and an explicit action sequence. Preserve supplied facts, obligations and qualifications; explain material edits and mark ambiguous claims for the content owner.

### Example prompt 2

> Review [newsletter content] with the RAG. Identify overlong sections, headings used only as decoration and a visual order inconsistent with the intended sequence. Propose a concise source-preserving revision.

## 3. Specify semantic, maintainable email templates

**Production stage:** Template production and implementation handoff

**Retrieve:** [S001 — Email_Accessibility.md](RAG_Reference.md#s001).

**Relevant source sections:** Sections 3–4 and 9; AGENTS: Markup.

### Tasks the repository can support

- Specify reading order, meaningful heading structure and appropriate HTML.
- Distinguish data tables from necessary email layout tables.
- Document compatibility dependencies rather than assuming browser behaviour.

**Expected output:** A template specification or annotated HTML-review brief.

**Human review:** The email developer verifies implementation in the actual production/client chain.

### Example prompt 1

> Use the RAG to review [supplied email HTML/template]. Inspect reading sequence, heading structure, table purpose and avoidable markup complexity. Propose precise repairs and identify client-dependent behaviour needing testing. Do not assume an installed validator or claim client compatibility from code inspection alone.

### Example prompt 2

> Challenge [template handoff] against the RAG. Find layout tables exposed as false data relationships, visual-only section structure and absent content order under layout change. Return implementation questions and a meaningful test plan.

## 4. Apply readable typography, colour and alignment

**Production stage:** Visual email design

**Retrieve:** [S001 — Email_Accessibility.md](RAG_Reference.md#s001).

**Relevant source sections:** Sections 5–6 and 12; AGENTS: Typography and Alignment.

### Tasks the repository can support

- Apply source-guide typography rules with explicit scope.
- Keep colour-independent meaning and recognisable links.
- Check actual text presentation without universal font guarantees.

**Expected output:** A style/contrast review and proposed design revisions.

**Human review:** The designer checks rendered email; a source size recommendation is not proof of universal readability.

### Example prompt 1

> Using the RAG, review [email visual specification]. Apply the guide’s 14pt minimum as its own rule, not a WCAG universal minimum. Examine type, emphasis, contrast, link cues and left-aligned ragged-right Latin prose. Respect language/script context and mark unmeasured colour or rendering properties unverified.

### Example prompt 2

> Challenge [email styles] with the RAG. Identify colour-only instructions, justified or unintended right-aligned text, decorative fonts and essential text reduced for fit. Propose corrections and real-client checks without asserting a font is accessible to everyone.

## 5. Create purpose-based images and meaningful links

**Production stage:** Asset production and content review

**Retrieve:** [S001 — Email_Accessibility.md](RAG_Reference.md#s001).

**Relevant source sections:** Sections 7–8.

### Tasks the repository can support

- Separate decorative images from informative and linked images.
- Write alternatives based on the actual asset’s role.
- Make action text meaningful outside immediate visual context.

**Expected output:** An image/alternative-text inventory and revised link labels.

**Human review:** Editors verify destinations and visual meaning; unseen assets remain unverified.

### Example prompt 1

> Use the RAG and [email assets, purposes and verified destinations] to specify image alternatives and link labels. Use empty alt for decorative images, retain essential meaning elsewhere and make link text understandable in context and when encountered separately. Do not fabricate a description for an unseen asset.

### Example prompt 2

> Review [email with images and links] against the RAG. Find an alt attribute that conveys no useful meaning, text trapped in artwork and ambiguous repeated actions. Produce asset-specific repairs while preserving the intended message.

## 6. Plan responsive and client-dependent presentation

**Production stage:** Responsive design and test commissioning

**Retrieve:** [S001 — Email_Accessibility.md](RAG_Reference.md#s001); [S003 — AGENTS.md](RAG_Reference.md#s003).

**Relevant source sections:** Sections 10 and 13; Review and evidence boundaries.

### Tasks the repository can support

- Preserve sequence, information and actions on smaller screens.
- Define relevant clients, viewports and display conditions.
- Plan checks for hidden, clipped or reordered content.

**Expected output:** A client/environment test brief and responsive repair list.

**Human review:** The email developer/tester establishes actual rendering in the chosen delivery context.

### Example prompt 1

> Using the RAG, plan responsive verification for [email, platform and audience environments]. Specify supported clients/viewports and meaningful tasks, including reading sequence and action access when layout changes. Propose further checks such as images unavailable or display changes as local test cases, not capabilities guaranteed by the repository.

### Example prompt 2

> Challenge [responsive email implementation evidence] with the RAG. Identify a browser preview substituted for client testing, clipped actions or reordered meaning. Return actual observed issues, unknown contexts and proportionate retest needs.

## 7. Maintain an equivalent plain-text version

**Production stage:** Multi-representation publishing

**Retrieve:** [S001 — Email_Accessibility.md](RAG_Reference.md#s001).

**Relevant source sections:** Section 11; AGENTS: Draft from meaning.

### Tasks the repository can support

- Retain essential facts, sequence and actions in text form.
- Make destinations usable without visual buttons.
- Keep revisions synchronised across representations.

**Expected output:** A plain-text content specification and HTML/text parity review.

**Human review:** The content owner verifies parity; MIME packaging and sending need separate technical evidence.

### Example prompt 1

> Use the RAG and [approved HTML email content] to prepare a plain-text version with equivalent facts, sequence and actions. Preserve verified destinations and avoid decorative clutter. Distinguish content production from construction or testing of multipart delivery; do not claim a message was sent.

### Example prompt 2

> Compare [HTML and plain-text drafts] using the RAG. Identify missing qualifications, stale links, visual-only instructions and divergent actions. Propose a coordinated revision and delivery checks that remain outstanding.

## 8. Review, repair and re-review the final email

**Production stage:** Pre-send QA and controlled reuse

**Retrieve:** [S001 — Email_Accessibility.md](RAG_Reference.md#s001); [S003 — AGENTS.md](RAG_Reference.md#s003).

**Relevant source sections:** Section 16; AGENTS: Review, Repair and Decision format.

### Tasks the repository can support

- Inspect the final content and track evidence by property.
- Repair known issues and recheck changed versions.
- Separate markup/content checks from rendering and assistive-technology tests.

**Expected output:** A scoped review report, repaired draft and outstanding checks.

**Human review:** The communication owner decides readiness; a prepared draft and successful checks are not send authorisation.

### Example prompt 1

> Use the RAG to review [final email content and available evidence]. Report each relevant check as observed, failed, unverified or inapplicable with reasons. Repair supported issues, preserve facts and re-review the revised draft. State which client, AT or delivery properties could not be tested; do not send or claim full accessibility.

### Example prompt 2

> Audit [pre-send review record] against the RAG. Identify tests claimed without evidence, an earlier review applied to changed copy and missing plain-text parity. Produce an honest readiness summary and required next checks.

## Editorial and production decision record

For each adopted result, record the project/task, source revision and sections used, observed editorial/production issue, barrier or opportunity, chosen option and rejected alternatives, expected outcome, evidence available, assumptions, unresolved constraints, accountable person, next check and review trigger. Use actual names and dates when agreed; leave them unassigned when unknown. Record acceptance and residual risk only when the accountable person has made the decision.

Revisit the reference when repository sources change, a new platform or context is introduced, implementation changes invalidate assumptions, or user feedback exposes a barrier. Compare changed sources rather than silently replacing the basis of existing decisions.
