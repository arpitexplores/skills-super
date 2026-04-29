## Source: references/skills/agent-memory-systems/SKILL.md

---
name: agent-memory-systems
description: "Memory is the cornerstone of intelligent agents. Without it, every interaction starts from zero. This skill covers the architecture of agent memory: short-term (context window), long-term (vector s..."
risk: unknown
source: "vibeship-spawner-skills (Apache 2.0)"
date_added: "2026-02-27"
---

# Agent Memory Systems

You are a cognitive architect who understands that memory makes agents intelligent.
You've built memory systems for agents handling millions of interactions. You know
that the hard part isn't storing - it's retrieving the right memory at the right time.

Your core insight: Memory failures look like intelligence failures. When an agent
"forgets" or gives inconsistent answers, it's almost always a retrieval problem,
not a storage problem. You obsess over chunking strategies, embedding quality,
and

## Capabilities

- agent-memory
- long-term-memory
- short-term-memory
- working-memory
- episodic-memory
- semantic-memory
- procedural-memory
- memory-retrieval
- memory-formation
- memory-decay

## Patterns

### Memory Type Architecture

Choosing the right memory type for different information

### Vector Store Selection Pattern

Choosing the right vector database for your use case

### Chunking Strategy Pattern

Breaking documents into retrievable chunks

## Anti-Patterns

### ❌ Store Everything Forever

### ❌ Chunk Without Testing Retrieval

### ❌ Single Memory Type for All Data

## ⚠️ Sharp Edges

| Issue | Severity | Solution |
|-------|----------|----------|
| Issue | critical | ## Contextual Chunking (Anthropic's approach) |
| Issue | high | ## Test different sizes |
| Issue | high | ## Always filter by metadata first |
| Issue | high | ## Add temporal scoring |
| Issue | medium | ## Detect conflicts on storage |
| Issue | medium | ## Budget tokens for different memory types |
| Issue | medium | ## Track embedding model in metadata |

## Related Skills

Works well with: `autonomous-agents`, `multi-agent-orchestration`, `llm-architect`, `agent-tool-builder`

## When to Use
This skill is applicable to execute the workflow or actions described in the overview.

---

## Merged Reference (legacy variant)

---
name: agent-memory-mcp
description: "A hybrid memory system that provides persistent, searchable knowledge management for AI agents (Architecture, Patterns, Decisions)."
risk: unknown
source: community
date_added: "2026-02-27"
---

# Agent Memory Skill

This skill provides a persistent, searchable memory bank that automatically syncs with project documentation. It runs as an MCP server to allow reading/writing/searching of long-term memories.

## Prerequisites

- Node.js (v18+)

## Setup

1. **Clone the Repository**:
   Clone the `agentMemory` project into your agent's workspace or a parallel directory:

   ```bash
   git clone https://github.com/webzler/agentMemory.git .agent/skills/agent-memory
   ```

2. **Install Dependencies**:

   ```bash
   cd .agent/skills/agent-memory
   npm install
   npm run compile
   ```

3. **Start the MCP Server**:
   Use the helper script to activate the memory bank for your current project:

   ```bash
   npm run start-server <project_id> <absolute_path_to_target_workspace>
   ```

   _Example for current directory:_

   ```bash
   npm run start-server my-project $(pwd)
   ```

## Capabilities (MCP Tools)

### `memory_search`

Search for memories by query, type, or tags.

- **Args**: `query` (string), `type?` (string), `tags?` (string[])
- **Usage**: "Find all authentication patterns" -> `memory_search({ query: "authentication", type: "pattern" })`

### `memory_write`

Record new knowledge or decisions.

- **Args**: `key` (string), `type` (string), `content` (string), `tags?` (string[])
- **Usage**: "Save this architecture decision" -> `memory_write({ key: "auth-v1", type: "decision", content: "..." })`

### `memory_read`

Retrieve specific memory content by key.

- **Args**: `key` (string)
- **Usage**: "Get the auth design" -> `memory_read({ key: "auth-v1" })`

### `memory_stats`

View analytics on memory usage.

- **Usage**: "Show memory statistics" -> `memory_stats({})`

## Dashboard

This skill includes a standalone dashboard to visualize memory usage.

```bash
npm run start-dashboard <absolute_path_to_target_workspace>
```

Access at: `http://localhost:3333`

## When to Use
This skill is applicable to execute the workflow or actions described in the overview.

---

## Merged Reference (legacy variant)

---
name: memory-systems
description: "Design short-term, long-term, and graph-based memory architectures"
risk: safe
source: "https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/tree/main/skills/memory-systems"
date_added: "2026-02-27"
---

## When to Use This Skill

Design short-term, long-term, and graph-based memory architectures

Use this skill when working with design short-term, long-term, and graph-based memory architectures.
# Memory System Design

Memory provides the persistence layer that allows agents to maintain continuity across sessions and reason over accumulated knowledge. Simple agents rely entirely on context for memory, losing all state when sessions end. Sophisticated agents implement layered memory architectures that balance immediate context needs with long-term knowledge retention. The evolution from vector stores to knowledge graphs to temporal knowledge graphs represents increasing investment in structured memory for improved retrieval and reasoning.

## When to Activate

Activate this skill when:
- Building agents that must persist across sessions
- Needing to maintain entity consistency across conversations
- Implementing reasoning over accumulated knowledge
- Designing systems that learn from past interactions
- Creating knowledge bases that grow over time
- Building temporal-aware systems that track state changes

## Core Concepts

Memory exists on a spectrum from immediate context to permanent storage. At one extreme, working memory in the context window provides zero-latency access but vanishes when sessions end. At the other extreme, permanent storage persists indefinitely but requires retrieval to enter context.

Simple vector stores lack relationship and temporal structure. Knowledge graphs preserve relationships for reasoning. Temporal knowledge graphs add validity periods for time-aware queries. Implementation choices depend on query complexity, infrastructure constraints, and accuracy requirements.

## Detailed Topics

### Memory Architecture Fundamentals

**The Context-Memory Spectrum**
Memory exists on a spectrum from immediate context to permanent storage. At one extreme, working memory in the context window provides zero-latency access but vanishes when sessions end. At the other extreme, permanent storage persists indefinitely but requires retrieval to enter context. Effective architectures use multiple layers along this spectrum.

The spectrum includes working memory (context window, zero latency, volatile), short-term memory (session-persistent, searchable, volatile), long-term memory (cross-session persistent, structured, semi-permanent), and permanent memory (archival, queryable, permanent). Each layer has different latency, capacity, and persistence characteristics.

**Why Simple Vector Stores Fall Short**
Vector RAG provides semantic retrieval by embedding queries and documents in a shared embedding space. Similarity search retrieves the most semantically similar documents. This works well for document retrieval but lacks structure for agent memory.

Vector stores lose relationship information. If an agent learns that "Customer X purchased Product Y on Date Z," a vector store can retrieve this fact if asked directly. But it cannot answer "What products did customers who purchased Product Y also buy?" because relationship structure is not preserved.

Vector stores also struggle with temporal validity. Facts change over time, but vector stores provide no mechanism to distinguish "current fact" from "outdated fact" except through explicit metadata and filtering.

**The Move to Graph-Based Memory**
Knowledge graphs preserve relationships between entities. Instead of isolated document chunks, graphs encode that Entity A has Relationship R to Entity B. This enables queries that traverse relationships rather than just similarity.

Temporal knowledge graphs add validity periods to facts. Each fact has a "valid from" and optionally "valid until" timestamp. This enables time-travel queries that reconstruct knowledge at specific points in time.

**Benchmark Performance Comparison**
The Deep Memory Retrieval (DMR) benchmark provides concrete performance data across memory architectures:

| Memory System | DMR Accuracy | Retrieval Latency | Notes |
|---------------|--------------|-------------------|-------|
| Zep (Temporal KG) | 94.8% | 2.58s | Best accuracy, fast retrieval |
| MemGPT | 93.4% | Variable | Good general performance |
| GraphRAG | ~75-85% | Variable | 20-35% gains over baseline RAG |
| Vector RAG | ~60-70% | Fast | Loses relationship structure |
| Recursive Summarization | 35.3% | Low | Severe information loss |

Zep demonstrated 90% reduction in retrieval latency compared to full-context baselines (2.58s vs 28.9s for GPT-5.2). This efficiency comes from retrieving only relevant subgraphs rather than entire context history.

GraphRAG achieves approximately 20-35% accuracy gains over baseline RAG in complex reasoning tasks and reduces hallucination by up to 30% through community-based summarization.

### Memory Layer Architecture

**Layer 1: Working Memory**
Working memory is the context window itself. It provides immediate access to information currently being processed but has limited capacity and vanishes when sessions end.

Working memory usage patterns include scratchpad calculations where agents track intermediate results, conversation history that preserves dialogue for current task, current task state that tracks progress on active objectives, and active retrieved documents that hold information currently being used.

Optimize working memory by keeping only active information, summarizing completed work before it falls out of attention, and using attention-favored positions for critical information.

**Layer 2: Short-Term Memory**
Short-term memory persists across the current session but not across sessions. It provides search and retrieval capabilities without the latency of permanent storage.

Common implementations include session-scoped databases that persist until session end, file-system storage in designated session directories, and in-memory caches keyed by session ID.

Short-term memory use cases include tracking conversation state across turns without stuffing context, storing intermediate results from tool calls that may be needed later, maintaining task checklists and progress tracking, and caching retrieved information within sessions.

**Layer 3: Long-Term Memory**
Long-term memory persists across sessions indefinitely. It enables agents to learn from past interactions and build knowledge over time.

Long-term memory implementations range from simple key-value stores to sophisticated graph databases. The choice depends on complexity of relationships to model, query patterns required, and acceptable infrastructure complexity.

Long-term memory use cases include learning user preferences across sessions, building domain knowledge bases that grow over time, maintaining entity registries with relationship history, and storing successful patterns that can be reused.

**Layer 4: Entity Memory**
Entity memory specifically tracks information about entities (people, places, concepts, objects) to maintain consistency. This creates a rudimentary knowledge graph where entities are recognized across multiple interactions.

Entity memory maintains entity identity by tracking that "John Doe" mentioned in one conversation is the same person in another. It maintains entity properties by storing facts discovered about entities over time. It maintains entity relationships by tracking relationships between entities as they are discovered.

**Layer 5: Temporal Knowledge Graphs**
Temporal knowledge graphs extend entity memory with explicit validity periods. Facts are not just true or false but true during specific time ranges.

This enables queries like "What was the user's address on Date X?" by retrieving facts valid during that date range. It prevents context clash when outdated information contradicts new data. It enables temporal reasoning about how entities changed over time.

### Memory Implementation Patterns

**Pattern 1: File-System-as-Memory**
The file system itself can serve as a memory layer. This pattern is simple, requires no additional infrastructure, and enables the same just-in-time loading that makes file-system-based context effective.

Implementation uses the file system hierarchy for organization. Use naming conventions that convey meaning. Store facts in structured formats (JSON, YAML). Use timestamps in filenames or metadata for temporal tracking.

Advantages: Simplicity, transparency, portability.
Disadvantages: No semantic search, no relationship tracking, manual organization required.

**Pattern 2: Vector RAG with Metadata**
Vector stores enhanced with rich metadata provide semantic search with filtering capabilities.

Implementation embeds facts or documents and stores with metadata including entity tags, temporal validity, source attribution, and confidence scores. Query includes metadata filters alongside semantic search.

**Pattern 3: Knowledge Graph**
Knowledge graphs explicitly model entities and relationships. Implementation defines entity types and relationship types, uses graph database or property graph storage, and maintains indexes for common query patterns.

**Pattern 4: Temporal Knowledge Graph**
Temporal knowledge graphs add validity periods to facts, enabling time-travel queries and preventing context clash from outdated information.

### Memory Retrieval Patterns

**Semantic Retrieval**
Retrieve memories semantically similar to current query using embedding similarity search.

**Entity-Based Retrieval**
Retrieve all memories related to specific entities by traversing graph relationships.

**Temporal Retrieval**
Retrieve memories valid at specific time or within time range using validity period filters.

### Memory Consolidation

Memories accumulate over time and require consolidation to prevent unbounded growth and remove outdated information.

**Consolidation Triggers**
Trigger consolidation after significant memory accumulation, when retrieval returns too many outdated results, periodically on a schedule, or when explicit consolidation is requested.

**Consolidation Process**
Identify outdated facts, merge related facts, update validity periods, archive or delete obsolete facts, and rebuild indexes.

## Practical Guidance

### Integration with Context

Memories must integrate with context systems to be useful. Use just-in-time memory loading to retrieve relevant memories when needed. Use strategic injection to place memories in attention-favored positions.

### Memory System Selection

Choose memory architecture based on requirements:
- Simple persistence needs: File-system memory
- Semantic search needs: Vector RAG with metadata
- Relationship reasoning needs: Knowledge graph
- Temporal validity needs: Temporal knowledge graph

## Examples

**Example 1: Entity Tracking**
```python
# Track entity across conversations
def remember_entity(entity_id, properties):
    memory.store({
        "type": "entity",
        "id": entity_id,
        "properties": properties,
        "last_updated": now()
    })

def get_entity(entity_id):
    return memory.retrieve_entity(entity_id)
```

**Example 2: Temporal Query**
```python
# What was the user's address on January 15, 2024?
def query_address_at_time(user_id, query_time):
    return temporal_graph.query("""
        MATCH (user)-[r:LIVES_AT]->(address)
        WHERE user.id = $user_id
        AND r.valid_from <= $query_time
        AND (r.valid_until IS NULL OR r.valid_until > $query_time)
        RETURN address
    """, {"user_id": user_id, "query_time": query_time})
```

## Guidelines

1. Match memory architecture to query requirements
2. Implement progressive disclosure for memory access
3. Use temporal validity to prevent outdated information conflicts
4. Consolidate memories periodically to prevent unbounded growth
5. Design for memory retrieval failures gracefully
6. Consider privacy implications of persistent memory
7. Implement backup and recovery for critical memories
8. Monitor memory growth and performance over time

## Integration

This skill builds on context-fundamentals. It connects to:

- multi-agent-patterns - Shared memory across agents
- context-optimization - Memory-based context loading
- evaluation - Evaluating memory quality

## References

Internal reference:
- Implementation Reference - Detailed implementation patterns

Related skills in this collection:
- context-fundamentals - Context basics
- multi-agent-patterns - Cross-agent memory

External resources:
- Graph database documentation (Neo4j, etc.)
- Vector store documentation (Pinecone, Weaviate, etc.)
- Research on knowledge graphs and reasoning

---

## Skill Metadata

**Created**: 2025-12-20
**Last Updated**: 2025-12-20
**Author**: Agent Skills for Context Engineering Contributors
**Version**: 1.0.0

---

## Merged Reference (legacy variant)

---
name: conversation-memory
description: "Persistent memory systems for LLM conversations including short-term, long-term, and entity-based memory Use when: conversation memory, remember, memory persistence, long-term memory, chat history."
risk: unknown
source: "vibeship-spawner-skills (Apache 2.0)"
date_added: "2026-02-27"
---

# Conversation Memory

You're a memory systems specialist who has built AI assistants that remember
users across months of interactions. You've implemented systems that know when
to remember, when to forget, and how to surface relevant memories.

You understand that memory is not just storage—it's about retrieval, relevance,
and context. You've seen systems that remember everything (and overwhelm context)
and systems that forget too much (frustrating users).

Your core principles:
1. Memory types differ—short-term, lo

## Capabilities

- short-term-memory
- long-term-memory
- entity-memory
- memory-persistence
- memory-retrieval
- memory-consolidation

## Patterns

### Tiered Memory System

Different memory tiers for different purposes

### Entity Memory

Store and update facts about entities

### Memory-Aware Prompting

Include relevant memories in prompts

## Anti-Patterns

### ❌ Remember Everything

### ❌ No Memory Retrieval

### ❌ Single Memory Store

## ⚠️ Sharp Edges

| Issue | Severity | Solution |
|-------|----------|----------|
| Memory store grows unbounded, system slows | high | // Implement memory lifecycle management |
| Retrieved memories not relevant to current query | high | // Intelligent memory retrieval |
| Memories from one user accessible to another | critical | // Strict user isolation in memory |

## Related Skills

Works well with: `context-window-management`, `rag-implementation`, `prompt-caching`, `llm-npc-dialogue`

## When to Use
This skill is applicable to execute the workflow or actions described in the overview.

---

## Merged Reference (legacy variant)

---
name: hierarchical-agent-memory
description: "Scoped AGENT_CONTEXT.md memory system that reduces context token spend. Creates directory-level context files, tracks savings via dashboard, and routes agents to the right sub-context."
risk: safe
source: "https://github.com/kromahlusenii-ops/ham"
date_added: "2026-02-27"
---

# Hierarchical Agent Memory (HAM)

Scoped memory system that gives AI coding agents a cheat sheet for each directory instead of re-reading your entire project every prompt. Root AGENT_CONTEXT.md holds global context (~200 tokens), subdirectory AGENT_CONTEXT.md files hold scoped context (~250 tokens each), and a `.memory/` layer stores decisions, patterns, and an inbox for unconfirmed inferences.

## When to Use This Skill

- Use when you want to reduce input token costs across AI coding assistant sessions
- Use when your project has 3+ directories and the agent keeps re-reading the same files
- Use when you want directory-scoped context instead of one monolithic AGENT_CONTEXT.md
- Use when you want a dashboard to visualize token savings, session history, and context health
- Use when setting up a new project and want structured agent memory from day one

## How It Works

### Step 1: Setup ("go ham")

Auto-detects your project platform and maturity, then generates the memory structure:

```
project/
├── AGENT_CONTEXT.md              # Root context (~200 tokens)
├── .memory/
│   ├── decisions.md       # Architecture Decision Records
│   ├── patterns.md        # Reusable patterns
│   ├── inbox.md           # Inferred items awaiting confirmation
│   └── audit-log.md       # Audit history
└── src/
    ├── api/AGENT_CONTEXT.md      # Scoped context for api/
    ├── components/AGENT_CONTEXT.md
    └── lib/AGENT_CONTEXT.md
```

### Step 2: Context Routing

The root AGENT_CONTEXT.md includes a routing section that tells the agent exactly which sub-context to load:

```markdown
## Context Routing

→ api: src/api/AGENT_CONTEXT.md
→ components: src/components/AGENT_CONTEXT.md
→ lib: src/lib/AGENT_CONTEXT.md
```

The agent reads root, then immediately loads the relevant subdirectory context — no guessing.

### Step 3: Dashboard ("ham dashboard")

Launches a web dashboard at localhost:7777 that visualizes:
- Token savings (HAM-on vs HAM-off sessions)
- Daily token and cost trends
- Per-directory session breakdown
- Context file health (missing/stale/inherited AGENT_CONTEXT.md coverage)
- Routing compliance (how often the agent follows the routing map)
- Carbon/energy estimates

## Commands

| Trigger | What it does |
|---|---|
| `go ham` | Set up HAM — auto-detect platform, generate AGENT_CONTEXT.md files |
| `ham savings` | Show token and cost savings report |
| `ham dashboard` | Launch the interactive web dashboard |
| `ham audit` | Health check on memory files |
| `ham insights` | Generate actionable insights from session data |
| `ham route` | Add/update Context Routing section in root AGENT_CONTEXT.md |
| `ham carbon` | Show energy and carbon efficiency data |

## Examples

### Example 1: First-time setup

```
User: go ham

Agent: HAM setup complete. Created 8 files.
  - AGENT_CONTEXT.md (root)
  - .memory/decisions.md
  - .memory/patterns.md
  - .memory/inbox.md
  - src/api/AGENT_CONTEXT.md
  - src/components/AGENT_CONTEXT.md
  - src/lib/AGENT_CONTEXT.md
  - src/utils/AGENT_CONTEXT.md

Baseline captured in .memory/baseline.json
Run "HAM savings" to see your token and cost savings.
```

### Example 2: Checking savings

```
User: ham savings

Agent:
  Before HAM: ~7,500 tokens/prompt
  After HAM:    ~450 tokens/prompt
  Savings:    7,050 tokens (94%)

  Monthly projection (1,500 prompts):
    Sonnet: ~$31.73 saved
    Opus:   ~$158.63 saved
```

## Best Practices

- Keep root AGENT_CONTEXT.md under 60 lines / 250 tokens
- Keep subdirectory AGENT_CONTEXT.md files under 75 lines each
- Run `ham audit` every 2 weeks to catch stale or missing context files
- Use `ham route` after adding new directories to keep routing current
- Review `.memory/inbox.md` periodically — confirm or reject inferred items

## Limitations

- Token estimates use ~4 chars = 1 token approximation, not a real tokenizer
- Baseline savings comparisons are estimates based on typical agent behavior
- Dashboard requires Node.js 18+ and reads session data from `tool-specific config pathsprojects/`
- Context routing detection relies on AGENT_CONTEXT.md read order in session JSONL files
- Does not auto-update subdirectory AGENT_CONTEXT.md content — you maintain those manually or via `ham audit`
- Carbon estimates use regional grid averages, not real-time energy data

## Related Skills

- `agent-memory-systems` — general agent memory architecture patterns
- `agent-memory-mcp` — MCP-based memory integration

---

## Merged Reference (legacy variant)

---
name: context-fundamentals
description: This skill should be used when the user asks to "understand context", "explain context windows", "design agent architecture", "debug context issues", "optimize context usage", or discusses context components, attention mechanics, progressive disclosure, or context budgeting....
---

# Context Engineering Fundamentals

Context is the complete state available to a language model at inference time. It includes everything the model can attend to when generating responses: system instructions, tool definitions, retrieved documents, message history, and tool outputs. Understanding context fundamentals is prerequisite to effective context engineering.

## When to Activate

Activate this skill when:
- Designing new agent systems or modifying existing architectures
- Debugging unexpected agent behavior that may relate to context
- Optimizing context usage to reduce token costs or improve performance
- Onboarding new team members to context engineering concepts
- Reviewing context-related design decisions

## Core Concepts

Context comprises several distinct components, each with different characteristics and constraints. The attention mechanism creates a finite budget that constrains effective context usage. Progressive disclosure manages this constraint by loading information only as needed. The engineering discipline is curating the smallest high-signal token set that achieves desired outcomes.

## Detailed Topics

### The Anatomy of Context

**System Prompts**
System prompts establish the agent's core identity, constraints, and behavioral guidelines. They are loaded once at session start and typically persist throughout the conversation. System prompts should be extremely clear and use simple, direct language at the right altitude for the agent.

The right altitude balances two failure modes. At one extreme, engineers hardcode complex brittle logic that creates fragility and maintenance burden. At the other extreme, engineers provide vague high-level guidance that fails to give concrete signals for desired outputs or falsely assumes shared context. The optimal altitude strikes a balance: specific enough to guide behavior effectively, yet flexible enough to provide strong heuristics.

Organize prompts into distinct sections using XML tagging or Markdown headers to delineate background information, instructions, tool guidance, and output description. The exact formatting matters less as models become more capable, but structural clarity remains valuable.

**Tool Definitions**
Tool definitions specify the actions an agent can take. Each tool includes a name, description, parameters, and return format. Tool definitions live near the front of context after serialization, typically before or after the system prompt.

Tool descriptions collectively steer agent behavior. Poor descriptions force agents to guess; optimized descriptions include usage context, examples, and defaults. The consolidation principle states that if a human engineer cannot definitively say which tool should be used in a given situation, an agent cannot be expected to do better.

**Retrieved Documents**
Retrieved documents provide domain-specific knowledge, reference materials, or task-relevant information. Agents use retrieval augmented generation to pull relevant documents into context at runtime rather than pre-loading all possible information.

The just-in-time approach maintains lightweight identifiers (file paths, stored queries, web links) and uses these references to load data into context dynamically. This mirrors human cognition: we generally do not memorize entire corpuses of information but rather use external organization and indexing systems to retrieve relevant information on demand.

**Message History**
Message history contains the conversation between the user and agent, including previous queries, responses, and reasoning. For long-running tasks, message history can grow to dominate context usage.

Message history serves as scratchpad memory where agents track progress, maintain task state, and preserve reasoning across turns. Effective management of message history is critical for long-horizon task completion.

**Tool Outputs**
Tool outputs are the results of agent actions: file contents, search results, command execution output, API responses, and similar data. Tool outputs comprise the majority of tokens in typical agent trajectories, with research showing observations (tool outputs) can reach 83.9% of total context usage.

Tool outputs consume context whether they are relevant to current decisions or not. This creates pressure for strategies like observation masking, compaction, and selective tool result retention.

### Context Windows and Attention Mechanics

**The Attention Budget Constraint**
Language models process tokens through attention mechanisms that create pairwise relationships between all tokens in context. For n tokens, this creates n² relationships that must be computed and stored. As context length increases, the model's ability to capture these relationships gets stretched thin.

Models develop attention patterns from training data distributions where shorter sequences predominate. This means models have less experience with and fewer specialized parameters for context-wide dependencies. The result is an "attention budget" that depletes as context grows.

**Position Encoding and Context Extension**
Position encoding interpolation allows models to handle longer sequences by adapting them to originally trained smaller contexts. However, this adaptation introduces degradation in token position understanding. Models remain highly capable at longer contexts but show reduced precision for information retrieval and long-range reasoning compared to performance on shorter contexts.

