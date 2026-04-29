---
name: super-legal-hr-compliance
description: "Legal, HR, and compliance: contracts, policies, and regulatory guidance (non-security)."
---

# Super Legal/HR/Compliance

## Overview
Provide structured legal/HR guidance and documentation support.


## User Intent Examples
- "Need help with HR Operations for my product/site."
- "Create a plan for Legal & Compliance."
- "Not sure where to start, need a quick assessment."

## Workflow
1. Clarify jurisdiction and scope.
2. Identify required policy or contract type.
3. Draft or review with compliance requirements.
4. Highlight risks and missing clauses.
5. Provide implementation checklist.

## Minimal Intake Questions
- Primary goal or outcome
- Scope (pages, systems, teams, or timeframe)
- Constraints (tools, budget, timeline)

## Output Format
- Policy/contract outline
- Compliance checklist
- Risk and gap notes
- Implementation steps

## Routing Map (Modules)
- **HR Operations** -> `references/modules/hr-pro.md`
- **Legal & Compliance** -> `references/modules/legal-advisor.md`

## Bundled References
- `references/modules/`
- `scripts/`
- `assets/`
- `agents/`

## Compatibility Notes
- If any module references slash commands or tool-specific paths, translate them into plain-language steps.
- Keep outputs platform-agnostic unless the user specifies a specific tool, stack, or agent.

## Guardrails
- Do not give jurisdiction-specific legal advice without context.
- Flag when licenced counsel is required.
- Separate templates from final legal review.
