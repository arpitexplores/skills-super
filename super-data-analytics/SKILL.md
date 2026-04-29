---
name: super-data-analytics
description: "Data & analytics: pipelines, BI, SQL optimisation, analytics tooling, and dashboards."
---

# Super Data & Analytics

## Overview
Build reliable data pipelines and analytics outputs with measurable insights.


## User Intent Examples
- "Need help with Product Analytics for my product/site."
- "Create a plan for Data Engineering."
- "Audit or improve Data Science."

## Workflow
1. Define business questions, metrics, and data sources.
2. Design ingestion and transformation pipelines.
3. Select storage, modelling, and access patterns.
4. Implement analytics, dashboards, and reporting.
5. Validate data quality and performance.
6. Document lineage, ownership, and SLAs.

## Minimal Intake Questions
- Primary goal or outcome
- Scope (pages, systems, teams, or timeframe)
- Constraints (tools, budget, timeline)

## Output Format
- Data pipeline plan
- Data model and storage choices
- Analytics and dashboard spec
- Data quality checklist
- Operations and SLA notes

## Routing Map (Modules)
- **Product Analytics** -> `references/modules/analytics-product.md`
- **Data Engineering** -> `references/modules/data-engineer.md`
- **Data Science** -> `references/modules/data-scientist.md`

## Bundled References
- `references/modules/`
- `references/toolkit/`
- `scripts/`
- `assets/`
- `agents/`

## Compatibility Notes
- If any module references slash commands or tool-specific legacy paths, translate them into plain-language steps.
- Keep outputs platform-agnostic unless the user specifies a specific tool, stack, or agent.

## Guardrails
- Do not report metrics without validation.
- Separate raw data from transformed outputs.
- Track lineage and ownership explicitly.
