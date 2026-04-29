# Super Legal HR Compliance

Draft, review, and structure contracts, policies, HR workflows, and non-security compliance guidance.

## Install

Copy this folder into your agent's skills directory, then restart or reload the agent.

```bash
cp -R super-legal-hr-compliance ~/.your-agent/skills/
```

Use it by name:

```text
Use $super-legal-hr-compliance to help with this request.
```

## Best For

- contract review
- policy drafting
- HR workflows
- employment documentation
- regulatory guidance outside security

## Outputs

- contract summary
- policy draft
- HR workflow plan
- compliance checklist
- risk notes

## Modules

| Module | Purpose |
| --- | --- |
| `contracts-legal.md` | Contracts, legal clauses, policy review, obligation mapping, and legal workflow support |
| `hr-pro.md` | HR policies, people operations, internal communications, onboarding, and employee workflows |

## Example Prompts

- `Use $super-legal-hr-compliance to review this contract clause.`
- `Use $super-legal-hr-compliance to draft an HR policy.`
- `Use $super-legal-hr-compliance to create an onboarding compliance checklist.`

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
