# Accessible Email Design

Guidance for the creation of accessible emails for use by systems that generate emails.

## Overview

This repository contains the source guidance and supporting operational policy for building accessible email content. It is designed for teams and systems that generate newsletters, transactional messages, and other communication that must remain usable for people with permanent, temporary, and situational accessibility needs.

The repository is split into two core parts:

- `Email_Accessibility.md` — the authoritative guidance document for accessible email design.
- `AGENTS.md` — the policy and validation framework for automated agents that generate, test, repair, and release email content.

Together, these documents define both the design principles and the operational checks needed to maintain those principles in practice.

## Repository contents

- `Email_Accessibility.md` — comprehensive guidance covering accessible email structure, readability, contrast, alternative text, code quality, and review practices.
- `AGENTS.md` — implementation rules for AI and automation systems, including generation constraints, test procedures, repair workflows, release gating, and audit requirements.
- `LICENSE` — repository license terms.
- `README.md` — repository overview and project guidance.

## What this repository covers

The guidance in this project addresses the core requirements for accessible email communication, including:

- meaningful reading order and semantic structure
- proper heading hierarchy and section planning
- readable typography with a minimum text size baseline
- colour contrast and non-colour cues
- meaningful image alternatives
- descriptive link text and destination clarity
- clean, well-structured HTML and accessibility-friendly markup
- responsive layouts for different screen sizes and devices
- text-only alternatives and MIME parity
- left-aligned prose with an uneven right edge for readability
- simplicity, consistency, and concise communication
- pre-send review and evidence-based quality checks

## Role of the policy document

`AGENTS.md` complements the source guidance by defining how automated systems should behave when generating and validating email. It includes:

- content and evidence contracts
- requirement traceability for each accessibility rule
- testing and repair procedures
- release criteria and decision logic
- escalation and audit handling
- implementation guidance for browser-based validation tooling

This document is intended to operationalise accessibility requirements without replacing the underlying design guidance.

## Typical use cases

This repository is relevant for:

- email designers and content teams
- developers creating accessible email templates
- automation systems generating personalized or bulk email
- accessibility review workflows and quality assurance teams
- organisations producing newsletters, announcements, and transactional email

## Notes

The source guide in `Email_Accessibility.md` is the authoritative requirement set. `AGENTS.md` does not relax those requirements; it provides the policy and evidence model needed to apply them consistently in automated workflows.

## License

This project is licensed under the terms in the `LICENSE` file.
