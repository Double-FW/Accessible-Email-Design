---
title: "Agent instructions for accessible email generation and validation"
version: "1.1.0"
author: "Repository maintainer"
date: "2026-11-06"
language: "en-GB"
artifact_type: "agent_policy_and_validation_specification"
source: "Email_Accessibility.md"
policy_schema_version: "1.0"
review_status: "adopted_for_repo_execution"
---

# AGENTS.md — Accessible Email Design

## Purpose and authority

This file governs any AI agent or automation system that generates, validates, repairs, or releases email content in this repository.

This repository is not a claim of universal accessibility conformance. It is a bounded operational policy for controlled validation and repair. The authoritative design requirements live in `Email_Accessibility.md`. This file operationalizes those requirements for automation only.

Rules:
- Do not relax the source guidance.
- Do not claim a full accessibility pass without evidence.
- Do not dispatch or release email without separate authorisation.
- When evidence is missing, ambiguous, or contradictory, return `hold` or `repair`, not `ready`.
- A `ready` result means only: the configured checks passed in the current environment; it does not mean “full WCAG conformance” or “fully accessible in all clients”.

## Scope

This repo is intended to support:
- accessible email generation
- HTML + plain-text parity checks
- browser-based validation with Playwright and axe-core
- repair workflows for broken or weak output
- explicit decision states: `ready`, `repair`, `hold`

This repository must not implement unrestricted network access, live sending, or release autonomy.

## Required repository conventions

Use the following repository layout:

```text
.
├── AGENTS.md
├── Email_Accessibility.md
├── README.md
├── LICENSE
├── package.json
├── package-lock.json
├── .gitignore
├── .github/
│   └── workflows/
│       └── accessibility-validation.yml
├── src/
│   ├── cli.js
│   └── validate.js
├── schemas/
│   ├── email-input.schema.json
│   └── validation-report.schema.json
├── fixtures/
│   ├── pass.json
│   ├── fail.json
│   └── hold.json
├── test/
│   └── validate.test.js
├── IMPLEMENTATION.md
└── artifacts/   (generated, ignored)
```

## Decision model

The agent must use exactly these states:

- `ready`: all applicable checks pass and the evidence is present
- `repair`: a fixable issue was found and the required validation must rerun
- `hold`: unresolved, missing evidence, blocked by policy, or not safe to release

Rules:
- `ready` is not a broad conformance claim.
- `repair` is only valid when a concrete change can be made and retested.
- `hold` is valid for missing evidence, invalid input, unsafe content, or policy violations.
- Any `hold` or `repair` result must include a reason or evidence gap.
- Release is never implicit. Dispatch requires separate authorisation.

## Required validation contract

The runner must support the following execution flow:

1. Load JSON input from a file or stdin.
2. Validate the structure against `schemas/email-input.schema.json`.
3. Reject malformed or unsupported inputs with `hold` and exit non-zero.
4. Run HTML rendering in a headless browser.
5. Verify block ordering, document language, image alt presence, and link/action semantics.
6. Run axe-core with a pinned version.
7. Produce a report matching `schemas/validation-report.schema.json`.
8. Return exit code:
   - 0 for `ready`
   - 1 for `hold`
   - 2 for invalid input or runner error

## Required output schema

The validation result must look like this:

```json
{
  "schema_version": "1.0",
  "message_id": "opaque-id",
  "decision": "ready",
  "release_authorized": false,
  "scope": "Bounded validation-only result. This does not prove all-client accessibility.",
  "checks": [
    { "id": "S01-language", "outcome": "pass", "detail": "Document language matches the required profile." }
  ],
  "tool_versions": {
    "node": "v22.x",
    "playwright": "1.56.1",
    "axe_core": "4.10.3"
  },
  "tested_at": "2026-11-06T12:00:00.000Z"
}
```

Rules:
- `release_authorized` is always `false` in this repo unless a separate, explicit deployment step authorises dispatch.
- `decision` must be one of: `ready`, `hold`
- `checks` must contain machine-readable observations and must not hide failures

## Required input schema

The input must be a JSON object with:

- `schema_version`: "1.0"
- `message_id`: non-empty string
- `profile`: "individual" or "organisation"
- `language`: language code such as "en-GB"
- `html`: non-empty HTML email string
- `text`: plain-text alternative
- `block_order`: ordered list of block IDs
- `blocks`: array of objects with `id` and `kind`
- `facts`: array of fact objects with `id`, `value`, and `source_ref`
- `actions`: array of action objects with `id`, `label`, and valid `https`/`mailto`/`tel` URL
- `semantic_evidence`: object with `status` and `provenance_ref`

