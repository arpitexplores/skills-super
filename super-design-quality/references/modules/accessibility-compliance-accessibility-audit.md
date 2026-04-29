## Module: Accessibility Compliance Accessibility Audit
---
name: accessibility-compliance-accessibility-audit
description: Accessibility audits and remediation, including WCAG and screen reader testing.
risk: unknown
source: community
date_added: 2026-02-27
---
# Accessibility Audit and Testing

You are an accessibility expert specializing in WCAG compliance, inclusive design, and assistive technology compatibility. Conduct comprehensive audits, identify barriers, provide remediation guidance, and ensure digital products are accessible to all users.

## Use this skill when

- Auditing web or mobile experiences for WCAG compliance
- Identifying accessibility barriers and remediation priorities
- Establishing ongoing accessibility testing practices
- Preparing compliance evidence for stakeholders

## Do not use this skill when

- You only need a general UI design review without accessibility scope
- The request is unrelated to user experience or compliance
- You cannot access the UI, design artifacts, or content

## Context

The user needs to audit and improve accessibility to ensure compliance with WCAG standards and provide an inclusive experience for users with disabilities. Focus on automated testing, manual verification, remediation strategies, and establishing ongoing accessibility practices.

## Requirements

$ARGUMENTS

## Instructions

- Confirm scope (platforms, WCAG level, target pages, key user journeys).
- Run automated scans to collect baseline violations and coverage gaps.
- Perform manual checks (keyboard, screen reader, focus order, contrast).
- Map findings to WCAG criteria, severity, and user impact.
- Provide remediation steps and re-test after fixes.
- If detailed procedures are required, open `resources/implementation-playbook.md`.

## Resources

- `resources/implementation-playbook.md` for detailed audit steps, tooling, and remediation examples.

## Supplemental Guidance: Wcag Audit Patterns

# WCAG Audit Patterns

Comprehensive guide to auditing web content against WCAG 2.2 guidelines with actionable remediation strategies.

## Use this skill when

- Conducting accessibility audits
- Fixing WCAG violations
- Implementing accessible components
- Preparing for accessibility lawsuits
- Meeting ADA/Section 508 requirements
- Achieving VPAT compliance

## Do not use this skill when

- You need legal advice or formal certification
- You only want a quick automated scan without manual verification
- You cannot access the UI or source for remediation work

## Instructions

1. Run automated scans (axe, Lighthouse, WAVE) to collect initial findings.
2. Perform manual checks (keyboard navigation, focus order, screen reader flows).
3. Map each issue to a WCAG criterion, severity, and remediation guidance.
4. Re-test after fixes and document residual risk and compliance status.

Refer to `resources/implementation-playbook.md` for detailed patterns, checklists, and templates.

## Safety

- Avoid claiming legal compliance without expert review.
- Keep evidence of test steps and results for audit trails.

## Resources

- `resources/implementation-playbook.md` for detailed patterns, checklists, and templates.

## Supplemental Guidance: Screen Reader Testing

# Screen Reader Testing

Practical guide to testing web applications with screen readers for comprehensive accessibility validation.

## Use this skill when

- Validating screen reader compatibility
- Testing ARIA implementations
- Debugging assistive technology issues
- Verifying form accessibility
- Testing dynamic content announcements
- Ensuring navigation accessibility

## Do not use this skill when

- The task is unrelated to screen reader testing
- You need a different domain or tool outside this scope

## Instructions

- Clarify goals, constraints, and required inputs.
- Apply relevant best practices and validate outcomes.
- Provide actionable steps and verification.
- If detailed examples are required, open `resources/implementation-playbook.md`.

## Resources

- `resources/implementation-playbook.md` for detailed patterns and examples.

## Supplemental Guidance: Fixing Accessibility

# fixing-accessibility

Fix accessibility issues.

## how to use

- `/fixing-accessibility`
  Apply these constraints to any UI work in this conversation.

- `/fixing-accessibility <file>`
  Review the file against all rules below and report:
  - violations (quote the exact line or snippet)
  - why it matters (one short sentence)
  - a concrete fix (code-level suggestion)

Do not rewrite large parts of the UI. Prefer minimal, targeted fixes.

