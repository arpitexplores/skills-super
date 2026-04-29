# Super Data Analytics

Build and improve analytics pipelines, BI, dashboards, SQL, data quality, and measurement workflows.

## Install

Copy this folder into your agent's skills directory, then restart or reload the agent.

```bash
cp -R super-data-analytics ~/.your-agent/skills/
```

Use it by name:

```text
Use $super-data-analytics to help with this request.
```

## Best For

- data engineering
- analytics pipelines
- BI and dashboards
- SQL optimisation
- data quality and modelling

## Outputs

- pipeline plan
- dashboard or metric design
- SQL review
- data quality checklist
- measurement recommendations

## Modules

| Module | Purpose |
| --- | --- |
| `bi-dashboard.md` | BI dashboards, KPI design, metric definitions, and reporting workflows |
| `data-engineer.md` | Data pipelines, ingestion, transformations, warehousing, quality, and orchestration |
| `sql-optimizer.md` | SQL performance, query structure, indexing, joins, and database efficiency |

## Example Prompts

- `Use $super-data-analytics to design a dashboard for these KPIs.`
- `Use $super-data-analytics to optimise this SQL query.`
- `Use $super-data-analytics to review this data pipeline.`

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