**The Progressive Disclosure Principle**
Progressive disclosure manages context efficiently by loading information only as needed. At startup, agents load only skill names and descriptions—sufficient to know when a skill might be relevant. Full content loads only when a skill is activated for specific tasks.

This approach keeps agents fast while giving them access to more context on demand. The principle applies at multiple levels: skill selection, document loading, and even tool result retrieval.

### Context Quality Versus Context Quantity

The assumption that larger context windows solve memory problems has been empirically debunked. Context engineering means finding the smallest possible set of high-signal tokens that maximize the likelihood of desired outcomes.

Several factors create pressure for context efficiency. Processing cost grows disproportionately with context length—not just double the cost for double the tokens, but exponentially more in time and computing resources. Model performance degrades beyond certain context lengths even when the window technically supports more tokens. Long inputs remain expensive even with prefix caching.

The guiding principle is informativity over exhaustiveness. Include what matters for the decision at hand, exclude what does not, and design systems that can access additional information on demand.

### Context as Finite Resource

Context must be treated as a finite resource with diminishing marginal returns. Like humans with limited working memory, language models have an attention budget drawn on when parsing large volumes of context.

Every new token introduced depletes this budget by some amount. This creates the need for careful curation of available tokens. The engineering problem is optimizing utility against inherent constraints.

Context engineering is iterative and the curation phase happens each time you decide what to pass to the model. It is not a one-time prompt writing exercise but an ongoing discipline of context management.

## Practical Guidance

### File-System-Based Access

Agents with filesystem access can use progressive disclosure naturally. Store reference materials, documentation, and data externally. Load files only when needed using standard filesystem operations. This pattern avoids stuffing context with information that may not be relevant.

The file system itself provides structure that agents can navigate. File sizes suggest complexity; naming conventions hint at purpose; timestamps serve as proxies for relevance. Metadata of file references provides a mechanism to efficiently refine behavior.

### Hybrid Strategies

The most effective agents employ hybrid strategies. Pre-load some context for speed (like AGENT_CONTEXT.md files or project rules), but enable autonomous exploration for additional context as needed. The decision boundary depends on task characteristics and context dynamics.

For contexts with less dynamic content, pre-loading more upfront makes sense. For rapidly changing or highly specific information, just-in-time loading avoids stale context.

### Context Budgeting

Design with explicit context budgets in mind. Know the effective context limit for your model and task. Monitor context usage during development. Implement compaction triggers at appropriate thresholds. Design systems assuming context will degrade rather than hoping it will not.

Effective context budgeting requires understanding not just raw token counts but also attention distribution patterns. The middle of context receives less attention than the beginning and end. Place critical information at attention-favored positions.

## Examples

**Example 1: Organizing System Prompts**
```markdown
<BACKGROUND_INFORMATION>
You are a Python expert helping a development team.
Current project: Data processing pipeline in Python 3.9+
</BACKGROUND_INFORMATION>

<INSTRUCTIONS>
- Write clean, idiomatic Python code
- Include type hints for function signatures
- Add docstrings for public functions
- Follow PEP 8 style guidelines
</INSTRUCTIONS>

<TOOL_GUIDANCE>
Use bash for shell operations, python for code tasks.
File operations should use pathlib for cross-platform compatibility.
</TOOL_GUIDANCE>

<OUTPUT_DESCRIPTION>
Provide code blocks with syntax highlighting.
Explain non-obvious decisions in comments.
</OUTPUT_DESCRIPTION>
```

**Example 2: Progressive Document Loading**
```markdown
# Instead of loading all documentation at once:

# Step 1: Load summary
docs/api_summary.md          # Lightweight overview

# Step 2: Load specific section as needed
docs/api/endpoints.md        # Only when API calls needed
docs/api/authentication.md   # Only when auth context needed
```

## Guidelines

1. Treat context as a finite resource with diminishing returns
2. Place critical information at attention-favored positions (beginning and end)
3. Use progressive disclosure to defer loading until needed
4. Organize system prompts with clear section boundaries
5. Monitor context usage during development
6. Implement compaction triggers at 70-80% utilization
7. Design for context degradation rather than hoping to avoid it
8. Prefer smaller high-signal context over larger low-signal context

## Integration

This skill provides foundational context that all other skills build upon. It should be studied first before exploring:

- context-degradation - Understanding how context fails
- context-optimization - Techniques for extending context capacity
- multi-agent-patterns - How context isolation enables multi-agent systems
- tool-design - How tool definitions interact with context

## References

Internal reference:
- Context Components Reference - Detailed technical reference

Related skills in this collection:
- context-degradation - Understanding context failure patterns
- context-optimization - Techniques for efficient context use

External resources:
- Research on transformer attention mechanisms
- Production engineering guides from leading AI labs
- Framework documentation on context window management

---

## Skill Metadata

**Created**: 2025-12-20
**Last Updated**: 2025-12-20
**Author**: Agent Skills for Context Engineering Contributors
**Version**: 1.0.0

---

## Merged Reference (legacy variant)

---
name: context-optimization
description: This skill should be used when the user asks to "optimize context", "reduce token costs", "improve context efficiency", "implement KV-cache optimization", "partition context", or mentions context limits, observation masking, context budgeting, or extending effective context...
---

# Context Optimization Techniques

Context optimization extends the effective capacity of limited context windows through strategic compression, masking, caching, and partitioning. The goal is not to magically increase context windows but to make better use of available capacity. Effective optimization can double or triple effective context capacity without requiring larger models or longer contexts.

## When to Activate

Activate this skill when:
- Context limits constrain task complexity
- Optimizing for cost reduction (fewer tokens = lower costs)
- Reducing latency for long conversations
- Implementing long-running agent systems
- Needing to handle larger documents or conversations
- Building production systems at scale

## Core Concepts

Context optimization extends effective capacity through four primary strategies: compaction (summarizing context near limits), observation masking (replacing verbose outputs with references), KV-cache optimization (reusing cached computations), and context partitioning (splitting work across isolated contexts).

The key insight is that context quality matters more than quantity. Optimization preserves signal while reducing noise. The art lies in selecting what to keep versus what to discard, and when to apply each technique.

## Detailed Topics

### Compaction Strategies

**What is Compaction**
Compaction is the practice of summarizing context contents when approaching limits, then reinitializing a new context window with the summary. This distills the contents of a context window in a high-fidelity manner, enabling the agent to continue with minimal performance degradation.

Compaction typically serves as the first lever in context optimization. The art lies in selecting what to keep versus what to discard.

**Compaction Implementation**
Compaction works by identifying sections that can be compressed, generating summaries that capture essential points, and replacing full content with summaries. Priority for compression goes to tool outputs (replace with summaries), old turns (summarize early conversation), retrieved docs (summarize if recent versions exist), and never compress system prompt.

**Summary Generation**
Effective summaries preserve different elements depending on message type:

Tool outputs: Preserve key findings, metrics, and conclusions. Remove verbose raw output.

Conversational turns: Preserve key decisions, commitments, and context shifts. Remove filler and back-and-forth.

Retrieved documents: Preserve key facts and claims. Remove supporting evidence and elaboration.

### Observation Masking

**The Observation Problem**
Tool outputs can comprise 80%+ of token usage in agent trajectories. Much of this is verbose output that has already served its purpose. Once an agent has used a tool output to make a decision, keeping the full output provides diminishing value while consuming significant context.

Observation masking replaces verbose tool outputs with compact references. The information remains accessible if needed but does not consume context continuously.

**Masking Strategy Selection**
Not all observations should be masked equally:

Never mask: Observations critical to current task, observations from the most recent turn, observations used in active reasoning.

Consider masking: Observations from 3+ turns ago, verbose outputs with key points extractable, observations whose purpose has been served.

Always mask: Repeated outputs, boilerplate headers/footers, outputs already summarized in conversation.

### KV-Cache Optimization

**Understanding KV-Cache**
The KV-cache stores Key and Value tensors computed during inference, growing linearly with sequence length. Caching the KV-cache across requests sharing identical prefixes avoids recomputation.

Prefix caching reuses KV blocks across requests with identical prefixes using hash-based block matching. This dramatically reduces cost and latency for requests with common prefixes like system prompts.

**Cache Optimization Patterns**
Optimize for caching by reordering context elements to maximize cache hits. Place stable elements first (system prompt, tool definitions), then frequently reused elements, then unique elements last.

Design prompts to maximize cache stability: avoid dynamic content like timestamps, use consistent formatting, keep structure stable across sessions.

### Context Partitioning

**Sub-Agent Partitioning**
The most aggressive form of context optimization is partitioning work across sub-agents with isolated contexts. Each sub-agent operates in a clean context focused on its subtask without carrying accumulated context from other subtasks.

This approach achieves separation of concerns—the detailed search context remains isolated within sub-agents while the coordinator focuses on synthesis and analysis.

**Result Aggregation**
Aggregate results from partitioned subtasks by validating all partitions completed, merging compatible results, and summarizing if still too large.

### Budget Management

**Context Budget Allocation**
Design explicit context budgets. Allocate tokens to categories: system prompt, tool definitions, retrieved docs, message history, and reserved buffer. Monitor usage against budget and trigger optimization when approaching limits.

**Trigger-Based Optimization**
Monitor signals for optimization triggers: token utilization above 80%, degradation indicators, and performance drops. Apply appropriate optimization techniques based on context composition.

## Practical Guidance

### Optimization Decision Framework

When to optimize:
- Context utilization exceeds 70%
- Response quality degrades as conversations extend
- Costs increase due to long contexts
- Latency increases with conversation length

What to apply:
- Tool outputs dominate: observation masking
- Retrieved documents dominate: summarization or partitioning
- Message history dominates: compaction with summarization
- Multiple components: combine strategies

### Performance Considerations

Compaction should achieve 50-70% token reduction with less than 5% quality degradation. Masking should achieve 60-80% reduction in masked observations. Cache optimization should achieve 70%+ hit rate for stable workloads.

Monitor and iterate on optimization strategies based on measured effectiveness.

## Examples

**Example 1: Compaction Trigger**
```python
if context_tokens / context_limit > 0.8:
    context = compact_context(context)
```

**Example 2: Observation Masking**
```python
if len(observation) > max_length:
    ref_id = store_observation(observation)
    return f"[Obs:{ref_id} elided. Key: {extract_key(observation)}]"
```

**Example 3: Cache-Friendly Ordering**
```python
# Stable content first
context = [system_prompt, tool_definitions]  # Cacheable
context += [reused_templates]  # Reusable
context += [unique_content]  # Unique
```

## Guidelines

1. Measure before optimizing—know your current state
2. Apply compaction before masking when possible
3. Design for cache stability with consistent prompts
4. Partition before context becomes problematic
5. Monitor optimization effectiveness over time
6. Balance token savings against quality preservation
7. Test optimization at production scale
8. Implement graceful degradation for edge cases

## Integration

This skill builds on context-fundamentals and context-degradation. It connects to:

- multi-agent-patterns - Partitioning as isolation
- evaluation - Measuring optimization effectiveness
- memory-systems - Offloading context to memory

## References

Internal reference:
- Optimization Techniques Reference - Detailed technical reference

Related skills in this collection:
- context-fundamentals - Context basics
- context-degradation - Understanding when to optimize
- evaluation - Measuring optimization

External resources:
- Research on context window limitations
- KV-cache optimization techniques
- Production engineering guides

---

## Skill Metadata

**Created**: 2025-12-20
**Last Updated**: 2025-12-20
**Author**: Agent Skills for Context Engineering Contributors
**Version**: 1.0.0

---

## Merged Reference (legacy variant)

---
name: context-management-context-save
description: "Use when working with context management context save"
risk: unknown
source: community
date_added: "2026-02-27"
---

# Context Save Tool: Intelligent Context Management Specialist

## Use this skill when

- Working on context save tool: intelligent context management specialist tasks or workflows
- Needing guidance, best practices, or checklists for context save tool: intelligent context management specialist

## Do not use this skill when

- The task is unrelated to context save tool: intelligent context management specialist
- You need a different domain or tool outside this scope

## Instructions

- Clarify goals, constraints, and required inputs.
- Apply relevant best practices and validate outcomes.
- Provide actionable steps and verification.
- If detailed examples are required, open `resources/implementation-playbook.md`.

## Role and Purpose
An elite context engineering specialist focused on comprehensive, semantic, and dynamically adaptable context preservation across AI workflows. This tool orchestrates advanced context capture, serialization, and retrieval strategies to maintain institutional knowledge and enable seamless multi-session collaboration.

## Context Management Overview
The Context Save Tool is a sophisticated context engineering solution designed to:
- Capture comprehensive project state and knowledge
- Enable semantic context retrieval
- Support multi-agent workflow coordination
- Preserve architectural decisions and project evolution
- Facilitate intelligent knowledge transfer

## Requirements and Argument Handling

### Input Parameters
- `$PROJECT_ROOT`: Absolute path to project root
- `$CONTEXT_TYPE`: Granularity of context capture (minimal, standard, comprehensive)
- `$STORAGE_FORMAT`: Preferred storage format (json, markdown, vector)
- `$TAGS`: Optional semantic tags for context categorization

## Context Extraction Strategies

### 1. Semantic Information Identification
- Extract high-level architectural patterns
- Capture decision-making rationales
- Identify cross-cutting concerns and dependencies
- Map implicit knowledge structures

### 2. State Serialization Patterns
- Use JSON Schema for structured representation
- Support nested, hierarchical context models
- Implement type-safe serialization
- Enable lossless context reconstruction

### 3. Multi-Session Context Management
- Generate unique context fingerprints
- Support version control for context artifacts
- Implement context drift detection
- Create semantic diff capabilities

### 4. Context Compression Techniques
- Use advanced compression algorithms
- Support lossy and lossless compression modes
- Implement semantic token reduction
- Optimize storage efficiency

### 5. Vector Database Integration
Supported Vector Databases:
- Pinecone
- Weaviate
- Qdrant

Integration Features:
- Semantic embedding generation
- Vector index construction
- Similarity-based context retrieval
- Multi-dimensional knowledge mapping

### 6. Knowledge Graph Construction
- Extract relational metadata
- Create ontological representations
- Support cross-domain knowledge linking
- Enable inference-based context expansion

### 7. Storage Format Selection
Supported Formats:
- Structured JSON
- Markdown with frontmatter
- Protocol Buffers
- MessagePack
- YAML with semantic annotations

## Code Examples

### 1. Context Extraction
```python
def extract_project_context(project_root, context_type='standard'):
    context = {
        'project_metadata': extract_project_metadata(project_root),
        'architectural_decisions': analyze_architecture(project_root),
        'dependency_graph': build_dependency_graph(project_root),
        'semantic_tags': generate_semantic_tags(project_root)
    }
    return context
```

### 2. State Serialization Schema
```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "properties": {
    "project_name": {"type": "string"},
    "version": {"type": "string"},
    "context_fingerprint": {"type": "string"},
    "captured_at": {"type": "string", "format": "date-time"},
    "architectural_decisions": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "decision_type": {"type": "string"},
          "rationale": {"type": "string"},
          "impact_score": {"type": "number"}
        }
      }
    }
  }
}
```

### 3. Context Compression Algorithm
```python
def compress_context(context, compression_level='standard'):
    strategies = {
        'minimal': remove_redundant_tokens,
        'standard': semantic_compression,
        'comprehensive': advanced_vector_compression
    }
    compressor = strategies.get(compression_level, semantic_compression)
    return compressor(context)
```

## Reference Workflows

### Workflow 1: Project Onboarding Context Capture
1. Analyze project structure
2. Extract architectural decisions
3. Generate semantic embeddings
4. Store in vector database
5. Create markdown summary

### Workflow 2: Long-Running Session Context Management
1. Periodically capture context snapshots
2. Detect significant architectural changes
3. Version and archive context
4. Enable selective context restoration

## Advanced Integration Capabilities
- Real-time context synchronization
- Cross-platform context portability
- Compliance with enterprise knowledge management standards
- Support for multi-modal context representation

## Limitations and Considerations
- Sensitive information must be explicitly excluded
- Context capture has computational overhead
- Requires careful configuration for optimal performance

## Future Roadmap
- Improved ML-driven context compression
- Enhanced cross-domain knowledge transfer
- Real-time collaborative context editing
- Predictive context recommendation systems

---

## Merged Reference (legacy variant)

---
name: context-management-context-restore
description: "Use when working with context management context restore"
risk: unknown
source: community
date_added: "2026-02-27"
---

# Context Restoration: Advanced Semantic Memory Rehydration

## Use this skill when

- Working on context restoration: advanced semantic memory rehydration tasks or workflows
- Needing guidance, best practices, or checklists for context restoration: advanced semantic memory rehydration

## Do not use this skill when

- The task is unrelated to context restoration: advanced semantic memory rehydration
- You need a different domain or tool outside this scope

## Instructions

- Clarify goals, constraints, and required inputs.
- Apply relevant best practices and validate outcomes.
- Provide actionable steps and verification.
- If detailed examples are required, open `resources/implementation-playbook.md`.

## Role Statement

Expert Context Restoration Specialist focused on intelligent, semantic-aware context retrieval and reconstruction across complex multi-agent AI workflows. Specializes in preserving and reconstructing project knowledge with high fidelity and minimal information loss.

## Context Overview

The Context Restoration tool is a sophisticated memory management system designed to:
- Recover and reconstruct project context across distributed AI workflows
- Enable seamless continuity in complex, long-running projects
- Provide intelligent, semantically-aware context rehydration
- Maintain historical knowledge integrity and decision traceability

## Core Requirements and Arguments

### Input Parameters
- `context_source`: Primary context storage location (vector database, file system)
- `project_identifier`: Unique project namespace
- `restoration_mode`:
  - `full`: Complete context restoration
  - `incremental`: Partial context update
  - `diff`: Compare and merge context versions
- `token_budget`: Maximum context tokens to restore (default: 8192)
- `relevance_threshold`: Semantic similarity cutoff for context components (default: 0.75)

## Advanced Context Retrieval Strategies

### 1. Semantic Vector Search
- Utilize multi-dimensional embedding models for context retrieval
- Employ cosine similarity and vector clustering techniques
- Support multi-modal embedding (text, code, architectural diagrams)

```python
def semantic_context_retrieve(project_id, query_vector, top_k=5):
    """Semantically retrieve most relevant context vectors"""
    vector_db = VectorDatabase(project_id)
    matching_contexts = vector_db.search(
        query_vector,
        similarity_threshold=0.75,
        max_results=top_k
    )
    return rank_and_filter_contexts(matching_contexts)
```

### 2. Relevance Filtering and Ranking
- Implement multi-stage relevance scoring
- Consider temporal decay, semantic similarity, and historical impact
- Dynamic weighting of context components

```python
def rank_context_components(contexts, current_state):
    """Rank context components based on multiple relevance signals"""
    ranked_contexts = []
    for context in contexts:
        relevance_score = calculate_composite_score(
            semantic_similarity=context.semantic_score,
            temporal_relevance=context.age_factor,
            historical_impact=context.decision_weight
        )
        ranked_contexts.append((context, relevance_score))

    return sorted(ranked_contexts, key=lambda x: x[1], reverse=True)
```

### 3. Context Rehydration Patterns
- Implement incremental context loading
- Support partial and full context reconstruction
- Manage token budgets dynamically

```python
def rehydrate_context(project_context, token_budget=8192):
    """Intelligent context rehydration with token budget management"""
    context_components = [
        'project_overview',
        'architectural_decisions',
        'technology_stack',
        'recent_agent_work',
        'known_issues'
    ]

    prioritized_components = prioritize_components(context_components)
    restored_context = {}

    current_tokens = 0
    for component in prioritized_components:
        component_tokens = estimate_tokens(component)
        if current_tokens + component_tokens <= token_budget:
            restored_context[component] = load_component(component)
            current_tokens += component_tokens

    return restored_context
```

### 4. Session State Reconstruction
- Reconstruct agent workflow state
- Preserve decision trails and reasoning contexts
- Support multi-agent collaboration history

### 5. Context Merging and Conflict Resolution
- Implement three-way merge strategies
- Detect and resolve semantic conflicts
- Maintain provenance and decision traceability

### 6. Incremental Context Loading
- Support lazy loading of context components
- Implement context streaming for large projects
- Enable dynamic context expansion

### 7. Context Validation and Integrity Checks
- Cryptographic context signatures
- Semantic consistency verification
- Version compatibility checks

### 8. Performance Optimization
- Implement efficient caching mechanisms
- Use probabilistic data structures for context indexing
- Optimize vector search algorithms

## Reference Workflows

### Workflow 1: Project Resumption
1. Retrieve most recent project context
2. Validate context against current codebase
3. Selectively restore relevant components
4. Generate resumption summary

### Workflow 2: Cross-Project Knowledge Transfer
1. Extract semantic vectors from source project
2. Map and transfer relevant knowledge
3. Adapt context to target project's domain
4. Validate knowledge transferability

## Usage Examples

```bash
# Full context restoration
context-restore project:ai-assistant --mode full

# Incremental context update
context-restore project:web-platform --mode incremental

# Semantic context query
context-restore project:ml-pipeline --query "model training strategy"
```

## Integration Patterns
- RAG (Retrieval Augmented Generation) pipelines
- Multi-agent workflow coordination
- Continuous learning systems
- Enterprise knowledge management

## Future Roadmap
- Enhanced multi-modal embedding support
- Quantum-inspired vector search algorithms
- Self-healing context reconstruction
- Adaptive learning context strategies

---

## Merged Reference (legacy variant)

---
name: context-window-management
description: "Strategies for managing LLM context windows including summarization, trimming, routing, and avoiding context rot Use when: context window, token limit, context management, context engineering, long..."
risk: unknown
source: "vibeship-spawner-skills (Apache 2.0)"
date_added: "2026-02-27"
---

# Context Window Management

You're a context engineering specialist who has optimized LLM applications handling
millions of conversations. You've seen systems hit token limits, suffer context rot,
and lose critical information mid-dialogue.

You understand that context is a finite resource with diminishing returns. More tokens
doesn't mean better results—the art is in curating the right information. You know
the serial position effect, the lost-in-the-middle problem, and when to summarize
versus when to retrieve.

Your cor

## Capabilities

- context-engineering
- context-summarization
- context-trimming
- context-routing
- token-counting
- context-prioritization

## Patterns

### Tiered Context Strategy

Different strategies based on context size

### Serial Position Optimization

Place important content at start and end

### Intelligent Summarization

Summarize by importance, not just recency

## Anti-Patterns

### ❌ Naive Truncation

### ❌ Ignoring Token Costs

### ❌ One-Size-Fits-All

## Related Skills

Works well with: `rag-implementation`, `conversation-memory`, `prompt-caching`, `llm-npc-dialogue`

## When to Use
This skill is applicable to execute the workflow or actions described in the overview.

---

## Merged Reference (legacy variant)

---
name: context-degradation
description: This skill should be used when the user asks to "diagnose context problems", "fix lost-in-middle issues", "debug agent failures", "understand context poisoning", or mentions context degradation, attention patterns, context clash, context confusion, or agent performance...
---

# Context Degradation Patterns

Language models exhibit predictable degradation patterns as context length increases. Understanding these patterns is essential for diagnosing failures and designing resilient systems. Context degradation is not a binary state but a continuum of performance degradation that manifests in several distinct ways.

## When to Activate

Activate this skill when:
- Agent performance degrades unexpectedly during long conversations
- Debugging cases where agents produce incorrect or irrelevant outputs
- Designing systems that must handle large contexts reliably
- Evaluating context engineering choices for production systems
- Investigating "lost in middle" phenomena in agent outputs
- Analyzing context-related failures in agent behavior

## Core Concepts

Context degradation manifests through several distinct patterns. The lost-in-middle phenomenon causes information in the center of context to receive less attention. Context poisoning occurs when errors compound through repeated reference. Context distraction happens when irrelevant information overwhelms relevant content. Context confusion arises when the model cannot determine which context applies. Context clash develops when accumulated information directly conflicts.

These patterns are predictable and can be mitigated through architectural patterns like compaction, masking, partitioning, and isolation.

## Detailed Topics

### The Lost-in-Middle Phenomenon

The most well-documented degradation pattern is the "lost-in-middle" effect, where models demonstrate U-shaped attention curves. Information at the beginning and end of context receives reliable attention, while information buried in the middle suffers from dramatically reduced recall accuracy.

**Empirical Evidence**
Research demonstrates that relevant information placed in the middle of context experiences 10-40% lower recall accuracy compared to the same information at the beginning or end. This is not a failure of the model but a consequence of attention mechanics and training data distributions.

Models allocate massive attention to the first token (often the BOS token) to stabilize internal states. This creates an "attention sink" that soaks up attention budget. As context grows, the limited budget is stretched thinner, and middle tokens fail to garner sufficient attention weight for reliable retrieval.

**Practical Implications**
Design context placement with attention patterns in mind. Place critical information at the beginning or end of context. Consider whether information will be queried directly or needs to support reasoning—if the latter, placement matters less but overall signal quality matters more.

For long documents or conversations, use summary structures that surface key information at attention-favored positions. Use explicit section headers and transitions to help models navigate structure.

### Context Poisoning

Context poisoning occurs when hallucinations, errors, or incorrect information enters context and compounds through repeated reference. Once poisoned, context creates feedback loops that reinforce incorrect beliefs.

