---
name: super-marketing-strategy
description: "Marketing strategy: positioning, ICP, growth hypotheses, and content strategy. Use to define the plan before execution."
---

# Super Marketing Strategy

## Overview
Define product positioning, target audience, and the strategic growth plan.


## User Intent Examples
- "Need help with Content Strategy for my product/site."
- "Create a plan for Marketing Ideas."
- "Audit or improve Product Marketing Context."

## Capabilities
- ICP, positioning, and messaging foundations
- Growth levers, hypotheses, and channel strategy
- Content strategy and demand generation planning
- Prioritized roadmap with KPIs

## Routing Map (Modules)
- **Content Strategy** -> `references/modules/content-strategy.md`
- **Marketing Ideas** -> `references/modules/marketing-ideas.md`
- **Product Marketing Context** -> `references/modules/product-marketing-context.md`

## Default Flow
1. If product and ICP are unclear, start with product-marketing context.
2. If the request is content-first, jump to content strategy.
3. If the request is idea generation or launch planning, jump to marketing ideas.

## Minimal Intake Questions
Ask only what is missing:
- Product and audience
- Primary goal (pipeline, revenue, retention)
- Timeline and constraints

## Output Format
- ICP and positioning
- Goals and KPIs
- Channel strategy and hypotheses
- Content plan and priorities
- 30/60/90 day roadmap

## Bundled References
- `references/modules/`

## Compatibility Notes
- If any module references slash commands or tool-specific legacy paths, translate them into plain-language steps.
- Keep outputs platform-agnostic unless the user specifies a specific tool, stack, or agent.

## Guardrails
- Do not invent market data.
- Keep strategy aligned to constraints.
- Favor clear priorities over long lists.