The runner must reject any input that:
- exceeds a reasonable size limit
- provides unsupported URL schemes
- has duplicate block IDs
- mismatches `block_order` and rendered block IDs
- omits required facts or actions
- fails schema validation

## Required checks

The minimal implementation must include these checks:

- `S01-language`: HTML `lang` matches the input contract
- `E03-dom-order`: rendered block IDs match the declared order
- `E05a-min-font`: visible text is at least roughly 14pt
- `E07a-image-alt`: every image has an explicit alt attribute
- `E08a-link-name`: links have non-empty name-like content
- `E08-action-contract`: action labels and URLs match the contract
- `E11-fact-parity-html`: required facts appear in the HTML representation
- `E11-fact-parity-text`: required facts appear in the plain-text representation
- `S02-safe-subset`: no executable or unsafe embedded behaviors are present
- `E10a-320px-overflow`: no horizontal overflow at 320 CSS px
- `axe-violations`: axe-core results are evaluated and reported
- `E07b-semantic-evidence`: provenance/ref status is present and called out as a limitation

Important:
- This is a bounded validation layer only.
- It does not prove semantic image quality, business correctness of facts, full client compatibility, MIME fidelity beyond the provided text/HTML pair, or real-world email-client rendering.

## Browser execution rules

Use Playwright with a headless Chromium instance.

Rules:
- Do not allow network access for the test content.
- Abort all requests during the render test.
- Load HTML via `page.setContent()`.
- Use DOM and computed-style checks.
- Run axe-core with a pinned version.
- Keep the result JSON machine-readable.
- Never mutate the input in place while validating.

## Repair policy

If a check fails:
- fix the issue if it is clearly within the repository's scope
- rerun the full validation after the fix
- ensure the previous evidence is invalidated by the change
- keep a reason for the change in the repair result

The agent may produce a `repair` result only when:
- the root cause is understood
- the fix is bounded and specific
- the fix can be retested
- the output still matches the source facts and content contract

If the issue is semantic, missing evidence, or not clearly fixable, use `hold`.

## Release policy

This repo must not release or dispatch email automatically.

The agent must enforce:
- `release_authorized: false` in all generated reports unless a separate caller explicitly authorises a send action
- a separate validation step before dispatch
- a digest/hash check before release if the system is extended
- no silent downgrade from HTML+plain text to plain text only without explicit policy
- no claim that this validation is equivalent to full legal or WCAG conformance

## CI and test requirements

The repository must include:
- `package.json` with pinned versions
- `package-lock.json` committed and version-pinned
- a GitHub Actions workflow for Node + Playwright
- tests in `test/validate.test.js`
- fixtures under `fixtures/`
- a `schemas/` directory
- a minimal `README` describing how to run validation

Example CI workflow:
```yaml
name: Accessible email validation

on:
  push:
  pull_request:

jobs:
  test:
    runs-on: ubuntu-latest
    timeout-minutes: 10
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '22'
          cache: npm
      - run: npm ci
      - run: npx playwright install --with-deps chromium
      - run: npm test
```

## Commands

The repository must support these commands:

```bash
npm ci
npm test
npm run validate -- --input fixtures/pass.json
npm run validate -- --input fixtures/fail.json
npm run validate -- --input fixtures/hold.json
npm run test:fixtures
```

Exit behavior:
- pass fixture -> exit 0
- fail fixture -> exit 1
- hold fixture -> exit 1
- malformed input -> exit 2

## Required non-goals

This repository is not:
- a full email client testing matrix
- a WWWCAG conformance engine
- an email sending system
- a business-signoff mechanism
- a substitute for human accessibility judgement where evidence is not available

## Agent operating instructions

When working in this repository, the agent must:
- inspect `Email_Accessibility.md` before making policy claims
- use the source guide as the requirement source
- prefer machine-checked evidence over model assumptions
- produce `hold` whenever required evidence is absent
- keep outputs deterministic and JSON-oriented
- refuse to fabricate checks, rule IDs, or results
- never claim dispatch authorization
- never return a pass for any unverified semantic claim

## Minimal implementation policy

The agent should prefer a small, testable implementation over a broad theoretical design.

Minimum viable implementation:
- one CLI entry point
- one validation runner
- schema validation
- Playwright HTML rendering test
- axe-core integration
- fixture-based tests
- CI execution

This is the minimum state that makes the repository “agent-executable” and reviewable.

## Final rule

If a requirement is not machine-checkable from the repository inputs, the correct outcome is `hold` or `repair`, not `ready`.

This is the policy boundary. Everything else is a claim beyond the repository’s evidence.
