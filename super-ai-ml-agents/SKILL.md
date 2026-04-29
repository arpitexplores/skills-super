---
name: super-ai-ml-agents
description: "Agent systems: architecture, tools, memory, orchestration, and autonomy. Use for building AI agents and workflows."
---

# Super AI/ML Agents

## Overview
Build reliable agent systems with clear tool boundaries, memory, and orchestration.


## User Intent Examples
- "Need help with Agent Memory Systems for my product/site."
- "Create a plan for Agent Architecture."
- "Audit or improve Multi-Agent Patterns."

## Workflow
1. Define the agent role, scope, and allowable actions.
2. Design tool interfaces and safety constraints.
3. Choose memory strategy: short-term, long-term, and retrieval.
4. Select orchestration pattern (single agent, multi-agent, supervisor).
5. Implement guardrails, fallbacks, and human-in-the-loop controls.
6. Validate behaviour with scenarios and regression tests.

## Minimal Intake Questions
- Primary goal or outcome
- Scope (pages, systems, teams, or timeframe)
- Constraints (tools, budget, timeline)

## Output Format
- Agent scope and behaviour contract
- Tooling and permissions plan
- Memory architecture
- Orchestration pattern and flow
- Validation plan with scenarios

## Routing Map (Modules)
- **Agent Memory Systems** -> `references/modules/agent-memory-systems.md`
- **Agent Architecture** -> `references/modules/ai-agents-architect.md`
- **Multi-Agent Patterns** -> `references/modules/multi-agent-patterns.md`

## Bundled References
- `references/modules/`
- `scripts/`
- `assets/`
- `agents/`

## Compatibility Notes
- If any module references slash commands or tool-specific paths, translate them into plain-language steps.
- Keep outputs platform-agnostic unless the user specifies a specific tool, stack, or agent.

## Guardrails
- Avoid ambiguous tool routing; keep responsibilities explicit.
- Keep memory bounded and purge stale data.
- Use human approval for high-risk actions.
