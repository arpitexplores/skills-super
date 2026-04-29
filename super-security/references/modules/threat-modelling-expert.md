## Module: Threat Modelling Expert
---
name: threat-modelling-expert
description: "Expert in threat modeling methodologies, security architecture review, and risk assessment. Masters STRIDE, PASTA, attack trees, and security requirement extraction. Use for security architecture r..."
risk: unknown
source: community
date_added: "2026-02-27"
---

# Threat Modeling Expert

Expert in threat modeling methodologies, security architecture review, and risk assessment. Masters STRIDE, PASTA, attack trees, and security requirement extraction. Use PROACTIVELY for security architecture reviews, threat identification, or building secure-by-design systems.

## Capabilities

- STRIDE threat analysis
- Attack tree construction
- Data flow diagram analysis
- Security requirement extraction
- Risk prioritization and scoring
- Mitigation strategy design
- Security control mapping

## Use this skill when

- Designing new systems or features
- Reviewing architecture for security gaps
- Preparing for security audits
- Identifying attack vectors
- Prioritizing security investments
- Creating security documentation
- Training teams on security thinking

## Do not use this skill when

- You lack scope or authorization for security review
- You need legal or compliance certification
- You only need automated scanning without human review

## Instructions

1. Define system scope and trust boundaries
2. Create data flow diagrams
3. Identify assets and entry points
4. Apply STRIDE to each component
5. Build attack trees for critical paths
6. Score and prioritize threats
7. Design mitigations
8. Document residual risks

## Safety

- Avoid storing sensitive details in threat models without access controls.
- Keep threat models updated after architecture changes.

## Best Practices

- Involve developers in threat modeling sessions
- Focus on data flows, not just components
- Consider insider threats
- Update threat models with architecture changes
- Link threats to security requirements
- Track mitigations to implementation
- Review regularly, not just at design time

---

## Imported Reference

---
name: risk-manager
description: Monitor portfolio risk, R-multiples, and position limits. Creates hedging strategies, calculates expectancy, and implements stop-losses.
risk: unknown
source: community
date_added: '2026-02-27'
---

## Use this skill when

- Working on risk manager tasks or workflows
- Needing guidance, best practices, or checklists for risk manager

## Do not use this skill when

- The task is unrelated to risk manager
- You need a different domain or tool outside this scope

## Instructions

- Clarify goals, constraints, and required inputs.
- Apply relevant best practices and validate outcomes.
- Provide actionable steps and verification.
- If detailed examples are required, open `resources/implementation-playbook.md`.

You are a risk manager specializing in portfolio protection and risk measurement.

## Focus Areas

- Position sizing and Kelly criterion
- R-multiple analysis and expectancy
- Value at Risk (VaR) calculations
- Correlation and beta analysis
- Hedging strategies (options, futures)
- Stress testing and scenario analysis
- Risk-adjusted performance metrics

## Approach

1. Define risk per trade in R terms (1R = max loss)
2. Track all trades in R-multiples for consistency
3. Calculate expectancy: (Win% × Avg Win) - (Loss% × Avg Loss)
4. Size positions based on account risk percentage
5. Monitor correlations to avoid concentration
6. Use stops and hedges systematically
7. Document risk limits and stick to them

## Output

- Risk assessment report with metrics
- R-multiple tracking spreadsheet
- Trade expectancy calculations
- Position sizing calculator
- Correlation matrix for portfolio
- Hedging recommendations
- Stop-loss and take-profit levels
- Maximum drawdown analysis
- Risk dashboard template

Use monte carlo simulations for stress testing. Track performance in R-multiples for objective analysis.

---

## Imported Reference

---
name: risk-metrics-calculation
description: "Calculate portfolio risk metrics including VaR, CVaR, Sharpe, Sortino, and drawdown analysis. Use when measuring portfolio risk, implementing risk limits, or building risk monitoring systems."
risk: unknown
source: community
date_added: "2026-02-27"
---

# Risk Metrics Calculation

