# Super Marketing Strategy

Define positioning, ICP, growth hypotheses, product marketing context, and content strategy before execution.

## Install

Copy this folder into your agent's skills directory, then restart or reload the agent.

```bash
cp -R super-marketing-strategy ~/.your-agent/skills/
```

Use it by name:

```text
Use $super-marketing-strategy to help with this request.
```

## Best For

- positioning and messaging
- ICP and customer context
- growth hypotheses
- content strategy
- launch and campaign strategy

## Outputs

- positioning summary
- ICP and message map
- growth experiment ideas
- content strategy plan

## Modules

| Module | Purpose |
| --- | --- |
| `content-strategy.md` | Content strategy, topic clusters, lead magnets, site structure, and distribution planning |
| `marketing-ideas.md` | Growth ideas, launch planning, campaign angles, and experiment generation |
| `product-marketing-context.md` | ICP, positioning, messaging, pricing context, and product marketing foundations |

## Example Prompts

- `Use $super-marketing-strategy to define positioning for this SaaS product.`
- `Use $super-marketing-strategy to create a content strategy for this audience.`
- `Use $super-marketing-strategy to generate growth hypotheses before launch.`

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