**How Poisoning Occurs**
Poisoning typically enters through three pathways. First, tool outputs may contain errors or unexpected formats that models accept as ground truth. Second, retrieved documents may contain incorrect or outdated information that models incorporate into reasoning. Third, model-generated summaries or intermediate outputs may introduce hallucinations that persist in context.

The compounding effect is severe. If an agent's goals section becomes poisoned, it develops strategies that take substantial effort to undo. Each subsequent decision references the poisoned content, reinforcing incorrect assumptions.

**Detection and Recovery**
Watch for symptoms including degraded output quality on tasks that previously succeeded, tool misalignment where agents call wrong tools or parameters, and hallucinations that persist despite correction attempts. When these symptoms appear, consider context poisoning.

Recovery requires removing or replacing poisoned content. This may involve truncating context to before the poisoning point, explicitly noting the poisoning in context and asking for re-evaluation, or restarting with clean context and preserving only verified information.

### Context Distraction

Context distraction emerges when context grows so long that models over-focus on provided information at the expense of their training knowledge. The model attends to everything in context regardless of relevance, and this creates pressure to use provided information even when internal knowledge is more accurate.

**The Distractor Effect**
Research shows that even a single irrelevant document in context reduces performance on tasks involving relevant documents. Multiple distractors compound degradation. The effect is not about noise in absolute terms but about attention allocation—irrelevant information competes with relevant information for limited attention budget.

Models do not have a mechanism to "skip" irrelevant context. They must attend to everything provided, and this obligation creates distraction even when the irrelevant information is clearly not useful.

**Mitigation Strategies**
Mitigate distraction through careful curation of what enters context. Apply relevance filtering before loading retrieved documents. Use namespacing and organization to make irrelevant sections easy to ignore structurally. Consider whether information truly needs to be in context or can be accessed through tool calls instead.

### Context Confusion

Context confusion arises when irrelevant information influences responses in ways that degrade quality. This is related to distraction but distinct—confusion concerns the influence of context on model behavior rather than attention allocation.

If you put something in context, the model has to pay attention to it. The model may incorporate irrelevant information, use inappropriate tool definitions, or apply constraints that came from different contexts. Confusion is especially problematic when context contains multiple task types or when switching between tasks within a single session.

**Signs of Confusion**
Watch for responses that address the wrong aspect of a query, tool calls that seem appropriate for a different task, or outputs that mix requirements from multiple sources. These indicate confusion about what context applies to the current situation.

**Architectural Solutions**
Architectural solutions include explicit task segmentation where different tasks get different context windows, clear transitions between task contexts, and state management that isolates context for different objectives.

### Context Clash

Context clash develops when accumulated information directly conflicts, creating contradictory guidance that derails reasoning. This differs from poisoning where one piece of information is incorrect—in clash, multiple correct pieces of information contradict each other.

**Sources of Clash**
Clash commonly arises from multi-source retrieval where different sources have contradictory information, version conflicts where outdated and current information both appear in context, and perspective conflicts where different viewpoints are valid but incompatible.

**Resolution Approaches**
Resolution approaches include explicit conflict marking that identifies contradictions and requests clarification, priority rules that establish which source takes precedence, and version filtering that excludes outdated information from context.

### Empirical Benchmarks and Thresholds

Research provides concrete data on degradation patterns that inform design decisions.

**RULER Benchmark Findings**
The RULER benchmark delivers sobering findings: only 50% of models claiming 32K+ context maintain satisfactory performance at 32K tokens. GPT-5.2 shows the least degradation among current models, while many still drop 30+ points at extended contexts. Near-perfect scores on simple needle-in-haystack tests do not translate to real long-context understanding.

**Model-Specific Degradation Thresholds**
| Model | Degradation Onset | Severe Degradation | Notes |
|-------|-------------------|-------------------|-------|
| GPT-5.2 | ~64K tokens | ~200K tokens | Best overall degradation resistance with thinking mode |
| AI assistant Opus 4.5 | ~100K tokens | ~180K tokens | 200K context window, strong attention management |
| AI assistant Sonnet 4.5 | ~80K tokens | ~150K tokens | Optimized for agents and coding tasks |
| Gemini 3 Pro | ~500K tokens | ~800K tokens | 1M context window, native multimodality |
| Gemini 3 Flash | ~300K tokens | ~600K tokens | 3x speed of Gemini 2.5, 81.2% MMMU-Pro |

**Model-Specific Behavior Patterns**
Different models exhibit distinct failure modes under context pressure:

- **AI assistant 4.5 series**: Lowest hallucination rates with calibrated uncertainty. AI assistant Opus 4.5 achieves 80.9% on SWE-bench Verified. Tends to refuse or ask clarification rather than fabricate.
- **GPT-5.2**: Two modes available - instant (fast) and thinking (reasoning). Thinking mode reduces hallucination through step-by-step verification but increases latency.
- **Gemini 3 Pro/Flash**: Native multimodality with 1M context window. Gemini 3 Flash offers 3x speed improvement over previous generation. Strong at multi-modal reasoning across text, code, images, audio, and video.

These patterns inform model selection for different use cases. High-stakes tasks benefit from AI assistant 4.5's conservative approach or GPT-5.2's thinking mode; speed-critical tasks may use instant modes.

### Counterintuitive Findings

Research reveals several counterintuitive patterns that challenge assumptions about context management.

**Shuffled Haystacks Outperform Coherent Ones**
Studies found that shuffled (incoherent) haystacks produce better performance than logically coherent ones. This suggests that coherent context may create false associations that confuse retrieval, while incoherent context forces models to rely on exact matching.

**Single Distractors Have Outsized Impact**
Even a single irrelevant document reduces performance significantly. The effect is not proportional to the amount of noise but follows a step function where the presence of any distractor triggers degradation.

**Needle-Question Similarity Correlation**
Lower similarity between needle and question pairs shows faster degradation with context length. Tasks requiring inference across dissimilar content are particularly vulnerable.

### When Larger Contexts Hurt

Larger context windows do not uniformly improve performance. In many cases, larger contexts create new problems that outweigh benefits.

**Performance Degradation Curves**
Models exhibit non-linear degradation with context length. Performance remains stable up to a threshold, then degrades rapidly. The threshold varies by model and task complexity. For many models, meaningful degradation begins around 8,000-16,000 tokens even when context windows support much larger sizes.

**Cost Implications**
Processing cost grows disproportionately with context length. The cost to process a 400K token context is not double the cost of 200K—it increases exponentially in both time and computing resources. For many applications, this makes large-context processing economically impractical.

**Cognitive Load Metaphor**
Even with an infinite context, asking a single model to maintain consistent quality across dozens of independent tasks creates a cognitive bottleneck. The model must constantly switch context between items, maintain a comparative framework, and ensure stylistic consistency. This is not a problem that more context solves.

## Practical Guidance

### The Four-Bucket Approach

Four strategies address different aspects of context degradation:

**Write**: Save context outside the window using scratchpads, file systems, or external storage. This keeps active context lean while preserving information access.

**Select**: Pull relevant context into the window through retrieval, filtering, and prioritization. This addresses distraction by excluding irrelevant information.

**Compress**: Reduce tokens while preserving information through summarization, abstraction, and observation masking. This extends effective context capacity.

**Isolate**: Split context across sub-agents or sessions to prevent any single context from growing large enough to degrade. This is the most aggressive strategy but often the most effective.

### Architectural Patterns

Implement these strategies through specific architectural patterns. Use just-in-time context loading to retrieve information only when needed. Use observation masking to replace verbose tool outputs with compact references. Use sub-agent architectures to isolate context for different tasks. Use compaction to summarize growing context before it exceeds limits.

## Examples

**Example 1: Detecting Degradation**
```yaml
# Context grows during long conversation
turn_1: 1000 tokens
turn_5: 8000 tokens
turn_10: 25000 tokens
turn_20: 60000 tokens (degradation begins)
turn_30: 90000 tokens (significant degradation)
```

**Example 2: Mitigating Lost-in-Middle**
```markdown
# Organize context with critical info at edges

[CURRENT TASK]                      # At start
- Goal: Generate quarterly report
- Deadline: End of week

[DETAILED CONTEXT]                  # Middle (less attention)
- 50 pages of data
- Multiple analysis sections
- Supporting evidence

[KEY FINDINGS]                     # At end
- Revenue up 15%
- Costs down 8%
- Growth in Region A
```

## Guidelines

1. Monitor context length and performance correlation during development
2. Place critical information at beginning or end of context
3. Implement compaction triggers before degradation becomes severe
4. Validate retrieved documents for accuracy before adding to context
5. Use versioning to prevent outdated information from causing clash
6. Segment tasks to prevent context confusion across different objectives
7. Design for graceful degradation rather than assuming perfect conditions
8. Test with progressively larger contexts to find degradation thresholds

## Integration

This skill builds on context-fundamentals and should be studied after understanding basic context concepts. It connects to:

- context-optimization - Techniques for mitigating degradation
- multi-agent-patterns - Using isolation to prevent degradation
- evaluation - Measuring and detecting degradation in production

## References

Internal reference:
- Degradation Patterns Reference - Detailed technical reference

Related skills in this collection:
- context-fundamentals - Context basics
- context-optimization - Mitigation techniques
- evaluation - Detection and measurement

External resources:
- Research on attention mechanisms and context window limitations
- Studies on the "lost-in-middle" phenomenon
- Production engineering guides from AI labs

---

## Skill Metadata

**Created**: 2025-12-20
**Last Updated**: 2025-12-20
**Author**: Agent Skills for Context Engineering Contributors
**Version**: 1.0.0

---

## Merged Reference (legacy variant)

---
name: context-compression
description: This skill should be used when the user asks to "compress context", "summarize conversation history", "implement compaction", "reduce token usage", or mentions context compression, structured summarization, tokens-per-task optimization, or long-running agent sessions...
---

# Context Compression Strategies

When agent sessions generate millions of tokens of conversation history, compression becomes mandatory. The naive approach is aggressive compression to minimize tokens per request. The correct optimization target is tokens per task: total tokens consumed to complete a task, including re-fetching costs when compression loses critical information.

## When to Activate

Activate this skill when:
- Agent sessions exceed context window limits
- Codebases exceed context windows (5M+ token systems)
- Designing conversation summarization strategies
- Debugging cases where agents "forget" what files they modified
- Building evaluation frameworks for compression quality

## Core Concepts

Context compression trades token savings against information loss. Three production-ready approaches exist:

1. **Anchored Iterative Summarization**: Maintain structured, persistent summaries with explicit sections for session intent, file modifications, decisions, and next steps. When compression triggers, summarize only the newly-truncated span and merge with the existing summary. Structure forces preservation by dedicating sections to specific information types.

2. **Opaque Compression**: Produce compressed representations optimized for reconstruction fidelity. Achieves highest compression ratios (99%+) but sacrifices interpretability. Cannot verify what was preserved.

3. **Regenerative Full Summary**: Generate detailed structured summaries on each compression. Produces readable output but may lose details across repeated compression cycles due to full regeneration rather than incremental merging.

The critical insight: structure forces preservation. Dedicated sections act as checklists that the summarizer must populate, preventing silent information drift.

## Detailed Topics

### Why Tokens-Per-Task Matters

Traditional compression metrics target tokens-per-request. This is the wrong optimization. When compression loses critical details like file paths or error messages, the agent must re-fetch information, re-explore approaches, and waste tokens recovering context.

The right metric is tokens-per-task: total tokens consumed from task start to completion. A compression strategy saving 0.5% more tokens but causing 20% more re-fetching costs more overall.

### The Artifact Trail Problem

Artifact trail integrity is the weakest dimension across all compression methods, scoring 2.2-2.5 out of 5.0 in evaluations. Even structured summarization with explicit file sections struggles to maintain complete file tracking across long sessions.

Coding agents need to know:
- Which files were created
- Which files were modified and what changed
- Which files were read but not changed
- Function names, variable names, error messages

This problem likely requires specialized handling beyond general summarization: a separate artifact index or explicit file-state tracking in agent scaffolding.

### Structured Summary Sections

Effective structured summaries include explicit sections:

```markdown
## Session Intent
[What the user is trying to accomplish]

## Files Modified
- auth.controller.ts: Fixed JWT token generation
- config/redis.ts: Updated connection pooling
- tests/auth.test.ts: Added mock setup for new config

## Decisions Made
- Using Redis connection pool instead of per-request connections
- Retry logic with exponential backoff for transient failures

## Current State
- 14 tests passing, 2 failing
- Remaining: mock setup for session service tests

## Next Steps
1. Fix remaining test failures
2. Run full test suite
3. Update documentation
```

This structure prevents silent loss of file paths or decisions because each section must be explicitly addressed.

### Compression Trigger Strategies

When to trigger compression matters as much as how to compress:

| Strategy | Trigger Point | Trade-off |
|----------|---------------|-----------|
| Fixed threshold | 70-80% context utilization | Simple but may compress too early |
| Sliding window | Keep last N turns + summary | Predictable context size |
| Importance-based | Compress low-relevance sections first | Complex but preserves signal |
| Task-boundary | Compress at logical task completions | Clean summaries but unpredictable timing |

The sliding window approach with structured summaries provides the best balance of predictability and quality for most coding agent use cases.

### Probe-Based Evaluation

Traditional metrics like ROUGE or embedding similarity fail to capture functional compression quality. A summary may score high on lexical overlap while missing the one file path the agent needs.

Probe-based evaluation directly measures functional quality by asking questions after compression:

| Probe Type | What It Tests | Example Question |
|------------|---------------|------------------|
| Recall | Factual retention | "What was the original error message?" |
| Artifact | File tracking | "Which files have we modified?" |
| Continuation | Task planning | "What should we do next?" |
| Decision | Reasoning chain | "What did we decide about the Redis issue?" |

If compression preserved the right information, the agent answers correctly. If not, it guesses or hallucinates.

### Evaluation Dimensions

Six dimensions capture compression quality for coding agents:

1. **Accuracy**: Are technical details correct? File paths, function names, error codes.
2. **Context Awareness**: Does the response reflect current conversation state?
3. **Artifact Trail**: Does the agent know which files were read or modified?
4. **Completeness**: Does the response address all parts of the question?
5. **Continuity**: Can work continue without re-fetching information?
6. **Instruction Following**: Does the response respect stated constraints?

Accuracy shows the largest variation between compression methods (0.6 point gap). Artifact trail is universally weak (2.2-2.5 range).

## Practical Guidance

### Three-Phase Compression Workflow

For large codebases or agent systems exceeding context windows, apply compression through three phases:

1. **Research Phase**: Produce a research document from architecture diagrams, documentation, and key interfaces. Compress exploration into a structured analysis of components and dependencies. Output: single research document.

2. **Planning Phase**: Convert research into implementation specification with function signatures, type definitions, and data flow. A 5M token codebase compresses to approximately 2,000 words of specification.

3. **Implementation Phase**: Execute against the specification. Context remains focused on the spec rather than raw codebase exploration.

### Using Example Artifacts as Seeds

When provided with a manual migration example or reference PR, use it as a template to understand the target pattern. The example reveals constraints that static analysis cannot surface: which invariants must hold, which services break on changes, and what a clean migration looks like.

This is particularly important when the agent cannot distinguish essential complexity (business requirements) from accidental complexity (legacy workarounds). The example artifact encodes that distinction.

### Implementing Anchored Iterative Summarization

1. Define explicit summary sections matching your agent's needs
2. On first compression trigger, summarize truncated history into sections
3. On subsequent compressions, summarize only new truncated content
4. Merge new summary into existing sections rather than regenerating
5. Track which information came from which compression cycle for debugging

### When to Use Each Approach

**Use anchored iterative summarization when:**
- Sessions are long-running (100+ messages)
- File tracking matters (coding, debugging)
- You need to verify what was preserved

**Use opaque compression when:**
- Maximum token savings required
- Sessions are relatively short
- Re-fetching costs are low

**Use regenerative summaries when:**
- Summary interpretability is critical
- Sessions have clear phase boundaries
- Full context review is acceptable on each compression

### Compression Ratio Considerations

| Method | Compression Ratio | Quality Score | Trade-off |
|--------|-------------------|---------------|-----------|
| Anchored Iterative | 98.6% | 3.70 | Best quality, slightly less compression |
| Regenerative | 98.7% | 3.44 | Good quality, moderate compression |
| Opaque | 99.3% | 3.35 | Best compression, quality loss |

The 0.7% additional tokens retained by structured summarization buys 0.35 quality points. For any task where re-fetching costs matter, this trade-off favors structured approaches.

## Examples

**Example 1: Debugging Session Compression**

Original context (89,000 tokens, 178 messages):
- 401 error on /api/auth/login endpoint
- Traced through auth controller, middleware, session store
- Found stale Redis connection
- Fixed connection pooling, added retry logic
- 14 tests passing, 2 failing

Structured summary after compression:

```markdown
## Session Intent
Debug 401 Unauthorized error on /api/auth/login despite valid credentials.

## Root Cause
Stale Redis connection in session store. JWT generated correctly but session could not be persisted.

## Files Modified
- auth.controller.ts: No changes (read only)
- middleware/cors.ts: No changes (examined)
- config/redis.ts: Fixed connection pooling configuration
- services/session.service.ts: Added retry logic for transient failures
- tests/auth.test.ts: Updated mock setup

## Test Status
14 passing, 2 failing (mock setup issues)

## Next Steps
1. Fix remaining test failures (mock session service)
2. Run full test suite
3. Deploy to staging
```

**Example 2: Probe Response Quality**

After compression, asking "What was the original error?":

Good response (structured summarization):
> "The original error was a 401 Unauthorized response from the /api/auth/login endpoint. Users received this error with valid credentials. Root cause was stale Redis connection in session store."

Poor response (aggressive compression):
> "We were debugging an authentication issue. The login was failing. We fixed some configuration problems."

The structured response preserves endpoint, error code, and root cause. The aggressive response loses all technical detail.

## Guidelines

1. Optimize for tokens-per-task, not tokens-per-request
2. Use structured summaries with explicit sections for file tracking
3. Trigger compression at 70-80% context utilization
4. Implement incremental merging rather than full regeneration
5. Test compression quality with probe-based evaluation
6. Track artifact trail separately if file tracking is critical
7. Accept slightly lower compression ratios for better quality retention
8. Monitor re-fetching frequency as a compression quality signal

## Integration

This skill connects to several others in the collection:

- context-degradation - Compression is a mitigation strategy for degradation
- context-optimization - Compression is one optimization technique among many
- evaluation - Probe-based evaluation applies to compression testing
- memory-systems - Compression relates to scratchpad and summary memory patterns

## References

Internal reference:
- Evaluation Framework Reference - Detailed probe types and scoring rubrics

Related skills in this collection:
- context-degradation - Understanding what compression prevents
- context-optimization - Broader optimization strategies
- evaluation - Building evaluation frameworks

External resources:
- Factory Research: Evaluating Context Compression for AI Agents (December 2025)
- Research on LLM-as-judge evaluation methodology (Zheng et al., 2023)
- Netflix Engineering: "The Infinite Software Crisis" - Three-phase workflow and context compression at scale (AI Summit 2025)

---

## Skill Metadata

**Created**: 2025-12-22
**Last Updated**: 2025-12-26
**Author**: Agent Skills for Context Engineering Contributors
**Version**: 1.1.0

---

## Merged Reference (legacy variant)

---
name: context-guardian
description: Guardiao de contexto que preserva dados criticos antes da compactacao automatica. Snapshots, verificacao de integridade e zero perda de informacao.
risk: safe
source: community
date_added: '2026-03-06'
author: renat
tags:
- context
- data-integrity
- snapshots
- verification
tools:
- agent-compatible
- agent-compatible
- agent-compatible
- agent-compatible
- agent-compatible
---

# Context Guardian

## Overview

Guardiao de contexto que preserva dados criticos antes da compactacao automatica. Snapshots, verificacao de integridade e zero perda de informacao.

## When to Use This Skill

- When the user mentions "compactacao contexto" or related topics
- When the user mentions "perda de contexto" or related topics
- When the user mentions "snapshot contexto" or related topics
- When the user mentions "preservar contexto" or related topics
- When the user mentions "contexto critico" or related topics
- When the user mentions "antes de compactar" or related topics

## Do Not Use This Skill When

- The task is unrelated to context guardian
- A simpler, more specific tool can handle the request
- The user needs general-purpose assistance without domain expertise

## How It Works

Sistema de integridade de contexto que protege projetos tecnicoss complexos contra
perda de informacao durante compactacao automatica do AI coding assistant. Enquanto o
`context-agent` atua APOS as sessoes (save/load), o context-guardian atua DURANTE
a sessao, detectando quando a compactacao esta proxima e executando protocolos de
preservacao com verificacao redundante.

## Por Que Isto Existe

O AI coding assistant compacta automaticamente mensagens antigas quando o contexto se
aproxima do limite da janela. Essa compactacao e heuristica — ela resume mensagens
para liberar espaco, mas inevitavelmente perde detalhes. Para projetos simples,
isso funciona bem. Mas para projetos tecnicos pesados (como ecossistemas com 21+
skills, auditorias de seguranca, refatoracoes de arquitetura), a perda de um unico
detalhe pode causar regressoes, re-trabalho ou inconsistencias graves.

O context-guardian resolve isso criando uma camada de protecao PRE-compactacao:
extrai, classifica, verifica e persiste todas as informacoes criticas ANTES que a
compactacao automatica as destrua.

## Localizacao

```
C:\Users\renat\skills\context-guardian\
├── SKILL.md                          # Este arquivo
├── references/
│   ├── extraction-protocol.md        # Protocolo detalhado de extracao
│   └── verification-checklist.md     # Checklist de verificacao e redundancia
└── scripts/
    └── context_snapshot.py           # Script de snapshot automatico
```

## Integracao Com O Ecossistema

```
context-guardian (PRE-compactacao)    context-agent (POS-sessao)
         │                                    │
         ├── Detecta contexto grande          ├── Salva resumo ao final
         ├── Extrai dados criticos            ├── Atualiza ACTIVE_CONTEXT.md
         ├── Verifica integridade             ├── Sincroniza MEMORY.md
         ├── Salva snapshot verificado        ├── Indexa busca FTS5
         └── Gera briefing de transicao       └── Arquiva sessoes antigas
```

O context-guardian e o context-agent sao complementares:
- **context-guardian**: protecao em tempo real, DURANTE a sessao
- **context-agent**: persistencia entre sessoes, APOS a sessao

## Ativacao Automatica (O AI assistant Deve Iniciar Sozinho)

1. **Limite de contexto**: quando perceber que ja consumiu ~60-70% da janela de
   contexto (indicadores: mensagens comecando a ser resumidas, aviso de compactacao)
2. **Projetos pesados**: sessoes com muitos arquivos editados, muitas tool calls,
   ou projetos com dependencias complexas entre componentes
3. **Antes de tarefas longas**: quando uma proxima tarefa pode gerar output extenso
   que empurraria o contexto para alem do limite

## Ativacao Manual (Usuario Solicita)

- "salva o estado antes de comprimir"
- "faz um checkpoint"
- "snapshot do contexto"
- "nao quero perder nada dessa sessao"
- "prepara pra compactacao"
- "o contexto ta grande, protege"

## Fase 1: Extracao Estruturada

Percorrer toda a conversa ate o momento e extrair categorias criticas.
Para cada categoria, classificar por prioridade (P0 = perda fatal, P1 = perda grave,
P2 = perda toleravel).

**P0 — Perda Fatal (preservar com redundancia tripla)**

| Categoria | O que extrair | Exemplo |
|-----------|--------------|---------|
| Decisoes tecnicas | Escolhas de arquitetura, padrao, tecnologia E motivo | "Usamos parameterized queries porque f-strings causam SQL injection" |
| Estado de tarefas | O que foi feito, o que falta, dependencias | "18/18 match OK, falta ZIP" |
| Correcoes aplicadas | Bug, causa raiz, solucao exata, arquivos afetados | "instagram/db.py: SQL injection via f-string → ? placeholders" |
| Codigo gerado/modificado | Caminho exato, linhas alteradas, natureza da mudanca | "match_skills.py:40-119: adicionou 5 categorias" |
| Erros encontrados | Mensagem exata, stack trace relevante, como resolveu | "TypeError at line 45 → cast para int" |
| Comandos que funcionaram | Comando completo que produziu resultado correto | "python verify_zips.py → 22/22 OK" |

**P1 — Perda Grave (preservar com verificacao)**

| Categoria | O que extrair |
|-----------|--------------|
| Padroes descobertos | Convencoes, patterns de codigo observados |
| Dependencias entre componentes | "scan_registry.py E match_skills.py devem ter categorias identicas" |
| Preferencias do usuario | Idioma, estilo, nivel de detalhe, workflow preferido |
| Contexto de projeto | Estrutura de diretorios, arquivos-chave, proposito |
| Questoes em aberto | Perguntas sem resposta, ambiguidades nao resolvidas |

**P2 — Perda Toleravel (resumo compacto)**

| Categoria | O que extrair |
|-----------|--------------|
| Historico de tentativas | "Tentei X, nao funcionou por Y, entao Z" |
| Metricas de progresso | Contadores, tempos, tamanhos |
| Discussoes exploratórias | Brainstorm, opcoes consideradas e descartadas |

## Fase 2: Verificacao De Integridade

Apos extrair, verificar que NADA critico foi omitido.