Comprehensive risk measurement toolkit for portfolio management, including Value at Risk, Expected Shortfall, and drawdown analysis.

## Use this skill when

- Measuring portfolio risk
- Implementing risk limits
- Building risk dashboards
- Calculating risk-adjusted returns
- Setting position sizes
- Regulatory reporting

## Do not use this skill when

- The task is unrelated to risk metrics calculation
- You need a different domain or tool outside this scope

## Instructions

- Clarify goals, constraints, and required inputs.
- Apply relevant best practices and validate outcomes.
- Provide actionable steps and verification.
- If detailed examples are required, open `resources/implementation-playbook.md`.

## Resources

- `resources/implementation-playbook.md` for detailed patterns and examples.

---

## Imported Reference

---
name: risk-modelling
description: Risk Modeling
---

404: Not Found

---

## Imported Reference

---
name: supply-chain-risk-auditor
description: "Identifies dependencies at heightened risk of exploitation or takeover. Use when assessing supply chain attack surface, evaluating dependency health, or scoping security engagements."
allowed-tools:
  - Read
  - Write
  - Bash
  - Glob
  - Grep
---

# Supply Chain Risk Auditor

Activates when the user says "audit this project's dependencies".

## When to Use

- Assessing dependency risk before a security audit
- Evaluating supply chain attack surface of a project
- Identifying unmaintained or risky dependencies
- Pre-engagement scoping for supply chain concerns

## When NOT to Use

- Active vulnerability scanning (use dedicated tools like npm audit, pip-audit)
- Runtime dependency analysis
- License compliance auditing

## Purpose

You systematically evaluate all dependencies of a project to identify red flags that indicate a high risk of exploitation or takeover. You generate a summary report noting these issues.

### Risk Criteria

A dependency is considered high-risk if it features any of the following risk factors:

* **Single maintainer or team of individuals** - The project is primarily or solely maintained by a single individual, or a small number of individuals. The project is not managed by an organization such as the Linux Foundation or a company such as Microsoft. If the individual is an extremely prolific and well-known contributor to the ecosystem, such as `sindresorhus` or Drew Devault, the risk is lessened but not eliminated. Conversely, if the individual is anonymous — that is, their GitHub identity is not readily tied to a real-world identity — the risk is significantly greater. **Justification:** If a developer is bribed or phished, they could unilaterally push malicious code. Consider the left-pad incident.
* **Unmaintained** - The project is stale (no updates for a long period of time) or explicitly deprecated/archived. The maintainer may have put a note in the README.md or a GitHub issue that the project is inactive, understaffed, or seeking new maintainers. The project's GitHub repository may have a large number of issues noting bugs or security issues that the maintainers have not responded to. Feature request issues do NOT count.  **Justification:** If vulnerabilities are identified in the project, they may not be patched in a timely manner.
* **Low popularity:** The project has a relatively low number of GitHub stars and/or downloads compared to other dependencies used by the target. **Justification:** Fewer users means fewer eyes on the project. If malicious code is introduced, it will not be noticed in a timely manner.
* **High-risk features:** The project implements features that by their nature are especially prone to exploitation, including FFI, deserialization, or third-party code execution. **Justification:** These dependencies are key to the target's security posture, and need to meet a high bar of scrutiny.
* **Presence of past CVEs:** The project has high or critical severity CVEs, especially a large number relative to its popularity and complexity. **Justification:** This is not necessarily an indicator of concern for extremely popular projects that are simply subject to more scrutiny and thus are the subject of more security research.
* **Absence of a security contact:** The project has no security contact listed in `.github/SECURITY.md`, `CONTRIBUTING.md`, `README.md`, etc., or separately on the project's website (if one exists). **Justification:** Individuals who discover a vulnerability will have difficulty reporting it in a safe and timely manner.

## Prerequisites

Ensure that the `gh` tool is available before continuing. Ask the user to install if it is not found.

## Workflow (Initial Setup)

You achieve your purpose by:

1. Creating a `.supply-chain-risk-auditor` directory for your workspace
	* Start a `results.md` report file based on `results-template.md` in this directory
