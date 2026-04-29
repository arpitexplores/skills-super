# Super AI/ML Foundation

Design core AI applications with model selection, prompt systems, RAG, embeddings, and vector search.

## Install

Copy this folder into your agent's skills directory, then restart or reload the agent.

```bash
cp -R super-ai-ml-foundation ~/.your-agent/skills/
```

Use it by name:

```text
Use $super-ai-ml-foundation to help with this request.
```

## Best For

- AI app architecture
- model and provider selection
- prompt system design
- RAG and retrieval design
- embedding and vector search workflows

## Outputs

- AI application plan
- model and prompt strategy
- RAG architecture
- retrieval and evaluation checklist

## Modules

| Module | Purpose |
| --- | --- |
| `ai-engineer.md` | AI application architecture, model selection, tool use, and implementation planning |
| `prompt-engineering-patterns.md` | Prompt patterns, instruction hierarchy, structured outputs, and prompt testing |
| `rag-engineer.md` | RAG design, chunking, retrieval, embeddings, ranking, and grounding workflows |

## Example Prompts

- `Use $super-ai-ml-foundation to design a RAG assistant for this knowledge base.`
- `Use $super-ai-ml-foundation to choose the right model strategy for this AI feature.`
- `Use $super-ai-ml-foundation to improve this prompt and retrieval flow.`

## Package Contents

- `SKILL.md` is the installable skill entry point.
- `references/modules/` contains detailed workflows loaded only when needed.
- `agents/` contains optional agent metadata where supported.
- `scripts/` and `assets/` are optional helpers when bundled.

## Compatibility

This skill is plain Markdown and is intended to be agent-agnostic. If a bundled helper mentions a specific tool path, translate that instruction to the equivalent path for your environment.

## Version

See `VERSION` and `CHANGELOG.md`.

## Licence

MIT. See the root repository `LICENSE`.