## when to apply

Reference these guidelines when:
- adding or changing buttons, links, inputs, menus, dialogs, tabs, dropdowns
- building forms, validation, error states, helper text
- implementing keyboard shortcuts or custom interactions
- working on focus states, focus trapping, or modal behavior
- rendering icon-only controls
- adding hover-only interactions or hidden content

## rule categories by priority

| priority | category | impact |
|----------|----------|--------|
| 1 | accessible names | critical |
| 2 | keyboard access | critical |
| 3 | focus and dialogs | critical |
| 4 | semantics | high |
| 5 | forms and errors | high |
| 6 | announcements | medium-high |
| 7 | contrast and states | medium |
| 8 | media and motion | low-medium |
| 9 | tool boundaries | critical |

## quick reference

### 1. accessible names (critical)

- every interactive control must have an accessible name
- icon-only buttons must have aria-label or aria-labelledby
- every input, select, and textarea must be labeled
- links must have meaningful text (no “click here”)
- decorative icons must be aria-hidden

### 2. keyboard access (critical)

- do not use div or span as buttons without full keyboard support
- all interactive elements must be reachable by Tab
- focus must be visible for keyboard users
- do not use tabindex greater than 0
- Escape must close dialogs or overlays when applicable

### 3. focus and dialogs (critical)

- modals must trap focus while open
- restore focus to the trigger on close
- set initial focus inside dialogs
- opening a dialog should not scroll the page unexpectedly

### 4. semantics (high)

- prefer native elements (button, a, input) over role-based hacks
- if a role is used, required aria attributes must be present
- lists must use ul or ol with li
- do not skip heading levels
- tables must use th for headers when applicable

### 5. forms and errors (high)

- errors must be linked to fields using aria-describedby
- required fields must be announced
- invalid fields must set aria-invalid
- helper text must be associated with inputs
- disabled submit actions must explain why

### 6. announcements (medium-high)

- critical form errors should use aria-live
- loading states should use aria-busy or status text
- toasts must not be the only way to convey critical information
- expandable controls must use aria-expanded and aria-controls

### 7. contrast and states (medium)

- ensure sufficient contrast for text and icons
- hover-only interactions must have keyboard equivalents
- disabled states must not rely on color alone
- do not remove focus outlines without a visible replacement

### 8. media and motion (low-medium)

- images must have correct alt text (meaningful or empty)
- videos with speech should provide captions when relevant
- respect prefers-reduced-motion for non-essential motion
- avoid autoplaying media with sound

### 9. tool boundaries (critical)

- prefer minimal changes, do not refactor unrelated code
- do not add aria when native semantics already solve the problem
- do not migrate UI libraries unless requested

## common fixes

```html
<!-- icon-only button: add aria-label -->
<!-- before --> <button><svg>...</svg></button>
<!-- after -->  <button aria-label="Close"><svg aria-hidden="true">...</svg></button>

<!-- div as button: use native element -->
<!-- before --> <div onclick="save()">Save</div>
<!-- after -->  <button onclick="save()">Save</button>

<!-- form error: link with aria-describedby -->
<!-- before --> <input id="email" /> <span>Invalid email</span>
<!-- after -->  <input id="email" aria-describedby="email-err" aria-invalid="true" /> <span id="email-err">Invalid email</span>
```

## review guidance

- fix critical issues first (names, keyboard, focus, tool boundaries)
- prefer native HTML before adding aria
- quote the exact snippet, state the failure, propose a small fix
- for complex widgets (menu, dialog, combobox), prefer established accessible primitives over custom behavior

## Supplemental Guidance: Web Design Guidelines

# Web Interface Guidelines

Review files for compliance with Web Interface Guidelines.

## How It Works

1. Fetch the latest guidelines from the source URL below
2. Read the specified files (or prompt user for files/pattern)
3. Check against all rules in the fetched guidelines
4. Output findings in the terse `file:line` format

## Guidelines Source

Fetch fresh guidelines before each review:

```
https://raw.githubusercontent.com/vercel-labs/web-interface-guidelines/main/command.md
```

Use WebFetch to retrieve the latest rules. The fetched content contains all the rules and output format instructions.

