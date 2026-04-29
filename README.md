# Super Skills

<!-- super-series-intro -->
> The go-to SUPER Skills catalogue for AI vibe coding: portable agent skills for SEO, AI SEO/GEO, marketing, UI/UX design, AI agents, automation, cloud, security, data, business, and operations.

[View the full SUPER Skills catalogue](https://github.com/arpitexplores/skills-super).
<!-- /super-series-intro -->

Super Skills are agent-ready Markdown skills organised around real work domains. Each skill is designed to be installed independently, used on its own, and expanded over time without exposing users to dozens of small overlapping skills.

## Why SUPER Skills For AI Vibe Coding

SUPER Skills are built to be the go-to skill layer for AI vibe coding: fast, agent-assisted building where the assistant needs domain expertise, practical workflows, guardrails, and implementation-ready outputs.

Instead of prompting from scratch, install the right SUPER Skill and give your AI coding agent a focused operating system for the task: technical SEO, AI SEO/GEO, marketing execution, UI/UX design, agent architecture, cloud, security, automation, data, business, and more.

**SEO and discovery keywords:** AI vibe coding, AI coding skills, agent skills, AI coding agents, AI development workflow, Markdown skills, technical SEO, SEO audit, AI SEO, GEO, generative engine optimisation, LLM visibility, marketing execution, UI/UX design, AI agents.

## How They Work

Each `super-*` folder is one installable skill:

```text
super-example/
├── SKILL.md
├── agents/
│   └── openai.yaml
└── references/
    └── modules/
        └── focused-module.md
```

The root `SKILL.md` is the public entry point. It explains what the skill does, what users can ask, what output to expect, and which internal module to load. Detailed workflows live in `references/modules/` so agents can load only the context they need.

## Product Model

This repository is the master catalogue, but each skill is structured to become its own standalone product over time.

Product-ready skill folders may include:

```text
super-example/
├── SKILL.md
├── README.md
├── CHANGELOG.md
├── VERSION
├── examples/
├── agents/
└── references/
```

All `21` skills are now product-packaged with standalone README, changelog, version, and examples scaffold.

See `CATALOG.md` and `catalog.json` for the full catalogue and product-package status.

To export each skill as a standalone product repository folder, see `PUBLISHING.md`.

## Install

Install one skill by copying its folder into your AI agent's skills directory, then restart or reload the agent.

Example:

```bash
cp -R super-seo-foundation ~/.your-agent/skills/
```

Use the installed skill by name, for example:

```text
Use $super-seo-foundation to audit this site: https://example.com
```

Exact install paths vary by tool. The skills themselves are plain Markdown and are intended to remain agent-agnostic.

## Skills

| Skill | What it covers |
| --- | --- |
| `super-ai-ml-agents` | The go-to AI vibe coding skill for agent systems: AI agents, tool use, memory, orchestration, multi-agent patterns, autonomy, and production guardrails. |
| `super-ai-ml-foundation` | The go-to AI vibe coding skill for AI application foundations: model selection, prompt engineering, RAG, embeddings, vector search, and production-ready AI app design. |
| `super-ai-ml-ops` | The go-to AI vibe coding skill for AI operations: LLM evaluation, monitoring, cost control, reliability, latency, release gates, and production AI governance. |
| `super-automation` | The go-to AI vibe coding skill for automation: SaaS workflows, API integrations, triggers, permissions, retries, monitoring, and GitHub automation. |
| `super-cloud` | The go-to AI vibe coding skill for cloud engineering: AWS, Azure, GCP, infrastructure as code, Terraform, networking, containers, reliability, and cost optimisation. |
| `super-data-analytics` | The go-to AI vibe coding skill for data and analytics: pipelines, BI dashboards, SQL optimisation, metrics, data quality, and analytics workflows. |
| `super-design-core` | The go-to AI vibe coding skill for product design: UI/UX, design systems, frontend UI patterns, information architecture, flows, visual systems, and implementable interface guidance. |
| `super-design-quality` | The go-to AI vibe coding skill for design QA: accessibility, WCAG, responsive testing, visual consistency, UI polish, and remediation plans. |
| `super-engineering-devops` | The go-to AI vibe coding skill for engineering and DevOps: architecture, full-stack implementation, CI/CD, observability, incidents, testing, and reliability. |
| `super-gaming-3d-media` | The go-to AI vibe coding skill for games, 3D, and media: game engines, Three.js, animation, audio/video workflows, asset pipelines, and performance. |
| `super-healthcare-wellness` | The go-to AI vibe coding skill for healthcare and wellness workflows: health trend analysis, care workflows, wellness data, safety boundaries, and non-diagnostic guidance. |
| `super-industry-ops` | The go-to AI vibe coding skill for industry operations: logistics, manufacturing, procurement, production scheduling, supply chain workflows, and operational quality. |
| `super-legal-hr-compliance` | The go-to AI vibe coding skill for legal, HR, and compliance workflows: contracts, policies, HR processes, obligations, internal comms, and non-security regulatory guidance. |
| `super-marketing-execution` | The go-to AI vibe coding skill for marketing execution: campaign orchestration, CRO, copywriting, analytics, email, social, paid ads, landing pages, and growth workflows. |
| `super-marketing-strategy` | The go-to AI vibe coding skill for marketing strategy: positioning, ICP, product marketing, growth hypotheses, content strategy, launch strategy, and GTM planning. |
| `super-office-docs-presentation` | The go-to AI vibe coding skill for office workflows: documents, PDFs, presentations, spreadsheets, documentation systems, templates, and productivity automation. |
| `super-product-business-finance` | The go-to AI vibe coding skill for product, business, and finance: market sizing, startup analysis, pricing, monetisation, roadmap decisions, and PM frameworks. |
| `super-security` | The go-to AI vibe coding skill for security: security audits, threat modelling, web security testing, application security, API security, and remediation workflows. |
| `super-seo-foundation` | The go-to AI vibe coding skill for technical SEO: SEO audits, crawlability, indexing, schema, sitemaps, hreflang, Core Web Vitals, and Google Search Console workflows. |
| `super-seo-growth` | The go-to AI vibe coding skill for SEO growth: AI SEO, GEO, LLM visibility, content optimisation, programmatic SEO, and citation-ready organic growth. |
| `super-specialized-platform-sdks` | The go-to AI vibe coding skill for specialised platform SDKs: Shopify, Salesforce, Telegram bots, commerce platforms, CRM/ERP integrations, and messaging workflows. |

## Compatibility

These skills are designed as portable Markdown instructions. Some bundled references may mention platform-specific commands or paths when they document a real integration, but the skill should still provide useful guidance without requiring a specific AI coding app.

## Design Rules

- One visible skill per `super-*` folder.
- Exactly one `SKILL.md` per super skill.
- Detailed content belongs in `references/modules/`.
- Modules should be self-contained enough to be useful without other installed skills.
- Avoid AI coding app branding unless the module is truly about that platform.
- Prefer practical workflows, checklists, and outputs over long explanations.

## Licence

MIT. See `LICENSE`.

## SUPER Skills Series

This repository is part of the **SUPER Skills** series: standalone, installable agent skills that can be used independently or together.

### Published Series Repositories

| Repository | Purpose |
| --- | --- |
| [skills-super](https://github.com/arpitexplores/skills-super) | Master catalogue for the full SUPER Skills collection: AI vibe coding skills, agent workflows, and installable Markdown skills. |
| [super-seo-growth](https://github.com/arpitexplores/super-seo-growth) | AI SEO, GEO, LLM visibility, content optimisation, programmatic SEO, and citation readiness. |
| [super-seo-foundation](https://github.com/arpitexplores/super-seo-foundation) | Technical SEO, SEO audits, crawlability, indexing, schema, sitemaps, hreflang, Core Web Vitals, and Google tooling. |
| [super-marketing-execution](https://github.com/arpitexplores/super-marketing-execution) | Campaign orchestration, CRO, copywriting, analytics, email, social, paid ads, and growth execution. |
| [super-design-core](https://github.com/arpitexplores/super-design-core) | UI/UX, product design, design systems, frontend UI patterns, IA, flows, and visual systems. |
| [super-ai-ml-agents](https://github.com/arpitexplores/super-ai-ml-agents) | AI agents, agent architecture, tool use, memory, orchestration, multi-agent systems, and guardrails. |
| [super-ai-ml-foundation](https://github.com/arpitexplores/super-ai-ml-foundation) | Model selection, prompt engineering, RAG, embeddings, vector search, and production-ready AI app design. |
| [super-ai-ml-ops](https://github.com/arpitexplores/super-ai-ml-ops) | LLM evaluation, monitoring, cost control, reliability, latency, release gates, and production AI governance. |
| [super-automation](https://github.com/arpitexplores/super-automation) | SaaS workflows, API integrations, triggers, permissions, retries, monitoring, and GitHub automation. |
| [super-cloud](https://github.com/arpitexplores/super-cloud) | AWS, Azure, GCP, infrastructure as code, Terraform, networking, containers, reliability, and cost optimisation. |
| [super-engineering-devops](https://github.com/arpitexplores/super-engineering-devops) | Architecture, full-stack implementation, CI/CD, observability, incidents, testing, and reliability. |
| [super-security](https://github.com/arpitexplores/super-security) | Security audits, threat modelling, web security testing, application security, API security, and remediation workflows. |

Start with the skill that matches the task. Use the catalogue when you want to browse the full collection or install multiple skills.

### Additional SUPER Skills In The Catalogue

The full catalogue also includes data analytics, design quality, gaming/3D/media, healthcare/wellness, industry ops, legal/HR/compliance, marketing strategy, office/docs/presentation, product/business/finance, and specialised platform SDK skills.
