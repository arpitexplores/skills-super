# Super Product Business Finance

Make product and business decisions with market sizing, startup analysis, pricing, monetisation, and PM frameworks.

## Install

Copy this folder into your agent's skills directory, then restart or reload the agent.

```bash
cp -R super-product-business-finance ~/.your-agent/skills/
```

Use it by name:

```text
Use $super-product-business-finance to help with this request.
```

## Best For

- market sizing
- startup analysis
- pricing strategy
- monetisation design
- product management decisions

## Outputs

- market sizing summary
- pricing and packaging plan
- financial assumptions
- roadmap priorities
- decision log

## Modules

| Module | Purpose |
| --- | --- |
| `pricing-strategy.md` | Pricing, packaging, monetisation, willingness-to-pay, and value metric design |
| `product-manager.md` | Product strategy, roadmap, discovery, prioritisation, requirements, and metrics |
| `startup-analyst.md` | Startup analysis, market sizing, business model review, risk, and investor-style assessment |

## Example Prompts

- `Use $super-product-business-finance to price this product.`
- `Use $super-product-business-finance to size this market.`
- `Use $super-product-business-finance to review this startup idea.`

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
