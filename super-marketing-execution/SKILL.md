---
name: super-marketing-execution
description: "Marketing execution: campaign orchestration, copywriting, CRO, analytics, paid ads, email, and social content. Use to ship campaigns and improve conversions."
---

# Super Marketing Execution

## Overview
Execute marketing work across campaigns, copy, CRO, channels, and measurement.


## User Intent Examples
- "Plan and co-ordinate a product launch campaign."
- "Need help with Analytics & Tracking for my product/site."
- "Create a plan for Copywriting."
- "Audit or improve Email Sequences."

## Capabilities
- Multi-channel campaign planning, launch readiness, and post-campaign reporting
- Trend-to-content operating loops with review gates and scheduling discipline
- Copywriting and creative production
- CRO audits and conversion improvements
- Analytics and tracking setups
- Paid ads and social content execution
- Email sequence planning and delivery

## Routing Map (Modules)
- **Campaign Orchestration** -> `references/modules/campaign-orchestration.md`
- **Analytics & Tracking** -> `references/modules/analytics-tracking.md`
- **Copywriting** -> `references/modules/copywriting.md`
- **Email Sequences** -> `references/modules/email-sequence.md`
- **CRO & Landing Pages** -> `references/modules/page-cro.md`
- **Paid Ads** -> `references/modules/paid-ads.md`
- **Social Content** -> `references/modules/social-content.md`

## Default Flow
1. Confirm goals, audience, and assets to ship.
2. If the request spans more than one channel, start with Campaign Orchestration.
3. If the request is channel-specific, jump to that module.
4. If CRO or tracking is missing, handle CRO/analytics before launch.

## Minimal Intake Questions
Ask only what is missing:
- Audience and offer
- Channel(s) and timeline
- Current assets or constraints

## Output Format
- Campaign brief, channel plan, or launch checklist
- Copy and creative assets
- CRO recommendations or changes
- Tracking plan
- Post-campaign report and next steps

## Bundled References
- `references/modules/`

## Compatibility Notes
- If any module references slash commands or tool-specific legacy paths, translate them into plain-language steps.
- Keep outputs platform-agnostic unless the user specifies a specific tool, stack, or agent.

## Guardrails
- Do not invent product claims.
- Tie changes to measurable outcomes.
- Keep execution aligned with strategy.
