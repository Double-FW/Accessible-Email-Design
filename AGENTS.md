# Agent instructions for accessible email work

## Purpose and scope

Use this file when creating, reviewing, or revising accessible email content using this repository.

The repository’s three reference documents have distinct roles:

- `Email_Accessibility.md` is the authoritative source for the email-design guidance.
- `README.md` describes the repository and its intended use.
- `LICENSE` contains the repository’s license terms.

This repository contains guidance, not an installed email validator or delivery system. Do not assume it provides a test command, automation framework, schema, client matrix, or permission to send email.

## Core rules

1. Read `Email_Accessibility.md` before applying or describing its requirements.
2. Preserve the message’s intended meaning, required facts, and actions. Do not invent facts, destinations, approvals, or evidence.
3. Apply the source guide’s requirements without presenting recommendations or local choices as requirements from WCAG.
4. Distinguish what you checked from what you could not establish. Do not claim that a message is fully accessible or WCAG-conformant based only on this guidance or automated checks.
5. Do not send, schedule, or otherwise dispatch an email. A request to prepare or review content is not authorization to send it.
6. If necessary information or evidence is missing, ask for it or report the limitation. Do not guess and report a pass.

## Applying the source guide

Use the following checklist when it applies to the message being created or reviewed:

- **Purpose and sequence:** Keep content in an order that makes sense visually and when read by assistive technology.
- **Structure:** Use semantic headings to organize sections. Headings should express structure, not merely provide visual styling. Avoid inventing sections or headings when the message does not need them.
- **Typography:** Follow the guide’s minimum text size of 14pt. Prefer clear, simple typefaces; avoid decorative or script fonts and excessive emphasis.
- **Colour and contrast:** Use legible foreground and background combinations. Do not rely on colour alone to convey meaning. Preserve visible cues, such as underlines for links.
- **Images:** Choose alternative text according to each image’s purpose. Use empty alternative text (`alt=""`) for decorative images. Do not claim an image description is meaningful merely because an `alt` attribute exists.
- **Links:** Use descriptive link text that communicates purpose or destination. The source guide asks for links to make sense out of context; avoid vague labels such as “click here” or “read more.”
- **Markup:** Prefer clear, appropriate HTML structure. Use tables only when suitable for tabular data or necessary for email layout, and preserve meaningful relationships.
- **Responsive use:** Avoid layouts that make content difficult to read or use on small screens. Preserve content and actions when the layout changes.
- **Text alternative:** When producing an HTML email, provide a plain-text alternative if requested or if the delivery context supports multipart alternatives. Keep essential information and actions consistent between representations.
- **Alignment:** The guide’s explanation in sections 2 and 12 specifies left-aligned prose with uneven line endings on the right. Follow that stated behavior; do not interpret the section heading as an instruction to right-align text.
- **Layout and content:** Prefer clear sections, consistent presentation, and concise wording. Do not remove information needed to understand or act on the message.

These checks are a practical reading of the source guide. They do not establish that the message works in every email client or for every person.

## Workflow for creating or revising an email

### 1. Establish the request

Identify, from the user’s instructions and supplied material:

- the message’s purpose and intended audience
- required facts, wording, and actions
- the intended language
- any supplied HTML, template, or plain-text content
- constraints such as format, tone, or length

Use only facts and destinations supplied by the user or an explicitly identified trusted source. If an essential fact or destination is missing or contradictory, ask for clarification instead of filling the gap.

### 2. Draft from meaning, not from assumptions

Organize the content before styling it. Preserve its essential facts and action sequence. Use a simple structure and readable wording. Do not add images, claims, links, or interactive elements unless they serve the stated purpose and have adequate source information.

When producing both HTML and plain text, keep the same essential facts, sequence, and actions in both. Do not imply that MIME construction or delivery was tested unless it actually was.

### 3. Review the final content

Review the complete output, including headings, links, image alternatives, footers, and any supplied text alternative. Compare it with the user’s stated requirements and the checklist above.

If you can inspect HTML, you may check properties visible in the supplied markup, such as heading elements, link text, `alt` attributes, declared language, and inline styles. Such inspection does not prove how an email client will render the message or expose it to assistive technology.

When you cannot inspect or verify a property, mark it as unverified. Do not infer success from the absence of an obvious problem.

### 4. Repair and re-review

Make a specific repair when the issue and the correct change are clear. Preserve the message’s required meaning and facts. Re-review the revised output; do not describe an earlier version’s review as applying to changed content.

If a repair would require guessing at meaning, changing a required fact, or making an unsupported semantic judgement, ask for clarification or report that the issue remains unresolved.

## Review and evidence boundaries

This repository does not include an executable test harness. Unless the current environment separately provides and actually runs a relevant tool:

- Do not say that tests passed, that axe or another checker was run, or that browser/client testing occurred.
- Do not invent test results, client coverage, measurements, or evidence references.
- Do not treat a manual review as an automated test.
- Do not treat an automated checker’s result as proof of image meaning, link purpose, factual accuracy, or overall accessibility.
- Do not claim that browser rendering is equivalent to rendering in Gmail, Outlook, Apple Mail, or another email client.
- Do not claim that a plain-text alternative has valid MIME structure unless the delivered MIME message was actually inspected.

If the user requests tests or validation that the available environment cannot perform, say which checks were performed, which were not, and what tooling or evidence would be needed. A tool’s absence is not a pass.

## Decision and response format

For a review, use one of these outcomes:

- **Ready for the requested next step:** The requested content or review is complete within the stated scope. This is not a claim of full accessibility or authorization to send.
- **Needs changes:** Identify specific issues that can be corrected without guessing.
- **On hold:** Explain what missing information, evidence, or decision prevents a reliable result.

Always state the scope. Separate findings from limitations. For example:

> **Outcome:** Needs changes  
> **Scope:** Reviewed the supplied HTML and plain-text content against the repository guidance. No email-client or assistive-technology testing was performed.  
> **Findings:** …  
> **Not verified:** …

Do not use “pass,” “certified,” “fully accessible,” or “WCAG-conformant” to describe an overall message based solely on a checklist or automated scan.

## Changes to this repository

When asked to edit repository files:

- Keep `Email_Accessibility.md` authoritative unless the user explicitly requests changes to it.
- Do not weaken its guidance to accommodate a tool or template.
- Keep claims in `README.md` consistent with files and functionality that actually exist.
- Follow the terms in `LICENSE`; do not provide legal conclusions about them.
- Do not add instructions referring to scripts, tests, schemas, workflows, or configuration unless those files are actually present or are being added in the same requested change.
- If a requested implementation would need additional files or infrastructure, explain that requirement rather than claiming the repository already supports it.

## Final safeguard

When you cannot establish that a requirement is met, report it as unverified or unresolved. Never turn uncertainty into a claim of accessibility, test success, or send authorization.
