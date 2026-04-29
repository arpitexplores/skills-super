# Super Healthcare Wellness

Analyse health and wellness workflows, trends, health data, and non-diagnostic guidance with clear safety boundaries.

## Install

Copy this folder into your agent's skills directory, then restart or reload the agent.

```bash
cp -R super-healthcare-wellness ~/.your-agent/skills/
```

Use it by name:

```text
Use $super-healthcare-wellness to help with this request.
```

## Best For

- health workflow analysis
- wellness trend analysis
- health data interpretation
- care or wellbeing workflows
- non-diagnostic guidance

## Outputs

- health workflow summary
- trend interpretation
- wellness plan considerations
- safety caveats
- next-step checklist

## Modules

| Module | Purpose |
| --- | --- |
| `health-trend-analyser.md` | Health and wellness trend interpretation, data patterns, and non-diagnostic analysis |
| `healthcare-workflows.md` | Healthcare, care, wellness, and operational workflow guidance with safety boundaries |

## Example Prompts

- `Use $super-healthcare-wellness to analyse these wellness trends.`
- `Use $super-healthcare-wellness to review this health workflow.`
- `Use $super-healthcare-wellness to structure a non-diagnostic wellbeing checklist.`

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
