# Super Security

Audit, threat-model, test, and remediate security risks across applications, APIs, and infrastructure.

## Install

Copy this folder into your agent's skills directory, then restart or reload the agent.

```bash
cp -R super-security ~/.your-agent/skills/
```

Use it by name:

```text
Use $super-security to help with this request.
```

## Best For

- security audits
- threat modelling
- web security testing
- risk prioritisation
- remediation planning

## Outputs

- threat model
- findings with severity
- remediation plan
- verification checklist
- residual risk notes

## Modules

| Module | Purpose |
| --- | --- |
| `security-auditor.md` | Security audits, risk review, control assessment, and prioritised remediation |
| `threat-modelling-expert.md` | Threat modelling, attack paths, abuse cases, and mitigation mapping |
| `web-security-testing.md` | Web and API security testing, validation, and remediation guidance |

## Example Prompts

- `Use $super-security to threat-model this architecture.`
- `Use $super-security to review this API for security risks.`
- `Use $super-security to prioritise these vulnerabilities.`

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
