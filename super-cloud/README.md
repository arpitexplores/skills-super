# Super Cloud

Plan and review cloud systems across AWS, Azure/GCP, infrastructure as code, networking, containers, and cost.

## Install

Copy this folder into your agent's skills directory, then restart or reload the agent.

```bash
cp -R super-cloud ~/.your-agent/skills/
```

Use it by name:

```text
Use $super-cloud to help with this request.
```

## Best For

- cloud architecture
- AWS/Azure/GCP planning
- infrastructure as code
- networking and containers
- cost and reliability reviews

## Outputs

- cloud architecture plan
- IaC and deployment checklist
- network/security considerations
- cost and reliability risks

## Modules

| Module | Purpose |
| --- | --- |
| `aws-skills.md` | AWS architecture, services, deployment, security, reliability, and cost patterns |
| `azure-gcp-skills.md` | Azure and GCP architecture, service mapping, migration, and platform-specific trade-offs |
| `terraform-infrastructure.md` | Infrastructure as code, Terraform structure, state, modules, review, and governance |

## Example Prompts

- `Use $super-cloud to design an AWS deployment for this app.`
- `Use $super-cloud to review this Terraform plan.`
- `Use $super-cloud to plan a multi-cloud migration approach.`

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
