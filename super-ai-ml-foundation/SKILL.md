---
name: super-ai-ml-foundation
description: "AI/ML foundations: model selection, prompt design, RAG, embeddings, and vector search. Use for core AI app design and build."
---

# Super AI/ML Foundation

## Overview
Establish the core AI/ML architecture before building agents or ops layers.


## User Intent Examples
- "Need help with AI Engineering for my product/site."
- "Create a plan for Prompt Engineering."
- "Audit or improve RAG Engineering."

## Workflow
1. Confirm use case, success criteria, latency, and cost targets.
2. Select model family and deployment approach (hosted vs self-hosted).
3. Design prompts, tool interfaces, and guardrails.
4. Plan and implement RAG: chunking, embeddings, indexing, retrieval.
5. Validate relevance, quality, and failure modes with small tests.
6. Document tradeoffs, risks, and next experiments.

## Minimal Intake Questions
- Primary goal or outcome
- Scope (pages, systems, teams, or timeframe)
- Constraints (tools, budget, timeline)

## Output Format
- Use-case brief and success metrics
- Model choice with rationale
- Prompt and tool plan
- RAG architecture plan
- Risks, mitigations, and next steps

## Routing Map (Modules)
- **AI Engineering** -> `references/modules/ai-engineer.md`
- **Prompt Engineering** -> `references/modules/prompt-engineering-patterns.md`
- **RAG Engineering** -> `references/modules/rag-engineer.md`

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
- Do not claim benchmark results without data.
- Separate measured results from hypotheses.
- Prefer the smallest viable model and simplest retrieval setup.
