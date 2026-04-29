---
name: super-cloud
description: "Cloud platform engineering across AWS/Azure/GCP, IaC, networking, containers, and cost optimisation."
---

# Super Cloud

## Overview
Design and operate cloud infrastructure with clear architecture, IaC, and governance.


## User Intent Examples
- "Need help with AWS for my product/site."
- "Create a plan for Azure Functions."
- "Audit or improve Cloud Architecture."

## Workflow
1. Confirm workloads, compliance needs, and availability targets.
2. Select cloud provider(s) and architecture patterns.
3. Define IaC and environment structure.
4. Plan networking, security baselines, and identity.
5. Design deployment and scaling approach.
6. Validate cost, resilience, and operational readiness.

## Minimal Intake Questions
- Primary goal or outcome
- Scope (pages, systems, teams, or timeframe)
- Constraints (tools, budget, timeline)

## Output Format
- Cloud architecture plan
- IaC structure and environment map
- Security and networking checklist
- Deployment and scaling strategy
- Cost risks and optimisations

## Routing Map (Modules)
- **AWS** -> `references/modules/aws-skills.md`
- **Azure Functions** -> `references/modules/azure-functions.md`
- **Cloud Architecture** -> `references/modules/cloud-architect.md`

## Bundled References
- `references/modules/`
- `scripts/`
- `assets/`
- `agents/`

## Compatibility Notes
- If any module references slash commands or tool-specific paths, translate them into plain-language steps.
- Keep outputs platform-agnostic unless the user specifies a specific tool, stack, or agent.

## Guardrails
- Do not assume credentials or production access.
- Separate current state from target state.
- Prefer repeatable IaC over manual steps.