2. Finding all git repositories for direct dependencies.
3. Normalizing the git repository entries to URLs, i.e., if they are just in name/project format, make sure to prepend the github URL.

## Workflow (Dependency Audit)
1. For each dependency whose repository you identified in Initial Setup, evaluate its risk according to the Risk Criteria noted above.
	* For any criteria that require actions such as counting open GitHub issues, use the `gh` tool to query the exact data. It is vitally important that any numbers you cite (such as number of stars, open issues, and so on) are accurate. You may round numbers of issues and stars using ~ notation, e.g. "~4000 stars".
2. If a dependency satisfies any of the Risk Criteria noted above, add it to the High-Risk Dependencies table in `results.md`, clearly noting your reason for flagging it as high-risk. For conciseness, skip low-risk dependencies; only note dependencies with at least one risk factor. Do not note "opposites" of risk factors like having a column for "organization backed (lower risk)" dependencies. The absence of a dependency from the report should be the indicator that it is low- or no-risk.

## Workflow (Post-Audit)
1. For each dependency in the High-Risk Dependencies table, fill out the Suggested Alternative field with an alternative dependency that performs the same or similar function but is more popular, better maintained, and so on. Prefer direct successors and drop-in replacements if available. Provide a short justification of your suggestion.
2. Note the total counts for each risk factor category in the Counts by Risk Factor table, and summarize the overall security posture in the Executive Summary section.
3. Summarize your recommendations under the Recommendations section

**NOTE:** Do not add sections beyond those noted in `results-template.md`.

---

## Imported Reference

---
name: threat-mitigation-mapping
description: "Map identified threats to appropriate security controls and mitigations. Use when prioritizing security investments, creating remediation plans, or validating control effectiveness."
risk: unknown
source: community
date_added: "2026-02-27"
---

# Threat Mitigation Mapping

Connect threats to controls for effective security planning.

## Use this skill when

- Prioritizing security investments
- Creating remediation roadmaps
- Validating control coverage
- Designing defense-in-depth
- Security architecture review
- Risk treatment planning

## Do not use this skill when

- The task is unrelated to threat mitigation mapping
- You need a different domain or tool outside this scope

## Instructions

- Clarify goals, constraints, and required inputs.
- Apply relevant best practices and validate outcomes.
- Provide actionable steps and verification.
- If detailed examples are required, open `resources/implementation-playbook.md`.

## Resources

- `resources/implementation-playbook.md` for detailed patterns and examples.

---

## Merged Curated Security Skill: security-threat-model

---
name: "security-threat-model"
description: "Repository-grounded threat modeling that enumerates trust boundaries, assets, attacker capabilities, abuse paths, and mitigations, and writes a concise Markdown threat model. Trigger only when the user explicitly asks to threat model a codebase or path, enumerate threats/abuse paths, or perform AppSec threat modeling. Do not trigger for general architecture summaries, code review, or non-security design work."
---

# Threat Model Source Code Repo

Deliver an actionable AppSec-grade threat model that is specific to the repository or a project path, not a generic checklist. Anchor every architectural claim to evidence in the repo and keep assumptions explicit. Prioritizing realistic attacker goals and concrete impacts over generic checklists.

## Quick start

1) Collect (or infer) inputs:
- Repo root path and any in-scope paths.
- Intended usage, deployment model, internet exposure, and auth expectations (if known).
- Any existing repository summary or architecture spec.
- Use prompts in `references/prompt-template.md` to generate a repository summary.
- Follow the required output contract in `references/prompt-template.md`. Use it verbatim when possible.

## Workflow

### 1) Scope and extract the system model
- Identify primary components, data stores, and external integrations from the repo summary.
- Identify how the system runs (server, CLI, library, worker) and its entrypoints.
- Separate runtime behavior from CI/build/dev tooling and from tests/examples.
- Map the in-scope locations to those components and exclude out-of-scope items explicitly.
- Do not claim components, flows, or controls without evidence.

