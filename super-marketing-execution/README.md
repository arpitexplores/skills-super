# Super Marketing Execution

Plan, ship, track, and improve campaigns across copy, CRO, email, social, paid ads, and analytics.

## Install

Copy this folder into your agent's skills directory, then restart or reload the agent.

```bash
cp -R super-marketing-execution ~/.your-agent/skills/
```

Use it by name:

```text
Use $super-marketing-execution to help with this request.
```

## Best For

- campaign orchestration
- copy and creative production
- landing page CRO
- email/social/ad execution
- tracking plans

## Outputs

- campaign brief
- asset plan
- launch checklist
- tracking plan
- post-campaign report

## Modules

| Module | Purpose |
| --- | --- |
| `analytics-tracking.md` | Marketing analytics, UTMs, KPI design, experiments, and attribution discipline |
| `campaign-orchestration.md` | Multi-channel campaign planning, launch readiness, scheduling, and reporting |
| `copywriting.md` | Conversion copy, ad creative, CTAs, brand voice, and message clarity |
| `email-sequence.md` | Lifecycle, nurture, outreach, onboarding, and re-engagement email sequences |
| `page-cro.md` | Landing page audits, funnel friction, forms, offers, and conversion experiments |
| `paid-ads.md` | Paid media planning, targeting, creative testing, and campaign optimisation |
| `social-content.md` | Social content systems, trend-to-content loops, calendars, and platform formatting |

## Example Prompts

- `Use $super-marketing-execution to plan a product launch campaign.`
- `Use $super-marketing-execution to create email, social, and landing page assets.`
- `Use $super-marketing-execution to review this campaign before launch.`

## Package Contents

- `SKILL.md` is the installable skill entry point.
- `references/modules/` contains detailed workflows loaded only when needed.
- `agents/` contains optional agent metadata where supported.
- `scripts/` and `assets/` are optional helpers when bundled.

## Compatibility

This skill is plain Markdown and is intended to be agent-agnostic. If a bundled helper mentions a specific tool path, translate that instruction to the equivalent path for your environment.

## Version

See `VERSION` and `CHANGELOG.md`.

## Licence

MIT. See the root repository `LICENSE`.
