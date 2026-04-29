# Skill Catalogue

This catalogue lists every installable super skill in this collection. Each `super-*` folder is designed to be installable on its own. Skills marked `Yes` in Product Package already include standalone README, changelog, version, and examples scaffold.

| Skill | Description | Modules | Product Package |
| --- | --- | ---: | --- |
| `super-ai-ml-agents` | Agent systems: architecture, tools, memory, orchestration, and autonomy. Use for building AI agents and workflows. | 3 | Yes |
| `super-ai-ml-foundation` | AI/ML foundations: model selection, prompt design, RAG, embeddings, and vector search. Use for core AI app design and build. | 3 | Yes |
| `super-ai-ml-ops` | AI/ML operations: evaluation, monitoring, cost control, and reliability. Use for productionizing AI systems. | 2 | Yes |
| `super-automation` | Workflow and app automations across SaaS tools, APIs, and integrations. | 2 | Yes |
| `super-cloud` | Cloud platform engineering across AWS/Azure/GCP, IaC, networking, containers, and cost optimisation. | 3 | Yes |
| `super-data-analytics` | Data & analytics: pipelines, BI, SQL optimisation, analytics tooling, and dashboards. | 3 | Yes |
| `super-design-core` | Core UI/UX and product design: IA, flows, visual systems, UI patterns, and generators. Use for end-to-end design work. | 4 | Yes |
| `super-design-quality` | Design QA: accessibility, WCAG compliance, and visual/consistency validation. Use for audits and remediation. | 2 | Yes |
| `super-engineering-devops` | Engineering and DevOps delivery: architecture, build, test, deploy, and operate reliable systems. | 3 | Yes |
| `super-gaming-3d-media` | Gaming, 3D, and media: engines, 3D web, animation, audio/video tooling. | 3 | Yes |
| `super-healthcare-wellness` | Healthcare and wellness analysis: health data, trends, and guidance workflows. | 2 | Yes |
| `super-industry-ops` | Industry-specific operations: logistics, manufacturing, procurement, and quality workflows. | 3 | Yes |
| `super-legal-hr-compliance` | Legal, HR, and compliance: contracts, policies, and regulatory guidance (non-security). | 2 | Yes |
| `super-marketing-execution` | Marketing execution: campaign orchestration, copywriting, CRO, analytics, paid ads, email, and social content. Use to ship campaigns and improve conversions. | 7 | Yes |
| `super-marketing-strategy` | Marketing strategy: positioning, ICP, growth hypotheses, and content strategy. Use to define the plan before execution. | 3 | Yes |
| `super-office-docs-presentation` | Office, docs, and presentations: PDFs, docs, slides, spreadsheets, and documentation workflows. | 2 | Yes |
| `super-product-business-finance` | Product, business, and finance: market sizing, pricing, monetisation, and PM frameworks. | 3 | Yes |
| `super-security` | Security audits, threat modelling, testing, and remediation across apps, APIs, and infrastructure. | 3 | Yes |
| `super-seo-foundation` | SEO foundations: audits, technical fixes, schema, sitemaps, hreflang, images, and tooling. Use for baseline health and technical readiness. | 3 | Yes |
| `super-seo-growth` | SEO growth: content optimisation, programmatic SEO, AI/GEO visibility, and ongoing performance improvements. Use after a baseline audit or run a quick check first. | 3 | Yes |
| `super-specialized-platform-sdks` | Specialized platform SDKs: ERP/CRM, commerce platforms, and messaging/bot platforms. | 3 | Yes |

## Versioning Model

- The collection has a root version in `catalog.json`.
- Each product-ready skill also has its own `VERSION` and `CHANGELOG.md`.
- Skills can be split into standalone repositories later without changing their internal `SKILL.md` entry point.

## Publishing Model

Start with this repository as the master catalogue. Publish individual skill folders as standalone products when they need their own roadmap, issues, releases, website, or package distribution.
