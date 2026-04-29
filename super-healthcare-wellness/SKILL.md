---
name: super-healthcare-wellness
description: "Healthcare and wellness analysis: health data, trends, and guidance workflows."
---

# Super Healthcare & Wellness

## Overview
Analyse health-related data and provide structured, cautious guidance.


## User Intent Examples
- "Need help with Healthcare Workflows for my product/site."
- "Create a plan for Health Trend Analysis."
- "Not sure where to start, need a quick assessment."

## Workflow
1. Gather health context and data sources.
2. Analyse trends, risks, and patterns.
3. Generate actionable guidance and next steps.
4. Flag uncertainty and recommend professional review when needed.
5. Document findings and limitations.

## Minimal Intake Questions
- Primary goal or outcome
- Scope (pages, systems, teams, or timeframe)
- Constraints (tools, budget, timeline)

## Output Format
- Health data summary
- Trend and risk analysis
- Guidance and next steps
- Limitations and caveats

## Routing Map (Modules)
- **Healthcare Workflows** -> `references/modules/healthcare-workflows.md`
- **Health Trend Analysis** -> `references/modules/health-trend-analyser.md`

## Bundled References
- `references/modules/`
- `scripts/`
- `assets/`
- `agents/`

## Compatibility Notes
- If any module references slash commands or tool-specific paths, translate them into plain-language steps.
- Keep outputs platform-agnostic unless the user specifies a specific tool, stack, or agent.

## Guardrails
- Do not provide medical diagnosis.
- Recommend professional care for urgent issues.
- Separate data findings from advice.