**Checklist de Verificacao (executar mentalmente para cada item):**

```
□ Cada arquivo modificado tem: caminho, natureza da mudanca, motivo
□ Cada bug corrigido tem: sintoma, causa raiz, solucao, arquivo
□ Cada decisao tem: o que, por que, alternativas descartadas
□ Cada tarefa pendente tem: descricao, prioridade, dependencias
□ Cada padrao/convencao tem: regra, motivo, exemplos
□ Nenhuma informacao de uma secao contradiz outra
□ Referencias cruzadas estao consistentes (ex: "18 queries testadas" aparece em
  multiplos lugares com o mesmo numero)
□ Caminhos de arquivo estao completos (absolutos, nao relativos)
```

Se qualquer item falhar, voltar a Fase 1 e re-extrair a informacao faltante.

Para detalhes sobre verificacao avancada, ler `references/verification-checklist.md`.

## Fase 3: Persistencia Redundante

Salvar as informacoes extraidas em 3 camadas de redundancia:

**Camada 1 — Snapshot estruturado (arquivo .md)**

```bash
python C:\Users\renat\skills\context-guardian\scripts\context_snapshot.py save
```

Gera `C:\Users\renat\skills\context-guardian\data\snapshot-YYYYMMDD-HHMMSS.md` com
todas as informacoes extraidas em formato estruturado.

Se o script nao estiver disponivel, criar manualmente o arquivo seguindo o formato
descrito em `references/extraction-protocol.md`.

**Camada 2 — MEMORY.md atualizado**

Atualizar `C:\Users\renat\.agent\projects\C--Users-renat-Skill-JUD\memory\MEMORY.md`
com as informacoes P0 mais criticas em formato ultra-compacto. O MEMORY.md e carregado
automaticamente em toda nova sessao, entao ele e a ultima linha de defesa.

**Camada 3 — Context-agent save**

```bash
python C:\Users\renat\skills\context-agent\scripts\context_manager.py save
```

Aciona o context-agent para salvar sessao completa com indexacao FTS5.

## Fase 4: Briefing De Transicao

Gerar um bloco de texto formatado que serve como "cartao de visita" para o AI assistant
que continuar apos a compactacao. Este briefing deve ser a ULTIMA coisa escrita antes
da compactacao, para que fique no topo do contexto compactado.

**Formato do briefing:**

```markdown

## Estado Atual

- Projeto: [nome]
- Fase: [fase atual]
- Progresso: [X/Y tarefas completas]

## O Que Foi Feito Nesta Sessao

1. [tarefa 1 — resultado]
2. [tarefa 2 — resultado]
...

## O Que Falta Fazer

1. [tarefa pendente — prioridade] [dependencia se houver]
2. ...

## Decisoes Criticas (Nao Alterar Sem Motivo)

- [decisao 1]: [motivo]
- [decisao 2]: [motivo]

## Correcoes Aplicadas (Nao Reverter)

- [arquivo]: [correcao] — [motivo]

## Caminhos Importantes

- [caminho 1]: [proposito]
- [caminho 2]: [proposito]

## Alertas

- [qualquer armadilha, edge case, ou cuidado especial]

## Onde Recuperar Mais Informacoes

- Snapshot: C:\Users\renat\skills\context-guardian\data\snapshot-[timestamp].md
- MEMORY.md: carregado automaticamente
- Context-agent: `python context_manager.py load`
- Busca historica: `python context_manager.py search "termo"`
```

## Protocolo Rapido (Quando O Tempo E Curto)

Se a compactacao esta iminente e nao ha tempo para o protocolo completo de 4 fases:

1. **30 segundos** — Escrever um mini-briefing com: tarefas pendentes, decisoes
   criticas, caminhos de arquivo modificados
2. **1 minuto** — Atualizar MEMORY.md com informacoes P0
3. **2 minutos** — Executar context-agent save

Mesmo o protocolo rapido e melhor que nenhuma protecao.

## Deteccao De Completude Pos-Compactacao

Quando uma sessao continuar apos compactacao, verificar se o contexto preservado
esta completo:

1. Ler MEMORY.md (ja estara carregado automaticamente)
2. Se disponivel, ler o snapshot mais recente em `data/`
3. Comparar com o briefing de transicao (se visivel no contexto compactado)
4. Se encontrar lacunas, executar:
   ```bash
   python C:\Users\renat\skills\context-agent\scripts\context_manager.py load
   ```
5. Se ainda houver lacunas, buscar por termo:
   ```bash
   python C:\Users\renat\skills\context-agent\scripts\context_manager.py search "termo"
   ```

## Exemplo De Uso Real

**Cenario**: Sessao longa criando advogado-especialista (46KB), corrigindo match_skills
(5 categorias novas), auditando seguranca (10 vulnerabilidades), gerando 22 ZIPs.

**Sem context-guardian**:
Compactacao resume tudo em "criou skill juridica, corrigiu bugs, gerou zips".
Proximo AI assistant nao sabe quais categorias foram adicionadas, quais vulnerabilidades
foram corrigidas, qual o estado de cada ZIP, ou por que certas decisoes foram tomadas.
Resultado: re-trabalho, inconsistencias, regressoes.

**Com context-guardian**:
Antes da compactacao, executa protocolo completo:
- Snapshot com 5 categorias novas listadas (legal, auction, security, image-generation, monitoring)
- 10 vulnerabilidades catalogadas com arquivo, tipo, e correcao exata
- 22 ZIPs verificados com checksums
- Decisoes documentadas ("removeu 'saude' de monitoring porque causava false positive")
- Briefing de transicao no topo do contexto
Proximo AI assistant continua com precisao total, zero re-trabalho.

## Consideracoes De Performance

- O protocolo completo leva 2-5 minutos de trabalho do AI assistant
- Para projetos simples, usar apenas o protocolo rapido
- Nao ativar para sessoes curtas ou conversas casuais
- A persistencia em 3 camadas (snapshot + MEMORY.md + context-agent) garante que
  mesmo se uma camada falhar, as outras duas preservam a informacao
- Snapshots antigos (>10) podem ser podados manualmente

## Best Practices

- Provide clear, specific context about your project and requirements
- Review all suggestions before applying them to production code
- Combine with other complementary skills for comprehensive analysis

## Common Pitfalls

- Using this skill for tasks outside its domain expertise
- Applying recommendations without understanding your specific context
- Not providing enough project context for accurate analysis

## Related Skills

- `context-agent` - Complementary skill for enhanced analysis

---

## Merged Reference (legacy variant)

---
name: filesystem-context
description: Use for file-based context management, dynamic context discovery, and reducing context window bloat. Offload context to files for just-in-time loading.
risk: unknown
source: community
---

# Filesystem-Based Context Engineering

The filesystem provides a single interface through which agents can flexibly store, retrieve, and update an effectively unlimited amount of context. This pattern addresses the fundamental constraint that context windows are limited while tasks often require more information than fits in a single window.

The core insight is that files enable dynamic context discovery: agents pull relevant context on demand rather than carrying everything in the context window. This contrasts with static context, which is always included regardless of relevance.

## When to Activate

Activate this skill when:
- Tool outputs are bloating the context window
- Agents need to persist state across long trajectories
- Sub-agents must share information without direct message passing
- Tasks require more context than fits in the window
- Building agents that learn and update their own instructions
- Implementing scratch pads for intermediate results
- Terminal outputs or logs need to be accessible to agents

## Core Concepts

Context engineering can fail in four predictable ways. First, when the context an agent needs is not in the total available context. Second, when retrieved context fails to encapsulate needed context. Third, when retrieved context far exceeds needed context, wasting tokens and degrading performance. Fourth, when agents cannot discover niche information buried in many files.

The filesystem addresses these failures by providing a persistent layer where agents write once and read selectively, offloading bulk content while preserving the ability to retrieve specific information through search tools.

## Detailed Topics

### The Static vs Dynamic Context Trade-off

**Static Context**
Static context is always included in the prompt: system instructions, tool definitions, and critical rules. Static context consumes tokens regardless of task relevance. As agents accumulate more capabilities (tools, skills, instructions), static context grows and crowds out space for dynamic information.

**Dynamic Context Discovery**
Dynamic context is loaded on-demand when relevant to the current task. The agent receives minimal static pointers (names, descriptions, file paths) and uses search tools to load full content when needed.

Dynamic discovery is more token-efficient because only necessary data enters the context window. It can also improve response quality by reducing potentially confusing or contradictory information.

The trade-off: dynamic discovery requires the model to correctly identify when to load additional context. This works well with current frontier models but may fail with less capable models that do not recognize when they need more information.

### Pattern 1: Filesystem as Scratch Pad

**The Problem**
Tool calls can return massive outputs. A web search may return 10k tokens of raw content. A database query may return hundreds of rows. If this content enters the message history, it remains for the entire conversation, inflating token costs and potentially degrading attention to more relevant information.

**The Solution**
Write large tool outputs to files instead of returning them directly to the context. The agent then uses targeted retrieval (grep, line-specific reads) to extract only the relevant portions.

**Implementation**
```python
def handle_tool_output(output: str, threshold: int = 2000) -> str:
    if len(output) < threshold:
        return output
    
    # Write to scratch pad
    file_path = f"scratch/{tool_name}_{timestamp}.txt"
    write_file(file_path, output)
    
    # Return reference instead of content
    key_summary = extract_summary(output, max_tokens=200)
    return f"[Output written to {file_path}. Summary: {key_summary}]"
```

The agent can then use `grep` to search for specific patterns or `read_file` with line ranges to retrieve targeted sections.

**Benefits**
- Reduces token accumulation over long conversations
- Preserves full output for later reference
- Enables targeted retrieval instead of carrying everything

### Pattern 2: Plan Persistence

**The Problem**
Long-horizon tasks require agents to make plans and follow them. But as conversations extend, plans can fall out of attention or be lost to summarization. The agent loses track of what it was supposed to do.

**The Solution**
Write plans to the filesystem. The agent can re-read its plan at any point, reminding itself of the current objective and progress. This is sometimes called "manipulating attention through recitation."

**Implementation**
Store plans in structured format:
```yaml
# scratch/current_plan.yaml
objective: "Refactor authentication module"
status: in_progress
steps:
  - id: 1
    description: "Audit current auth endpoints"
    status: completed
  - id: 2
    description: "Design new token validation flow"
    status: in_progress
  - id: 3
    description: "Implement and test changes"
    status: pending
```

The agent reads this file at the start of each turn or when it needs to re-orient.

### Pattern 3: Sub-Agent Communication via Filesystem

**The Problem**
In multi-agent systems, sub-agents typically report findings to a coordinator agent through message passing. This creates a "game of telephone" where information degrades through summarization at each hop.

**The Solution**
Sub-agents write their findings directly to the filesystem. The coordinator reads these files directly, bypassing intermediate message passing. This preserves fidelity and reduces context accumulation in the coordinator.

**Implementation**
```
workspace/
  agents/
    research_agent/
      findings.md        # Research agent writes here
      sources.jsonl      # Source tracking
    code_agent/
      changes.md         # Code agent writes here
      test_results.txt   # Test output
  coordinator/
    synthesis.md         # Coordinator reads agent outputs, writes synthesis
```

Each agent operates in relative isolation but shares state through the filesystem.

### Pattern 4: Dynamic Skill Loading

**The Problem**
Agents may have many skills or instruction sets, but most are irrelevant to any given task. Stuffing all instructions into the system prompt wastes tokens and can confuse the model with contradictory or irrelevant guidance.

**The Solution**
Store skills as files. Include only skill names and brief descriptions in static context. The agent uses search tools to load relevant skill content when the task requires it.

**Implementation**
Static context includes:
```
Available skills (load with read_file when relevant):
- database-optimization: Query tuning and indexing strategies
- api-design: REST/GraphQL best practices
- testing-strategies: Unit, integration, and e2e testing patterns
```

Agent loads `skills/database-optimization/SKILL.md` only when working on database tasks.

### Pattern 5: Terminal and Log Persistence

**The Problem**
Terminal output from long-running processes accumulates rapidly. Copying and pasting output into agent input is manual and inefficient.

**The Solution**
Sync terminal output to files automatically. The agent can then grep for relevant sections (error messages, specific commands) without loading entire terminal histories.

**Implementation**
Terminal sessions are persisted as files:
```
terminals/
  1.txt    # Terminal session 1 output
  2.txt    # Terminal session 2 output
```

Agents query with targeted grep:
```bash
grep -A 5 "error" terminals/1.txt
```

### Pattern 6: Learning Through Self-Modification

**The Problem**
Agents often lack context that users provide implicitly or explicitly during interactions. Traditionally, this requires manual system prompt updates between sessions.

**The Solution**
Agents write learned information to their own instruction files. Subsequent sessions load these files, incorporating learned context automatically.

**Implementation**
After user provides preference:
```python
def remember_preference(key: str, value: str):
    preferences_file = "agent/user_preferences.yaml"
    prefs = load_yaml(preferences_file)
    prefs[key] = value
    write_yaml(preferences_file, prefs)
```

Subsequent sessions include a step to load user preferences if the file exists.

**Caution**
This pattern is still emerging. Self-modification requires careful guardrails to prevent agents from accumulating incorrect or contradictory instructions over time.

### Filesystem Search Techniques

Models are specifically trained to understand filesystem traversal. The combination of `ls`, `glob`, `grep`, and `read_file` with line ranges provides powerful context discovery:

- `ls` / `list_dir`: Discover directory structure
- `glob`: Find files matching patterns (e.g., `**/*.py`)
- `grep`: Search file contents for patterns, returns matching lines
- `read_file` with ranges: Read specific line ranges without loading entire files

This combination often outperforms semantic search for technical content (code, API docs) where semantic meaning is sparse but structural patterns are clear.

Semantic search and filesystem search work well together: semantic search for conceptual queries, filesystem search for structural and exact-match queries.

## Practical Guidance

### When to Use Filesystem Context

**Use filesystem patterns when:**
- Tool outputs exceed 2000 tokens
- Tasks span multiple conversation turns
- Multiple agents need to share state
- Skills or instructions exceed what fits comfortably in system prompt
- Logs or terminal output need selective querying

**Avoid filesystem patterns when:**
- Tasks complete in single turns
- Context fits comfortably in window
- Latency is critical (file I/O adds overhead)
- Simple model incapable of filesystem tool use

### File Organization

Structure files for discoverability:
```
project/
  scratch/           # Temporary working files
    tool_outputs/    # Large tool results
    plans/           # Active plans and checklists
  memory/            # Persistent learned information
    preferences.yaml # User preferences
    patterns.md      # Learned patterns
  skills/            # Loadable skill definitions
  agents/            # Sub-agent workspaces
```

Use consistent naming conventions. Include timestamps or IDs in scratch files for disambiguation.

### Token Accounting

Track where tokens originate:
- Measure static vs dynamic context ratio
- Monitor tool output sizes before and after offloading
- Track how often dynamic context is actually loaded

Optimize based on measurements, not assumptions.

## Examples

**Example 1: Tool Output Offloading**
```
Input: Web search returns 8000 tokens
Before: 8000 tokens added to message history
After: 
  - Write to scratch/search_results_001.txt
  - Return: "[Results in scratch/search_results_001.txt. Key finding: API rate limit is 1000 req/min]"
  - Agent greps file when needing specific details
Result: ~100 tokens in context, 8000 tokens accessible on demand
```

**Example 2: Dynamic Skill Loading**
```
Input: User asks about database indexing
Static context: "database-optimization: Query tuning and indexing"
Agent action: read_file("skills/database-optimization/SKILL.md")
Result: Full skill loaded only when relevant
```

**Example 3: Chat History as File Reference**
```
Trigger: Context window limit reached, summarization required
Action: 
  1. Write full history to history/session_001.txt
  2. Generate summary for new context window
  3. Include reference: "Full history in history/session_001.txt"
Result: Agent can search history file to recover details lost in summarization
```

## Guidelines

1. Write large outputs to files; return summaries and references to context
2. Store plans and state in structured files for re-reading
3. Use sub-agent file workspaces instead of message chains
4. Load skills dynamically rather than stuffing all into system prompt
5. Persist terminal and log output as searchable files
6. Combine grep/glob with semantic search for comprehensive discovery
7. Organize files for agent discoverability with clear naming
8. Measure token savings to validate filesystem patterns are effective
9. Implement cleanup for scratch files to prevent unbounded growth
10. Guard self-modification patterns with validation

## Integration

This skill connects to:

- context-optimization - Filesystem offloading is a form of observation masking
- memory-systems - Filesystem-as-memory is a simple memory layer
- multi-agent-patterns - Sub-agent file workspaces enable isolation
- context-compression - File references enable lossless "compression"
- tool-design - Tools should return file references for large outputs

## References

Internal reference:
- Implementation Patterns - Detailed pattern implementations

Related skills in this collection:
- context-optimization - Token reduction techniques
- memory-systems - Persistent storage patterns
- multi-agent-patterns - Agent coordination

External resources:
- LangChain Deep Agents: How agents can use filesystems for context engineering
- Cursor: Dynamic context discovery patterns
- Anthropic: Agent Skills specification

---

## Skill Metadata

**Created**: 2026-01-07
**Last Updated**: 2026-01-07
**Author**: Agent Skills for Context Engineering Contributors
**Version**: 1.0.0

---

## Merged Reference (legacy variant)

---
name: data-structure-protocol
description: "Give agents persistent structural memory of a codebase — navigate dependencies, track public APIs, and understand why connections exist without re-reading the whole repo."
risk: safe
source: "https://github.com/k-kolomeitsev/data-structure-protocol"
date_added: "2026-02-27"
---

# Data Structure Protocol (DSP)

LLM coding agents lose context between tasks. On large codebases they spend most of their tokens on "orientation" — figuring out where things live, what depends on what, and what is safe to change. DSP solves this by externalizing the project's structural map into a persistent, queryable graph stored in a `.dsp/` directory next to the code.

DSP is NOT documentation for humans and NOT an AST dump. It captures three things: **meaning** (why an entity exists), **boundaries** (what it imports and exposes), and **reasons** (why each connection exists). This is enough for an agent to navigate, refactor, and generate code without loading the entire source tree into the context window.

## When to Use

Use this skill when:
- The project has a `.dsp/` directory (DSP is already set up)
- The user asks to set up DSP, bootstrap, or map a project's structure
- Creating, modifying, or deleting code files in a DSP-tracked project (to keep the graph updated)
- Navigating project structure, understanding dependencies, or finding specific modules
- The user mentions DSP, dsp-cli, `.dsp`, or structure mapping
- Performing impact analysis before a refactor or dependency replacement

## Core Concepts

### Code = graph

DSP models the codebase as a directed graph. Nodes are **entities**, edges are **imports** and **shared/exports**.

Two entity kinds exist:
- **Object**: any "thing" that isn't a function (module/file/class/config/resource/external dependency)
- **Function**: an exported function/method/handler/pipeline

### Identity by UID, not by file path

Every entity gets a stable UID: `obj-<8hex>` for objects, `func-<8hex>` for functions. File paths are attributes that can change; UIDs survive renames, moves, and reformatting.

For entities inside a file, the UID is anchored with a comment marker in source code:

```js
// @dsp func-7f3a9c12
export function calculateTotal(items) { ... }
```

```python
# @dsp obj-e5f6g7h8
class UserService:
```

### Every connection has a "why"

When an import is recorded, DSP stores a short reason explaining *why* that dependency exists. This lives in the `exports/` reverse index of the imported entity. A dependency graph without reasons tells you *what imports what*; reasons tell you **what is safe to change and who will break**.

### Storage format

Each entity gets a small directory under `.dsp/`:

```
.dsp/
├── TOC                        # ordered list of all entity UIDs from root
├── obj-a1b2c3d4/
│   ├── description            # source path, kind, purpose (1-3 sentences)
│   ├── imports                # UIDs this entity depends on (one per line)
│   ├── shared                 # UIDs of public API / exported entities
│   └── exports/               # reverse index: who imports this and why
│       ├── <importer_uid>     # file content = "why" text
│       └── <shared_uid>/
│           ├── description    # what is exported
│           └── <importer_uid> # why this specific export is imported
└── func-7f3a9c12/
    ├── description
    ├── imports
    └── exports/
```

Everything is plain text. Diffable. Reviewable. No database needed.

### Full import coverage

Every file or artifact that is imported anywhere must be represented in `.dsp` as an Object — code, images, styles, configs, JSON, wasm, everything. External dependencies (npm packages, stdlib, etc.) are recorded as `kind: external` but their internals are never analyzed.

## How It Works

### Initial Setup

The skill relies on a standalone Python CLI script `dsp-cli.py`. If it is missing from the project, download it:

```bash
curl -O https://raw.githubusercontent.com/k-kolomeitsev/data-structure-protocol/main/skills/data-structure-protocol/scripts/dsp-cli.py
```

Requires **Python 3.10+**. All commands use `python dsp-cli.py --root <project-root> <command>`.

### Bootstrap (initial mapping)

If `.dsp/` is empty, traverse the project from root entrypoint(s) via DFS on imports:

1. Identify root entrypoints (`package.json` main, framework entry, `main.py`, etc.)
2. Document the root file: `create-object`, `create-function` for each export, `create-shared`, `add-import` for all dependencies
3. Take the first non-external import, document it fully, descend into its imports
4. Backtrack when no unvisited local imports remain; continue until all reachable files are documented
5. External dependencies: `create-object --kind external`, add to TOC, but never descend into `node_modules`/`site-packages`/etc.

### Workflow Rules

- **Before changing code**: Find affected entities via `search`, `find-by-source`, or `read-toc`. Read their `description` and `imports` to understand context.
- **When creating a file/module**: Call `create-object`. For each exported function — `create-function` (with `--owner`). Register exports via `create-shared`.
- **When adding an import**: Call `add-import` with a brief `why`. For external deps — first `create-object --kind external` if the entity doesn't exist.
- **When removing import/export/file**: Call `remove-import`, `remove-shared`, `remove-entity`. Cascade cleanup is automatic.
- **When renaming/moving a file**: Call `move-entity`. UID does not change.
- **Don't touch DSP** if only internal implementation changed without affecting purpose or dependencies.

### Key Commands

| Category | Commands |
|----------|----------|
| **Create** | `init`, `create-object`, `create-function`, `create-shared`, `add-import` |
| **Update** | `update-description`, `update-import-why`, `move-entity` |
| **Delete** | `remove-import`, `remove-shared`, `remove-entity` |
| **Navigate** | `get-entity`, `get-children --depth N`, `get-parents --depth N`, `get-path`, `get-recipients`, `read-toc` |
| **Search** | `search <query>`, `find-by-source <path>` |
| **Diagnostics** | `detect-cycles`, `get-orphans`, `get-stats` |

### When to Update DSP

| Code Change | DSP Action |
|---|---|
| New file/module | `create-object` + `create-function` + `create-shared` + `add-import` |
| New import added | `add-import` (+ `create-object --kind external` if new dep) |
| Import removed | `remove-import` |
| Export added | `create-shared` (+ `create-function` if new) |
| Export removed | `remove-shared` |
| File renamed/moved | `move-entity` |
| File deleted | `remove-entity` |
| Purpose changed | `update-description` |
| Internal-only change | **No DSP update needed** |

## Examples

### Example 1: Setting up DSP and documenting a module

```bash
python dsp-cli.py --root . init

python dsp-cli.py --root . create-object "src/app.ts" "Main application entrypoint"
# Output: obj-a1b2c3d4

python dsp-cli.py --root . create-function "src/app.ts#start" "Starts the HTTP server" --owner obj-a1b2c3d4
# Output: func-7f3a9c12

python dsp-cli.py --root . create-shared obj-a1b2c3d4 func-7f3a9c12

python dsp-cli.py --root . add-import obj-a1b2c3d4 obj-deadbeef "HTTP routing"
```

### Example 2: Navigating the graph before making changes

```bash
python dsp-cli.py --root . search "authentication"
python dsp-cli.py --root . get-entity obj-a1b2c3d4
python dsp-cli.py --root . get-children obj-a1b2c3d4 --depth 2
python dsp-cli.py --root . get-recipients obj-a1b2c3d4
python dsp-cli.py --root . get-path obj-a1b2c3d4 func-7f3a9c12
```

### Example 3: Impact analysis before replacing a library

```bash
python dsp-cli.py --root . find-by-source "lodash"
# Output: obj-11223344

python dsp-cli.py --root . get-recipients obj-11223344
# Shows every module that imports lodash and WHY — lets you systematically replace it
```

## Best Practices

- ✅ **Do:** Update DSP immediately when creating new files, adding imports, or changing public APIs
- ✅ **Do:** Always add a meaningful `why` reason when recording an import — this is where most of DSP's value lives
- ✅ **Do:** Use `kind: external` for third-party libraries without analyzing their internals
- ✅ **Do:** Keep descriptions minimal (1-3 sentences about purpose, not implementation)
- ✅ **Do:** Treat `.dsp/` diffs like code diffs — review them, keep them accurate
- ❌ **Don't:** Touch `.dsp/` for internal-only changes that don't affect purpose or dependencies
- ❌ **Don't:** Change an entity's UID on rename/move (use `move-entity` instead)
- ❌ **Don't:** Create UIDs for every local variable or helper — only file-level Objects and public/shared entities

## Integration