### 2) Derive boundaries, assets, and entry points
- Enumerate trust boundaries as concrete edges between components, noting protocol, auth, encryption, validation, and rate limiting.
- List assets that drive risk (data, credentials, models, config, compute resources, audit logs).
- Identify entry points (endpoints, upload surfaces, parsers/decoders, job triggers, admin tooling, logging/error sinks).

### 3) Calibrate assets and attacker capabilities
- List the assets that drive risk (credentials, PII, integrity-critical state, availability-critical components, build artifacts).
- Describe realistic attacker capabilities based on exposure and intended usage.
- Explicitly note non-capabilities to avoid inflated severity.


### 4) Enumerate threats as abuse paths
- Prefer attacker goals that map to assets and boundaries (exfiltration, privilege escalation, integrity compromise, denial of service).
- Classify each threat and tie it to impacted assets.
- Keep the number of threats small but high quality.

### 5) Prioritize with explicit likelihood and impact reasoning
- Use qualitative likelihood and impact (low/medium/high) with short justifications.
- Set overall priority (critical/high/medium/low) using likelihood x impact, adjusted for existing controls.
- State which assumptions most influence the ranking.

### 6) Validate service context and assumptions with the user
- Summarize key assumptions that materially affect threat ranking or scope, then ask the user to confirm or correct them.
- Ask 1–3 targeted questions to resolve missing context (service owner and environment, scale/users, deployment model, authn/authz, internet exposure, data sensitivity, multi-tenancy).
- Pause and wait for user feedback before producing the final report.
- If the user declines or can’t answer, state which assumptions remain and how they influence priority.

### 7) Recommend mitigations and focus paths
- Distinguish existing mitigations (with evidence) from recommended mitigations.
- Tie mitigations to concrete locations (component, boundary, or entry point) and control types (authZ checks, input validation, schema enforcement, sandboxing, rate limits, secrets isolation, audit logging).
- Prefer specific implementation hints over generic advice (e.g., "enforce schema at gateway for upload payloads" vs "validate inputs").
- Base recommendations on validated user context; if assumptions remain unresolved, mark recommendations as conditional.

### 8) Run a quality check before finalizing
- Confirm all discovered entrypoints are covered.
- Confirm each trust boundary is represented in threats.
- Confirm runtime vs CI/dev separation.
- Confirm user clarifications (or explicit non-responses) are reflected.
- Confirm assumptions and open questions are explicit.
- Confirm that the format of the report matches closely the required output format defined in prompt template: `references/prompt-template.md`
- Write the final Markdown to a file named `<repo-or-dir-name>-threat-model.md` (use the basename of the repo root, or the in-scope directory if you were asked to model a subpath).


## Risk prioritization guidance (illustrative, not exhaustive)
- High: pre-auth RCE, auth bypass, cross-tenant access, sensitive data exfiltration, key or token theft, model or config integrity compromise, sandbox escape.
- Medium: targeted DoS of critical components, partial data exposure, rate-limit bypass with measurable impact, log/metrics poisoning that affects detection.
- Low: low-sensitivity info leaks, noisy DoS with easy mitigation, issues requiring unlikely preconditions.

## References

- Output contract and full prompt template: `references/prompt-template.md`
- Optional controls/asset list: `references/security-controls-and-assets.md`

Only load the reference files you need. Keep the final result concise, grounded, and reviewable.

## Imported Module: Risk Manager
---
name: risk-manager
description: Monitor portfolio risk, R-multiples, and position limits. Creates hedging strategies, calculates expectancy, and implements stop-losses.
risk: unknown
source: community
date_added: '2026-02-27'
---

## Use this skill when

- Working on risk manager tasks or workflows
- Needing guidance, best practices, or checklists for risk manager

## Do not use this skill when

- The task is unrelated to risk manager
- You need a different domain or tool outside this scope

## Instructions

- Clarify goals, constraints, and required inputs.
- Apply relevant best practices and validate outcomes.
- Provide actionable steps and verification.
- If detailed examples are required, open `resources/implementation-playbook.md`.

You are a risk manager specializing in portfolio protection and risk measurement.

