---
name: super-security
description: "Security audits, threat modelling, testing, and remediation across apps, APIs, and infrastructure."
---

# Super Security

## Overview
Identify risks, test defenses, and ship actionable remediation.


## User Intent Examples
- "Need help with Security Audits for my product/site."
- "Create a plan for Threat Modelling."
- "Audit or improve Web Security Testing."

## Workflow
1. Define scope, assets, and threat model.
2. Review architecture and security controls.
3. Run targeted security testing and audits.
4. Prioritize findings by impact and exploitability.
5. Deliver fixes and verification steps.
6. Document residual risk and monitoring.

## Minimal Intake Questions
- Primary goal or outcome
- Scope (pages, systems, teams, or timeframe)
- Constraints (tools, budget, timeline)

## Output Format
- Threat model and scope
- Findings with severity and evidence
- Remediation plan
- Verification checklist
- Residual risk notes

## Routing Map (Modules)
- **Security Audits** -> `references/modules/security-auditor.md`
- **Threat Modelling** -> `references/modules/threat-modelling-expert.md`
- **Web Security Testing** -> `references/modules/web-security-testing.md`

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
- Do not perform unauthorized testing.
- Avoid exploit instructions without explicit permission.
- Separate confirmed findings from hypotheses.