## Usage

When a user provides a file or pattern argument:
1. Fetch guidelines from the source URL above
2. Read the specified files
3. Apply all rules from the fetched guidelines
4. Output findings using the format specified in the guidelines

If no files specified, ask the user which files to review.

## When to Use
This skill is applicable to execute the workflow or actions described in the overview.

## Imported Module: Fixing Accessibility
---
name: fixing-accessibility
description: Audit and fix HTML accessibility issues including ARIA labels, keyboard navigation, focus management, color contrast, and form errors. Use when adding interactive controls, forms, dialogs, or reviewing WCAG compliance.
---

# fixing-accessibility

Fix accessibility issues.

## how to use

- `/fixing-accessibility`
  Apply these constraints to any UI work in this conversation.

- `/fixing-accessibility <file>`
  Review the file against all rules below and report:
  - violations (quote the exact line or snippet)
  - why it matters (one short sentence)
  - a concrete fix (code-level suggestion)

Do not rewrite large parts of the UI. Prefer minimal, targeted fixes.

## when to apply

Reference these guidelines when:
- adding or changing buttons, links, inputs, menus, dialogs, tabs, dropdowns
- building forms, validation, error states, helper text
- implementing keyboard shortcuts or custom interactions
- working on focus states, focus trapping, or modal behavior
- rendering icon-only controls
- adding hover-only interactions or hidden content

## rule categories by priority

| priority | category | impact |
|----------|----------|--------|
| 1 | accessible names | critical |
| 2 | keyboard access | critical |
| 3 | focus and dialogs | critical |
| 4 | semantics | high |
| 5 | forms and errors | high |
| 6 | announcements | medium-high |
| 7 | contrast and states | medium |
| 8 | media and motion | low-medium |
| 9 | tool boundaries | critical |

## quick reference

### 1. accessible names (critical)

- every interactive control must have an accessible name
- icon-only buttons must have aria-label or aria-labelledby
- every input, select, and textarea must be labeled
- links must have meaningful text (no “click here”)
- decorative icons must be aria-hidden

### 2. keyboard access (critical)

- do not use div or span as buttons without full keyboard support
- all interactive elements must be reachable by Tab
- focus must be visible for keyboard users
- do not use tabindex greater than 0
- Escape must close dialogs or overlays when applicable

### 3. focus and dialogs (critical)

- modals must trap focus while open
- restore focus to the trigger on close
- set initial focus inside dialogs
- opening a dialog should not scroll the page unexpectedly

### 4. semantics (high)

- prefer native elements (button, a, input) over role-based hacks
- if a role is used, required aria attributes must be present
- lists must use ul or ol with li
- do not skip heading levels
- tables must use th for headers when applicable

### 5. forms and errors (high)

- errors must be linked to fields using aria-describedby
- required fields must be announced
- invalid fields must set aria-invalid
- helper text must be associated with inputs
- disabled submit actions must explain why

### 6. announcements (medium-high)

- critical form errors should use aria-live
- loading states should use aria-busy or status text
- toasts must not be the only way to convey critical information
- expandable controls must use aria-expanded and aria-controls

### 7. contrast and states (medium)

- ensure sufficient contrast for text and icons
- hover-only interactions must have keyboard equivalents
- disabled states must not rely on color alone
- do not remove focus outlines without a visible replacement

### 8. media and motion (low-medium)

- images must have correct alt text (meaningful or empty)
- videos with speech should provide captions when relevant
- respect prefers-reduced-motion for non-essential motion
- avoid autoplaying media with sound

### 9. tool boundaries (critical)

- prefer minimal changes, do not refactor unrelated code
- do not add aria when native semantics already solve the problem
- do not migrate UI libraries unless requested

## common fixes

```html
<!-- icon-only button: add aria-label -->
<!-- before --> <button><svg>...</svg></button>
<!-- after -->  <button aria-label="Close"><svg aria-hidden="true">...</svg></button>

<!-- div as button: use native element -->
<!-- before --> <div onclick="save()">Save</div>
<!-- after -->  <button onclick="save()">Save</button>

<!-- form error: link with aria-describedby -->
<!-- before --> <input id="email" /> <span>Invalid email</span>
<!-- after -->  <input id="email" aria-describedby="email-err" aria-invalid="true" /> <span id="email-err">Invalid email</span>
```

