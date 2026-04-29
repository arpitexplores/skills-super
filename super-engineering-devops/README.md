# Super Engineering DevOps

Architect, build, test, deploy, observe, and operate reliable software systems.

## Install

Copy this folder into your agent's skills directory, then restart or reload the agent.

```bash
cp -R super-engineering-devops ~/.your-agent/skills/
```

Use it by name:

```text
Use $super-engineering-devops to help with this request.
```

## Best For

- software architecture
- full-stack engineering
- DevOps delivery
- observability
- testing and operations

## Outputs

- architecture plan
- implementation guidance
- deployment checklist
- observability plan
- risk and reliability notes

## Modules

| Module | Purpose |
| --- | --- |
| `devops-incident.md` | DevOps workflows, deployment, CI/CD, incident response, and operational reliability |
| `observability-engineer.md` | Logging, metrics, tracing, alerting, SLOs, dashboards, and debugging workflows |
| `senior-fullstack.md` | Full-stack architecture, code quality, implementation patterns, testing, and review |

## Example Prompts

- `Use $super-engineering-devops to review this architecture.`
- `Use $super-engineering-devops to plan CI/CD for this app.`
- `Use $super-engineering-devops to improve observability for this service.`

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