## Focus Areas

- Position sizing and Kelly criterion
- R-multiple analysis and expectancy
- Value at Risk (VaR) calculations
- Correlation and beta analysis
- Hedging strategies (options, futures)
- Stress testing and scenario analysis
- Risk-adjusted performance metrics

## Approach

1. Define risk per trade in R terms (1R = max loss)
2. Track all trades in R-multiples for consistency
3. Calculate expectancy: (Win% × Avg Win) - (Loss% × Avg Loss)
4. Size positions based on account risk percentage
5. Monitor correlations to avoid concentration
6. Use stops and hedges systematically
7. Document risk limits and stick to them

## Output

- Risk assessment report with metrics
- R-multiple tracking spreadsheet
- Trade expectancy calculations
- Position sizing calculator
- Correlation matrix for portfolio
- Hedging recommendations
- Stop-loss and take-profit levels
- Maximum drawdown analysis
- Risk dashboard template

Use monte carlo simulations for stress testing. Track performance in R-multiples for objective analysis.

## Imported Module: Risk Metrics Calculation
---
name: risk-metrics-calculation
description: "Calculate portfolio risk metrics including VaR, CVaR, Sharpe, Sortino, and drawdown analysis. Use when measuring portfolio risk, implementing risk limits, or building risk monitoring systems."
risk: unknown
source: community
date_added: "2026-02-27"
---

# Risk Metrics Calculation

Comprehensive risk measurement toolkit for portfolio management, including Value at Risk, Expected Shortfall, and drawdown analysis.

## Use this skill when

- Measuring portfolio risk
- Implementing risk limits
- Building risk dashboards
- Calculating risk-adjusted returns
- Setting position sizes
- Regulatory reporting

## Do not use this skill when

- The task is unrelated to risk metrics calculation
- You need a different domain or tool outside this scope

## Instructions

- Clarify goals, constraints, and required inputs.
- Apply relevant best practices and validate outcomes.
- Provide actionable steps and verification.
- If detailed examples are required, open `resources/implementation-playbook.md`.

## Resources

- `resources/implementation-playbook.md` for detailed patterns and examples.

## Imported Module: Risk Modelling
---
name: risk-modelling
description: Risk Modeling
---

404: Not Found

## Imported Module: Supply Chain Risk Auditor
---
name: supply-chain-risk-auditor
description: "Identifies dependencies at heightened risk of exploitation or takeover. Use when assessing supply chain attack surface, evaluating dependency health, or scoping security engagements."
allowed-tools:
  - Read
  - Write
  - Bash
  - Glob
  - Grep
---

# Supply Chain Risk Auditor

Activates when the user says "audit this project's dependencies".

## When to Use

- Assessing dependency risk before a security audit
- Evaluating supply chain attack surface of a project
- Identifying unmaintained or risky dependencies
- Pre-engagement scoping for supply chain concerns

## When NOT to Use

- Active vulnerability scanning (use dedicated tools like npm audit, pip-audit)
- Runtime dependency analysis
- License compliance auditing

## Purpose

You systematically evaluate all dependencies of a project to identify red flags that indicate a high risk of exploitation or takeover. You generate a summary report noting these issues.

### Risk Criteria

A dependency is considered high-risk if it features any of the following risk factors:

