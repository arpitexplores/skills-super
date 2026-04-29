# Super Design Quality

Audit and improve accessibility, WCAG compliance, responsive behaviour, visual consistency, and design QA.

## Install

Copy this folder into your agent's skills directory, then restart or reload the agent.

```bash
cp -R super-design-quality ~/.your-agent/skills/
```

Use it by name:

```text
Use $super-design-quality to help with this request.
```

## Best For

- accessibility audits
- WCAG compliance
- responsive QA
- visual consistency checks
- design remediation plans

## Outputs

- accessibility findings
- responsive QA checklist
- visual consistency issues
- prioritised remediation plan

## Modules

| Module | Purpose |
| --- | --- |
| `accessibility-wcag.md` | WCAG checks, accessibility remediation, semantic structure, contrast, keyboard, and assistive technology guidance |
| `visual-design-validator.md` | Responsive QA, visual consistency, layout checks, spacing, typography, and UI polish |

## Example Prompts

- `Use $super-design-quality to audit this page for accessibility.`
- `Use $super-design-quality to check mobile responsiveness.`
- `Use $super-design-quality to review this UI for visual consistency.`

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