This skill connects naturally to:
- **context-compression** — DSP reduces the need for compression by providing targeted retrieval instead of loading everything
- **context-optimization** — DSP is a structural optimization: agents pull minimal "context bundles" instead of raw source
- **architecture** — DSP captures architectural boundaries (imports/exports) that feed system design decisions

## References

- **Full architecture specification**: [ARCHITECTURE.md](https://github.com/k-kolomeitsev/data-structure-protocol/blob/main/ARCHITECTURE.md)
- **CLI source + reference docs**: [skills/data-structure-protocol](https://github.com/k-kolomeitsev/data-structure-protocol/tree/main/skills/data-structure-protocol)
- **Introduction article**: [article.md](https://github.com/k-kolomeitsev/data-structure-protocol/blob/main/article.md)

## Source: references/skills/agent-memory-systems/references/legacy/agent-memory-mcp/SKILL.md

---
name: agent-memory-mcp
description: "A hybrid memory system that provides persistent, searchable knowledge management for AI agents (Architecture, Patterns, Decisions)."
risk: unknown
source: community
date_added: "2026-02-27"
---

# Agent Memory Skill

This skill provides a persistent, searchable memory bank that automatically syncs with project documentation. It runs as an MCP server to allow reading/writing/searching of long-term memories.

## Prerequisites

- Node.js (v18+)

## Setup

1. **Clone the Repository**:
   Clone the `agentMemory` project into your agent's workspace or a parallel directory:

   ```bash
   git clone https://github.com/webzler/agentMemory.git .agent/skills/agent-memory
   ```

2. **Install Dependencies**:

   ```bash
   cd .agent/skills/agent-memory
   npm install
   npm run compile
   ```

3. **Start the MCP Server**:
   Use the helper script to activate the memory bank for your current project:

   ```bash
   npm run start-server <project_id> <absolute_path_to_target_workspace>
   ```

   _Example for current directory:_

   ```bash
   npm run start-server my-project $(pwd)
   ```

## Capabilities (MCP Tools)

### `memory_search`

Search for memories by query, type, or tags.

- **Args**: `query` (string), `type?` (string), `tags?` (string[])
- **Usage**: "Find all authentication patterns" -> `memory_search({ query: "authentication", type: "pattern" })`

### `memory_write`

Record new knowledge or decisions.

- **Args**: `key` (string), `type` (string), `content` (string), `tags?` (string[])
- **Usage**: "Save this architecture decision" -> `memory_write({ key: "auth-v1", type: "decision", content: "..." })`

### `memory_read`

Retrieve specific memory content by key.

- **Args**: `key` (string)
- **Usage**: "Get the auth design" -> `memory_read({ key: "auth-v1" })`

### `memory_stats`

View analytics on memory usage.

- **Usage**: "Show memory statistics" -> `memory_stats({})`

## Dashboard

This skill includes a standalone dashboard to visualize memory usage.

```bash
npm run start-dashboard <absolute_path_to_target_workspace>
```

Access at: `http://localhost:3333`

## When to Use
This skill is applicable to execute the workflow or actions described in the overview.

## Source: references/skills/agent-memory-systems/references/legacy/context-compression/SKILL.md

---
name: context-compression
description: This skill should be used when the user asks to "compress context", "summarize conversation history", "implement compaction", "reduce token usage", or mentions context compression, structured summarization, tokens-per-task optimization, or long-running agent sessions...
---

# Context Compression Strategies

When agent sessions generate millions of tokens of conversation history, compression becomes mandatory. The naive approach is aggressive compression to minimize tokens per request. The correct optimization target is tokens per task: total tokens consumed to complete a task, including re-fetching costs when compression loses critical information.

## When to Activate

Activate this skill when:
- Agent sessions exceed context window limits
- Codebases exceed context windows (5M+ token systems)
- Designing conversation summarization strategies
- Debugging cases where agents "forget" what files they modified
- Building evaluation frameworks for compression quality

## Core Concepts

Context compression trades token savings against information loss. Three production-ready approaches exist:

1. **Anchored Iterative Summarization**: Maintain structured, persistent summaries with explicit sections for session intent, file modifications, decisions, and next steps. When compression triggers, summarize only the newly-truncated span and merge with the existing summary. Structure forces preservation by dedicating sections to specific information types.

2. **Opaque Compression**: Produce compressed representations optimized for reconstruction fidelity. Achieves highest compression ratios (99%+) but sacrifices interpretability. Cannot verify what was preserved.

3. **Regenerative Full Summary**: Generate detailed structured summaries on each compression. Produces readable output but may lose details across repeated compression cycles due to full regeneration rather than incremental merging.

The critical insight: structure forces preservation. Dedicated sections act as checklists that the summarizer must populate, preventing silent information drift.

## Detailed Topics

### Why Tokens-Per-Task Matters

Traditional compression metrics target tokens-per-request. This is the wrong optimization. When compression loses critical details like file paths or error messages, the agent must re-fetch information, re-explore approaches, and waste tokens recovering context.

The right metric is tokens-per-task: total tokens consumed from task start to completion. A compression strategy saving 0.5% more tokens but causing 20% more re-fetching costs more overall.

### The Artifact Trail Problem

Artifact trail integrity is the weakest dimension across all compression methods, scoring 2.2-2.5 out of 5.0 in evaluations. Even structured summarization with explicit file sections struggles to maintain complete file tracking across long sessions.

Coding agents need to know:
- Which files were created
- Which files were modified and what changed
- Which files were read but not changed
- Function names, variable names, error messages

This problem likely requires specialized handling beyond general summarization: a separate artifact index or explicit file-state tracking in agent scaffolding.

### Structured Summary Sections

Effective structured summaries include explicit sections:

```markdown
## Session Intent
[What the user is trying to accomplish]

## Files Modified
- auth.controller.ts: Fixed JWT token generation
- config/redis.ts: Updated connection pooling
- tests/auth.test.ts: Added mock setup for new config

## Decisions Made
- Using Redis connection pool instead of per-request connections
- Retry logic with exponential backoff for transient failures

## Current State
- 14 tests passing, 2 failing
- Remaining: mock setup for session service tests

## Next Steps
1. Fix remaining test failures
2. Run full test suite
3. Update documentation
```

This structure prevents silent loss of file paths or decisions because each section must be explicitly addressed.

### Compression Trigger Strategies

When to trigger compression matters as much as how to compress:

| Strategy | Trigger Point | Trade-off |
|----------|---------------|-----------|
| Fixed threshold | 70-80% context utilization | Simple but may compress too early |
| Sliding window | Keep last N turns + summary | Predictable context size |
| Importance-based | Compress low-relevance sections first | Complex but preserves signal |
| Task-boundary | Compress at logical task completions | Clean summaries but unpredictable timing |

The sliding window approach with structured summaries provides the best balance of predictability and quality for most coding agent use cases.

### Probe-Based Evaluation

Traditional metrics like ROUGE or embedding similarity fail to capture functional compression quality. A summary may score high on lexical overlap while missing the one file path the agent needs.

Probe-based evaluation directly measures functional quality by asking questions after compression:

| Probe Type | What It Tests | Example Question |
|------------|---------------|------------------|
| Recall | Factual retention | "What was the original error message?" |
| Artifact | File tracking | "Which files have we modified?" |
| Continuation | Task planning | "What should we do next?" |
| Decision | Reasoning chain | "What did we decide about the Redis issue?" |

If compression preserved the right information, the agent answers correctly. If not, it guesses or hallucinates.

### Evaluation Dimensions

Six dimensions capture compression quality for coding agents:

1. **Accuracy**: Are technical details correct? File paths, function names, error codes.
2. **Context Awareness**: Does the response reflect current conversation state?
3. **Artifact Trail**: Does the agent know which files were read or modified?
4. **Completeness**: Does the response address all parts of the question?
5. **Continuity**: Can work continue without re-fetching information?
6. **Instruction Following**: Does the response respect stated constraints?

Accuracy shows the largest variation between compression methods (0.6 point gap). Artifact trail is universally weak (2.2-2.5 range).

## Practical Guidance

### Three-Phase Compression Workflow

For large codebases or agent systems exceeding context windows, apply compression through three phases:

1. **Research Phase**: Produce a research document from architecture diagrams, documentation, and key interfaces. Compress exploration into a structured analysis of components and dependencies. Output: single research document.

2. **Planning Phase**: Convert research into implementation specification with function signatures, type definitions, and data flow. A 5M token codebase compresses to approximately 2,000 words of specification.

3. **Implementation Phase**: Execute against the specification. Context remains focused on the spec rather than raw codebase exploration.

### Using Example Artifacts as Seeds

When provided with a manual migration example or reference PR, use it as a template to understand the target pattern. The example reveals constraints that static analysis cannot surface: which invariants must hold, which services break on changes, and what a clean migration looks like.

This is particularly important when the agent cannot distinguish essential complexity (business requirements) from accidental complexity (legacy workarounds). The example artifact encodes that distinction.

### Implementing Anchored Iterative Summarization

1. Define explicit summary sections matching your agent's needs
2. On first compression trigger, summarize truncated history into sections
3. On subsequent compressions, summarize only new truncated content
4. Merge new summary into existing sections rather than regenerating
5. Track which information came from which compression cycle for debugging

### When to Use Each Approach

**Use anchored iterative summarization when:**
- Sessions are long-running (100+ messages)
- File tracking matters (coding, debugging)
- You need to verify what was preserved

**Use opaque compression when:**
- Maximum token savings required
- Sessions are relatively short
- Re-fetching costs are low

**Use regenerative summaries when:**
- Summary interpretability is critical
- Sessions have clear phase boundaries
- Full context review is acceptable on each compression

### Compression Ratio Considerations

| Method | Compression Ratio | Quality Score | Trade-off |
|--------|-------------------|---------------|-----------|
| Anchored Iterative | 98.6% | 3.70 | Best quality, slightly less compression |
| Regenerative | 98.7% | 3.44 | Good quality, moderate compression |
| Opaque | 99.3% | 3.35 | Best compression, quality loss |

The 0.7% additional tokens retained by structured summarization buys 0.35 quality points. For any task where re-fetching costs matter, this trade-off favors structured approaches.

## Examples

**Example 1: Debugging Session Compression**

Original context (89,000 tokens, 178 messages):
- 401 error on /api/auth/login endpoint
- Traced through auth controller, middleware, session store
- Found stale Redis connection
- Fixed connection pooling, added retry logic
- 14 tests passing, 2 failing

Structured summary after compression:

```markdown
## Session Intent
Debug 401 Unauthorized error on /api/auth/login despite valid credentials.

## Root Cause
Stale Redis connection in session store. JWT generated correctly but session could not be persisted.

## Files Modified
- auth.controller.ts: No changes (read only)
- middleware/cors.ts: No changes (examined)
- config/redis.ts: Fixed connection pooling configuration
- services/session.service.ts: Added retry logic for transient failures
- tests/auth.test.ts: Updated mock setup

## Test Status
14 passing, 2 failing (mock setup issues)

## Next Steps
1. Fix remaining test failures (mock session service)
2. Run full test suite
3. Deploy to staging
```

**Example 2: Probe Response Quality**

After compression, asking "What was the original error?":

Good response (structured summarization):
> "The original error was a 401 Unauthorized response from the /api/auth/login endpoint. Users received this error with valid credentials. Root cause was stale Redis connection in session store."

Poor response (aggressive compression):
> "We were debugging an authentication issue. The login was failing. We fixed some configuration problems."

The structured response preserves endpoint, error code, and root cause. The aggressive response loses all technical detail.

## Guidelines

1. Optimize for tokens-per-task, not tokens-per-request
2. Use structured summaries with explicit sections for file tracking
3. Trigger compression at 70-80% context utilization
4. Implement incremental merging rather than full regeneration
5. Test compression quality with probe-based evaluation
6. Track artifact trail separately if file tracking is critical
7. Accept slightly lower compression ratios for better quality retention
8. Monitor re-fetching frequency as a compression quality signal

## Integration

This skill connects to several others in the collection:

- context-degradation - Compression is a mitigation strategy for degradation
- context-optimization - Compression is one optimization technique among many
- evaluation - Probe-based evaluation applies to compression testing
- memory-systems - Compression relates to scratchpad and summary memory patterns

## References

Internal reference:
- Evaluation Framework Reference - Detailed probe types and scoring rubrics

Related skills in this collection:
- context-degradation - Understanding what compression prevents
- context-optimization - Broader optimization strategies
- evaluation - Building evaluation frameworks

External resources:
- Factory Research: Evaluating Context Compression for AI Agents (December 2025)
- Research on LLM-as-judge evaluation methodology (Zheng et al., 2023)
- Netflix Engineering: "The Infinite Software Crisis" - Three-phase workflow and context compression at scale (AI Summit 2025)

---

## Skill Metadata

**Created**: 2025-12-22
**Last Updated**: 2025-12-26
**Author**: Agent Skills for Context Engineering Contributors
**Version**: 1.1.0


## Source: references/skills/agent-memory-systems/references/legacy/context-degradation/SKILL.md

---
name: context-degradation
description: This skill should be used when the user asks to "diagnose context problems", "fix lost-in-middle issues", "debug agent failures", "understand context poisoning", or mentions context degradation, attention patterns, context clash, context confusion, or agent performance...
---

# Context Degradation Patterns

Language models exhibit predictable degradation patterns as context length increases. Understanding these patterns is essential for diagnosing failures and designing resilient systems. Context degradation is not a binary state but a continuum of performance degradation that manifests in several distinct ways.

## When to Activate

Activate this skill when:
- Agent performance degrades unexpectedly during long conversations
- Debugging cases where agents produce incorrect or irrelevant outputs
- Designing systems that must handle large contexts reliably
- Evaluating context engineering choices for production systems
- Investigating "lost in middle" phenomena in agent outputs
- Analyzing context-related failures in agent behavior

## Core Concepts

Context degradation manifests through several distinct patterns. The lost-in-middle phenomenon causes information in the center of context to receive less attention. Context poisoning occurs when errors compound through repeated reference. Context distraction happens when irrelevant information overwhelms relevant content. Context confusion arises when the model cannot determine which context applies. Context clash develops when accumulated information directly conflicts.

These patterns are predictable and can be mitigated through architectural patterns like compaction, masking, partitioning, and isolation.

## Detailed Topics

### The Lost-in-Middle Phenomenon

The most well-documented degradation pattern is the "lost-in-middle" effect, where models demonstrate U-shaped attention curves. Information at the beginning and end of context receives reliable attention, while information buried in the middle suffers from dramatically reduced recall accuracy.

**Empirical Evidence**
Research demonstrates that relevant information placed in the middle of context experiences 10-40% lower recall accuracy compared to the same information at the beginning or end. This is not a failure of the model but a consequence of attention mechanics and training data distributions.

Models allocate massive attention to the first token (often the BOS token) to stabilize internal states. This creates an "attention sink" that soaks up attention budget. As context grows, the limited budget is stretched thinner, and middle tokens fail to garner sufficient attention weight for reliable retrieval.

**Practical Implications**
Design context placement with attention patterns in mind. Place critical information at the beginning or end of context. Consider whether information will be queried directly or needs to support reasoning—if the latter, placement matters less but overall signal quality matters more.

For long documents or conversations, use summary structures that surface key information at attention-favored positions. Use explicit section headers and transitions to help models navigate structure.

### Context Poisoning

Context poisoning occurs when hallucinations, errors, or incorrect information enters context and compounds through repeated reference. Once poisoned, context creates feedback loops that reinforce incorrect beliefs.

**How Poisoning Occurs**
Poisoning typically enters through three pathways. First, tool outputs may contain errors or unexpected formats that models accept as ground truth. Second, retrieved documents may contain incorrect or outdated information that models incorporate into reasoning. Third, model-generated summaries or intermediate outputs may introduce hallucinations that persist in context.

The compounding effect is severe. If an agent's goals section becomes poisoned, it develops strategies that take substantial effort to undo. Each subsequent decision references the poisoned content, reinforcing incorrect assumptions.

**Detection and Recovery**
Watch for symptoms including degraded output quality on tasks that previously succeeded, tool misalignment where agents call wrong tools or parameters, and hallucinations that persist despite correction attempts. When these symptoms appear, consider context poisoning.

Recovery requires removing or replacing poisoned content. This may involve truncating context to before the poisoning point, explicitly noting the poisoning in context and asking for re-evaluation, or restarting with clean context and preserving only verified information.

### Context Distraction

Context distraction emerges when context grows so long that models over-focus on provided information at the expense of their training knowledge. The model attends to everything in context regardless of relevance, and this creates pressure to use provided information even when internal knowledge is more accurate.

**The Distractor Effect**
Research shows that even a single irrelevant document in context reduces performance on tasks involving relevant documents. Multiple distractors compound degradation. The effect is not about noise in absolute terms but about attention allocation—irrelevant information competes with relevant information for limited attention budget.

Models do not have a mechanism to "skip" irrelevant context. They must attend to everything provided, and this obligation creates distraction even when the irrelevant information is clearly not useful.

**Mitigation Strategies**
Mitigate distraction through careful curation of what enters context. Apply relevance filtering before loading retrieved documents. Use namespacing and organization to make irrelevant sections easy to ignore structurally. Consider whether information truly needs to be in context or can be accessed through tool calls instead.

### Context Confusion

Context confusion arises when irrelevant information influences responses in ways that degrade quality. This is related to distraction but distinct—confusion concerns the influence of context on model behavior rather than attention allocation.

If you put something in context, the model has to pay attention to it. The model may incorporate irrelevant information, use inappropriate tool definitions, or apply constraints that came from different contexts. Confusion is especially problematic when context contains multiple task types or when switching between tasks within a single session.

**Signs of Confusion**
Watch for responses that address the wrong aspect of a query, tool calls that seem appropriate for a different task, or outputs that mix requirements from multiple sources. These indicate confusion about what context applies to the current situation.

**Architectural Solutions**
Architectural solutions include explicit task segmentation where different tasks get different context windows, clear transitions between task contexts, and state management that isolates context for different objectives.

### Context Clash

Context clash develops when accumulated information directly conflicts, creating contradictory guidance that derails reasoning. This differs from poisoning where one piece of information is incorrect—in clash, multiple correct pieces of information contradict each other.

**Sources of Clash**
Clash commonly arises from multi-source retrieval where different sources have contradictory information, version conflicts where outdated and current information both appear in context, and perspective conflicts where different viewpoints are valid but incompatible.

**Resolution Approaches**
Resolution approaches include explicit conflict marking that identifies contradictions and requests clarification, priority rules that establish which source takes precedence, and version filtering that excludes outdated information from context.

### Empirical Benchmarks and Thresholds

Research provides concrete data on degradation patterns that inform design decisions.

**RULER Benchmark Findings**
The RULER benchmark delivers sobering findings: only 50% of models claiming 32K+ context maintain satisfactory performance at 32K tokens. GPT-5.2 shows the least degradation among current models, while many still drop 30+ points at extended contexts. Near-perfect scores on simple needle-in-haystack tests do not translate to real long-context understanding.

**Model-Specific Degradation Thresholds**
| Model | Degradation Onset | Severe Degradation | Notes |
|-------|-------------------|-------------------|-------|
| GPT-5.2 | ~64K tokens | ~200K tokens | Best overall degradation resistance with thinking mode |
| AI assistant Opus 4.5 | ~100K tokens | ~180K tokens | 200K context window, strong attention management |
| AI assistant Sonnet 4.5 | ~80K tokens | ~150K tokens | Optimized for agents and coding tasks |
| Gemini 3 Pro | ~500K tokens | ~800K tokens | 1M context window, native multimodality |
| Gemini 3 Flash | ~300K tokens | ~600K tokens | 3x speed of Gemini 2.5, 81.2% MMMU-Pro |

**Model-Specific Behavior Patterns**
Different models exhibit distinct failure modes under context pressure:

- **AI assistant 4.5 series**: Lowest hallucination rates with calibrated uncertainty. AI assistant Opus 4.5 achieves 80.9% on SWE-bench Verified. Tends to refuse or ask clarification rather than fabricate.
- **GPT-5.2**: Two modes available - instant (fast) and thinking (reasoning). Thinking mode reduces hallucination through step-by-step verification but increases latency.
- **Gemini 3 Pro/Flash**: Native multimodality with 1M context window. Gemini 3 Flash offers 3x speed improvement over previous generation. Strong at multi-modal reasoning across text, code, images, audio, and video.

These patterns inform model selection for different use cases. High-stakes tasks benefit from AI assistant 4.5's conservative approach or GPT-5.2's thinking mode; speed-critical tasks may use instant modes.

### Counterintuitive Findings

Research reveals several counterintuitive patterns that challenge assumptions about context management.

**Shuffled Haystacks Outperform Coherent Ones**
Studies found that shuffled (incoherent) haystacks produce better performance than logically coherent ones. This suggests that coherent context may create false associations that confuse retrieval, while incoherent context forces models to rely on exact matching.

**Single Distractors Have Outsized Impact**
Even a single irrelevant document reduces performance significantly. The effect is not proportional to the amount of noise but follows a step function where the presence of any distractor triggers degradation.

**Needle-Question Similarity Correlation**
Lower similarity between needle and question pairs shows faster degradation with context length. Tasks requiring inference across dissimilar content are particularly vulnerable.

### When Larger Contexts Hurt

Larger context windows do not uniformly improve performance. In many cases, larger contexts create new problems that outweigh benefits.

**Performance Degradation Curves**
Models exhibit non-linear degradation with context length. Performance remains stable up to a threshold, then degrades rapidly. The threshold varies by model and task complexity. For many models, meaningful degradation begins around 8,000-16,000 tokens even when context windows support much larger sizes.

**Cost Implications**
Processing cost grows disproportionately with context length. The cost to process a 400K token context is not double the cost of 200K—it increases exponentially in both time and computing resources. For many applications, this makes large-context processing economically impractical.

**Cognitive Load Metaphor**
Even with an infinite context, asking a single model to maintain consistent quality across dozens of independent tasks creates a cognitive bottleneck. The model must constantly switch context between items, maintain a comparative framework, and ensure stylistic consistency. This is not a problem that more context solves.

## Practical Guidance

### The Four-Bucket Approach

Four strategies address different aspects of context degradation:

**Write**: Save context outside the window using scratchpads, file systems, or external storage. This keeps active context lean while preserving information access.

**Select**: Pull relevant context into the window through retrieval, filtering, and prioritization. This addresses distraction by excluding irrelevant information.

**Compress**: Reduce tokens while preserving information through summarization, abstraction, and observation masking. This extends effective context capacity.

**Isolate**: Split context across sub-agents or sessions to prevent any single context from growing large enough to degrade. This is the most aggressive strategy but often the most effective.

### Architectural Patterns

Implement these strategies through specific architectural patterns. Use just-in-time context loading to retrieve information only when needed. Use observation masking to replace verbose tool outputs with compact references. Use sub-agent architectures to isolate context for different tasks. Use compaction to summarize growing context before it exceeds limits.

## Examples

**Example 1: Detecting Degradation**
```yaml
# Context grows during long conversation
turn_1: 1000 tokens
turn_5: 8000 tokens
turn_10: 25000 tokens
turn_20: 60000 tokens (degradation begins)
turn_30: 90000 tokens (significant degradation)
```

**Example 2: Mitigating Lost-in-Middle**
```markdown
# Organize context with critical info at edges

[CURRENT TASK]                      # At start
- Goal: Generate quarterly report
- Deadline: End of week

[DETAILED CONTEXT]                  # Middle (less attention)
- 50 pages of data
- Multiple analysis sections
- Supporting evidence

[KEY FINDINGS]                     # At end
- Revenue up 15%
- Costs down 8%
- Growth in Region A
```

## Guidelines

1. Monitor context length and performance correlation during development
2. Place critical information at beginning or end of context
3. Implement compaction triggers before degradation becomes severe
4. Validate retrieved documents for accuracy before adding to context
5. Use versioning to prevent outdated information from causing clash
6. Segment tasks to prevent context confusion across different objectives
7. Design for graceful degradation rather than assuming perfect conditions
8. Test with progressively larger contexts to find degradation thresholds

## Integration

This skill builds on context-fundamentals and should be studied after understanding basic context concepts. It connects to:

- context-optimization - Techniques for mitigating degradation
- multi-agent-patterns - Using isolation to prevent degradation
- evaluation - Measuring and detecting degradation in production

## References

Internal reference:
- Degradation Patterns Reference - Detailed technical reference

Related skills in this collection:
- context-fundamentals - Context basics
- context-optimization - Mitigation techniques
- evaluation - Detection and measurement

External resources:
- Research on attention mechanisms and context window limitations
- Studies on the "lost-in-middle" phenomenon
- Production engineering guides from AI labs

---

## Skill Metadata

**Created**: 2025-12-20
**Last Updated**: 2025-12-20
**Author**: Agent Skills for Context Engineering Contributors
**Version**: 1.0.0

## Source: references/skills/agent-memory-systems/references/legacy/context-fundamentals/SKILL.md

---
name: context-fundamentals
description: This skill should be used when the user asks to "understand context", "explain context windows", "design agent architecture", "debug context issues", "optimize context usage", or discusses context components, attention mechanics, progressive disclosure, or context budgeting....
---

# Context Engineering Fundamentals

Context is the complete state available to a language model at inference time. It includes everything the model can attend to when generating responses: system instructions, tool definitions, retrieved documents, message history, and tool outputs. Understanding context fundamentals is prerequisite to effective context engineering.

## When to Activate

Activate this skill when:
- Designing new agent systems or modifying existing architectures
- Debugging unexpected agent behavior that may relate to context
- Optimizing context usage to reduce token costs or improve performance
- Onboarding new team members to context engineering concepts
- Reviewing context-related design decisions

## Core Concepts

Context comprises several distinct components, each with different characteristics and constraints. The attention mechanism creates a finite budget that constrains effective context usage. Progressive disclosure manages this constraint by loading information only as needed. The engineering discipline is curating the smallest high-signal token set that achieves desired outcomes.

## Detailed Topics

### The Anatomy of Context

**System Prompts**
System prompts establish the agent's core identity, constraints, and behavioral guidelines. They are loaded once at session start and typically persist throughout the conversation. System prompts should be extremely clear and use simple, direct language at the right altitude for the agent.

The right altitude balances two failure modes. At one extreme, engineers hardcode complex brittle logic that creates fragility and maintenance burden. At the other extreme, engineers provide vague high-level guidance that fails to give concrete signals for desired outputs or falsely assumes shared context. The optimal altitude strikes a balance: specific enough to guide behavior effectively, yet flexible enough to provide strong heuristics.

Organize prompts into distinct sections using XML tagging or Markdown headers to delineate background information, instructions, tool guidance, and output description. The exact formatting matters less as models become more capable, but structural clarity remains valuable.

**Tool Definitions**
Tool definitions specify the actions an agent can take. Each tool includes a name, description, parameters, and return format. Tool definitions live near the front of context after serialization, typically before or after the system prompt.

Tool descriptions collectively steer agent behavior. Poor descriptions force agents to guess; optimized descriptions include usage context, examples, and defaults. The consolidation principle states that if a human engineer cannot definitively say which tool should be used in a given situation, an agent cannot be expected to do better.

**Retrieved Documents**
Retrieved documents provide domain-specific knowledge, reference materials, or task-relevant information. Agents use retrieval augmented generation to pull relevant documents into context at runtime rather than pre-loading all possible information.

The just-in-time approach maintains lightweight identifiers (file paths, stored queries, web links) and uses these references to load data into context dynamically. This mirrors human cognition: we generally do not memorize entire corpuses of information but rather use external organization and indexing systems to retrieve relevant information on demand.

**Message History**
Message history contains the conversation between the user and agent, including previous queries, responses, and reasoning. For long-running tasks, message history can grow to dominate context usage.

Message history serves as scratchpad memory where agents track progress, maintain task state, and preserve reasoning across turns. Effective management of message history is critical for long-horizon task completion.

**Tool Outputs**
Tool outputs are the results of agent actions: file contents, search results, command execution output, API responses, and similar data. Tool outputs comprise the majority of tokens in typical agent trajectories, with research showing observations (tool outputs) can reach 83.9% of total context usage.

Tool outputs consume context whether they are relevant to current decisions or not. This creates pressure for strategies like observation masking, compaction, and selective tool result retention.

### Context Windows and Attention Mechanics

**The Attention Budget Constraint**
Language models process tokens through attention mechanisms that create pairwise relationships between all tokens in context. For n tokens, this creates n² relationships that must be computed and stored. As context length increases, the model's ability to capture these relationships gets stretched thin.

Models develop attention patterns from training data distributions where shorter sequences predominate. This means models have less experience with and fewer specialized parameters for context-wide dependencies. The result is an "attention budget" that depletes as context grows.

**Position Encoding and Context Extension**
Position encoding interpolation allows models to handle longer sequences by adapting them to originally trained smaller contexts. However, this adaptation introduces degradation in token position understanding. Models remain highly capable at longer contexts but show reduced precision for information retrieval and long-range reasoning compared to performance on shorter contexts.

**The Progressive Disclosure Principle**
Progressive disclosure manages context efficiently by loading information only as needed. At startup, agents load only skill names and descriptions—sufficient to know when a skill might be relevant. Full content loads only when a skill is activated for specific tasks.

This approach keeps agents fast while giving them access to more context on demand. The principle applies at multiple levels: skill selection, document loading, and even tool result retrieval.

### Context Quality Versus Context Quantity

The assumption that larger context windows solve memory problems has been empirically debunked. Context engineering means finding the smallest possible set of high-signal tokens that maximize the likelihood of desired outcomes.

Several factors create pressure for context efficiency. Processing cost grows disproportionately with context length—not just double the cost for double the tokens, but exponentially more in time and computing resources. Model performance degrades beyond certain context lengths even when the window technically supports more tokens. Long inputs remain expensive even with prefix caching.

The guiding principle is informativity over exhaustiveness. Include what matters for the decision at hand, exclude what does not, and design systems that can access additional information on demand.

### Context as Finite Resource

Context must be treated as a finite resource with diminishing marginal returns. Like humans with limited working memory, language models have an attention budget drawn on when parsing large volumes of context.

Every new token introduced depletes this budget by some amount. This creates the need for careful curation of available tokens. The engineering problem is optimizing utility against inherent constraints.

Context engineering is iterative and the curation phase happens each time you decide what to pass to the model. It is not a one-time prompt writing exercise but an ongoing discipline of context management.

## Practical Guidance

### File-System-Based Access

Agents with filesystem access can use progressive disclosure naturally. Store reference materials, documentation, and data externally. Load files only when needed using standard filesystem operations. This pattern avoids stuffing context with information that may not be relevant.

The file system itself provides structure that agents can navigate. File sizes suggest complexity; naming conventions hint at purpose; timestamps serve as proxies for relevance. Metadata of file references provides a mechanism to efficiently refine behavior.

### Hybrid Strategies

The most effective agents employ hybrid strategies. Pre-load some context for speed (like AGENT_CONTEXT.md files or project rules), but enable autonomous exploration for additional context as needed. The decision boundary depends on task characteristics and context dynamics.

For contexts with less dynamic content, pre-loading more upfront makes sense. For rapidly changing or highly specific information, just-in-time loading avoids stale context.

### Context Budgeting

Design with explicit context budgets in mind. Know the effective context limit for your model and task. Monitor context usage during development. Implement compaction triggers at appropriate thresholds. Design systems assuming context will degrade rather than hoping it will not.

Effective context budgeting requires understanding not just raw token counts but also attention distribution patterns. The middle of context receives less attention than the beginning and end. Place critical information at attention-favored positions.

## Examples

**Example 1: Organizing System Prompts**
```markdown
<BACKGROUND_INFORMATION>
You are a Python expert helping a development team.
Current project: Data processing pipeline in Python 3.9+
</BACKGROUND_INFORMATION>

<INSTRUCTIONS>
- Write clean, idiomatic Python code
- Include type hints for function signatures
- Add docstrings for public functions
- Follow PEP 8 style guidelines
</INSTRUCTIONS>

<TOOL_GUIDANCE>
Use bash for shell operations, python for code tasks.
File operations should use pathlib for cross-platform compatibility.
</TOOL_GUIDANCE>

<OUTPUT_DESCRIPTION>
Provide code blocks with syntax highlighting.
Explain non-obvious decisions in comments.
</OUTPUT_DESCRIPTION>
```

**Example 2: Progressive Document Loading**
```markdown
# Instead of loading all documentation at once:

# Step 1: Load summary
docs/api_summary.md          # Lightweight overview

# Step 2: Load specific section as needed
docs/api/endpoints.md        # Only when API calls needed
docs/api/authentication.md   # Only when auth context needed
```

## Guidelines

1. Treat context as a finite resource with diminishing returns
2. Place critical information at attention-favored positions (beginning and end)
3. Use progressive disclosure to defer loading until needed
4. Organize system prompts with clear section boundaries
5. Monitor context usage during development
6. Implement compaction triggers at 70-80% utilization
7. Design for context degradation rather than hoping to avoid it
8. Prefer smaller high-signal context over larger low-signal context

## Integration

This skill provides foundational context that all other skills build upon. It should be studied first before exploring:

- context-degradation - Understanding how context fails
- context-optimization - Techniques for extending context capacity
- multi-agent-patterns - How context isolation enables multi-agent systems
- tool-design - How tool definitions interact with context

## References

Internal reference:
- Context Components Reference - Detailed technical reference

Related skills in this collection:
- context-degradation - Understanding context failure patterns
- context-optimization - Techniques for efficient context use

External resources:
- Research on transformer attention mechanisms
- Production engineering guides from leading AI labs
- Framework documentation on context window management

---

## Skill Metadata

**Created**: 2025-12-20
**Last Updated**: 2025-12-20
**Author**: Agent Skills for Context Engineering Contributors
**Version**: 1.0.0

## Source: references/skills/agent-memory-systems/references/legacy/context-guardian/SKILL.md

---
name: context-guardian
description: Guardiao de contexto que preserva dados criticos antes da compactacao automatica. Snapshots, verificacao de integridade e zero perda de informacao.
risk: safe
source: community
date_added: '2026-03-06'
author: renat
tags:
- context
- data-integrity
- snapshots
- verification
tools:
- agent-compatible
- agent-compatible
- agent-compatible
- agent-compatible
- agent-compatible
---

# Context Guardian

## Overview

Guardiao de contexto que preserva dados criticos antes da compactacao automatica. Snapshots, verificacao de integridade e zero perda de informacao.

## When to Use This Skill

- When the user mentions "compactacao contexto" or related topics
- When the user mentions "perda de contexto" or related topics
- When the user mentions "snapshot contexto" or related topics
- When the user mentions "preservar contexto" or related topics
- When the user mentions "contexto critico" or related topics
- When the user mentions "antes de compactar" or related topics

## Do Not Use This Skill When

- The task is unrelated to context guardian
- A simpler, more specific tool can handle the request
- The user needs general-purpose assistance without domain expertise

## How It Works

Sistema de integridade de contexto que protege projetos tecnicoss complexos contra
perda de informacao durante compactacao automatica do AI coding assistant. Enquanto o
`context-agent` atua APOS as sessoes (save/load), o context-guardian atua DURANTE
a sessao, detectando quando a compactacao esta proxima e executando protocolos de
preservacao com verificacao redundante.

## Por Que Isto Existe

O AI coding assistant compacta automaticamente mensagens antigas quando o contexto se
aproxima do limite da janela. Essa compactacao e heuristica — ela resume mensagens
para liberar espaco, mas inevitavelmente perde detalhes. Para projetos simples,
isso funciona bem. Mas para projetos tecnicos pesados (como ecossistemas com 21+
skills, auditorias de seguranca, refatoracoes de arquitetura), a perda de um unico
detalhe pode causar regressoes, re-trabalho ou inconsistencias graves.

O context-guardian resolve isso criando uma camada de protecao PRE-compactacao:
extrai, classifica, verifica e persiste todas as informacoes criticas ANTES que a
compactacao automatica as destrua.

## Localizacao

```
C:\Users\renat\skills\context-guardian\
├── SKILL.md                          # Este arquivo
├── references/
│   ├── extraction-protocol.md        # Protocolo detalhado de extracao
│   └── verification-checklist.md     # Checklist de verificacao e redundancia
└── scripts/
    └── context_snapshot.py           # Script de snapshot automatico
```

## Integracao Com O Ecossistema

```
context-guardian (PRE-compactacao)    context-agent (POS-sessao)
         │                                    │
         ├── Detecta contexto grande          ├── Salva resumo ao final
         ├── Extrai dados criticos            ├── Atualiza ACTIVE_CONTEXT.md
         ├── Verifica integridade             ├── Sincroniza MEMORY.md
         ├── Salva snapshot verificado        ├── Indexa busca FTS5
         └── Gera briefing de transicao       └── Arquiva sessoes antigas
```

O context-guardian e o context-agent sao complementares:
- **context-guardian**: protecao em tempo real, DURANTE a sessao
- **context-agent**: persistencia entre sessoes, APOS a sessao

## Ativacao Automatica (O AI assistant Deve Iniciar Sozinho)

1. **Limite de contexto**: quando perceber que ja consumiu ~60-70% da janela de
   contexto (indicadores: mensagens comecando a ser resumidas, aviso de compactacao)
2. **Projetos pesados**: sessoes com muitos arquivos editados, muitas tool calls,
   ou projetos com dependencias complexas entre componentes
3. **Antes de tarefas longas**: quando uma proxima tarefa pode gerar output extenso
   que empurraria o contexto para alem do limite

## Ativacao Manual (Usuario Solicita)

- "salva o estado antes de comprimir"
- "faz um checkpoint"
- "snapshot do contexto"
- "nao quero perder nada dessa sessao"
- "prepara pra compactacao"
- "o contexto ta grande, protege"

## Fase 1: Extracao Estruturada

Percorrer toda a conversa ate o momento e extrair categorias criticas.
Para cada categoria, classificar por prioridade (P0 = perda fatal, P1 = perda grave,
P2 = perda toleravel).

**P0 — Perda Fatal (preservar com redundancia tripla)**

| Categoria | O que extrair | Exemplo |
|-----------|--------------|---------|
| Decisoes tecnicas | Escolhas de arquitetura, padrao, tecnologia E motivo | "Usamos parameterized queries porque f-strings causam SQL injection" |
| Estado de tarefas | O que foi feito, o que falta, dependencias | "18/18 match OK, falta ZIP" |
| Correcoes aplicadas | Bug, causa raiz, solucao exata, arquivos afetados | "instagram/db.py: SQL injection via f-string → ? placeholders" |
| Codigo gerado/modificado | Caminho exato, linhas alteradas, natureza da mudanca | "match_skills.py:40-119: adicionou 5 categorias" |
| Erros encontrados | Mensagem exata, stack trace relevante, como resolveu | "TypeError at line 45 → cast para int" |
| Comandos que funcionaram | Comando completo que produziu resultado correto | "python verify_zips.py → 22/22 OK" |

**P1 — Perda Grave (preservar com verificacao)**

| Categoria | O que extrair |
|-----------|--------------|
| Padroes descobertos | Convencoes, patterns de codigo observados |
| Dependencias entre componentes | "scan_registry.py E match_skills.py devem ter categorias identicas" |
| Preferencias do usuario | Idioma, estilo, nivel de detalhe, workflow preferido |
| Contexto de projeto | Estrutura de diretorios, arquivos-chave, proposito |
| Questoes em aberto | Perguntas sem resposta, ambiguidades nao resolvidas |

**P2 — Perda Toleravel (resumo compacto)**

| Categoria | O que extrair |
|-----------|--------------|
| Historico de tentativas | "Tentei X, nao funcionou por Y, entao Z" |
| Metricas de progresso | Contadores, tempos, tamanhos |
| Discussoes exploratórias | Brainstorm, opcoes consideradas e descartadas |

## Fase 2: Verificacao De Integridade

Apos extrair, verificar que NADA critico foi omitido.

**Checklist de Verificacao (executar mentalmente para cada item):**

```
□ Cada arquivo modificado tem: caminho, natureza da mudanca, motivo
□ Cada bug corrigido tem: sintoma, causa raiz, solucao, arquivo
□ Cada decisao tem: o que, por que, alternativas descartadas
□ Cada tarefa pendente tem: descricao, prioridade, dependencias
□ Cada padrao/convencao tem: regra, motivo, exemplos
□ Nenhuma informacao de uma secao contradiz outra
□ Referencias cruzadas estao consistentes (ex: "18 queries testadas" aparece em
  multiplos lugares com o mesmo numero)
□ Caminhos de arquivo estao completos (absolutos, nao relativos)
```

Se qualquer item falhar, voltar a Fase 1 e re-extrair a informacao faltante.

Para detalhes sobre verificacao avancada, ler `references/verification-checklist.md`.

## Fase 3: Persistencia Redundante

Salvar as informacoes extraidas em 3 camadas de redundancia:

**Camada 1 — Snapshot estruturado (arquivo .md)**

```bash
python C:\Users\renat\skills\context-guardian\scripts\context_snapshot.py save
```

Gera `C:\Users\renat\skills\context-guardian\data\snapshot-YYYYMMDD-HHMMSS.md` com
todas as informacoes extraidas em formato estruturado.

Se o script nao estiver disponivel, criar manualmente o arquivo seguindo o formato
descrito em `references/extraction-protocol.md`.

**Camada 2 — MEMORY.md atualizado**

Atualizar `C:\Users\renat\.agent\projects\C--Users-renat-Skill-JUD\memory\MEMORY.md`
com as informacoes P0 mais criticas em formato ultra-compacto. O MEMORY.md e carregado
automaticamente em toda nova sessao, entao ele e a ultima linha de defesa.

**Camada 3 — Context-agent save**

```bash
python C:\Users\renat\skills\context-agent\scripts\context_manager.py save
```

Aciona o context-agent para salvar sessao completa com indexacao FTS5.

## Fase 4: Briefing De Transicao

Gerar um bloco de texto formatado que serve como "cartao de visita" para o AI assistant
que continuar apos a compactacao. Este briefing deve ser a ULTIMA coisa escrita antes
da compactacao, para que fique no topo do contexto compactado.

**Formato do briefing:**

```markdown

## Estado Atual

- Projeto: [nome]
- Fase: [fase atual]
- Progresso: [X/Y tarefas completas]

## O Que Foi Feito Nesta Sessao

1. [tarefa 1 — resultado]
2. [tarefa 2 — resultado]
...

## O Que Falta Fazer

1. [tarefa pendente — prioridade] [dependencia se houver]
2. ...

## Decisoes Criticas (Nao Alterar Sem Motivo)

- [decisao 1]: [motivo]
- [decisao 2]: [motivo]

## Correcoes Aplicadas (Nao Reverter)

- [arquivo]: [correcao] — [motivo]

## Caminhos Importantes

- [caminho 1]: [proposito]
- [caminho 2]: [proposito]

## Alertas

- [qualquer armadilha, edge case, ou cuidado especial]

## Onde Recuperar Mais Informacoes

- Snapshot: C:\Users\renat\skills\context-guardian\data\snapshot-[timestamp].md
- MEMORY.md: carregado automaticamente
- Context-agent: `python context_manager.py load`
- Busca historica: `python context_manager.py search "termo"`
```

## Protocolo Rapido (Quando O Tempo E Curto)

Se a compactacao esta iminente e nao ha tempo para o protocolo completo de 4 fases:

1. **30 segundos** — Escrever um mini-briefing com: tarefas pendentes, decisoes
   criticas, caminhos de arquivo modificados
2. **1 minuto** — Atualizar MEMORY.md com informacoes P0
3. **2 minutos** — Executar context-agent save

Mesmo o protocolo rapido e melhor que nenhuma protecao.

## Deteccao De Completude Pos-Compactacao

Quando uma sessao continuar apos compactacao, verificar se o contexto preservado
esta completo:

1. Ler MEMORY.md (ja estara carregado automaticamente)
2. Se disponivel, ler o snapshot mais recente em `data/`
3. Comparar com o briefing de transicao (se visivel no contexto compactado)
4. Se encontrar lacunas, executar:
   ```bash
   python C:\Users\renat\skills\context-agent\scripts\context_manager.py load
   ```
5. Se ainda houver lacunas, buscar por termo:
   ```bash
   python C:\Users\renat\skills\context-agent\scripts\context_manager.py search "termo"
   ```

## Exemplo De Uso Real

**Cenario**: Sessao longa criando advogado-especialista (46KB), corrigindo match_skills
(5 categorias novas), auditando seguranca (10 vulnerabilidades), gerando 22 ZIPs.

**Sem context-guardian**:
Compactacao resume tudo em "criou skill juridica, corrigiu bugs, gerou zips".
Proximo AI assistant nao sabe quais categorias foram adicionadas, quais vulnerabilidades
foram corrigidas, qual o estado de cada ZIP, ou por que certas decisoes foram tomadas.
Resultado: re-trabalho, inconsistencias, regressoes.

**Com context-guardian**:
Antes da compactacao, executa protocolo completo:
- Snapshot com 5 categorias novas listadas (legal, auction, security, image-generation, monitoring)
- 10 vulnerabilidades catalogadas com arquivo, tipo, e correcao exata
- 22 ZIPs verificados com checksums
- Decisoes documentadas ("removeu 'saude' de monitoring porque causava false positive")
- Briefing de transicao no topo do contexto
Proximo AI assistant continua com precisao total, zero re-trabalho.

## Consideracoes De Performance

- O protocolo completo leva 2-5 minutos de trabalho do AI assistant
- Para projetos simples, usar apenas o protocolo rapido
- Nao ativar para sessoes curtas ou conversas casuais
- A persistencia em 3 camadas (snapshot + MEMORY.md + context-agent) garante que
  mesmo se uma camada falhar, as outras duas preservam a informacao
- Snapshots antigos (>10) podem ser podados manualmente

## Best Practices

- Provide clear, specific context about your project and requirements
- Review all suggestions before applying them to production code
- Combine with other complementary skills for comprehensive analysis

## Common Pitfalls

- Using this skill for tasks outside its domain expertise
- Applying recommendations without understanding your specific context
- Not providing enough project context for accurate analysis

## Related Skills

- `context-agent` - Complementary skill for enhanced analysis

## Source: references/skills/agent-memory-systems/references/legacy/context-management-context-restore/SKILL.md

---
name: context-management-context-restore
description: "Use when working with context management context restore"
risk: unknown
source: community
date_added: "2026-02-27"
---

# Context Restoration: Advanced Semantic Memory Rehydration

## Use this skill when

- Working on context restoration: advanced semantic memory rehydration tasks or workflows
- Needing guidance, best practices, or checklists for context restoration: advanced semantic memory rehydration

## Do not use this skill when

- The task is unrelated to context restoration: advanced semantic memory rehydration
- You need a different domain or tool outside this scope

## Instructions

- Clarify goals, constraints, and required inputs.
- Apply relevant best practices and validate outcomes.
- Provide actionable steps and verification.
- If detailed examples are required, open `resources/implementation-playbook.md`.

## Role Statement

Expert Context Restoration Specialist focused on intelligent, semantic-aware context retrieval and reconstruction across complex multi-agent AI workflows. Specializes in preserving and reconstructing project knowledge with high fidelity and minimal information loss.

## Context Overview

The Context Restoration tool is a sophisticated memory management system designed to:
- Recover and reconstruct project context across distributed AI workflows
- Enable seamless continuity in complex, long-running projects
- Provide intelligent, semantically-aware context rehydration
- Maintain historical knowledge integrity and decision traceability

## Core Requirements and Arguments

### Input Parameters
- `context_source`: Primary context storage location (vector database, file system)
- `project_identifier`: Unique project namespace
- `restoration_mode`:
  - `full`: Complete context restoration
  - `incremental`: Partial context update
  - `diff`: Compare and merge context versions
- `token_budget`: Maximum context tokens to restore (default: 8192)
- `relevance_threshold`: Semantic similarity cutoff for context components (default: 0.75)

## Advanced Context Retrieval Strategies

### 1. Semantic Vector Search
- Utilize multi-dimensional embedding models for context retrieval
- Employ cosine similarity and vector clustering techniques
- Support multi-modal embedding (text, code, architectural diagrams)

```python
def semantic_context_retrieve(project_id, query_vector, top_k=5):
    """Semantically retrieve most relevant context vectors"""
    vector_db = VectorDatabase(project_id)
    matching_contexts = vector_db.search(
        query_vector,
        similarity_threshold=0.75,
        max_results=top_k
    )
    return rank_and_filter_contexts(matching_contexts)
```

### 2. Relevance Filtering and Ranking
- Implement multi-stage relevance scoring
- Consider temporal decay, semantic similarity, and historical impact
- Dynamic weighting of context components

```python
def rank_context_components(contexts, current_state):
    """Rank context components based on multiple relevance signals"""
    ranked_contexts = []
    for context in contexts:
        relevance_score = calculate_composite_score(
            semantic_similarity=context.semantic_score,
            temporal_relevance=context.age_factor,
            historical_impact=context.decision_weight
        )
        ranked_contexts.append((context, relevance_score))

    return sorted(ranked_contexts, key=lambda x: x[1], reverse=True)
```

### 3. Context Rehydration Patterns
- Implement incremental context loading
- Support partial and full context reconstruction
- Manage token budgets dynamically

```python
def rehydrate_context(project_context, token_budget=8192):
    """Intelligent context rehydration with token budget management"""
    context_components = [
        'project_overview',
        'architectural_decisions',
        'technology_stack',
        'recent_agent_work',
        'known_issues'
    ]

    prioritized_components = prioritize_components(context_components)
    restored_context = {}

    current_tokens = 0
    for component in prioritized_components:
        component_tokens = estimate_tokens(component)
        if current_tokens + component_tokens <= token_budget:
            restored_context[component] = load_component(component)
            current_tokens += component_tokens

    return restored_context
```

### 4. Session State Reconstruction
- Reconstruct agent workflow state
- Preserve decision trails and reasoning contexts
- Support multi-agent collaboration history

### 5. Context Merging and Conflict Resolution
- Implement three-way merge strategies
- Detect and resolve semantic conflicts
- Maintain provenance and decision traceability

### 6. Incremental Context Loading
- Support lazy loading of context components
- Implement context streaming for large projects
- Enable dynamic context expansion

### 7. Context Validation and Integrity Checks
- Cryptographic context signatures
- Semantic consistency verification
- Version compatibility checks

### 8. Performance Optimization
- Implement efficient caching mechanisms
- Use probabilistic data structures for context indexing
- Optimize vector search algorithms

## Reference Workflows

### Workflow 1: Project Resumption
1. Retrieve most recent project context
2. Validate context against current codebase
3. Selectively restore relevant components
4. Generate resumption summary

### Workflow 2: Cross-Project Knowledge Transfer
1. Extract semantic vectors from source project
2. Map and transfer relevant knowledge
3. Adapt context to target project's domain
4. Validate knowledge transferability

## Usage Examples

```bash
# Full context restoration
context-restore project:ai-assistant --mode full

# Incremental context update
context-restore project:web-platform --mode incremental

# Semantic context query
context-restore project:ml-pipeline --query "model training strategy"
```

## Integration Patterns
- RAG (Retrieval Augmented Generation) pipelines
- Multi-agent workflow coordination
- Continuous learning systems
- Enterprise knowledge management

## Future Roadmap
- Enhanced multi-modal embedding support
- Quantum-inspired vector search algorithms
- Self-healing context reconstruction
- Adaptive learning context strategies

## Source: references/skills/agent-memory-systems/references/legacy/context-management-context-save/SKILL.md

---
name: context-management-context-save
description: "Use when working with context management context save"
risk: unknown
source: community
date_added: "2026-02-27"
---

# Context Save Tool: Intelligent Context Management Specialist

## Use this skill when

- Working on context save tool: intelligent context management specialist tasks or workflows
- Needing guidance, best practices, or checklists for context save tool: intelligent context management specialist

## Do not use this skill when

- The task is unrelated to context save tool: intelligent context management specialist
- You need a different domain or tool outside this scope

## Instructions

- Clarify goals, constraints, and required inputs.
- Apply relevant best practices and validate outcomes.
- Provide actionable steps and verification.
- If detailed examples are required, open `resources/implementation-playbook.md`.

## Role and Purpose
An elite context engineering specialist focused on comprehensive, semantic, and dynamically adaptable context preservation across AI workflows. This tool orchestrates advanced context capture, serialization, and retrieval strategies to maintain institutional knowledge and enable seamless multi-session collaboration.

## Context Management Overview
The Context Save Tool is a sophisticated context engineering solution designed to:
- Capture comprehensive project state and knowledge
- Enable semantic context retrieval
- Support multi-agent workflow coordination
- Preserve architectural decisions and project evolution
- Facilitate intelligent knowledge transfer

## Requirements and Argument Handling

### Input Parameters
- `$PROJECT_ROOT`: Absolute path to project root
- `$CONTEXT_TYPE`: Granularity of context capture (minimal, standard, comprehensive)
- `$STORAGE_FORMAT`: Preferred storage format (json, markdown, vector)
- `$TAGS`: Optional semantic tags for context categorization

## Context Extraction Strategies

### 1. Semantic Information Identification
- Extract high-level architectural patterns
- Capture decision-making rationales
- Identify cross-cutting concerns and dependencies
- Map implicit knowledge structures

### 2. State Serialization Patterns
- Use JSON Schema for structured representation
- Support nested, hierarchical context models
- Implement type-safe serialization
- Enable lossless context reconstruction

### 3. Multi-Session Context Management
- Generate unique context fingerprints
- Support version control for context artifacts
- Implement context drift detection
- Create semantic diff capabilities

### 4. Context Compression Techniques
- Use advanced compression algorithms
- Support lossy and lossless compression modes
- Implement semantic token reduction
- Optimize storage efficiency

### 5. Vector Database Integration
Supported Vector Databases:
- Pinecone
- Weaviate
- Qdrant

Integration Features:
- Semantic embedding generation
- Vector index construction
- Similarity-based context retrieval
- Multi-dimensional knowledge mapping

### 6. Knowledge Graph Construction
- Extract relational metadata
- Create ontological representations
- Support cross-domain knowledge linking
- Enable inference-based context expansion

### 7. Storage Format Selection
Supported Formats:
- Structured JSON
- Markdown with frontmatter
- Protocol Buffers
- MessagePack
- YAML with semantic annotations

## Code Examples

### 1. Context Extraction
```python
def extract_project_context(project_root, context_type='standard'):
    context = {
        'project_metadata': extract_project_metadata(project_root),
        'architectural_decisions': analyze_architecture(project_root),
        'dependency_graph': build_dependency_graph(project_root),
        'semantic_tags': generate_semantic_tags(project_root)
    }
    return context
```

### 2. State Serialization Schema
```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "properties": {
    "project_name": {"type": "string"},
    "version": {"type": "string"},
    "context_fingerprint": {"type": "string"},
    "captured_at": {"type": "string", "format": "date-time"},
    "architectural_decisions": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "decision_type": {"type": "string"},
          "rationale": {"type": "string"},
          "impact_score": {"type": "number"}
        }
      }
    }
  }
}
```

### 3. Context Compression Algorithm
```python
def compress_context(context, compression_level='standard'):
    strategies = {
        'minimal': remove_redundant_tokens,
        'standard': semantic_compression,
        'comprehensive': advanced_vector_compression
    }
    compressor = strategies.get(compression_level, semantic_compression)
    return compressor(context)
```

## Reference Workflows

### Workflow 1: Project Onboarding Context Capture
1. Analyze project structure
2. Extract architectural decisions
3. Generate semantic embeddings
4. Store in vector database
5. Create markdown summary

### Workflow 2: Long-Running Session Context Management
1. Periodically capture context snapshots
2. Detect significant architectural changes
3. Version and archive context
4. Enable selective context restoration

## Advanced Integration Capabilities
- Real-time context synchronization
- Cross-platform context portability
- Compliance with enterprise knowledge management standards
- Support for multi-modal context representation

## Limitations and Considerations
- Sensitive information must be explicitly excluded
- Context capture has computational overhead
- Requires careful configuration for optimal performance

## Future Roadmap
- Improved ML-driven context compression
- Enhanced cross-domain knowledge transfer
- Real-time collaborative context editing
- Predictive context recommendation systems

## Source: references/skills/agent-memory-systems/references/legacy/context-optimization/SKILL.md

---
name: context-optimization
description: This skill should be used when the user asks to "optimize context", "reduce token costs", "improve context efficiency", "implement KV-cache optimization", "partition context", or mentions context limits, observation masking, context budgeting, or extending effective context...
---

# Context Optimization Techniques

Context optimization extends the effective capacity of limited context windows through strategic compression, masking, caching, and partitioning. The goal is not to magically increase context windows but to make better use of available capacity. Effective optimization can double or triple effective context capacity without requiring larger models or longer contexts.

## When to Activate

Activate this skill when:
- Context limits constrain task complexity
- Optimizing for cost reduction (fewer tokens = lower costs)
- Reducing latency for long conversations
- Implementing long-running agent systems
- Needing to handle larger documents or conversations
- Building production systems at scale

## Core Concepts

Context optimization extends effective capacity through four primary strategies: compaction (summarizing context near limits), observation masking (replacing verbose outputs with references), KV-cache optimization (reusing cached computations), and context partitioning (splitting work across isolated contexts).

The key insight is that context quality matters more than quantity. Optimization preserves signal while reducing noise. The art lies in selecting what to keep versus what to discard, and when to apply each technique.

## Detailed Topics

### Compaction Strategies

**What is Compaction**
Compaction is the practice of summarizing context contents when approaching limits, then reinitializing a new context window with the summary. This distills the contents of a context window in a high-fidelity manner, enabling the agent to continue with minimal performance degradation.

Compaction typically serves as the first lever in context optimization. The art lies in selecting what to keep versus what to discard.

**Compaction Implementation**
Compaction works by identifying sections that can be compressed, generating summaries that capture essential points, and replacing full content with summaries. Priority for compression goes to tool outputs (replace with summaries), old turns (summarize early conversation), retrieved docs (summarize if recent versions exist), and never compress system prompt.

**Summary Generation**
Effective summaries preserve different elements depending on message type:

Tool outputs: Preserve key findings, metrics, and conclusions. Remove verbose raw output.

Conversational turns: Preserve key decisions, commitments, and context shifts. Remove filler and back-and-forth.

Retrieved documents: Preserve key facts and claims. Remove supporting evidence and elaboration.

### Observation Masking

**The Observation Problem**
Tool outputs can comprise 80%+ of token usage in agent trajectories. Much of this is verbose output that has already served its purpose. Once an agent has used a tool output to make a decision, keeping the full output provides diminishing value while consuming significant context.

Observation masking replaces verbose tool outputs with compact references. The information remains accessible if needed but does not consume context continuously.

**Masking Strategy Selection**
Not all observations should be masked equally:

Never mask: Observations critical to current task, observations from the most recent turn, observations used in active reasoning.

Consider masking: Observations from 3+ turns ago, verbose outputs with key points extractable, observations whose purpose has been served.

Always mask: Repeated outputs, boilerplate headers/footers, outputs already summarized in conversation.

### KV-Cache Optimization

**Understanding KV-Cache**
The KV-cache stores Key and Value tensors computed during inference, growing linearly with sequence length. Caching the KV-cache across requests sharing identical prefixes avoids recomputation.

Prefix caching reuses KV blocks across requests with identical prefixes using hash-based block matching. This dramatically reduces cost and latency for requests with common prefixes like system prompts.

**Cache Optimization Patterns**
Optimize for caching by reordering context elements to maximize cache hits. Place stable elements first (system prompt, tool definitions), then frequently reused elements, then unique elements last.

Design prompts to maximize cache stability: avoid dynamic content like timestamps, use consistent formatting, keep structure stable across sessions.

### Context Partitioning

**Sub-Agent Partitioning**
The most aggressive form of context optimization is partitioning work across sub-agents with isolated contexts. Each sub-agent operates in a clean context focused on its subtask without carrying accumulated context from other subtasks.

This approach achieves separation of concerns—the detailed search context remains isolated within sub-agents while the coordinator focuses on synthesis and analysis.

**Result Aggregation**
Aggregate results from partitioned subtasks by validating all partitions completed, merging compatible results, and summarizing if still too large.

### Budget Management

**Context Budget Allocation**
Design explicit context budgets. Allocate tokens to categories: system prompt, tool definitions, retrieved docs, message history, and reserved buffer. Monitor usage against budget and trigger optimization when approaching limits.

**Trigger-Based Optimization**
Monitor signals for optimization triggers: token utilization above 80%, degradation indicators, and performance drops. Apply appropriate optimization techniques based on context composition.

## Practical Guidance

### Optimization Decision Framework

When to optimize:
- Context utilization exceeds 70%
- Response quality degrades as conversations extend
- Costs increase due to long contexts
- Latency increases with conversation length

What to apply:
- Tool outputs dominate: observation masking
- Retrieved documents dominate: summarization or partitioning
- Message history dominates: compaction with summarization
- Multiple components: combine strategies

### Performance Considerations

Compaction should achieve 50-70% token reduction with less than 5% quality degradation. Masking should achieve 60-80% reduction in masked observations. Cache optimization should achieve 70%+ hit rate for stable workloads.

Monitor and iterate on optimization strategies based on measured effectiveness.

## Examples

**Example 1: Compaction Trigger**
```python
if context_tokens / context_limit > 0.8:
    context = compact_context(context)
```

**Example 2: Observation Masking**
```python
if len(observation) > max_length:
    ref_id = store_observation(observation)
    return f"[Obs:{ref_id} elided. Key: {extract_key(observation)}]"
```

**Example 3: Cache-Friendly Ordering**
```python
# Stable content first
context = [system_prompt, tool_definitions]  # Cacheable
context += [reused_templates]  # Reusable
context += [unique_content]  # Unique
```

## Guidelines

1. Measure before optimizing—know your current state
2. Apply compaction before masking when possible
3. Design for cache stability with consistent prompts
4. Partition before context becomes problematic
5. Monitor optimization effectiveness over time
6. Balance token savings against quality preservation
7. Test optimization at production scale
8. Implement graceful degradation for edge cases

## Integration

This skill builds on context-fundamentals and context-degradation. It connects to:

- multi-agent-patterns - Partitioning as isolation
- evaluation - Measuring optimization effectiveness
- memory-systems - Offloading context to memory

## References

Internal reference:
- Optimization Techniques Reference - Detailed technical reference

Related skills in this collection:
- context-fundamentals - Context basics
- context-degradation - Understanding when to optimize
- evaluation - Measuring optimization

External resources:
- Research on context window limitations
- KV-cache optimization techniques
- Production engineering guides

---

## Skill Metadata

**Created**: 2025-12-20
**Last Updated**: 2025-12-20
**Author**: Agent Skills for Context Engineering Contributors
**Version**: 1.0.0

## Source: references/skills/agent-memory-systems/references/legacy/context-window-management/SKILL.md

---
name: context-window-management
description: "Strategies for managing LLM context windows including summarization, trimming, routing, and avoiding context rot Use when: context window, token limit, context management, context engineering, long..."
risk: unknown
source: "vibeship-spawner-skills (Apache 2.0)"
date_added: "2026-02-27"
---

# Context Window Management

You're a context engineering specialist who has optimized LLM applications handling
millions of conversations. You've seen systems hit token limits, suffer context rot,
and lose critical information mid-dialogue.

You understand that context is a finite resource with diminishing returns. More tokens
doesn't mean better results—the art is in curating the right information. You know
the serial position effect, the lost-in-the-middle problem, and when to summarize
versus when to retrieve.

Your cor

## Capabilities

- context-engineering
- context-summarization
- context-trimming
- context-routing
- token-counting
- context-prioritization

## Patterns

### Tiered Context Strategy

Different strategies based on context size

### Serial Position Optimization

Place important content at start and end

### Intelligent Summarization

Summarize by importance, not just recency

## Anti-Patterns

### ❌ Naive Truncation

### ❌ Ignoring Token Costs

### ❌ One-Size-Fits-All

## Related Skills

Works well with: `rag-implementation`, `conversation-memory`, `prompt-caching`, `llm-npc-dialogue`

## When to Use
This skill is applicable to execute the workflow or actions described in the overview.

## Source: references/skills/agent-memory-systems/references/legacy/conversation-memory/SKILL.md

---
name: conversation-memory
description: "Persistent memory systems for LLM conversations including short-term, long-term, and entity-based memory Use when: conversation memory, remember, memory persistence, long-term memory, chat history."
risk: unknown
source: "vibeship-spawner-skills (Apache 2.0)"
date_added: "2026-02-27"
---

# Conversation Memory

You're a memory systems specialist who has built AI assistants that remember
users across months of interactions. You've implemented systems that know when
to remember, when to forget, and how to surface relevant memories.

You understand that memory is not just storage—it's about retrieval, relevance,
and context. You've seen systems that remember everything (and overwhelm context)
and systems that forget too much (frustrating users).

Your core principles:
1. Memory types differ—short-term, lo

## Capabilities

- short-term-memory
- long-term-memory
- entity-memory
- memory-persistence
- memory-retrieval
- memory-consolidation

## Patterns

### Tiered Memory System

Different memory tiers for different purposes

### Entity Memory

Store and update facts about entities

### Memory-Aware Prompting

Include relevant memories in prompts

## Anti-Patterns

### ❌ Remember Everything

### ❌ No Memory Retrieval

### ❌ Single Memory Store

## ⚠️ Sharp Edges

| Issue | Severity | Solution |
|-------|----------|----------|
| Memory store grows unbounded, system slows | high | // Implement memory lifecycle management |
| Retrieved memories not relevant to current query | high | // Intelligent memory retrieval |
| Memories from one user accessible to another | critical | // Strict user isolation in memory |

## Related Skills

Works well with: `context-window-management`, `rag-implementation`, `prompt-caching`, `llm-npc-dialogue`

## When to Use
This skill is applicable to execute the workflow or actions described in the overview.

## Source: references/skills/agent-memory-systems/references/legacy/data-structure-protocol/SKILL.md

---
name: data-structure-protocol
description: "Give agents persistent structural memory of a codebase — navigate dependencies, track public APIs, and understand why connections exist without re-reading the whole repo."
risk: safe
source: "https://github.com/k-kolomeitsev/data-structure-protocol"
date_added: "2026-02-27"
---

# Data Structure Protocol (DSP)

LLM coding agents lose context between tasks. On large codebases they spend most of their tokens on "orientation" — figuring out where things live, what depends on what, and what is safe to change. DSP solves this by externalizing the project's structural map into a persistent, queryable graph stored in a `.dsp/` directory next to the code.

DSP is NOT documentation for humans and NOT an AST dump. It captures three things: **meaning** (why an entity exists), **boundaries** (what it imports and exposes), and **reasons** (why each connection exists). This is enough for an agent to navigate, refactor, and generate code without loading the entire source tree into the context window.

## When to Use

Use this skill when:
- The project has a `.dsp/` directory (DSP is already set up)
- The user asks to set up DSP, bootstrap, or map a project's structure
- Creating, modifying, or deleting code files in a DSP-tracked project (to keep the graph updated)
- Navigating project structure, understanding dependencies, or finding specific modules
- The user mentions DSP, dsp-cli, `.dsp`, or structure mapping
- Performing impact analysis before a refactor or dependency replacement

## Core Concepts

### Code = graph

DSP models the codebase as a directed graph. Nodes are **entities**, edges are **imports** and **shared/exports**.

Two entity kinds exist:
- **Object**: any "thing" that isn't a function (module/file/class/config/resource/external dependency)
- **Function**: an exported function/method/handler/pipeline

### Identity by UID, not by file path

Every entity gets a stable UID: `obj-<8hex>` for objects, `func-<8hex>` for functions. File paths are attributes that can change; UIDs survive renames, moves, and reformatting.

For entities inside a file, the UID is anchored with a comment marker in source code:

```js
// @dsp func-7f3a9c12
export function calculateTotal(items) { ... }
```

```python
# @dsp obj-e5f6g7h8
class UserService:
```

### Every connection has a "why"

When an import is recorded, DSP stores a short reason explaining *why* that dependency exists. This lives in the `exports/` reverse index of the imported entity. A dependency graph without reasons tells you *what imports what*; reasons tell you **what is safe to change and who will break**.

### Storage format

Each entity gets a small directory under `.dsp/`:

```
.dsp/
├── TOC                        # ordered list of all entity UIDs from root
├── obj-a1b2c3d4/
│   ├── description            # source path, kind, purpose (1-3 sentences)
│   ├── imports                # UIDs this entity depends on (one per line)
│   ├── shared                 # UIDs of public API / exported entities
│   └── exports/               # reverse index: who imports this and why
│       ├── <importer_uid>     # file content = "why" text
│       └── <shared_uid>/
│           ├── description    # what is exported
│           └── <importer_uid> # why this specific export is imported
└── func-7f3a9c12/
    ├── description
    ├── imports
    └── exports/
```

Everything is plain text. Diffable. Reviewable. No database needed.

### Full import coverage

Every file or artifact that is imported anywhere must be represented in `.dsp` as an Object — code, images, styles, configs, JSON, wasm, everything. External dependencies (npm packages, stdlib, etc.) are recorded as `kind: external` but their internals are never analyzed.

## How It Works

### Initial Setup

The skill relies on a standalone Python CLI script `dsp-cli.py`. If it is missing from the project, download it:

```bash
curl -O https://raw.githubusercontent.com/k-kolomeitsev/data-structure-protocol/main/skills/data-structure-protocol/scripts/dsp-cli.py
```

Requires **Python 3.10+**. All commands use `python dsp-cli.py --root <project-root> <command>`.

### Bootstrap (initial mapping)

If `.dsp/` is empty, traverse the project from root entrypoint(s) via DFS on imports:

1. Identify root entrypoints (`package.json` main, framework entry, `main.py`, etc.)
2. Document the root file: `create-object`, `create-function` for each export, `create-shared`, `add-import` for all dependencies
3. Take the first non-external import, document it fully, descend into its imports
4. Backtrack when no unvisited local imports remain; continue until all reachable files are documented
5. External dependencies: `create-object --kind external`, add to TOC, but never descend into `node_modules`/`site-packages`/etc.

### Workflow Rules

- **Before changing code**: Find affected entities via `search`, `find-by-source`, or `read-toc`. Read their `description` and `imports` to understand context.
- **When creating a file/module**: Call `create-object`. For each exported function — `create-function` (with `--owner`). Register exports via `create-shared`.
- **When adding an import**: Call `add-import` with a brief `why`. For external deps — first `create-object --kind external` if the entity doesn't exist.
- **When removing import/export/file**: Call `remove-import`, `remove-shared`, `remove-entity`. Cascade cleanup is automatic.
- **When renaming/moving a file**: Call `move-entity`. UID does not change.
- **Don't touch DSP** if only internal implementation changed without affecting purpose or dependencies.

### Key Commands

| Category | Commands |
|----------|----------|
| **Create** | `init`, `create-object`, `create-function`, `create-shared`, `add-import` |
| **Update** | `update-description`, `update-import-why`, `move-entity` |
| **Delete** | `remove-import`, `remove-shared`, `remove-entity` |
| **Navigate** | `get-entity`, `get-children --depth N`, `get-parents --depth N`, `get-path`, `get-recipients`, `read-toc` |
| **Search** | `search <query>`, `find-by-source <path>` |
| **Diagnostics** | `detect-cycles`, `get-orphans`, `get-stats` |

### When to Update DSP

| Code Change | DSP Action |
|---|---|
| New file/module | `create-object` + `create-function` + `create-shared` + `add-import` |
| New import added | `add-import` (+ `create-object --kind external` if new dep) |
| Import removed | `remove-import` |
| Export added | `create-shared` (+ `create-function` if new) |
| Export removed | `remove-shared` |
| File renamed/moved | `move-entity` |
| File deleted | `remove-entity` |
| Purpose changed | `update-description` |
| Internal-only change | **No DSP update needed** |

## Examples

### Example 1: Setting up DSP and documenting a module

```bash
python dsp-cli.py --root . init

python dsp-cli.py --root . create-object "src/app.ts" "Main application entrypoint"
# Output: obj-a1b2c3d4

python dsp-cli.py --root . create-function "src/app.ts#start" "Starts the HTTP server" --owner obj-a1b2c3d4
# Output: func-7f3a9c12

python dsp-cli.py --root . create-shared obj-a1b2c3d4 func-7f3a9c12

python dsp-cli.py --root . add-import obj-a1b2c3d4 obj-deadbeef "HTTP routing"
```

### Example 2: Navigating the graph before making changes

```bash
python dsp-cli.py --root . search "authentication"
python dsp-cli.py --root . get-entity obj-a1b2c3d4
python dsp-cli.py --root . get-children obj-a1b2c3d4 --depth 2
python dsp-cli.py --root . get-recipients obj-a1b2c3d4
python dsp-cli.py --root . get-path obj-a1b2c3d4 func-7f3a9c12
```

### Example 3: Impact analysis before replacing a library

```bash
python dsp-cli.py --root . find-by-source "lodash"
# Output: obj-11223344

python dsp-cli.py --root . get-recipients obj-11223344
# Shows every module that imports lodash and WHY — lets you systematically replace it
```

## Best Practices

- ✅ **Do:** Update DSP immediately when creating new files, adding imports, or changing public APIs
- ✅ **Do:** Always add a meaningful `why` reason when recording an import — this is where most of DSP's value lives
- ✅ **Do:** Use `kind: external` for third-party libraries without analyzing their internals
- ✅ **Do:** Keep descriptions minimal (1-3 sentences about purpose, not implementation)
- ✅ **Do:** Treat `.dsp/` diffs like code diffs — review them, keep them accurate
- ❌ **Don't:** Touch `.dsp/` for internal-only changes that don't affect purpose or dependencies
- ❌ **Don't:** Change an entity's UID on rename/move (use `move-entity` instead)
- ❌ **Don't:** Create UIDs for every local variable or helper — only file-level Objects and public/shared entities

## Integration

This skill connects naturally to:
- **context-compression** — DSP reduces the need for compression by providing targeted retrieval instead of loading everything
- **context-optimization** — DSP is a structural optimization: agents pull minimal "context bundles" instead of raw source
- **architecture** — DSP captures architectural boundaries (imports/exports) that feed system design decisions

## References

- **Full architecture specification**: [ARCHITECTURE.md](https://github.com/k-kolomeitsev/data-structure-protocol/blob/main/ARCHITECTURE.md)
- **CLI source + reference docs**: [skills/data-structure-protocol](https://github.com/k-kolomeitsev/data-structure-protocol/tree/main/skills/data-structure-protocol)
- **Introduction article**: [article.md](https://github.com/k-kolomeitsev/data-structure-protocol/blob/main/article.md)

## Source: references/skills/agent-memory-systems/references/legacy/filesystem-context/SKILL.md

---
name: filesystem-context
description: Use for file-based context management, dynamic context discovery, and reducing context window bloat. Offload context to files for just-in-time loading.
risk: unknown
source: community
---

# Filesystem-Based Context Engineering

The filesystem provides a single interface through which agents can flexibly store, retrieve, and update an effectively unlimited amount of context. This pattern addresses the fundamental constraint that context windows are limited while tasks often require more information than fits in a single window.

The core insight is that files enable dynamic context discovery: agents pull relevant context on demand rather than carrying everything in the context window. This contrasts with static context, which is always included regardless of relevance.

## When to Activate

Activate this skill when:
- Tool outputs are bloating the context window
- Agents need to persist state across long trajectories
- Sub-agents must share information without direct message passing
- Tasks require more context than fits in the window
- Building agents that learn and update their own instructions
- Implementing scratch pads for intermediate results
- Terminal outputs or logs need to be accessible to agents

## Core Concepts

Context engineering can fail in four predictable ways. First, when the context an agent needs is not in the total available context. Second, when retrieved context fails to encapsulate needed context. Third, when retrieved context far exceeds needed context, wasting tokens and degrading performance. Fourth, when agents cannot discover niche information buried in many files.

The filesystem addresses these failures by providing a persistent layer where agents write once and read selectively, offloading bulk content while preserving the ability to retrieve specific information through search tools.

## Detailed Topics

### The Static vs Dynamic Context Trade-off

**Static Context**
Static context is always included in the prompt: system instructions, tool definitions, and critical rules. Static context consumes tokens regardless of task relevance. As agents accumulate more capabilities (tools, skills, instructions), static context grows and crowds out space for dynamic information.

**Dynamic Context Discovery**
Dynamic context is loaded on-demand when relevant to the current task. The agent receives minimal static pointers (names, descriptions, file paths) and uses search tools to load full content when needed.

Dynamic discovery is more token-efficient because only necessary data enters the context window. It can also improve response quality by reducing potentially confusing or contradictory information.

The trade-off: dynamic discovery requires the model to correctly identify when to load additional context. This works well with current frontier models but may fail with less capable models that do not recognize when they need more information.

### Pattern 1: Filesystem as Scratch Pad

**The Problem**
Tool calls can return massive outputs. A web search may return 10k tokens of raw content. A database query may return hundreds of rows. If this content enters the message history, it remains for the entire conversation, inflating token costs and potentially degrading attention to more relevant information.

**The Solution**
Write large tool outputs to files instead of returning them directly to the context. The agent then uses targeted retrieval (grep, line-specific reads) to extract only the relevant portions.

**Implementation**
```python
def handle_tool_output(output: str, threshold: int = 2000) -> str:
    if len(output) < threshold:
        return output
    
    # Write to scratch pad
    file_path = f"scratch/{tool_name}_{timestamp}.txt"
    write_file(file_path, output)
    
    # Return reference instead of content
    key_summary = extract_summary(output, max_tokens=200)
    return f"[Output written to {file_path}. Summary: {key_summary}]"
```

The agent can then use `grep` to search for specific patterns or `read_file` with line ranges to retrieve targeted sections.

**Benefits**
- Reduces token accumulation over long conversations
- Preserves full output for later reference
- Enables targeted retrieval instead of carrying everything

### Pattern 2: Plan Persistence

**The Problem**
Long-horizon tasks require agents to make plans and follow them. But as conversations extend, plans can fall out of attention or be lost to summarization. The agent loses track of what it was supposed to do.

**The Solution**
Write plans to the filesystem. The agent can re-read its plan at any point, reminding itself of the current objective and progress. This is sometimes called "manipulating attention through recitation."

**Implementation**
Store plans in structured format:
```yaml
# scratch/current_plan.yaml
objective: "Refactor authentication module"
status: in_progress
steps:
  - id: 1
    description: "Audit current auth endpoints"
    status: completed
  - id: 2
    description: "Design new token validation flow"
    status: in_progress
  - id: 3
    description: "Implement and test changes"
    status: pending
```

The agent reads this file at the start of each turn or when it needs to re-orient.

### Pattern 3: Sub-Agent Communication via Filesystem

**The Problem**
In multi-agent systems, sub-agents typically report findings to a coordinator agent through message passing. This creates a "game of telephone" where information degrades through summarization at each hop.

**The Solution**
Sub-agents write their findings directly to the filesystem. The coordinator reads these files directly, bypassing intermediate message passing. This preserves fidelity and reduces context accumulation in the coordinator.

**Implementation**
```
workspace/
  agents/
    research_agent/
      findings.md        # Research agent writes here
      sources.jsonl      # Source tracking
    code_agent/
      changes.md         # Code agent writes here
      test_results.txt   # Test output
  coordinator/
    synthesis.md         # Coordinator reads agent outputs, writes synthesis
```

Each agent operates in relative isolation but shares state through the filesystem.

### Pattern 4: Dynamic Skill Loading

**The Problem**
Agents may have many skills or instruction sets, but most are irrelevant to any given task. Stuffing all instructions into the system prompt wastes tokens and can confuse the model with contradictory or irrelevant guidance.

**The Solution**
Store skills as files. Include only skill names and brief descriptions in static context. The agent uses search tools to load relevant skill content when the task requires it.

**Implementation**
Static context includes:
```
Available skills (load with read_file when relevant):
- database-optimization: Query tuning and indexing strategies
- api-design: REST/GraphQL best practices
- testing-strategies: Unit, integration, and e2e testing patterns
```

Agent loads `skills/database-optimization/SKILL.md` only when working on database tasks.

### Pattern 5: Terminal and Log Persistence

**The Problem**
Terminal output from long-running processes accumulates rapidly. Copying and pasting output into agent input is manual and inefficient.

**The Solution**
Sync terminal output to files automatically. The agent can then grep for relevant sections (error messages, specific commands) without loading entire terminal histories.

**Implementation**
Terminal sessions are persisted as files:
```
terminals/
  1.txt    # Terminal session 1 output
  2.txt    # Terminal session 2 output
```

Agents query with targeted grep:
```bash
grep -A 5 "error" terminals/1.txt
```

### Pattern 6: Learning Through Self-Modification

**The Problem**
Agents often lack context that users provide implicitly or explicitly during interactions. Traditionally, this requires manual system prompt updates between sessions.

**The Solution**
Agents write learned information to their own instruction files. Subsequent sessions load these files, incorporating learned context automatically.

**Implementation**
After user provides preference:
```python
def remember_preference(key: str, value: str):
    preferences_file = "agent/user_preferences.yaml"
    prefs = load_yaml(preferences_file)
    prefs[key] = value
    write_yaml(preferences_file, prefs)
```

Subsequent sessions include a step to load user preferences if the file exists.

**Caution**
This pattern is still emerging. Self-modification requires careful guardrails to prevent agents from accumulating incorrect or contradictory instructions over time.

### Filesystem Search Techniques

Models are specifically trained to understand filesystem traversal. The combination of `ls`, `glob`, `grep`, and `read_file` with line ranges provides powerful context discovery:

- `ls` / `list_dir`: Discover directory structure
- `glob`: Find files matching patterns (e.g., `**/*.py`)
- `grep`: Search file contents for patterns, returns matching lines
- `read_file` with ranges: Read specific line ranges without loading entire files

This combination often outperforms semantic search for technical content (code, API docs) where semantic meaning is sparse but structural patterns are clear.

Semantic search and filesystem search work well together: semantic search for conceptual queries, filesystem search for structural and exact-match queries.

## Practical Guidance

### When to Use Filesystem Context

**Use filesystem patterns when:**
- Tool outputs exceed 2000 tokens
- Tasks span multiple conversation turns
- Multiple agents need to share state
- Skills or instructions exceed what fits comfortably in system prompt
- Logs or terminal output need selective querying

**Avoid filesystem patterns when:**
- Tasks complete in single turns
- Context fits comfortably in window
- Latency is critical (file I/O adds overhead)
- Simple model incapable of filesystem tool use

### File Organization

Structure files for discoverability:
```
project/
  scratch/           # Temporary working files
    tool_outputs/    # Large tool results
    plans/           # Active plans and checklists
  memory/            # Persistent learned information
    preferences.yaml # User preferences
    patterns.md      # Learned patterns
  skills/            # Loadable skill definitions
  agents/            # Sub-agent workspaces
```

Use consistent naming conventions. Include timestamps or IDs in scratch files for disambiguation.

### Token Accounting

Track where tokens originate:
- Measure static vs dynamic context ratio
- Monitor tool output sizes before and after offloading
- Track how often dynamic context is actually loaded

Optimize based on measurements, not assumptions.

## Examples

**Example 1: Tool Output Offloading**
```
Input: Web search returns 8000 tokens
Before: 8000 tokens added to message history
After: 
  - Write to scratch/search_results_001.txt
  - Return: "[Results in scratch/search_results_001.txt. Key finding: API rate limit is 1000 req/min]"
  - Agent greps file when needing specific details
Result: ~100 tokens in context, 8000 tokens accessible on demand
```

**Example 2: Dynamic Skill Loading**
```
Input: User asks about database indexing
Static context: "database-optimization: Query tuning and indexing"
Agent action: read_file("skills/database-optimization/SKILL.md")
Result: Full skill loaded only when relevant
```

**Example 3: Chat History as File Reference**
```
Trigger: Context window limit reached, summarization required
Action: 
  1. Write full history to history/session_001.txt
  2. Generate summary for new context window
  3. Include reference: "Full history in history/session_001.txt"
Result: Agent can search history file to recover details lost in summarization
```

## Guidelines

1. Write large outputs to files; return summaries and references to context
2. Store plans and state in structured files for re-reading
3. Use sub-agent file workspaces instead of message chains
4. Load skills dynamically rather than stuffing all into system prompt
5. Persist terminal and log output as searchable files
6. Combine grep/glob with semantic search for comprehensive discovery
7. Organize files for agent discoverability with clear naming
8. Measure token savings to validate filesystem patterns are effective
9. Implement cleanup for scratch files to prevent unbounded growth
10. Guard self-modification patterns with validation

## Integration

This skill connects to:

- context-optimization - Filesystem offloading is a form of observation masking
- memory-systems - Filesystem-as-memory is a simple memory layer
- multi-agent-patterns - Sub-agent file workspaces enable isolation
- context-compression - File references enable lossless "compression"
- tool-design - Tools should return file references for large outputs

## References

Internal reference:
- Implementation Patterns - Detailed pattern implementations

Related skills in this collection:
- context-optimization - Token reduction techniques
- memory-systems - Persistent storage patterns
- multi-agent-patterns - Agent coordination

External resources:
- LangChain Deep Agents: How agents can use filesystems for context engineering
- Cursor: Dynamic context discovery patterns
- Anthropic: Agent Skills specification

---

## Skill Metadata

**Created**: 2026-01-07
**Last Updated**: 2026-01-07
**Author**: Agent Skills for Context Engineering Contributors
**Version**: 1.0.0


## Source: references/skills/agent-memory-systems/references/legacy/hierarchical-agent-memory/SKILL.md

---
name: hierarchical-agent-memory
description: "Scoped AGENT_CONTEXT.md memory system that reduces context token spend. Creates directory-level context files, tracks savings via dashboard, and routes agents to the right sub-context."
risk: safe
source: "https://github.com/kromahlusenii-ops/ham"
date_added: "2026-02-27"
---

# Hierarchical Agent Memory (HAM)

Scoped memory system that gives AI coding agents a cheat sheet for each directory instead of re-reading your entire project every prompt. Root AGENT_CONTEXT.md holds global context (~200 tokens), subdirectory AGENT_CONTEXT.md files hold scoped context (~250 tokens each), and a `.memory/` layer stores decisions, patterns, and an inbox for unconfirmed inferences.

## When to Use This Skill

- Use when you want to reduce input token costs across AI coding assistant sessions
- Use when your project has 3+ directories and the agent keeps re-reading the same files
- Use when you want directory-scoped context instead of one monolithic AGENT_CONTEXT.md
- Use when you want a dashboard to visualize token savings, session history, and context health
- Use when setting up a new project and want structured agent memory from day one

## How It Works

### Step 1: Setup ("go ham")

Auto-detects your project platform and maturity, then generates the memory structure:

```
project/
├── AGENT_CONTEXT.md              # Root context (~200 tokens)
├── .memory/
│   ├── decisions.md       # Architecture Decision Records
│   ├── patterns.md        # Reusable patterns
│   ├── inbox.md           # Inferred items awaiting confirmation
│   └── audit-log.md       # Audit history
└── src/
    ├── api/AGENT_CONTEXT.md      # Scoped context for api/
    ├── components/AGENT_CONTEXT.md
    └── lib/AGENT_CONTEXT.md
```

### Step 2: Context Routing

The root AGENT_CONTEXT.md includes a routing section that tells the agent exactly which sub-context to load:

```markdown
## Context Routing

→ api: src/api/AGENT_CONTEXT.md
→ components: src/components/AGENT_CONTEXT.md
→ lib: src/lib/AGENT_CONTEXT.md
```

The agent reads root, then immediately loads the relevant subdirectory context — no guessing.

### Step 3: Dashboard ("ham dashboard")

Launches a web dashboard at localhost:7777 that visualizes:
- Token savings (HAM-on vs HAM-off sessions)
- Daily token and cost trends
- Per-directory session breakdown
- Context file health (missing/stale/inherited AGENT_CONTEXT.md coverage)
- Routing compliance (how often the agent follows the routing map)
- Carbon/energy estimates

## Commands

| Trigger | What it does |
|---|---|
| `go ham` | Set up HAM — auto-detect platform, generate AGENT_CONTEXT.md files |
| `ham savings` | Show token and cost savings report |
| `ham dashboard` | Launch the interactive web dashboard |
| `ham audit` | Health check on memory files |
| `ham insights` | Generate actionable insights from session data |
| `ham route` | Add/update Context Routing section in root AGENT_CONTEXT.md |
| `ham carbon` | Show energy and carbon efficiency data |

## Examples

### Example 1: First-time setup

```
User: go ham

Agent: HAM setup complete. Created 8 files.
  - AGENT_CONTEXT.md (root)
  - .memory/decisions.md
  - .memory/patterns.md
  - .memory/inbox.md
  - src/api/AGENT_CONTEXT.md
  - src/components/AGENT_CONTEXT.md
  - src/lib/AGENT_CONTEXT.md
  - src/utils/AGENT_CONTEXT.md

Baseline captured in .memory/baseline.json
Run "HAM savings" to see your token and cost savings.
```

### Example 2: Checking savings

```
User: ham savings

Agent:
  Before HAM: ~7,500 tokens/prompt
  After HAM:    ~450 tokens/prompt
  Savings:    7,050 tokens (94%)

  Monthly projection (1,500 prompts):
    Sonnet: ~$31.73 saved
    Opus:   ~$158.63 saved
```

## Best Practices

- Keep root AGENT_CONTEXT.md under 60 lines / 250 tokens
- Keep subdirectory AGENT_CONTEXT.md files under 75 lines each
- Run `ham audit` every 2 weeks to catch stale or missing context files
- Use `ham route` after adding new directories to keep routing current
- Review `.memory/inbox.md` periodically — confirm or reject inferred items

## Limitations

- Token estimates use ~4 chars = 1 token approximation, not a real tokenizer
- Baseline savings comparisons are estimates based on typical agent behavior
- Dashboard requires Node.js 18+ and reads session data from `tool-specific config pathsprojects/`
- Context routing detection relies on AGENT_CONTEXT.md read order in session JSONL files
- Does not auto-update subdirectory AGENT_CONTEXT.md content — you maintain those manually or via `ham audit`
- Carbon estimates use regional grid averages, not real-time energy data

## Related Skills

- `agent-memory-systems` — general agent memory architecture patterns
- `agent-memory-mcp` — MCP-based memory integration

## Source: references/skills/agent-memory-systems/references/legacy/memory-systems/SKILL.md

---
name: memory-systems
description: "Design short-term, long-term, and graph-based memory architectures"
risk: safe
source: "https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/tree/main/skills/memory-systems"
date_added: "2026-02-27"
---

## When to Use This Skill

Design short-term, long-term, and graph-based memory architectures

Use this skill when working with design short-term, long-term, and graph-based memory architectures.
# Memory System Design

Memory provides the persistence layer that allows agents to maintain continuity across sessions and reason over accumulated knowledge. Simple agents rely entirely on context for memory, losing all state when sessions end. Sophisticated agents implement layered memory architectures that balance immediate context needs with long-term knowledge retention. The evolution from vector stores to knowledge graphs to temporal knowledge graphs represents increasing investment in structured memory for improved retrieval and reasoning.

## When to Activate

Activate this skill when:
- Building agents that must persist across sessions
- Needing to maintain entity consistency across conversations
- Implementing reasoning over accumulated knowledge
- Designing systems that learn from past interactions
- Creating knowledge bases that grow over time
- Building temporal-aware systems that track state changes

## Core Concepts

Memory exists on a spectrum from immediate context to permanent storage. At one extreme, working memory in the context window provides zero-latency access but vanishes when sessions end. At the other extreme, permanent storage persists indefinitely but requires retrieval to enter context.

Simple vector stores lack relationship and temporal structure. Knowledge graphs preserve relationships for reasoning. Temporal knowledge graphs add validity periods for time-aware queries. Implementation choices depend on query complexity, infrastructure constraints, and accuracy requirements.

## Detailed Topics

### Memory Architecture Fundamentals

**The Context-Memory Spectrum**
Memory exists on a spectrum from immediate context to permanent storage. At one extreme, working memory in the context window provides zero-latency access but vanishes when sessions end. At the other extreme, permanent storage persists indefinitely but requires retrieval to enter context. Effective architectures use multiple layers along this spectrum.

The spectrum includes working memory (context window, zero latency, volatile), short-term memory (session-persistent, searchable, volatile), long-term memory (cross-session persistent, structured, semi-permanent), and permanent memory (archival, queryable, permanent). Each layer has different latency, capacity, and persistence characteristics.

**Why Simple Vector Stores Fall Short**
Vector RAG provides semantic retrieval by embedding queries and documents in a shared embedding space. Similarity search retrieves the most semantically similar documents. This works well for document retrieval but lacks structure for agent memory.

Vector stores lose relationship information. If an agent learns that "Customer X purchased Product Y on Date Z," a vector store can retrieve this fact if asked directly. But it cannot answer "What products did customers who purchased Product Y also buy?" because relationship structure is not preserved.

Vector stores also struggle with temporal validity. Facts change over time, but vector stores provide no mechanism to distinguish "current fact" from "outdated fact" except through explicit metadata and filtering.

**The Move to Graph-Based Memory**
Knowledge graphs preserve relationships between entities. Instead of isolated document chunks, graphs encode that Entity A has Relationship R to Entity B. This enables queries that traverse relationships rather than just similarity.

Temporal knowledge graphs add validity periods to facts. Each fact has a "valid from" and optionally "valid until" timestamp. This enables time-travel queries that reconstruct knowledge at specific points in time.

**Benchmark Performance Comparison**
The Deep Memory Retrieval (DMR) benchmark provides concrete performance data across memory architectures:

| Memory System | DMR Accuracy | Retrieval Latency | Notes |
|---------------|--------------|-------------------|-------|
| Zep (Temporal KG) | 94.8% | 2.58s | Best accuracy, fast retrieval |
| MemGPT | 93.4% | Variable | Good general performance |
| GraphRAG | ~75-85% | Variable | 20-35% gains over baseline RAG |
| Vector RAG | ~60-70% | Fast | Loses relationship structure |
| Recursive Summarization | 35.3% | Low | Severe information loss |

Zep demonstrated 90% reduction in retrieval latency compared to full-context baselines (2.58s vs 28.9s for GPT-5.2). This efficiency comes from retrieving only relevant subgraphs rather than entire context history.

GraphRAG achieves approximately 20-35% accuracy gains over baseline RAG in complex reasoning tasks and reduces hallucination by up to 30% through community-based summarization.

### Memory Layer Architecture

**Layer 1: Working Memory**
Working memory is the context window itself. It provides immediate access to information currently being processed but has limited capacity and vanishes when sessions end.

Working memory usage patterns include scratchpad calculations where agents track intermediate results, conversation history that preserves dialogue for current task, current task state that tracks progress on active objectives, and active retrieved documents that hold information currently being used.

Optimize working memory by keeping only active information, summarizing completed work before it falls out of attention, and using attention-favored positions for critical information.

**Layer 2: Short-Term Memory**
Short-term memory persists across the current session but not across sessions. It provides search and retrieval capabilities without the latency of permanent storage.

Common implementations include session-scoped databases that persist until session end, file-system storage in designated session directories, and in-memory caches keyed by session ID.

Short-term memory use cases include tracking conversation state across turns without stuffing context, storing intermediate results from tool calls that may be needed later, maintaining task checklists and progress tracking, and caching retrieved information within sessions.

**Layer 3: Long-Term Memory**
Long-term memory persists across sessions indefinitely. It enables agents to learn from past interactions and build knowledge over time.

Long-term memory implementations range from simple key-value stores to sophisticated graph databases. The choice depends on complexity of relationships to model, query patterns required, and acceptable infrastructure complexity.

Long-term memory use cases include learning user preferences across sessions, building domain knowledge bases that grow over time, maintaining entity registries with relationship history, and storing successful patterns that can be reused.

**Layer 4: Entity Memory**
Entity memory specifically tracks information about entities (people, places, concepts, objects) to maintain consistency. This creates a rudimentary knowledge graph where entities are recognized across multiple interactions.

Entity memory maintains entity identity by tracking that "John Doe" mentioned in one conversation is the same person in another. It maintains entity properties by storing facts discovered about entities over time. It maintains entity relationships by tracking relationships between entities as they are discovered.

**Layer 5: Temporal Knowledge Graphs**
Temporal knowledge graphs extend entity memory with explicit validity periods. Facts are not just true or false but true during specific time ranges.

This enables queries like "What was the user's address on Date X?" by retrieving facts valid during that date range. It prevents context clash when outdated information contradicts new data. It enables temporal reasoning about how entities changed over time.

### Memory Implementation Patterns

**Pattern 1: File-System-as-Memory**
The file system itself can serve as a memory layer. This pattern is simple, requires no additional infrastructure, and enables the same just-in-time loading that makes file-system-based context effective.

Implementation uses the file system hierarchy for organization. Use naming conventions that convey meaning. Store facts in structured formats (JSON, YAML). Use timestamps in filenames or metadata for temporal tracking.

Advantages: Simplicity, transparency, portability.
Disadvantages: No semantic search, no relationship tracking, manual organization required.

**Pattern 2: Vector RAG with Metadata**
Vector stores enhanced with rich metadata provide semantic search with filtering capabilities.

Implementation embeds facts or documents and stores with metadata including entity tags, temporal validity, source attribution, and confidence scores. Query includes metadata filters alongside semantic search.

**Pattern 3: Knowledge Graph**
Knowledge graphs explicitly model entities and relationships. Implementation defines entity types and relationship types, uses graph database or property graph storage, and maintains indexes for common query patterns.

**Pattern 4: Temporal Knowledge Graph**
Temporal knowledge graphs add validity periods to facts, enabling time-travel queries and preventing context clash from outdated information.

### Memory Retrieval Patterns

**Semantic Retrieval**
Retrieve memories semantically similar to current query using embedding similarity search.

**Entity-Based Retrieval**
Retrieve all memories related to specific entities by traversing graph relationships.

**Temporal Retrieval**
Retrieve memories valid at specific time or within time range using validity period filters.

### Memory Consolidation

Memories accumulate over time and require consolidation to prevent unbounded growth and remove outdated information.

**Consolidation Triggers**
Trigger consolidation after significant memory accumulation, when retrieval returns too many outdated results, periodically on a schedule, or when explicit consolidation is requested.

**Consolidation Process**
Identify outdated facts, merge related facts, update validity periods, archive or delete obsolete facts, and rebuild indexes.

## Practical Guidance

### Integration with Context

Memories must integrate with context systems to be useful. Use just-in-time memory loading to retrieve relevant memories when needed. Use strategic injection to place memories in attention-favored positions.

### Memory System Selection

Choose memory architecture based on requirements:
- Simple persistence needs: File-system memory
- Semantic search needs: Vector RAG with metadata
- Relationship reasoning needs: Knowledge graph
- Temporal validity needs: Temporal knowledge graph

## Examples

**Example 1: Entity Tracking**
```python
# Track entity across conversations
def remember_entity(entity_id, properties):
    memory.store({
        "type": "entity",
        "id": entity_id,
        "properties": properties,
        "last_updated": now()
    })

def get_entity(entity_id):
    return memory.retrieve_entity(entity_id)
```

**Example 2: Temporal Query**
```python
# What was the user's address on January 15, 2024?
def query_address_at_time(user_id, query_time):
    return temporal_graph.query("""
        MATCH (user)-[r:LIVES_AT]->(address)
        WHERE user.id = $user_id
        AND r.valid_from <= $query_time
        AND (r.valid_until IS NULL OR r.valid_until > $query_time)
        RETURN address
    """, {"user_id": user_id, "query_time": query_time})
```

## Guidelines

1. Match memory architecture to query requirements
2. Implement progressive disclosure for memory access
3. Use temporal validity to prevent outdated information conflicts
4. Consolidate memories periodically to prevent unbounded growth
5. Design for memory retrieval failures gracefully
6. Consider privacy implications of persistent memory
7. Implement backup and recovery for critical memories
8. Monitor memory growth and performance over time

## Integration

This skill builds on context-fundamentals. It connects to:

- multi-agent-patterns - Shared memory across agents
- context-optimization - Memory-based context loading
- evaluation - Evaluating memory quality

## References

Internal reference:
- Implementation Reference - Detailed implementation patterns

Related skills in this collection:
- context-fundamentals - Context basics
- multi-agent-patterns - Cross-agent memory

External resources:
- Graph database documentation (Neo4j, etc.)
- Vector store documentation (Pinecone, Weaviate, etc.)
- Research on knowledge graphs and reasoning

---

## Skill Metadata

**Created**: 2025-12-20
**Last Updated**: 2025-12-20
**Author**: Agent Skills for Context Engineering Contributors
**Version**: 1.0.0

