# Super Skills

Super Skills are agent-ready Markdown skills organised around real work domains. Each skill is designed to be installed independently, used on its own, and expanded over time without exposing users to dozens of small overlapping skills.

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
| `super-ai-ml-agents` | Agent architecture, tools, memory, orchestration, and autonomy. |
| `super-ai-ml-foundation` | Model selection, prompt design, RAG, embeddings, and vector search. |
| `super-ai-ml-ops` | Evaluation, monitoring, cost control, and production reliability for AI systems. |
| `super-automation` | Workflow and app automations across SaaS tools, APIs, and integrations. |
| `super-cloud` | Cloud architecture, AWS/Azure/GCP, IaC, networking, containers, and cost optimisation. |
| `super-data-analytics` | Pipelines, BI, SQL optimisation, analytics tooling, and dashboards. |
| `super-design-core` | UI/UX, product design, IA, flows, visual systems, UI patterns, and generators. |
| `super-design-quality` | Accessibility, WCAG compliance, responsive QA, and visual consistency validation. |
| `super-engineering-devops` | Architecture, build, test, deploy, observability, and reliable system delivery. |
| `super-gaming-3d-media` | Game engines, Three.js, animation, audio/video workflows, and media tooling. |
| `super-healthcare-wellness` | Health workflows, wellness analysis, health data, and trend guidance. |
| `super-industry-ops` | Logistics, manufacturing, procurement, production scheduling, and operational quality. |
| `super-legal-hr-compliance` | Contracts, policies, HR workflows, and non-security regulatory guidance. |
| `super-marketing-execution` | Campaign orchestration, copywriting, CRO, analytics, paid ads, email, social content, and launch delivery. |
| `super-marketing-strategy` | Positioning, ICP, growth hypotheses, product marketing, and content strategy. |
| `super-office-docs-presentation` | PDFs, documents, slides, spreadsheets, and documentation workflows. |
| `super-product-business-finance` | Market sizing, startup analysis, pricing, monetisation, and PM frameworks. |
| `super-security` | Security audits, threat modelling, testing, and remediation. |
| `super-seo-foundation` | Technical SEO audits, schema, sitemaps, hreflang, images, and tooling. |
| `super-seo-growth` | Content optimisation, programmatic SEO, AI/GEO visibility, and SEO iteration. |
| `super-specialized-platform-sdks` | Salesforce, Shopify, ERP/CRM platforms, and messaging/bot SDKs. |

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
