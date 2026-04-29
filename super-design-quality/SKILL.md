---
name: super-design-quality
description: "Design QA: accessibility, WCAG compliance, and visual/consistency validation. Use for audits and remediation."
---

# Super Design Quality

## Overview
Audit accessibility and UI quality, then prescribe fixes and validation steps.


## User Intent Examples
- "Need help with Accessibility Audit for my product/site."
- "Create a plan for Visual QA."
- "Not sure where to start, need a quick assessment."

## Capabilities
- Accessibility and WCAG compliance audits
- Screen reader and keyboard testing guidance
- Visual QA and consistency checks
- Remediation plans and verification steps

## Routing Map (Modules)
- **Accessibility Audit** -> `references/modules/accessibility-compliance-accessibility-audit.md`
- **Visual QA** -> `references/modules/ui-visual-validator.md`

## Default Flow
1. Identify target surfaces and user flows.
2. If accessibility is requested, run the accessibility module.
3. If visual QA is requested, run the visual validator module.

## Minimal Intake Questions
Ask only what is missing:
- Target pages or flows
- Platforms/browsers to prioritize
- Any known issues or constraints

## Output Format
- Issues and severity
- Fix guidance
- Validation checklist

## Bundled References
- `references/modules/`

## Compatibility Notes
- If any module references slash commands or tool-specific legacy paths, translate them into plain-language steps.
- Keep outputs platform-agnostic unless the user specifies a specific tool, stack, or agent.

## Guardrails
- Distinguish confirmed issues from hypotheses.
- Prioritize fixes by impact and effort.
