---
name: super-engineering-devops
description: "Engineering and DevOps delivery: architecture, build, test, deploy, and operate reliable systems."
---

# Super Engineering/DevOps

## Overview
Build and run software with strong architecture, quality, and delivery practices.


## User Intent Examples
- "Need help with DevOps & Deployment for my product/site."
- "Create a plan for Observability."
- "Audit or improve Full-Stack Engineering."

## Workflow
1. Clarify requirements, constraints, and success metrics.
2. Select architecture and core tech stack.
3. Design data models, APIs, and integration boundaries.
4. Implement with tests and quality checks.
5. Set up CI/CD and deployment strategy.
6. Add observability and runbooks.

## Minimal Intake Questions
- Primary goal or outcome
- Scope (pages, systems, teams, or timeframe)
- Constraints (tools, budget, timeline)

## Output Format
- Architecture and design summary
- Implementation plan
- Test and QA plan
- CI/CD and deployment plan
- Observability checklist

## Routing Map (Modules)
- **DevOps & Deployment** -> `references/modules/devops-deploy.md`
- **Observability** -> `references/modules/observability-engineer.md`
- **Full-Stack Engineering** -> `references/modules/senior-fullstack.md`

## Bundled References
- `references/modules/`
- `scripts/`
- `assets/`
- `agents/`

## Compatibility Notes
- If any module references slash commands or tool-specific paths, translate them into plain-language steps.
- Keep outputs platform-agnostic unless the user specifies a specific tool, stack, or agent.

## Guardrails
- Do not claim performance gains without measurements.
- Keep testing requirements explicit.
- Prefer incremental delivery and rollback safety.