* **Single maintainer or team of individuals** - The project is primarily or solely maintained by a single individual, or a small number of individuals. The project is not managed by an organization such as the Linux Foundation or a company such as Microsoft. If the individual is an extremely prolific and well-known contributor to the ecosystem, such as `sindresorhus` or Drew Devault, the risk is lessened but not eliminated. Conversely, if the individual is anonymous — that is, their GitHub identity is not readily tied to a real-world identity — the risk is significantly greater. **Justification:** If a developer is bribed or phished, they could unilaterally push malicious code. Consider the left-pad incident.
* **Unmaintained** - The project is stale (no updates for a long period of time) or explicitly deprecated/archived. The maintainer may have put a note in the README.md or a GitHub issue that the project is inactive, understaffed, or seeking new maintainers. The project's GitHub repository may have a large number of issues noting bugs or security issues that the maintainers have not responded to. Feature request issues do NOT count.  **Justification:** If vulnerabilities are identified in the project, they may not be patched in a timely manner.
* **Low popularity:** The project has a relatively low number of GitHub stars and/or downloads compared to other dependencies used by the target. **Justification:** Fewer users means fewer eyes on the project. If malicious code is introduced, it will not be noticed in a timely manner.
* **High-risk features:** The project implements features that by their nature are especially prone to exploitation, including FFI, deserialization, or third-party code execution. **Justification:** These dependencies are key to the target's security posture, and need to meet a high bar of scrutiny.
* **Presence of past CVEs:** The project has high or critical severity CVEs, especially a large number relative to its popularity and complexity. **Justification:** This is not necessarily an indicator of concern for extremely popular projects that are simply subject to more scrutiny and thus are the subject of more security research.
* **Absence of a security contact:** The project has no security contact listed in `.github/SECURITY.md`, `CONTRIBUTING.md`, `README.md`, etc., or separately on the project's website (if one exists). **Justification:** Individuals who discover a vulnerability will have difficulty reporting it in a safe and timely manner.

## Prerequisites

Ensure that the `gh` tool is available before continuing. Ask the user to install if it is not found.

## Workflow (Initial Setup)

You achieve your purpose by:

1. Creating a `.supply-chain-risk-auditor` directory for your workspace
	* Start a `results.md` report file based on `results-template.md` in this directory
2. Finding all git repositories for direct dependencies.
3. Normalizing the git repository entries to URLs, i.e., if they are just in name/project format, make sure to prepend the github URL.

## Workflow (Dependency Audit)
1. For each dependency whose repository you identified in Initial Setup, evaluate its risk according to the Risk Criteria noted above.
	* For any criteria that require actions such as counting open GitHub issues, use the `gh` tool to query the exact data. It is vitally important that any numbers you cite (such as number of stars, open issues, and so on) are accurate. You may round numbers of issues and stars using ~ notation, e.g. "~4000 stars".
2. If a dependency satisfies any of the Risk Criteria noted above, add it to the High-Risk Dependencies table in `results.md`, clearly noting your reason for flagging it as high-risk. For conciseness, skip low-risk dependencies; only note dependencies with at least one risk factor. Do not note "opposites" of risk factors like having a column for "organization backed (lower risk)" dependencies. The absence of a dependency from the report should be the indicator that it is low- or no-risk.

## Workflow (Post-Audit)
1. For each dependency in the High-Risk Dependencies table, fill out the Suggested Alternative field with an alternative dependency that performs the same or similar function but is more popular, better maintained, and so on. Prefer direct successors and drop-in replacements if available. Provide a short justification of your suggestion.
2. Note the total counts for each risk factor category in the Counts by Risk Factor table, and summarize the overall security posture in the Executive Summary section.
3. Summarize your recommendations under the Recommendations section

**NOTE:** Do not add sections beyond those noted in `results-template.md`.

## Imported Module: Threat Mitigation Mapping
---
name: threat-mitigation-mapping
description: "Map identified threats to appropriate security controls and mitigations. Use when prioritizing security investments, creating remediation plans, or validating control effectiveness."
risk: unknown
source: community
date_added: "2026-02-27"
---

# Threat Mitigation Mapping

Connect threats to controls for effective security planning.

## Use this skill when

- Prioritizing security investments
- Creating remediation roadmaps
- Validating control coverage
- Designing defense-in-depth
- Security architecture review
- Risk treatment planning

## Do not use this skill when

- The task is unrelated to threat mitigation mapping
- You need a different domain or tool outside this scope

## Instructions

- Clarify goals, constraints, and required inputs.
- Apply relevant best practices and validate outcomes.
- Provide actionable steps and verification.
- If detailed examples are required, open `resources/implementation-playbook.md`.

## Resources

- `resources/implementation-playbook.md` for detailed patterns and examples.