## review guidance

- fix critical issues first (names, keyboard, focus, tool boundaries)
- prefer native HTML before adding aria
- quote the exact snippet, state the failure, propose a small fix
- for complex widgets (menu, dialog, combobox), prefer established accessible primitives over custom behavior

## Imported Module: Screen Reader Testing
---
name: screen-reader-testing
description: "Test web applications with screen readers including VoiceOver, NVDA, and JAWS. Use when validating screen reader compatibility, debugging accessibility issues, or ensuring assistive technology supp..."
risk: unknown
source: community
date_added: "2026-02-27"
---

# Screen Reader Testing

Practical guide to testing web applications with screen readers for comprehensive accessibility validation.

## Use this skill when

- Validating screen reader compatibility
- Testing ARIA implementations
- Debugging assistive technology issues
- Verifying form accessibility
- Testing dynamic content announcements
- Ensuring navigation accessibility

## Do not use this skill when

- The task is unrelated to screen reader testing
- You need a different domain or tool outside this scope

## Instructions

- Clarify goals, constraints, and required inputs.
- Apply relevant best practices and validate outcomes.
- Provide actionable steps and verification.
- If detailed examples are required, open `resources/implementation-playbook.md`.

## Resources

- `resources/implementation-playbook.md` for detailed patterns and examples.

## Imported Module: Wcag Audit Patterns
---
name: wcag-audit-patterns
description: "Conduct WCAG 2.2 accessibility audits with automated testing, manual verification, and remediation guidance. Use when auditing websites for accessibility, fixing WCAG violations, or implementing ac..."
risk: unknown
source: community
date_added: "2026-02-27"
---

# WCAG Audit Patterns

Comprehensive guide to auditing web content against WCAG 2.2 guidelines with actionable remediation strategies.

## Use this skill when

- Conducting accessibility audits
- Fixing WCAG violations
- Implementing accessible components
- Preparing for accessibility lawsuits
- Meeting ADA/Section 508 requirements
- Achieving VPAT compliance

## Do not use this skill when

- You need legal advice or formal certification
- You only want a quick automated scan without manual verification
- You cannot access the UI or source for remediation work

## Instructions

1. Run automated scans (axe, Lighthouse, WAVE) to collect initial findings.
2. Perform manual checks (keyboard navigation, focus order, screen reader flows).
3. Map each issue to a WCAG criterion, severity, and remediation guidance.
4. Re-test after fixes and document residual risk and compliance status.

Refer to `resources/implementation-playbook.md` for detailed patterns, checklists, and templates.

## Safety

- Avoid claiming legal compliance without expert review.
- Keep evidence of test steps and results for audit trails.

## Resources

- `resources/implementation-playbook.md` for detailed patterns, checklists, and templates.

## Imported Module: Web Design Guidelines
---
name: web-design-guidelines
description: "Review UI code for Web Interface Guidelines compliance. Use when asked to \\\"review my UI\\\", \\\"check accessibility\\\", \\\"audit design\\\", \\\"review UX\\\", or \\\"check my site aga..."
risk: unknown
source: community
date_added: "2026-02-27"
---

# Web Interface Guidelines

Review files for compliance with Web Interface Guidelines.

## How It Works

1. Fetch the latest guidelines from the source URL below
2. Read the specified files (or prompt user for files/pattern)
3. Check against all rules in the fetched guidelines
4. Output findings in the terse `file:line` format

## Guidelines Source

Fetch fresh guidelines before each review:

```
https://raw.githubusercontent.com/vercel-labs/web-interface-guidelines/main/command.md
```

Use WebFetch to retrieve the latest rules. The fetched content contains all the rules and output format instructions.

## Usage

When a user provides a file or pattern argument:
1. Fetch guidelines from the source URL above
2. Read the specified files
3. Apply all rules from the fetched guidelines
4. Output findings using the format specified in the guidelines

If no files specified, ask the user which files to review.

## When to Use
This skill is applicable to execute the workflow or actions described in the overview.

