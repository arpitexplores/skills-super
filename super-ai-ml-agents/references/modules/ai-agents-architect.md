## Module: Ai Agents Architect
---
name: ai-agents-architect
description: "Expert in designing and building autonomous AI agents. Masters tool use, memory systems, planning strategies, and multi-agent orchestration. Use when: build agent, AI agent, autonomous agent, tool ..."
risk: unknown
source: "vibeship-spawner-skills (Apache 2.0)"
date_added: "2026-02-27"
---

# AI Agents Architect

**Role**: AI Agent Systems Architect

I build AI systems that can act autonomously while remaining controllable.
I understand that agents fail in unexpected ways - I design for graceful
degradation and clear failure modes. I balance autonomy with oversight,
knowing when an agent should ask for help vs proceed independently.

## Capabilities

- Agent architecture design
- Tool and function calling
- Agent memory systems
- Planning and reasoning strategies
- Multi-agent orchestration
- Agent evaluation and debugging

## Requirements

- LLM API usage
- Understanding of function calling
- Basic prompt engineering

## Patterns

### ReAct Loop

Reason-Act-Observe cycle for step-by-step execution

```javascript
- Thought: reason about what to do next
- Action: select and invoke a tool
- Observation: process tool result
- Repeat until task complete or stuck
- Include max iteration limits
```

### Plan-and-Execute

Plan first, then execute steps

```javascript
- Planning phase: decompose task into steps
- Execution phase: execute each step
- Replanning: adjust plan based on results
- Separate planner and executor models possible
```

### Tool Registry

Dynamic tool discovery and management

```javascript
- Register tools with schema and examples
- Tool selector picks relevant tools for task
- Lazy loading for expensive tools
- Usage tracking for optimization
```

## Anti-Patterns

### ❌ Unlimited Autonomy

### ❌ Tool Overload

### ❌ Memory Hoarding

## ⚠️ Sharp Edges

| Issue | Severity | Solution |
|-------|----------|----------|
| Agent loops without iteration limits | critical | Always set limits: |
| Vague or incomplete tool descriptions | high | Write complete tool specs: |
| Tool errors not surfaced to agent | high | Explicit error handling: |
| Storing everything in agent memory | medium | Selective memory: |
| Agent has too many tools | medium | Curate tools per task: |
| Using multiple agents when one would work | medium | Justify multi-agent: |
| Agent internals not logged or traceable | medium | Implement tracing: |
| Fragile parsing of agent outputs | medium | Robust output handling: |
| Agent workflows lost on crash or restart | high | Use durable execution (e.g. DBOS) to persist workflow state: |

## Related Skills

Works well with: `rag-engineer`, `prompt-engineer`, `backend`, `mcp-builder`, `dbos-python`

## When to Use
This skill is applicable to execute the workflow or actions described in the overview.

---

## Imported Reference

---
name: ai-agent-development
description: "AI agent development workflow for building autonomous agents, multi-agent systems, and agent orchestration with CrewAI, LangGraph, and custom agents."
category: granular-workflow-bundle
risk: safe
source: personal
date_added: "2026-02-27"
---

# AI Agent Development Workflow

## Overview

Specialized workflow for building AI agents including single autonomous agents, multi-agent systems, agent orchestration, tool integration, and human-in-the-loop patterns.

## When to Use This Workflow

Use this workflow when:
- Building autonomous AI agents
- Creating multi-agent systems
- Implementing agent orchestration
- Adding tool integration to agents
- Setting up agent memory

## Workflow Phases

### Phase 1: Agent Design

#### Skills to Invoke
- `ai-agents-architect` - Agent architecture
- `autonomous-agents` - Autonomous patterns

#### Actions
1. Define agent purpose
2. Design agent capabilities
3. Plan tool integration
4. Design memory system
5. Define success metrics

#### Copy-Paste Prompts
```
Use @ai-agents-architect to design AI agent architecture
```

### Phase 2: Single Agent Implementation

#### Skills to Invoke
- `autonomous-agent-patterns` - Agent patterns
- `autonomous-agents` - Autonomous agents

#### Actions
1. Choose agent framework
2. Implement agent logic
3. Add tool integration
4. Configure memory
5. Test agent behavior

#### Copy-Paste Prompts
```
Use @autonomous-agent-patterns to implement single agent
```

### Phase 3: Multi-Agent System

#### Skills to Invoke
- `crewai` - CrewAI framework
- `multi-agent-patterns` - Multi-agent patterns

#### Actions
1. Define agent roles
2. Set up agent communication
3. Configure orchestration
4. Implement task delegation
5. Test coordination

#### Copy-Paste Prompts
```
Use @crewai to build multi-agent system with roles
```

### Phase 4: Agent Orchestration

#### Skills to Invoke
- `langgraph` - LangGraph orchestration
- `workflow-orchestration-patterns` - Orchestration

#### Actions
1. Design workflow graph
2. Implement state management
3. Add conditional branches
4. Configure persistence
5. Test workflows

#### Copy-Paste Prompts
```
Use @langgraph to create stateful agent workflows
```

### Phase 5: Tool Integration

#### Skills to Invoke
- `agent-tool-builder` - Tool building
- `tool-design` - Tool design

#### Actions
1. Identify tool needs
2. Design tool interfaces
3. Implement tools
4. Add error handling
5. Test tool usage

#### Copy-Paste Prompts
```
Use @agent-tool-builder to create agent tools
```

### Phase 6: Memory Systems

#### Skills to Invoke
- `agent-memory-systems` - Memory architecture
- `conversation-memory` - Conversation memory

#### Actions
1. Design memory structure
2. Implement short-term memory
3. Set up long-term memory
4. Add entity memory
5. Test memory retrieval

#### Copy-Paste Prompts
```
Use @agent-memory-systems to implement agent memory
```

### Phase 7: Evaluation

#### Skills to Invoke
- `agent-evaluation` - Agent evaluation
- `evaluation` - AI evaluation

#### Actions
1. Define evaluation criteria
2. Create test scenarios
3. Measure agent performance
4. Test edge cases
5. Iterate improvements

#### Copy-Paste Prompts
```
Use @agent-evaluation to evaluate agent performance
```

## Agent Architecture

```
User Input -> Planner -> Agent -> Tools -> Memory -> Response
              |          |        |        |
         Decompose   LLM Core  Actions  Short/Long-term
```

## Quality Gates

- [ ] Agent logic working
- [ ] Tools integrated
- [ ] Memory functional
- [ ] Orchestration tested
- [ ] Evaluation passing

## Related Workflow Bundles

- `ai-ml` - AI/ML development
- `rag-implementation` - RAG systems
- `workflow-automation` - Workflow patterns

---

## Imported Reference

---
name: autonomous-agents
description: "Autonomous agents are AI systems that can independently decompose goals, plan actions, execute tools, and self-correct without constant human guidance. The challenge isn't making them capable - it'..."
risk: unknown
source: "vibeship-spawner-skills (Apache 2.0)"
date_added: "2026-02-27"
---

# Autonomous Agents

You are an agent architect who has learned the hard lessons of autonomous AI.
You've seen the gap between impressive demos and production disasters. You know
that a 95% success rate per step means only 60% by step 10.

Your core insight: Autonomy is earned, not granted. Start with heavily
constrained agents that do one thing reliably. Add autonomy only as you prove
reliability. The best agents look less impressive but work consistently.

You push for guardrails before capabilities, logging befor

## Capabilities

- autonomous-agents
- agent-loops
- goal-decomposition
- self-correction
- reflection-patterns
- react-pattern
- plan-execute
- agent-reliability
- agent-guardrails

## Patterns

### ReAct Agent Loop

Alternating reasoning and action steps

### Plan-Execute Pattern

Separate planning phase from execution

### Reflection Pattern

Self-evaluation and iterative improvement

## Anti-Patterns

### ❌ Unbounded Autonomy

### ❌ Trusting Agent Outputs

### ❌ General-Purpose Autonomy

## ⚠️ Sharp Edges

| Issue | Severity | Solution |
|-------|----------|----------|
| Issue | critical | ## Reduce step count |
| Issue | critical | ## Set hard cost limits |
| Issue | critical | ## Test at scale before production |
| Issue | high | ## Validate against ground truth |
| Issue | high | ## Build robust API clients |
| Issue | high | ## Least privilege principle |
| Issue | medium | ## Track context usage |
| Issue | medium | ## Structured logging |

## Related Skills

Works well with: `agent-tool-builder`, `agent-memory-systems`, `multi-agent-orchestration`, `agent-evaluation`

## When to Use
This skill is applicable to execute the workflow or actions described in the overview.

---

## Imported Reference

---
name: autonomous-agent-patterns
description: "Design patterns for building autonomous coding agents. Covers tool integration, permission systems, browser automation, and human-in-the-loop workflows. Use when building AI agents, designing tool ..."
risk: unknown
source: community
date_added: "2026-02-27"
---

# 🕹️ Autonomous Agent Patterns

> Design patterns for building autonomous coding agents, inspired by autonomous coding agents.

## When to Use This Skill

Use this skill when:

- Building autonomous AI agents
- Designing tool/function calling APIs
- Implementing permission and approval systems
- Creating browser automation for agents
- Designing human-in-the-loop workflows

---

## 1. Core Agent Architecture

### 1.1 Agent Loop

```
┌─────────────────────────────────────────────────────────────┐
│                     AGENT LOOP                               │
│                                                              │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐              │
│  │  Think   │───▶│  Decide  │───▶│   Act    │              │
│  │ (Reason) │    │ (Plan)   │    │ (Execute)│              │
│  └──────────┘    └──────────┘    └──────────┘              │
│       ▲                               │                     │
│       │         ┌──────────┐          │                     │
│       └─────────│ Observe  │◀─────────┘                     │
│                 │ (Result) │                                │
│                 └──────────┘                                │
└─────────────────────────────────────────────────────────────┘
```

```python
class AgentLoop:
    def __init__(self, llm, tools, max_iterations=50):
        self.llm = llm
        self.tools = {t.name: t for t in tools}
        self.max_iterations = max_iterations
        self.history = []

    def run(self, task: str) -> str:
        self.history.append({"role": "user", "content": task})

        for i in range(self.max_iterations):
            # Think: Get LLM response with tool options
            response = self.llm.chat(
                messages=self.history,
                tools=self._format_tools(),
                tool_choice="auto"
            )

            # Decide: Check if agent wants to use a tool
            if response.tool_calls:
                for tool_call in response.tool_calls:
                    # Act: Execute the tool
                    result = self._execute_tool(tool_call)

                    # Observe: Add result to history
                    self.history.append({
                        "role": "tool",
                        "tool_call_id": tool_call.id,
                        "content": str(result)
                    })
            else:
                # No more tool calls = task complete
                return response.content

        return "Max iterations reached"

    def _execute_tool(self, tool_call) -> Any:
        tool = self.tools[tool_call.name]
        args = json.loads(tool_call.arguments)
        return tool.execute(**args)
```

### 1.2 Multi-Model Architecture

```python
class MultiModelAgent:
    """
    Use different models for different purposes:
    - Fast model for planning
    - Powerful model for complex reasoning
    - Specialized model for code generation
    """

    def __init__(self):
        self.models = {
            "fast": "gpt-3.5-turbo",      # Quick decisions
            "smart": "gpt-4-turbo",        # Complex reasoning
            "code": "example-model",     # Code generation
        }

    def select_model(self, task_type: str) -> str:
        if task_type == "planning":
            return self.models["fast"]
        elif task_type == "analysis":
            return self.models["smart"]
        elif task_type == "code":
            return self.models["code"]
        return self.models["smart"]
```

---

## 2. Tool Design Patterns

### 2.1 Tool Schema

```python
class Tool:
    """Base class for agent tools"""

    @property
    def schema(self) -> dict:
        """JSON Schema for the tool"""
        return {
            "name": self.name,
            "description": self.description,
            "parameters": {
                "type": "object",
                "properties": self._get_parameters(),
                "required": self._get_required()
            }
        }

    def execute(self, **kwargs) -> ToolResult:
        """Execute the tool and return result"""
        raise NotImplementedError

class ReadFileTool(Tool):
    name = "read_file"
    description = "Read the contents of a file from the filesystem"

    def _get_parameters(self):
        return {
            "path": {
                "type": "string",
                "description": "Absolute path to the file"
            },
            "start_line": {
                "type": "integer",
                "description": "Line to start reading from (1-indexed)"
            },
            "end_line": {
                "type": "integer",
                "description": "Line to stop reading at (inclusive)"
            }
        }

    def _get_required(self):
        return ["path"]

    def execute(self, path: str, start_line: int = None, end_line: int = None) -> ToolResult:
        try:
            with open(path, 'r') as f:
                lines = f.readlines()

            if start_line and end_line:
                lines = lines[start_line-1:end_line]

            return ToolResult(
                success=True,
                output="".join(lines)
            )
        except FileNotFoundError:
            return ToolResult(
                success=False,
                error=f"File not found: {path}"
            )
```

### 2.2 Essential Agent Tools

```python
CODING_AGENT_TOOLS = {
    # File operations
    "read_file": "Read file contents",
    "write_file": "Create or overwrite a file",
    "edit_file": "Make targeted edits to a file",
    "list_directory": "List files and folders",
    "search_files": "Search for files by pattern",

    # Code understanding
    "search_code": "Search for code patterns (grep)",
    "get_definition": "Find function/class definition",
    "get_references": "Find all references to a symbol",

    # Terminal
    "run_command": "Execute a shell command",
    "read_output": "Read command output",
    "send_input": "Send input to running command",

    # Browser (optional)
    "open_browser": "Open URL in browser",
    "click_element": "Click on page element",
    "type_text": "Type text into input",
    "screenshot": "Capture screenshot",

    # Context
    "ask_user": "Ask the user a question",
    "search_web": "Search the web for information"
}
```

### 2.3 Edit Tool Design

```python
class EditFileTool(Tool):
    """
    Precise file editing with conflict detection.
    Uses search/replace pattern for reliable edits.
    """

    name = "edit_file"
    description = "Edit a file by replacing specific content"

    def execute(
        self,
        path: str,
        search: str,
        replace: str,
        expected_occurrences: int = 1
    ) -> ToolResult:
        """
        Args:
            path: File to edit
            search: Exact text to find (must match exactly, including whitespace)
            replace: Text to replace with
            expected_occurrences: How many times search should appear (validation)
        """
        with open(path, 'r') as f:
            content = f.read()

        # Validate
        actual_occurrences = content.count(search)
        if actual_occurrences != expected_occurrences:
            return ToolResult(
                success=False,
                error=f"Expected {expected_occurrences} occurrences, found {actual_occurrences}"
            )

        if actual_occurrences == 0:
            return ToolResult(
                success=False,
                error="Search text not found in file"
            )

        # Apply edit
        new_content = content.replace(search, replace)

        with open(path, 'w') as f:
            f.write(new_content)

        return ToolResult(
            success=True,
            output=f"Replaced {actual_occurrences} occurrence(s)"
        )
```

---

## 3. Permission & Safety Patterns

### 3.1 Permission Levels

```python
class PermissionLevel(Enum):
    # Fully automatic - no user approval needed
    AUTO = "auto"

    # Ask once per session
    ASK_ONCE = "ask_once"

    # Ask every time
    ASK_EACH = "ask_each"

    # Never allow
    NEVER = "never"

PERMISSION_CONFIG = {
    # Low risk - can auto-approve
    "read_file": PermissionLevel.AUTO,
    "list_directory": PermissionLevel.AUTO,
    "search_code": PermissionLevel.AUTO,

    # Medium risk - ask once
    "write_file": PermissionLevel.ASK_ONCE,
    "edit_file": PermissionLevel.ASK_ONCE,

    # High risk - ask each time
    "run_command": PermissionLevel.ASK_EACH,
    "delete_file": PermissionLevel.ASK_EACH,

    # Dangerous - never auto-approve
    "sudo_command": PermissionLevel.NEVER,
    "format_disk": PermissionLevel.NEVER
}
```

### 3.2 Approval UI Pattern

```python
class ApprovalManager:
    def __init__(self, ui, config):
        self.ui = ui
        self.config = config
        self.session_approvals = {}

    def request_approval(self, tool_name: str, args: dict) -> bool:
        level = self.config.get(tool_name, PermissionLevel.ASK_EACH)

        if level == PermissionLevel.AUTO:
            return True

        if level == PermissionLevel.NEVER:
            self.ui.show_error(f"Tool '{tool_name}' is not allowed")
            return False

        if level == PermissionLevel.ASK_ONCE:
            if tool_name in self.session_approvals:
                return self.session_approvals[tool_name]

        # Show approval dialog
        approved = self.ui.show_approval_dialog(
            tool=tool_name,
            args=args,
            risk_level=self._assess_risk(tool_name, args)
        )

        if level == PermissionLevel.ASK_ONCE:
            self.session_approvals[tool_name] = approved

        return approved

    def _assess_risk(self, tool_name: str, args: dict) -> str:
        """Analyze specific call for risk level"""
        if tool_name == "run_command":
            cmd = args.get("command", "")
            if any(danger in cmd for danger in ["rm -rf", "sudo", "chmod"]):
                return "HIGH"
        return "MEDIUM"
```

### 3.3 Sandboxing

```python
class SandboxedExecution:
    """
    Execute code/commands in isolated environment
    """

    def __init__(self, workspace_dir: str):
        self.workspace = workspace_dir
        self.allowed_commands = ["npm", "python", "node", "git", "ls", "cat"]
        self.blocked_paths = ["/etc", "/usr", "/bin", os.path.expanduser("~")]

    def validate_path(self, path: str) -> bool:
        """Ensure path is within workspace"""
        real_path = os.path.realpath(path)
        workspace_real = os.path.realpath(self.workspace)
        return real_path.startswith(workspace_real)

    def validate_command(self, command: str) -> bool:
        """Check if command is allowed"""
        cmd_parts = shlex.split(command)
        if not cmd_parts:
            return False

        base_cmd = cmd_parts[0]
        return base_cmd in self.allowed_commands

    def execute_sandboxed(self, command: str) -> ToolResult:
        if not self.validate_command(command):
            return ToolResult(
                success=False,
                error=f"Command not allowed: {command}"
            )

        # Execute in isolated environment
        result = subprocess.run(
            command,
            shell=True,
            cwd=self.workspace,
            capture_output=True,
            timeout=30,
            env={
                **os.environ,
                "HOME": self.workspace,  # Isolate home directory
            }
        )

        return ToolResult(
            success=result.returncode == 0,
            output=result.stdout.decode(),
            error=result.stderr.decode() if result.returncode != 0 else None
        )
```

---

## 4. Browser Automation

### 4.1 Browser Tool Pattern

```python
class BrowserTool:
    """
    Browser automation for agents using Playwright/Puppeteer.
    Enables visual debugging and web testing.
    """

    def __init__(self, headless: bool = True):
        self.browser = None
        self.page = None
        self.headless = headless

    async def open_url(self, url: str) -> ToolResult:
        """Navigate to URL and return page info"""
        if not self.browser:
            self.browser = await playwright.chromium.launch(headless=self.headless)
            self.page = await self.browser.new_page()

        await self.page.goto(url)

        # Capture state
        screenshot = await self.page.screenshot(type='png')
        title = await self.page.title()

        return ToolResult(
            success=True,
            output=f"Loaded: {title}",
            metadata={
                "screenshot": base64.b64encode(screenshot).decode(),
                "url": self.page.url
            }
        )

    async def click(self, selector: str) -> ToolResult:
        """Click on an element"""
        try:
            await self.page.click(selector, timeout=5000)
            await self.page.wait_for_load_state("networkidle")

            screenshot = await self.page.screenshot()
            return ToolResult(
                success=True,
                output=f"Clicked: {selector}",
                metadata={"screenshot": base64.b64encode(screenshot).decode()}
            )
        except TimeoutError:
            return ToolResult(
                success=False,
                error=f"Element not found: {selector}"
            )

    async def type_text(self, selector: str, text: str) -> ToolResult:
        """Type text into an input"""
        await self.page.fill(selector, text)
        return ToolResult(success=True, output=f"Typed into {selector}")

    async def get_page_content(self) -> ToolResult:
        """Get accessible text content of the page"""
        content = await self.page.evaluate("""
            () => {
                // Get visible text
                const walker = document.createTreeWalker(
                    document.body,
                    NodeFilter.SHOW_TEXT,
                    null,
                    false
                );

                let text = '';
                while (walker.nextNode()) {
                    const node = walker.currentNode;
                    if (node.textContent.trim()) {
                        text += node.textContent.trim() + '\\n';
                    }
                }
                return text;
            }
        """)
        return ToolResult(success=True, output=content)
```

### 4.2 Visual Agent Pattern

```python
class VisualAgent:
    """
    Agent that uses screenshots to understand web pages.
    Can identify elements visually without selectors.
    """

    def __init__(self, llm, browser):
        self.llm = llm
        self.browser = browser

    async def describe_page(self) -> str:
        """Use vision model to describe current page"""
        screenshot = await self.browser.screenshot()

        response = self.llm.chat([
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "Describe this webpage. List all interactive elements you see."},
                    {"type": "image", "data": screenshot}
                ]
            }
        ])

        return response.content

    async def find_and_click(self, description: str) -> ToolResult:
        """Find element by visual description and click it"""
        screenshot = await self.browser.screenshot()

        # Ask vision model to find element
        response = self.llm.chat([
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": f"""
                        Find the element matching: "{description}"
                        Return the approximate coordinates as JSON: {{"x": number, "y": number}}
                        """
                    },
                    {"type": "image", "data": screenshot}
                ]
            }
        ])

        coords = json.loads(response.content)
        await self.browser.page.mouse.click(coords["x"], coords["y"])

        return ToolResult(success=True, output=f"Clicked at ({coords['x']}, {coords['y']})")
```

---

## 5. Context Management

### 5.1 Context Injection Patterns

````python
class ContextManager:
    """
    Manage context provided to the agent.
    Inspired by Cline's @-mention patterns.
    """

    def __init__(self, workspace: str):
        self.workspace = workspace
        self.context = []

    def add_file(self, path: str) -> None:
        """@file - Add file contents to context"""
        with open(path, 'r') as f:
            content = f.read()

        self.context.append({
            "type": "file",
            "path": path,
            "content": content
        })

    def add_folder(self, path: str, max_files: int = 20) -> None:
        """@folder - Add all files in folder"""
        for root, dirs, files in os.walk(path):
            for file in files[:max_files]:
                file_path = os.path.join(root, file)
                self.add_file(file_path)

    def add_url(self, url: str) -> None:
        """@url - Fetch and add URL content"""
        response = requests.get(url)
        content = html_to_markdown(response.text)

        self.context.append({
            "type": "url",
            "url": url,
            "content": content
        })

    def add_problems(self, diagnostics: list) -> None:
        """@problems - Add IDE diagnostics"""
        self.context.append({
            "type": "diagnostics",
            "problems": diagnostics
        })

    def format_for_prompt(self) -> str:
        """Format all context for LLM prompt"""
        parts = []
        for item in self.context:
            if item["type"] == "file":
                parts.append(f"## File: {item['path']}\n```\n{item['content']}\n```")
            elif item["type"] == "url":
                parts.append(f"## URL: {item['url']}\n{item['content']}")
            elif item["type"] == "diagnostics":
                parts.append(f"## Problems:\n{json.dumps(item['problems'], indent=2)}")

        return "\n\n".join(parts)
````

### 5.2 Checkpoint/Resume

```python
class CheckpointManager:
    """
    Save and restore agent state for long-running tasks.
    """

    def __init__(self, storage_dir: str):
        self.storage_dir = storage_dir
        os.makedirs(storage_dir, exist_ok=True)

    def save_checkpoint(self, session_id: str, state: dict) -> str:
        """Save current agent state"""
        checkpoint = {
            "timestamp": datetime.now().isoformat(),
            "session_id": session_id,
            "history": state["history"],
            "context": state["context"],
            "workspace_state": self._capture_workspace(state["workspace"]),
            "metadata": state.get("metadata", {})
        }

        path = os.path.join(self.storage_dir, f"{session_id}.json")
        with open(path, 'w') as f:
            json.dump(checkpoint, f, indent=2)

        return path

    def restore_checkpoint(self, checkpoint_path: str) -> dict:
        """Restore agent state from checkpoint"""
        with open(checkpoint_path, 'r') as f:
            checkpoint = json.load(f)

        return {
            "history": checkpoint["history"],
            "context": checkpoint["context"],
            "workspace": self._restore_workspace(checkpoint["workspace_state"]),
            "metadata": checkpoint["metadata"]
        }

    def _capture_workspace(self, workspace: str) -> dict:
        """Capture relevant workspace state"""
        # Git status, file hashes, etc.
        return {
            "git_ref": subprocess.getoutput(f"cd {workspace} && git rev-parse HEAD"),
            "git_dirty": subprocess.getoutput(f"cd {workspace} && git status --porcelain")
        }
```

---

## 6. MCP (Model Context Protocol) Integration

### 6.1 MCP Server Pattern

```python
from mcp import Server, Tool

class MCPAgent:
    """
    Agent that can dynamically discover and use MCP tools.
    'Add a tool that...' pattern from Cline.
    """

    def __init__(self, llm):
        self.llm = llm
        self.mcp_servers = {}
        self.available_tools = {}

    def connect_server(self, name: str, config: dict) -> None:
        """Connect to an MCP server"""
        server = Server(config)
        self.mcp_servers[name] = server

        # Discover tools
        tools = server.list_tools()
        for tool in tools:
            self.available_tools[tool.name] = {
                "server": name,
                "schema": tool.schema
            }

    async def create_tool(self, description: str) -> str:
        """
        Create a new MCP server based on user description.
        'Add a tool that fetches Jira tickets'
        """
        # Generate MCP server code
        code = self.llm.generate(f"""
        Create a Python MCP server with a tool that does:
        {description}

        Use the FastMCP framework. Include proper error handling.
        Return only the Python code.
        """)

        # Save and install
        server_name = self._extract_name(description)
        path = f"./mcp_servers/{server_name}/server.py"

        with open(path, 'w') as f:
            f.write(code)

        # Hot-reload
        self.connect_server(server_name, {"path": path})

        return f"Created tool: {server_name}"
```

---

## Best Practices Checklist

### Agent Design

- [ ] Clear task decomposition
- [ ] Appropriate tool granularity
- [ ] Error handling at each step
- [ ] Progress visibility to user

### Safety

- [ ] Permission system implemented
- [ ] Dangerous operations blocked
- [ ] Sandbox for untrusted code
- [ ] Audit logging enabled

### UX

- [ ] Approval UI is clear
- [ ] Progress updates provided
- [ ] Undo/rollback available
- [ ] Explanation of actions

---

## Resources

- [Cline](https://github.com/cline/cline)
- code-generation agent
- [Model Context Protocol](https://modelcontextprotocol.io/)
- provider tool-use documentation

---

## Imported Reference

---
name: agent-orchestrator
description: Meta-skill que orquestra todos os agentes do ecossistema. Scan automatico de skills, match por capacidades, coordenacao de workflows multi-skill e registry management.
risk: safe
source: community
date_added: '2026-03-06'
author: renat
tags:
- orchestration
- multi-agent
- workflow
- automation
tools:
- agent-compatible
- agent-compatible
- agent-compatible
- agent-compatible
- agent-compatible
---

# Agent Orchestrator

## Overview

Meta-skill que orquestra todos os agentes do ecossistema. Scan automatico de skills, match por capacidades, coordenacao de workflows multi-skill e registry management.

## When to Use This Skill

- When you need specialized assistance with this domain

## Do Not Use This Skill When

- The task is unrelated to agent orchestrator
- A simpler, more specific tool can handle the request
- The user needs general-purpose assistance without domain expertise

## How It Works

Meta-skill que funciona como camada central de decisao e coordenacao para todo
o ecossistema de skills. Faz varredura automatica, identifica agentes relevantes
e orquestra multiplos skills para tarefas complexas.

## Principio: Zero Intervencao Manual

- **SEMPRE faz varredura** antes de processar qualquer solicitacao
- Novas skills sao **auto-detectadas e incluidas** ao criar SKILL.md em qualquer subpasta
- Skills removidas sao **auto-excluidas** do registry
- Nenhum comando manual e necessario para registrar novas skills

---

## Workflow Obrigatorio (Toda Solicitacao)

Execute estes passos ANTES de processar qualquer request do usuario.
Os scripts usam paths relativos automaticamente - funciona de qualquer diretorio.

## Passo 1: Auto-Discovery (Varredura)

```bash
python agent-orchestrator/scripts/scan_registry.py
```

Ultra-rapido (<100ms) via cache de hashes MD5. So re-processa arquivos alterados.
Retorna JSON com resumo de todos os skills encontrados.

## Passo 2: Match De Skills

```bash
python agent-orchestrator/scripts/match_skills.py "<solicitacao do usuario>"
```

Retorna JSON com skills ranqueadas por relevancia. Interpretar o resultado:

| Resultado              | Acao                                                    |
|:-----------------------|:--------------------------------------------------------|
| `matched: 0`          | Nenhum skill relevante. Operar normalmente sem skills.  |
| `matched: 1`          | Um skill relevante. Carregar seu SKILL.md e seguir.     |
| `matched: 2+`         | Multiplos skills. Executar Passo 3 (orquestracao).      |

## Passo 3: Orquestracao (Se Matched >= 2)

```bash
python agent-orchestrator/scripts/orchestrate.py --skills skill1,skill2 --query "<solicitacao>"
```

Retorna plano de execucao com padrao, ordem dos steps e data flow entre skills.

## Passo Rapido (Atalho)

Para queries simples, os passos 1+2 podem ser combinados em sequencia:
```bash
python agent-orchestrator/scripts/scan_registry.py && python agent-orchestrator/scripts/match_skills.py "<solicitacao>"
```

---

## Skill Registry

O registry vive em:
```
agent-orchestrator/data/registry.json
```

## Locais De Busca

O scanner procura SKILL.md em:
1. `.agent/skills/*/` (skills registradas no AI coding assistant)
2. `*/` (skills standalone no top-level)
3. `*/*\` (skills em subpastas, ate profundidade 3)

## Metadata Por Skill

Cada entrada no registry contem:

| Campo          | Descricao                                          |
|:---------------|:---------------------------------------------------|
| name           | Nome da skill (do frontmatter YAML)                |
| description    | Descricao completa (triggers inclusos)             |
| location       | Caminho absoluto do diretorio                      |
| skill_md       | Caminho absoluto do SKILL.md                       |
| registered     | Se esta em .agent/skills/ (true/false)            |
| capabilities   | Tags de capacidade (auto-extraidas + explicitas)   |
| triggers       | Keywords de ativacao extraidas da description      |
| language       | Linguagem principal (python/nodejs/bash/none)      |
| status         | active / incomplete / missing                      |

## Comandos Do Registry

```bash

## Scan Rapido (Usa Cache De Hashes)

python agent-orchestrator/scripts/scan_registry.py

## Tabela De Status Detalhada

python agent-orchestrator/scripts/scan_registry.py --status

## Re-Scan Completo (Ignora Cache)

python agent-orchestrator/scripts/scan_registry.py --force
```

---

## Algoritmo De Matching

Para cada solicitacao, o matcher pontua skills usando:

| Criterio                     | Pontos | Exemplo                               |
|:-----------------------------|:-------|:--------------------------------------|
| Nome do skill na query       | +15    | "use web-scraper" -> web-scraper      |
| Keyword trigger exata        | +10    | "scrape" -> web-scraper               |
| Categoria de capacidade      | +5     | data-extraction -> web-scraper        |
| Sobreposicao de palavras     | +1     | Palavras da query na description      |
| Boost de projeto             | +20    | Skill atribuida ao projeto ativo      |

Threshold minimo: 5 pontos. Skills abaixo disso sao ignoradas.

## Match Com Projeto

```bash
python agent-orchestrator/scripts/match_skills.py --project meu-projeto "query aqui"
```

Skills atribuidas ao projeto recebem +20 de boost automatico.

---

## Padroes De Orquestracao

Quando multiplos skills sao relevantes, o orchestrator classifica o padrao:

## 1. Pipeline Sequencial

Skills formam uma cadeia onde o output de uma alimenta a proxima.

**Quando:** Mix de skills "produtoras" (data-extraction, government-data) e "consumidoras" (messaging, social-media).

**Exemplo:** web-scraper coleta precos -> whatsapp-cloud-api envia alerta

```
user_query -> web-scraper -> whatsapp-cloud-api -> result
```

## 2. Execucao Paralela

Skills trabalham independentemente em aspectos diferentes da solicitacao.

**Quando:** Todas as skills tem o mesmo papel (todas produtoras ou todas consumidoras).

**Exemplo:** instagram publica post + whatsapp envia notificacao (ambos recebem o mesmo conteudo)

```
user_query -> [instagram, whatsapp-cloud-api] -> aggregated_result
```

## 3. Primario + Suporte

Uma skill principal lidera; outras fornecem dados de apoio.

**Quando:** Uma skill tem score muito superior as demais (>= 2x).

**Exemplo:** whatsapp-cloud-api envia mensagem (primario) + web-scraper fornece dados (suporte)

```
user_query -> whatsapp-cloud-api (primary) + web-scraper (support) -> result
```

## Detalhes Em `References/Orchestration-Patterns.Md`

---

## Gerenciamento De Projetos

Atribuir skills a projetos permite boost de relevancia e contexto persistente.

## Arquivo De Projetos

```
agent-orchestrator/data/projects.json
```

## Operacoes

**Criar projeto:**
Adicionar entrada ao projects.json:
```json
{
  "name": "nome-do-projeto",
  "created_at": "2026-02-25T12:00:00",
  "skills": ["web-scraper", "whatsapp-cloud-api"],
  "description": "Descricao do projeto"
}
```

**Adicionar skill a projeto:** Atualizar o array `skills` do projeto.

**Remover skill de projeto:** Remover do array `skills`.

**Consultar skills do projeto:** Ler o projects.json e listar skills atribuidas.

---

## Adicionando Novas Skills

Para adicionar uma nova skill ao ecossistema:

1. Criar uma pasta em qualquer lugar sob `skills root:`
2. Criar um `SKILL.md` com frontmatter YAML:
```yaml
---
name: minha-nova-skill
description: "Descricao com keywords de ativacao..."
---

## Documentacao Da Skill

```
3. **Pronto!** O auto-discovery detecta automaticamente na proxima solicitacao.

Opcionalmente, para discovery nativo do AI coding assistant:
4. Copiar o SKILL.md para `.agent/skills/<nome>/SKILL.md`

## Tags De Capacidade Explicitas (Opcional)

Adicionar ao frontmatter para matching mais preciso:
```yaml
capabilities: [data-extraction, web-automation]
```

---

## Ver Status De Todos Os Skills

```bash
python agent-orchestrator/scripts/scan_registry.py --status
```

## Interpretar Status

| Status     | Significado                                        |
|:-----------|:---------------------------------------------------|
| active     | SKILL.md com name + description presentes          |
| incomplete | SKILL.md existe mas falta name ou description      |
| missing    | Diretorio existe mas sem SKILL.md                  |

---

## Skills Atuais Do Ecossistema

| Skill              | Capacidades                           | Status  |
|:-------------------|:--------------------------------------|:--------|
| web-scraper        | data-extraction, web-automation       | active  |
| junta-leiloeiros   | government-data, data-extraction      | active  |
| whatsapp-cloud-api | messaging, api-integration            | active  |
| instagram          | social-media, api-integration         | partial |

*Esta tabela e atualizada automaticamente via `scan_registry.py --status`.*

## Best Practices

- Provide clear, specific context about your project and requirements
- Review all suggestions before applying them to production code
- Combine with other complementary skills for comprehensive analysis

## Common Pitfalls

- Using this skill for tasks outside its domain expertise
- Applying recommendations without understanding your specific context
- Not providing enough project context for accurate analysis

## Related Skills

- `multi-advisor` - Complementary skill for enhanced analysis
- `task-intelligence` - Complementary skill for enhanced analysis

---

## Imported Reference

---
name: agent-orchestration-improve-agent
description: "Systematic improvement of existing agents through performance analysis, prompt engineering, and continuous iteration."
risk: unknown
source: community
date_added: "2026-02-27"
---

# Agent Performance Optimization Workflow

Systematic improvement of existing agents through performance analysis, prompt engineering, and continuous iteration.

[Extended thinking: Agent optimization requires a data-driven approach combining performance metrics, user feedback analysis, and advanced prompt engineering techniques. Success depends on systematic evaluation, targeted improvements, and rigorous testing with rollback capabilities for production safety.]

## Use this skill when

- Improving an existing agent's performance or reliability
- Analyzing failure modes, prompt quality, or tool usage
- Running structured A/B tests or evaluation suites
- Designing iterative optimization workflows for agents

## Do not use this skill when

- You are building a brand-new agent from scratch
- There are no metrics, feedback, or test cases available
- The task is unrelated to agent performance or prompt quality

## Instructions

1. Establish baseline metrics and collect representative examples.
2. Identify failure modes and prioritize high-impact fixes.
3. Apply prompt and workflow improvements with measurable goals.
4. Validate with tests and roll out changes in controlled stages.

## Safety

- Avoid deploying prompt changes without regression testing.
- Roll back quickly if quality or safety metrics regress.

## Phase 1: Performance Analysis and Baseline Metrics

Comprehensive analysis of agent performance using context-manager for historical data collection.

### 1.1 Gather Performance Data

```
Use: context-manager
Command: analyze-agent-performance $ARGUMENTS --days 30
```

Collect metrics including:

- Task completion rate (successful vs failed tasks)
- Response accuracy and factual correctness
- Tool usage efficiency (correct tools, call frequency)
- Average response time and token consumption
- User satisfaction indicators (corrections, retries)
- Hallucination incidents and error patterns

### 1.2 User Feedback Pattern Analysis

Identify recurring patterns in user interactions:

- **Correction patterns**: Where users consistently modify outputs
- **Clarification requests**: Common areas of ambiguity
- **Task abandonment**: Points where users give up
- **Follow-up questions**: Indicators of incomplete responses
- **Positive feedback**: Successful patterns to preserve

### 1.3 Failure Mode Classification

Categorize failures by root cause:

- **Instruction misunderstanding**: Role or task confusion
- **Output format errors**: Structure or formatting issues
- **Context loss**: Long conversation degradation
- **Tool misuse**: Incorrect or inefficient tool selection
- **Constraint violations**: Safety or business rule breaches
- **Edge case handling**: Unusual input scenarios

### 1.4 Baseline Performance Report

Generate quantitative baseline metrics:

```
Performance Baseline:
- Task Success Rate: [X%]
- Average Corrections per Task: [Y]
- Tool Call Efficiency: [Z%]
- User Satisfaction Score: [1-10]
- Average Response Latency: [Xms]
- Token Efficiency Ratio: [X:Y]
```

## Phase 2: Prompt Engineering Improvements

Apply advanced prompt optimization techniques using prompt-engineer agent.

### 2.1 Chain-of-Thought Enhancement

Implement structured reasoning patterns:

```
Use: prompt-engineer
Technique: chain-of-thought-optimization
```

- Add explicit reasoning steps: "Let's approach this step-by-step..."
- Include self-verification checkpoints: "Before proceeding, verify that..."
- Implement recursive decomposition for complex tasks
- Add reasoning trace visibility for debugging

### 2.2 Few-Shot Example Optimization

Curate high-quality examples from successful interactions:

- **Select diverse examples** covering common use cases
- **Include edge cases** that previously failed
- **Show both positive and negative examples** with explanations
- **Order examples** from simple to complex
- **Annotate examples** with key decision points

Example structure:

```
Good Example:
Input: [User request]
Reasoning: [Step-by-step thought process]
Output: [Successful response]
Why this works: [Key success factors]

Bad Example:
Input: [Similar request]
Output: [Failed response]
Why this fails: [Specific issues]
Correct approach: [Fixed version]
```

### 2.3 Role Definition Refinement

Strengthen agent identity and capabilities:

- **Core purpose**: Clear, single-sentence mission
- **Expertise domains**: Specific knowledge areas
- **Behavioral traits**: Personality and interaction style
- **Tool proficiency**: Available tools and when to use them
- **Constraints**: What the agent should NOT do
- **Success criteria**: How to measure task completion

### 2.4 Constitutional AI Integration

Implement self-correction mechanisms:

```
Constitutional Principles:
1. Verify factual accuracy before responding
2. Self-check for potential biases or harmful content
3. Validate output format matches requirements
4. Ensure response completeness
5. Maintain consistency with previous responses
```

Add critique-and-revise loops:

- Initial response generation
- Self-critique against principles
- Automatic revision if issues detected
- Final validation before output

### 2.5 Output Format Tuning

Optimize response structure:

- **Structured templates** for common tasks
- **Dynamic formatting** based on complexity
- **Progressive disclosure** for detailed information
- **Markdown optimization** for readability
- **Code block formatting** with syntax highlighting
- **Table and list generation** for data presentation

## Phase 3: Testing and Validation

Comprehensive testing framework with A/B comparison.

### 3.1 Test Suite Development

Create representative test scenarios:

```
Test Categories:
1. Golden path scenarios (common successful cases)
2. Previously failed tasks (regression testing)
3. Edge cases and corner scenarios
4. Stress tests (complex, multi-step tasks)
5. Adversarial inputs (potential breaking points)
6. Cross-domain tasks (combining capabilities)
```

### 3.2 A/B Testing Framework

Compare original vs improved agent:

```
Use: parallel-test-runner
Config:
  - Agent A: Original version
  - Agent B: Improved version
  - Test set: 100 representative tasks
  - Metrics: Success rate, speed, token usage
  - Evaluation: Blind human review + automated scoring
```

Statistical significance testing:

- Minimum sample size: 100 tasks per variant
- Confidence level: 95% (p < 0.05)
- Effect size calculation (Cohen's d)
- Power analysis for future tests

### 3.3 Evaluation Metrics

Comprehensive scoring framework:

**Task-Level Metrics:**

- Completion rate (binary success/failure)
- Correctness score (0-100% accuracy)
- Efficiency score (steps taken vs optimal)
- Tool usage appropriateness
- Response relevance and completeness

**Quality Metrics:**

- Hallucination rate (factual errors per response)
- Consistency score (alignment with previous responses)
- Format compliance (matches specified structure)
- Safety score (constraint adherence)
- User satisfaction prediction

**Performance Metrics:**

- Response latency (time to first token)
- Total generation time
- Token consumption (input + output)
- Cost per task (API usage fees)
- Memory/context efficiency

### 3.4 Human Evaluation Protocol

Structured human review process:

- Blind evaluation (evaluators don't know version)
- Standardized rubric with clear criteria
- Multiple evaluators per sample (inter-rater reliability)
- Qualitative feedback collection
- Preference ranking (A vs B comparison)

## Phase 4: Version Control and Deployment

Safe rollout with monitoring and rollback capabilities.

### 4.1 Version Management

Systematic versioning strategy:

```
Version Format: agent-name-v[MAJOR].[MINOR].[PATCH]
Example: customer-support-v2.3.1

MAJOR: Significant capability changes
MINOR: Prompt improvements, new examples
PATCH: Bug fixes, minor adjustments
```

Maintain version history:

- Git-based prompt storage
- Changelog with improvement details
- Performance metrics per version
- Rollback procedures documented

### 4.2 Staged Rollout

Progressive deployment strategy:

1. **Alpha testing**: Internal team validation (5% traffic)
2. **Beta testing**: Selected users (20% traffic)
3. **Canary release**: Gradual increase (20% → 50% → 100%)
4. **Full deployment**: After success criteria met
5. **Monitoring period**: 7-day observation window

### 4.3 Rollback Procedures

Quick recovery mechanism:

```
Rollback Triggers:
- Success rate drops >10% from baseline
- Critical errors increase >5%
- User complaints spike
- Cost per task increases >20%
- Safety violations detected

Rollback Process:
1. Detect issue via monitoring
2. Alert team immediately
3. Switch to previous stable version
4. Analyze root cause
5. Fix and re-test before retry
```

### 4.4 Continuous Monitoring

Real-time performance tracking:

- Dashboard with key metrics
- Anomaly detection alerts
- User feedback collection
- Automated regression testing
- Weekly performance reports

## Success Criteria

Agent improvement is successful when:

- Task success rate improves by ≥15%
- User corrections decrease by ≥25%
- No increase in safety violations
- Response time remains within 10% of baseline
- Cost per task doesn't increase >5%
- Positive user feedback increases

## Post-Deployment Review

After 30 days of production use:

1. Analyze accumulated performance data
2. Compare against baseline and targets
3. Identify new improvement opportunities
4. Document lessons learned
5. Plan next optimization cycle

## Continuous Improvement Cycle

Establish regular improvement cadence:

- **Weekly**: Monitor metrics and collect feedback
- **Monthly**: Analyze patterns and plan improvements
- **Quarterly**: Major version updates with new capabilities
- **Annually**: Strategic review and architecture updates

Remember: Agent optimization is an iterative process. Each cycle builds upon previous learnings, gradually improving performance while maintaining stability and safety.

---

## Imported Reference

---
name: agent-manager-skill
description: "Manage multiple local CLI agents via tmux sessions (start/stop/monitor/assign) with cron-friendly scheduling."
risk: unknown
source: community
date_added: "2026-02-27"
---

# Agent Manager Skill

## When to use

Use this skill when you need to:

- run multiple local CLI agents in parallel (separate tmux sessions)
- start/stop agents and tail their logs
- assign tasks to agents and monitor output
- schedule recurring agent work (cron)

## Prerequisites

Install `agent-manager-skill` in your workspace:

```bash
git clone https://github.com/fractalmind-ai/agent-manager-skill.git
```

## Common commands

```bash
python3 agent-manager/scripts/main.py doctor
python3 agent-manager/scripts/main.py list
python3 agent-manager/scripts/main.py start EMP_0001
python3 agent-manager/scripts/main.py monitor EMP_0001 --follow
python3 agent-manager/scripts/main.py assign EMP_0002 <<'EOF'
Follow teams/fractalmind-ai-maintenance.md Workflow
EOF
```

## Notes

- Requires `tmux` and `python3`.
- Agents are configured under an `agents/` directory (see the repo for examples).

---

## Imported Reference

---
name: tool-design
description: "Build tools that agents can use effectively, including architectural reduction patterns"
risk: safe
source: "https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/tree/main/skills/tool-design"
date_added: "2026-02-27"
---

## When to Use This Skill

Build tools that agents can use effectively, including architectural reduction patterns

Use this skill when working with build tools that agents can use effectively, including architectural reduction patterns.
# Tool Design for Agents

Tools are the primary mechanism through which agents interact with the world. They define the contract between deterministic systems and non-deterministic agents. Unlike traditional software APIs designed for developers, tool APIs must be designed for language models that reason about intent, infer parameter values, and generate calls from natural language requests. Poor tool design creates failure modes that no amount of prompt engineering can fix. Effective tool design follows specific principles that account for how agents perceive and use tools.

## When to Activate

Activate this skill when:
- Creating new tools for agent systems
- Debugging tool-related failures or misuse
- Optimizing existing tool sets for better agent performance
- Designing tool APIs from scratch
- Evaluating third-party tools for agent integration
- Standardizing tool conventions across a codebase

## Core Concepts

Tools are contracts between deterministic systems and non-deterministic agents. The consolidation principle states that if a human engineer cannot definitively say which tool should be used in a given situation, an agent cannot be expected to do better. Effective tool descriptions are prompt engineering that shapes agent behavior.

Key principles include: clear descriptions that answer what, when, and what returns; response formats that balance completeness and token efficiency; error messages that enable recovery; and consistent conventions that reduce cognitive load.

## Detailed Topics

### The Tool-Agent Interface

**Tools as Contracts**
Tools are contracts between deterministic systems and non-deterministic agents. When humans call APIs, they understand the contract and make appropriate requests. Agents must infer the contract from descriptions and generate calls that match expected formats.

This fundamental difference requires rethinking API design. The contract must be unambiguous, examples must illustrate expected patterns, and error messages must guide correction. Every ambiguity in tool definitions becomes a potential failure mode.

**Tool Description as Prompt**
Tool descriptions are loaded into agent context and collectively steer behavior. The descriptions are not just documentation—they are prompt engineering that shapes how agents reason about tool use.

Poor descriptions like "Search the database" with cryptic parameter names force agents to guess. Optimized descriptions include usage context, examples, and defaults. The description answers: what the tool does, when to use it, and what it produces.

**Namespacing and Organization**
As tool collections grow, organization becomes critical. Namespacing groups related tools under common prefixes, helping agents select appropriate tools at the right time.

Namespacing creates clear boundaries between functionality. When an agent needs database information, it routes to the database namespace. When it needs web search, it routes to web namespace.

### The Consolidation Principle

**Single Comprehensive Tools**
The consolidation principle states that if a human engineer cannot definitively say which tool should be used in a given situation, an agent cannot be expected to do better. This leads to a preference for single comprehensive tools over multiple narrow tools.

Instead of implementing list_users, list_events, and create_event, implement schedule_event that finds availability and schedules. The comprehensive tool handles the full workflow internally rather than requiring agents to chain multiple calls.

**Why Consolidation Works**
Agents have limited context and attention. Each tool in the collection competes for attention in the tool selection phase. Each tool adds description tokens that consume context budget. Overlapping functionality creates ambiguity about which tool to use.

Consolidation reduces token consumption by eliminating redundant descriptions. It eliminates ambiguity by having one tool cover each workflow. It reduces tool selection complexity by shrinking the effective tool set.

**When Not to Consolidate**
Consolidation is not universally correct. Tools with fundamentally different behaviors should remain separate. Tools used in different contexts benefit from separation. Tools that might be called independently should not be artificially bundled.

### Architectural Reduction

The consolidation principle, taken to its logical extreme, leads to architectural reduction: removing most specialized tools in favor of primitive, general-purpose capabilities. Production evidence shows this approach can outperform sophisticated multi-tool architectures.

**The File System Agent Pattern**
Instead of building custom tools for data exploration, schema lookup, and query validation, provide direct file system access through a single command execution tool. The agent uses standard Unix utilities (grep, cat, find, ls) to explore, understand, and operate on your system.

This works because:
1. File systems are a proven abstraction that models understand deeply
2. Standard tools have predictable, well-documented behavior
3. The agent can chain primitives flexibly rather than being constrained to predefined workflows
4. Good documentation in files replaces the need for summarization tools

**When Reduction Outperforms Complexity**
Reduction works when:
- Your data layer is well-documented and consistently structured
- The model has sufficient reasoning capability to navigate complexity
- Your specialized tools were constraining rather than enabling the model
- You're spending more time maintaining scaffolding than improving outcomes

Reduction fails when:
- Your underlying data is messy, inconsistent, or poorly documented
- The domain requires specialized knowledge the model lacks
- Safety constraints require limiting what the agent can do
- Operations are truly complex and benefit from structured workflows

**Stop Constraining Reasoning**
A common anti-pattern is building tools to "protect" the model from complexity. Pre-filtering context, constraining options, wrapping interactions in validation logic. These guardrails often become liabilities as models improve.

The question to ask: are your tools enabling new capabilities, or are they constraining reasoning the model could handle on its own?

**Build for Future Models**
Models improve faster than tooling can keep up. An architecture optimized for today's model may be over-constrained for tomorrow's. Build minimal architectures that can benefit from model improvements rather than sophisticated architectures that lock in current limitations.

See Architectural Reduction Case Study for production evidence.

### Tool Description Engineering

**Description Structure**
Effective tool descriptions answer four questions:

What does the tool do? Clear, specific description of functionality. Avoid vague language like "helps with" or "can be used for." State exactly what the tool accomplishes.

When should it be used? Specific triggers and contexts. Include both direct triggers ("User asks about pricing") and indirect signals ("Need current market rates").

What inputs does it accept? Parameter descriptions with types, constraints, and defaults. Explain what each parameter controls.

What does it return? Output format and structure. Include examples of successful responses and error conditions.

**Default Parameter Selection**
Defaults should reflect common use cases. They reduce agent burden by eliminating unnecessary parameter specification. They prevent errors from omitted parameters.

### Response Format Optimization

Tool response size significantly impacts context usage. Implementing response format options gives agents control over verbosity.

Concise format returns essential fields only, appropriate for confirmation or basic information. Detailed format returns complete objects with all fields, appropriate when full context is needed for decisions.

Include guidance in tool descriptions about when to use each format. Agents learn to select appropriate formats based on task requirements.

### Error Message Design

Error messages serve two audiences: developers debugging issues and agents recovering from failures. For agents, error messages must be actionable. They must tell the agent what went wrong and how to correct it.

Design error messages that enable recovery. For retryable errors, include retry guidance. For input errors, include corrected format. For missing data, include what's needed.

### Tool Definition Schema

Use a consistent schema across all tools. Establish naming conventions: verb-noun pattern for tool names, consistent parameter names across tools, consistent return field names.

### Tool Collection Design

Research shows tool description overlap causes model confusion. More tools do not always lead to better outcomes. A reasonable guideline is 10-20 tools for most applications. If more are needed, use namespacing to create logical groupings.

Implement mechanisms to help agents select the right tool: tool grouping, example-based selection, and hierarchy with umbrella tools that route to specialized sub-tools.

### MCP Tool Naming Requirements

When using MCP (Model Context Protocol) tools, always use fully qualified tool names to avoid "tool not found" errors.

Format: `ServerName:tool_name`

```python
# Correct: Fully qualified names
"Use the BigQuery:bigquery_schema tool to retrieve table schemas."
"Use the GitHub:create_issue tool to create issues."

# Incorrect: Unqualified names
"Use the bigquery_schema tool..."  # May fail with multiple servers
```

Without the server prefix, agents may fail to locate tools, especially when multiple MCP servers are available. Establish naming conventions that include server context in all tool references.

### Using Agents to Optimize Tools

AI assistant can optimize its own tools. When given a tool and observed failure modes, it diagnoses issues and suggests improvements. Production testing shows this approach achieves 40% reduction in task completion time by helping future agents avoid mistakes.

**The Tool-Testing Agent Pattern**:

```python
def optimize_tool_description(tool_spec, failure_examples):
    """
    Use an agent to analyze tool failures and improve descriptions.
    
    Process:
    1. Agent attempts to use tool across diverse tasks
    2. Collect failure modes and friction points
    3. Agent analyzes failures and proposes improvements
    4. Test improved descriptions against same tasks
    """
    prompt = f"""
    Analyze this tool specification and the observed failures.
    
    Tool: {tool_spec}
    
    Failures observed:
    {failure_examples}
    
    Identify:
    1. Why agents are failing with this tool
    2. What information is missing from the description
    3. What ambiguities cause incorrect usage
    
    Propose an improved tool description that addresses these issues.
    """
    
    return get_agent_response(prompt)
```

This creates a feedback loop: agents using tools generate failure data, which agents then use to improve tool descriptions, which reduces future failures.

### Testing Tool Design

Evaluate tool designs against criteria: unambiguity, completeness, recoverability, efficiency, and consistency. Test tools by presenting representative agent requests and evaluating the resulting tool calls.

## Practical Guidance

### Anti-Patterns to Avoid

Vague descriptions: "Search the database for customer information" leaves too many questions unanswered.

Cryptic parameter names: Parameters named x, val, or param1 force agents to guess meaning.

Missing error handling: Tools that fail with generic errors provide no recovery guidance.

Inconsistent naming: Using id in some tools, identifier in others, and customer_id in some creates confusion.

### Tool Selection Framework

When designing tool collections:
1. Identify distinct workflows agents must accomplish
2. Group related actions into comprehensive tools
3. Ensure each tool has a clear, unambiguous purpose
4. Document error cases and recovery paths
5. Test with actual agent interactions

## Examples

**Example 1: Well-Designed Tool**
```python
def get_customer(customer_id: str, format: str = "concise"):
    """
    Retrieve customer information by ID.
    
    Use when:
    - User asks about specific customer details
    - Need customer context for decision-making
    - Verifying customer identity
    
    Args:
        customer_id: Format "CUST-######" (e.g., "CUST-000001")
        format: "concise" for key fields, "detailed" for complete record
    
    Returns:
        Customer object with requested fields
    
    Errors:
        NOT_FOUND: Customer ID not found
        INVALID_FORMAT: ID must match CUST-###### pattern
    """
```

**Example 2: Poor Tool Design**

This example demonstrates several tool design anti-patterns:

```python
def search(query):
    """Search the database."""
    pass
```

**Problems with this design:**

1. **Vague name**: "search" is ambiguous - search what, for what purpose?
2. **Missing parameters**: What database? What format should query take?
3. **No return description**: What does this function return? A list? A string? Error handling?
4. **No usage context**: When should an agent use this versus other tools?
5. **No error handling**: What happens if the database is unavailable?

**Failure modes:**
- Agents may call this tool when they should use a more specific tool
- Agents cannot determine correct query format
- Agents cannot interpret results
- Agents cannot recover from failures

## Guidelines

1. Write descriptions that answer what, when, and what returns
2. Use consolidation to reduce ambiguity
3. Implement response format options for token efficiency
4. Design error messages for agent recovery
5. Establish and follow consistent naming conventions
6. Limit tool count and use namespacing for organization
7. Test tool designs with actual agent interactions
8. Iterate based on observed failure modes
9. Question whether each tool enables or constrains the model
10. Prefer primitive, general-purpose tools over specialized wrappers
11. Invest in documentation quality over tooling sophistication
12. Build minimal architectures that benefit from model improvements

## Integration

This skill connects to:
- context-fundamentals - How tools interact with context
- multi-agent-patterns - Specialized tools per agent
- evaluation - Evaluating tool effectiveness

## References

Internal references:
- Best Practices Reference - Detailed tool design guidelines
- Architectural Reduction Case Study - Production evidence for tool minimalism

Related skills in this collection:
- context-fundamentals - Tool context interactions
- evaluation - Tool testing patterns

External resources:
- MCP (Model Context Protocol) documentation
- Framework tool conventions
- API design best practices for agents
- Vercel d0 agent architecture case study

---

## Skill Metadata

**Created**: 2025-12-20
**Last Updated**: 2025-12-23
**Author**: Agent Skills for Context Engineering Contributors
**Version**: 1.1.0

---

## Imported Reference

---
name: agent-tool-builder
description: "Tools are how AI agents interact with the world. A well-designed tool is the difference between an agent that works and one that hallucinates, fails silently, or costs 10x more tokens than necessar..."
risk: unknown
source: "vibeship-spawner-skills (Apache 2.0)"
date_added: "2026-02-27"
---

# Agent Tool Builder

You are an expert in the interface between LLMs and the outside world.
You've seen tools that work beautifully and tools that cause agents to
hallucinate, loop, or fail silently. The difference is almost always
in the design, not the implementation.

Your core insight: The LLM never sees your code. It only sees the schema
and description. A perfectly implemented tool with a vague description
will fail. A simple tool with crystal-clear documentation will succeed.

You push for explicit error hand

## Capabilities

- agent-tools
- function-calling
- tool-schema-design
- mcp-tools
- tool-validation
- tool-error-handling

## Patterns

### Tool Schema Design

Creating clear, unambiguous JSON Schema for tools

### Tool with Input Examples

Using examples to guide LLM tool usage

### Tool Error Handling

Returning errors that help the LLM recover

## Anti-Patterns

### ❌ Vague Descriptions

### ❌ Silent Failures

### ❌ Too Many Tools

## Related Skills

Works well with: `multi-agent-orchestration`, `api-designer`, `llm-architect`, `backend`

## When to Use
This skill is applicable to execute the workflow or actions described in the overview.

---

## Imported Reference

---
name: computer-use-agents
description: "Build AI agents that interact with computers like humans do - viewing screens, moving cursors, clicking buttons, and typing text. Covers Anthropic's Computer Use, OpenAI's Operator/CUA, and open-so..."
risk: unknown
source: "vibeship-spawner-skills (Apache 2.0)"
date_added: "2026-02-27"
---

# Computer Use Agents

## Patterns

### Perception-Reasoning-Action Loop

The fundamental architecture of computer use agents: observe screen,
reason about next action, execute action, repeat. This loop integrates
vision models with action execution through an iterative pipeline.

Key components:
1. PERCEPTION: Screenshot captures current screen state
2. REASONING: Vision-language model analyzes and plans
3. ACTION: Execute mouse/keyboard operations
4. FEEDBACK: Observe result, continue or correct

Critical insight: Vision agents are completely still during "thinking"
phase (1-5 seconds), creating a detectable pause pattern.


**When to use**: ['Building any computer use agent from scratch', 'Integrating vision models with desktop control', 'Understanding agent behavior patterns']

```python
from llm_provider import LLMClient
from PIL import Image
import base64
import pyautogui
import time

class ComputerUseAgent:
    """
    Perception-Reasoning-Action loop implementation.
    Based on Anthropic Computer Use patterns.
    """

    def __init__(self, client: Anthropic, model: str = "example-balanced-model"):
        self.client = client
        self.model = model
        self.max_steps = 50  # Prevent runaway loops
        self.action_delay = 0.5  # Seconds between actions

    def capture_screenshot(self) -> str:
        """Capture screen and return base64 encoded image."""
        screenshot = pyautogui.screenshot()
        # Resize for token efficiency (1280x800 is good balance)
        screenshot = screenshot.resize((1280, 800), Image.LANCZOS)

        import io
        buffer = io.BytesIO()
        screenshot.save(buffer, format="PNG")
        return base64.b64encode(buffer.getvalue()).decode()

    def execute_action(self, action: dict) -> dict:
        """Execute mouse/keyboard action on the computer."""
        action_type = action.get("type")

        if action_type == "click":
            x, y = action["x"], action["y"]
            button = action.get("button", "left")
            pyautogui.click(x, y, button=button)
            return {"success": True, "action": f"clicked at ({x}, {y})"}

        elif action_type == "type":
            text = action["text"]
            pyautogui.typewrite(text, interval=0.02)
            return {"success": True, "action": f"typed {len(text)} chars"}

        elif action_type == "key":
            key = action["key"]
            pyautogui.press(key)
            return {"success": True, "action": f"pressed {key}"}

        elif action_type == "scroll":
            direction = action.get("direction", "down")
            amount = action.get("amount", 3)
            scroll = -amount if direction == "down" else amount
            pyautogui.scroll(scroll)
            return {"success": True, "action": f"scrolled {dir
```

### Sandboxed Environment Pattern

Computer use agents MUST run in isolated, sandboxed environments.
Never give agents direct access to your main system - the security
risks are too high. Use Docker containers with virtual desktops.

Key isolation requirements:
1. NETWORK: Restrict to necessary endpoints only
2. FILESYSTEM: Read-only or scoped to temp directories
3. CREDENTIALS: No access to host credentials
4. SYSCALLS: Filter dangerous system calls
5. RESOURCES: Limit CPU, memory, time

The goal is "blast radius minimization" - if the agent goes wrong,
damage is contained to the sandbox.


**When to use**: ['Deploying any computer use agent', 'Testing agent behavior safely', 'Running untrusted automation tasks']

```python
# Dockerfile for sandboxed computer use environment
# Based on Anthropic's reference implementation pattern

FROM ubuntu:22.04

# Install desktop environment
RUN apt-get update && apt-get install -y \
    xvfb \
    x11vnc \
    fluxbox \
    xterm \
    firefox \
    python3 \
    python3-pip \
    supervisor

# Security: Create non-root user
RUN useradd -m -s /bin/bash agent && \
    mkdir -p /home/agent/.vnc

# Install Python dependencies
COPY requirements.txt /tmp/
RUN pip3 install -r /tmp/requirements.txt

# Security: Drop capabilities
RUN apt-get install -y --no-install-recommends libcap2-bin && \
    setcap -r /usr/bin/python3 || true

# Copy agent code
COPY --chown=agent:agent . /app
WORKDIR /app

# Supervisor config for virtual display + VNC
COPY supervisord.conf /etc/supervisor/conf.d/

# Expose VNC port only (not desktop directly)
EXPOSE 5900

# Run as non-root
USER agent

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]

---

# docker-compose.yml with security constraints
version: '3.8'

services:
  computer-use-agent:
    build: .
    ports:
      - "5900:5900"  # VNC for observation
      - "8080:8080"  # API for control

    # Security constraints
    security_opt:
      - no-new-privileges:true
      - seccomp:seccomp-profile.json

    # Resource limits
    deploy:
      resources:
        limits:
          cpus: '2'
          memory: 4G
        reservations:
          cpus: '0.5'
          memory: 1G

    # Network isolation
    networks:
      - agent-network

    # No access to host filesystem
    volumes:
      - agent-tmp:/tmp

    # Read-only root filesystem
    read_only: true
    tmpfs:
      - /run
      - /var/run

    # Environment
    environment:
      - DISPLAY=:99
      - NO_PROXY=localhost

networks:
  agent-network:
    driver: bridge
    internal: true  # No internet by default

volumes:
  agent-tmp:

---

# Python wrapper with additional runtime sandboxing
import subprocess
import os
from dataclasses im
```

### Anthropic Computer Use Implementation

Official implementation pattern using AI assistant's computer use capability.
AI assistant 3.5 Sonnet was the first frontier model to offer computer use.
AI assistant Opus 4.5 is now the "best model in the world for computer use."

Key capabilities:
- screenshot: Capture current screen state
- mouse: Click, move, drag operations
- keyboard: Type text, press keys
- bash: Run shell commands
- text_editor: View and edit files

Tool versions:
- computer_20251124 (Opus 4.5): Adds zoom action for detailed inspection
- computer_20250124 (All other models): Standard capabilities

Critical limitation: "Some UI elements (like dropdowns and scrollbars)
might be tricky for AI assistant to manipulate" - Anthropic docs


**When to use**: ['Building production computer use agents', 'Need highest quality vision understanding', 'Full desktop control (not just browser)']

```python
from llm_provider import LLMClient
from anthropic.types.beta import (
    BetaToolComputerUse20241022,
    BetaToolBash20241022,
    BetaToolTextEditor20241022,
)
import subprocess
import base64
from PIL import Image
import io

class AnthropicComputerUse:
    """
    Official Anthropic Computer Use implementation.

    Requires:
    - Docker container with virtual display
    - VNC for viewing agent actions
    - Proper tool implementations
    """

    def __init__(self):
        self.client = LLMClient()
        self.model = "example-balanced-model"  # Best for computer use
        self.screen_size = (1280, 800)

    def get_tools(self) -> list:
        """Define computer use tools."""
        return [
            BetaToolComputerUse20241022(
                type="computer_20241022",
                name="computer",
                display_width_px=self.screen_size[0],
                display_height_px=self.screen_size[1],
            ),
            BetaToolBash20241022(
                type="bash_20241022",
                name="bash",
            ),
            BetaToolTextEditor20241022(
                type="text_editor_20241022",
                name="str_replace_editor",
            ),
        ]

    def execute_tool(self, name: str, input: dict) -> dict:
        """Execute a tool and return result."""

        if name == "computer":
            return self._handle_computer_action(input)
        elif name == "bash":
            return self._handle_bash(input)
        elif name == "str_replace_editor":
            return self._handle_editor(input)
        else:
            return {"error": f"Unknown tool: {name}"}

    def _handle_computer_action(self, input: dict) -> dict:
        """Handle computer control actions."""
        action = input.get("action")

        if action == "screenshot":
            # Capture via xdotool/scrot
            subprocess.run(["scrot", "/tmp/screenshot.png"])

            with open("/tmp/screenshot.png", "rb") as f:
            
```

## ⚠️ Sharp Edges

| Issue | Severity | Solution |
|-------|----------|----------|
| Issue | critical | ## Defense in depth - no single solution works |
| Issue | medium | ## Add human-like variance to actions |
| Issue | high | ## Use keyboard alternatives when possible |
| Issue | medium | ## Accept the tradeoff |
| Issue | high | ## Implement context management |
| Issue | high | ## Monitor and limit costs |
| Issue | critical | ## ALWAYS use sandboxing |

## When to Use
This skill is applicable to execute the workflow or actions described in the overview.

---

## Imported Reference

---
name: hosted-agents
description: Build background agents in sandboxed environments. Use for hosted coding agents, sandboxed VMs, Modal sandboxes, and remote coding environments.
risk: unknown
source: community
---

# Hosted Agent Infrastructure

Hosted agents run in remote sandboxed environments rather than on local machines. When designed well, they provide unlimited concurrency, consistent execution environments, and multiplayer collaboration. The critical insight is that session speed should be limited only by model provider time-to-first-token, with all infrastructure setup completed before the user starts their session.

## When to Activate

Activate this skill when:
- Building background coding agents that run independently of user devices
- Designing sandboxed execution environments for agent workloads
- Implementing multiplayer agent sessions with shared state
- Creating multi-client agent interfaces (Slack, Web, Chrome extensions)
- Scaling agent infrastructure beyond local machine constraints
- Building systems where agents spawn sub-agents for parallel work

## Core Concepts

Hosted agents address the fundamental limitation of local agent execution: resource contention, environment inconsistency, and single-user constraints. By moving agent execution to remote sandboxed environments, teams gain unlimited concurrency, reproducible environments, and collaborative workflows.

The architecture consists of three layers: sandbox infrastructure for isolated execution, API layer for state management and client coordination, and client interfaces for user interaction across platforms. Each layer has specific design requirements that enable the system to scale.

## Detailed Topics

### Sandbox Infrastructure

**The Core Challenge**
Spinning up full development environments quickly is the primary technical challenge. Users expect near-instant session starts, but development environments require cloning repositories, installing dependencies, and running build steps.

**Image Registry Pattern**
Pre-build environment images on a regular cadence (every 30 minutes works well). Each image contains:
- Cloned repository at a known commit
- All runtime dependencies installed
- Initial setup and build commands completed
- Cached files from running app and test suite once

When starting a session, spin up a sandbox from the most recent image. The repository is at most 30 minutes out of date, making synchronization with the latest code much faster.

**Snapshot and Restore**
Take filesystem snapshots at key points:
- After initial image build (base snapshot)
- When agent finishes making changes (session snapshot)
- Before sandbox exit for potential follow-up

This enables instant restoration for follow-up prompts without re-running setup.

**Git Configuration for Background Agents**
Since git operations are not tied to a specific user during image builds:
- Generate GitHub app installation tokens for repository access during clone
- Update git config's `user.name` and `user.email` when committing and pushing changes
- Use the prompting user's identity for commits, not the app identity

**Warm Pool Strategy**
Maintain a pool of pre-warmed sandboxes for high-volume repositories:
- Sandboxes are ready before users start sessions
- Expire and recreate pool entries as new image builds complete
- Start warming sandbox as soon as user begins typing (predictive warm-up)

### Agent Framework Selection

**Server-First Architecture**
Choose an agent framework structured as a server first, with TUI and desktop apps as clients. This enables:
- Multiple custom clients without duplicating agent logic
- Consistent behavior across all interaction surfaces
- Plugin systems for extending functionality
- Event-driven architectures for real-time updates

**Code as Source of Truth**
Select frameworks where the agent can read its own source code to understand behavior. This is underrated in AI development: having the code as source of truth prevents hallucination about the agent's own capabilities.

**Plugin System Requirements**
The framework should support plugins that:
- Listen to tool execution events (e.g., `tool.execute.before`)
- Block or modify tool calls conditionally
- Inject context or state at runtime

### Speed Optimizations

**Predictive Warm-Up**
Start warming the sandbox as soon as a user begins typing their prompt:
- Clone latest changes in parallel with user typing
- Run initial setup before user hits enter
- For fast spin-up, sandbox can be ready before user finishes typing

**Parallel File Reading**
Allow the agent to start reading files immediately, even if sync from latest base branch is not complete:
- In large repositories, incoming prompts rarely modify recently-changed files
- Agent can research immediately without waiting for git sync
- Block file edits (not reads) until synchronization completes

**Maximize Build-Time Work**
Move everything possible to the image build step:
- Full dependency installation
- Database schema setup
- Initial app and test suite runs (populates caches)
- Build-time duration is invisible to users

### Self-Spawning Agents

**Agent-Spawned Sessions**
Create tools that allow agents to spawn new sessions:
- Research tasks across different repositories
- Parallel subtask execution for large changes
- Multiple smaller PRs from one major task

Frontier models are capable of containing themselves. The tools should:
- Start a new session with specified parameters
- Read status of any session (check-in capability)
- Continue main work while sub-sessions run in parallel

**Prompt Engineering for Self-Spawning**
Engineer prompts to guide when agents spawn sub-sessions:
- Research tasks that require cross-repository exploration
- Breaking monolithic changes into smaller PRs
- Parallel exploration of different approaches

### API Layer

**Per-Session State Isolation**
Each session requires its own isolated state storage:
- Dedicated database per session (SQLite per session works well)
- No session can impact another's performance
- Handles hundreds of concurrent sessions

**Real-Time Streaming**
Agent work involves high-frequency updates:
- Token streaming from model providers
- Tool execution status updates
- File change notifications

WebSocket connections with hibernation APIs reduce compute costs during idle periods while maintaining open connections.

**Synchronization Across Clients**
Build a single state system that synchronizes across:
- Chat interfaces
- Slack bots
- Chrome extensions
- Web interfaces
- VS Code instances

All changes sync to the session state, enabling seamless client switching.

### Multiplayer Support

**Why Multiplayer Matters**
Multiplayer enables:
- Teaching non-engineers to use AI effectively
- Live QA sessions with multiple team members
- Real-time PR review with immediate changes
- Collaborative debugging sessions

**Implementation Requirements**
- Data model must not tie sessions to single authors
- Pass authorship info to each prompt
- Attribute code changes to the prompting user
- Share session links for instant collaboration

With proper synchronization architecture, multiplayer support is nearly free to add.

### Authentication and Authorization

**User-Based Commits**
Use GitHub authentication to:
- Obtain user tokens for PR creation
- Open PRs on behalf of the user (not the app)
- Prevent users from approving their own changes

**Sandbox-to-API Flow**
1. Sandbox pushes changes (updating git user config)
2. Sandbox sends event to API with branch name and session ID
3. API uses user's GitHub token to create PR
4. GitHub webhooks notify API of PR events

### Client Implementations

**Slack Integration**
The most effective distribution channel for internal adoption:
- Creates virality loop as team members see others using it
- No syntax required, natural chat interface
- Classify repository from message, thread context, and channel name

Build a classifier to determine which repository to work in:
- Fast model with descriptions of available repositories
- Include hints for common repositories
- Allow "unknown" option for ambiguous cases

**Web Interface**
Core features:
- Works on desktop and mobile
- Real-time streaming of agent work
- Hosted VS Code instance running inside sandbox
- Streamed desktop view for visual verification
- Before/after screenshots for PRs

Statistics page showing:
- Sessions resulting in merged PRs (primary metric)
- Usage over time
- Live "humans prompting" count (prompts in last 5 minutes)

**Chrome Extension**
For non-engineering users:
- Sidebar chat interface with screenshot tool
- DOM and React internals extraction instead of raw images
- Reduces token usage while maintaining precision
- Distribute via managed device policy (bypasses Chrome Web Store)

## Practical Guidance

### Follow-Up Message Handling

Decide how to handle messages sent during execution:
- **Queue approach**: Messages wait until current prompt completes
- **Insert approach**: Messages are processed immediately

Queueing is simpler to manage and lets users send thoughts on next steps while agent works. Build mechanism to stop agent mid-execution when needed.

### Metrics That Matter

Track metrics that indicate real value:
- Sessions resulting in merged PRs (primary success metric)
- Time from session start to first model response
- PR approval rate and revision count
- Agent-written code percentage across repositories

### Adoption Strategy

Internal adoption patterns that work:
- Work in public spaces (Slack channels) for visibility
- Let the product create virality loops
- Don't force usage over existing tools
- Build to people's needs, not hypothetical requirements

## Guidelines

1. Pre-build environment images on regular cadence (30 minutes is a good default)
2. Start warming sandboxes when users begin typing, not when they submit
3. Allow file reads before git sync completes; block only writes
4. Structure agent framework as server-first with clients as thin wrappers
5. Isolate state per session to prevent cross-session interference
6. Attribute commits to the user who prompted, not the app
7. Track merged PRs as primary success metric
8. Build for multiplayer from the start; it is nearly free with proper sync architecture

## Integration

This skill builds on multi-agent-patterns for agent coordination and tool-design for agent-tool interfaces. It connects to:

- multi-agent-patterns - Self-spawning agents follow supervisor patterns
- tool-design - Building tools for agent spawning and status checking
- context-optimization - Managing context across distributed sessions
- filesystem-context - Using filesystem for session state and artifacts

## References

Internal reference:
- Infrastructure Patterns - Detailed implementation patterns

Related skills in this collection:
- multi-agent-patterns - Coordination patterns for self-spawning agents
- tool-design - Designing tools for hosted environments
- context-optimization - Managing context in distributed systems

External resources:
- [Ramp](https://builders.ramp.com/post/why-we-built-our-background-agent) - Why We Built Our Own Background Agent
- [Modal Sandboxes](https://modal.com/docs/guide/sandbox) - Cloud sandbox infrastructure
- [Cloudflare Durable Objects](https://developers.cloudflare.com/durable-objects/) - Per-session state management
- Server-first agent framework pattern

---

## Skill Metadata

**Created**: 2026-01-12
**Last Updated**: 2026-01-12
**Author**: Agent Skills for Context Engineering Contributors
**Version**: 1.0.0


## When to Use

Use this skill when tackling tasks related to its primary domain or functionality as described above.

---

## Imported Reference

---
name: hosted-agents-v2-py
description: "Build hosted agents using Azure AI Projects SDK with ImageBasedHostedAgentDefinition. Use when creating container-based agents in Azure AI Foundry."
risk: unknown
source: community
date_added: "2026-02-27"
---

# Azure AI Hosted Agents (Python)

Build container-based hosted agents using `ImageBasedHostedAgentDefinition` from the Azure AI Projects SDK.

## Installation

```bash
pip install azure-ai-projects>=2.0.0b3 azure-identity
```

**Minimum SDK Version:** `2.0.0b3` or later required for hosted agent support.

## Environment Variables

```bash
AZURE_AI_PROJECT_ENDPOINT=https://<resource>.services.ai.azure.com/api/projects/<project>
```

## Prerequisites

Before creating hosted agents:

1. **Container Image** - Build and push to Azure Container Registry (ACR)
2. **ACR Pull Permissions** - Grant your project's managed identity `AcrPull` role on the ACR
3. **Capability Host** - Account-level capability host with `enablePublicHostingEnvironment=true`
4. **SDK Version** - Ensure `azure-ai-projects>=2.0.0b3`

## Authentication

Always use `DefaultAzureCredential`:

```python
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

credential = DefaultAzureCredential()
client = AIProjectClient(
    endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    credential=credential
)
```

## Core Workflow

### 1. Imports

```python
import os
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import (
    ImageBasedHostedAgentDefinition,
    ProtocolVersionRecord,
    AgentProtocol,
)
```

### 2. Create Hosted Agent

```python
client = AIProjectClient(
    endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    credential=DefaultAzureCredential()
)

agent = client.agents.create_version(
    agent_name="my-hosted-agent",
    definition=ImageBasedHostedAgentDefinition(
        container_protocol_versions=[
            ProtocolVersionRecord(protocol=AgentProtocol.RESPONSES, version="v1")
        ],
        cpu="1",
        memory="2Gi",
        image="myregistry.azurecr.io/my-agent:latest",
        tools=[{"type": "code_interpreter"}],
        environment_variables={
            "AZURE_AI_PROJECT_ENDPOINT": os.environ["AZURE_AI_PROJECT_ENDPOINT"],
            "MODEL_NAME": "gpt-4o-mini"
        }
    )
)

print(f"Created agent: {agent.name} (version: {agent.version})")
```

### 3. List Agent Versions

```python
versions = client.agents.list_versions(agent_name="my-hosted-agent")
for version in versions:
    print(f"Version: {version.version}, State: {version.state}")
```

### 4. Delete Agent Version

```python
client.agents.delete_version(
    agent_name="my-hosted-agent",
    version=agent.version
)
```

## ImageBasedHostedAgentDefinition Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `container_protocol_versions` | `list[ProtocolVersionRecord]` | Yes | Protocol versions the agent supports |
| `image` | `str` | Yes | Full container image path (registry/image:tag) |
| `cpu` | `str` | No | CPU allocation (e.g., "1", "2") |
| `memory` | `str` | No | Memory allocation (e.g., "2Gi", "4Gi") |
| `tools` | `list[dict]` | No | Tools available to the agent |
| `environment_variables` | `dict[str, str]` | No | Environment variables for the container |

## Protocol Versions

The `container_protocol_versions` parameter specifies which protocols your agent supports:

```python
from azure.ai.projects.models import ProtocolVersionRecord, AgentProtocol

# RESPONSES protocol - standard agent responses
container_protocol_versions=[
    ProtocolVersionRecord(protocol=AgentProtocol.RESPONSES, version="v1")
]
```

**Available Protocols:**
| Protocol | Description |
|----------|-------------|
| `AgentProtocol.RESPONSES` | Standard response protocol for agent interactions |

## Resource Allocation

Specify CPU and memory for your container:

```python
definition=ImageBasedHostedAgentDefinition(
    container_protocol_versions=[...],
    image="myregistry.azurecr.io/my-agent:latest",
    cpu="2",      # 2 CPU cores
    memory="4Gi"  # 4 GiB memory
)
```

**Resource Limits:**
| Resource | Min | Max | Default |
|----------|-----|-----|---------|
| CPU | 0.5 | 4 | 1 |
| Memory | 1Gi | 8Gi | 2Gi |

## Tools Configuration

Add tools to your hosted agent:

### Code Interpreter

```python
tools=[{"type": "code_interpreter"}]
```

### MCP Tools

```python
tools=[
    {"type": "code_interpreter"},
    {
        "type": "mcp",
        "server_label": "my-mcp-server",
        "server_url": "https://my-mcp-server.example.com"
    }
]
```

### Multiple Tools

```python
tools=[
    {"type": "code_interpreter"},
    {"type": "file_search"},
    {
        "type": "mcp",
        "server_label": "custom-tool",
        "server_url": "https://custom-tool.example.com"
    }
]
```

## Environment Variables

Pass configuration to your container:

```python
environment_variables={
    "AZURE_AI_PROJECT_ENDPOINT": os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    "MODEL_NAME": "gpt-4o-mini",
    "LOG_LEVEL": "INFO",
    "CUSTOM_CONFIG": "value"
}
```

**Best Practice:** Never hardcode secrets. Use environment variables or Azure Key Vault.

## Complete Example

```python
import os
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import (
    ImageBasedHostedAgentDefinition,
    ProtocolVersionRecord,
    AgentProtocol,
)

def create_hosted_agent():
    """Create a hosted agent with custom container image."""
    
    client = AIProjectClient(
        endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
        credential=DefaultAzureCredential()
    )
    
    agent = client.agents.create_version(
        agent_name="data-processor-agent",
        definition=ImageBasedHostedAgentDefinition(
            container_protocol_versions=[
                ProtocolVersionRecord(
                    protocol=AgentProtocol.RESPONSES,
                    version="v1"
                )
            ],
            image="myregistry.azurecr.io/data-processor:v1.0",
            cpu="2",
            memory="4Gi",
            tools=[
                {"type": "code_interpreter"},
                {"type": "file_search"}
            ],
            environment_variables={
                "AZURE_AI_PROJECT_ENDPOINT": os.environ["AZURE_AI_PROJECT_ENDPOINT"],
                "MODEL_NAME": "gpt-4o-mini",
                "MAX_RETRIES": "3"
            }
        )
    )
    
    print(f"Created hosted agent: {agent.name}")
    print(f"Version: {agent.version}")
    print(f"State: {agent.state}")
    
    return agent

if __name__ == "__main__":
    create_hosted_agent()
```

## Async Pattern

```python
import os
from azure.identity.aio import DefaultAzureCredential
from azure.ai.projects.aio import AIProjectClient
from azure.ai.projects.models import (
    ImageBasedHostedAgentDefinition,
    ProtocolVersionRecord,
    AgentProtocol,
)

async def create_hosted_agent_async():
    """Create a hosted agent asynchronously."""
    
    async with DefaultAzureCredential() as credential:
        async with AIProjectClient(
            endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
            credential=credential
        ) as client:
            agent = await client.agents.create_version(
                agent_name="async-agent",
                definition=ImageBasedHostedAgentDefinition(
                    container_protocol_versions=[
                        ProtocolVersionRecord(
                            protocol=AgentProtocol.RESPONSES,
                            version="v1"
                        )
                    ],
                    image="myregistry.azurecr.io/async-agent:latest",
                    cpu="1",
                    memory="2Gi"
                )
            )
            return agent
```

## Common Errors

| Error | Cause | Solution |
|-------|-------|----------|
| `ImagePullBackOff` | ACR pull permission denied | Grant `AcrPull` role to project's managed identity |
| `InvalidContainerImage` | Image not found | Verify image path and tag exist in ACR |
| `CapabilityHostNotFound` | No capability host configured | Create account-level capability host |
| `ProtocolVersionNotSupported` | Invalid protocol version | Use `AgentProtocol.RESPONSES` with version `"v1"` |

## Best Practices

1. **Version Your Images** - Use specific tags, not `latest` in production
2. **Minimal Resources** - Start with minimum CPU/memory, scale up as needed
3. **Environment Variables** - Use for all configuration, never hardcode
4. **Error Handling** - Wrap agent creation in try/except blocks
5. **Cleanup** - Delete unused agent versions to free resources

## Reference Links

- [Azure AI Projects SDK](https://pypi.org/project/azure-ai-projects/)
- [Hosted Agents Documentation](https://learn.microsoft.com/azure/ai-services/agents/how-to/hosted-agents)
- [Azure Container Registry](https://learn.microsoft.com/azure/container-registry/)

## When to Use
This skill is applicable to execute the workflow or actions described in the overview.

---

## Imported Reference

---
name: agents-md
description: This skill should be used when the user asks to "create AGENTS.md", "update AGENTS.md", "maintain agent docs", "set up AGENT_CONTEXT.md", or needs to keep agent instructions concise. Enforces research-backed best practices for minimal, high-signal agent documentation.
---

# Maintaining AGENTS.md

AGENTS.md is the canonical agent-facing documentation. Keep it minimal—agents are capable and don't need hand-holding. Target under 60 lines; never exceed 100. Instruction-following quality degrades as document length increases.

## File Setup

1. Create `AGENTS.md` at project root
2. Create symlink: `ln -s AGENTS.md AGENT_CONTEXT.md`

## Before Writing

Analyze the project to understand what belongs in the file:

1. **Package manager** — Check for lock files (`pnpm-lock.yaml`, `yarn.lock`, `package-lock.json`, `uv.lock`, `poetry.lock`)
2. **Linter/formatter configs** — Look for `.eslintrc`, `biome.json`, `ruff.toml`, `.prettierrc`, etc. (don't duplicate these in AGENTS.md)
3. **CI/build commands** — Check `Makefile`, `package.json` scripts, CI configs for canonical commands
4. **Monorepo indicators** — Check for `pnpm-workspace.yaml`, `nx.json`, Cargo workspace, or subdirectory `package.json` files
5. **Existing conventions** — Check for existing CONTRIBUTING.md, docs/, or README patterns

## Writing Rules

- **Headers + bullets** — No paragraphs
- **Code blocks** — For commands and templates
- **Reference, don't embed** — Point to existing docs: "See `CONTRIBUTING.md` for setup" or "Follow patterns in `src/api/routes/`"
- **No filler** — No intros, conclusions, or pleasantries
- **Trust capabilities** — Omit obvious context
- **Prefer file-scoped commands** — Per-file test/lint/typecheck commands over project-wide builds
- **Don't duplicate linters** — Code style lives in linter configs, not AGENTS.md

## Required Sections

### Package Manager
Which tool and key commands only:
```markdown
## Package Manager
Use **pnpm**: `pnpm install`, `pnpm dev`, `pnpm test`
```

### File-Scoped Commands
Per-file commands are faster and cheaper than full project builds. Always include when available:
```markdown
## File-Scoped Commands
| Task | Command |
|------|---------|
| Typecheck | `pnpm tsc --noEmit path/to/file.ts` |
| Lint | `pnpm eslint path/to/file.ts` |
| Test | `pnpm jest path/to/file.test.ts` |
```

### Commit Attribution
Always include this section. Agents should use their own identity:
```markdown
## Commit Attribution
AI commits MUST include:
```
Co-Authored-By: (the agent model's name and attribution byline)
```
Example: `Co-Authored-By: AI assistant Sonnet 4 <noreply@example.com>`
```

### Key Conventions
Project-specific patterns agents must follow. Keep brief.

## Optional Sections

Add only if truly needed:
- API route patterns (show template, not explanation)
- CLI commands (table format)
- File naming conventions
- Project structure hints (point to critical files, flag legacy code to avoid)
- Monorepo overrides (subdirectory `AGENTS.md` files override root)

## Anti-Patterns

Omit these:
- "Welcome to..." or "This document explains..."
- "You should..." or "Remember to..."
- Linter/formatter rules already in config files (`.eslintrc`, `biome.json`, `ruff.toml`)
- Listing installed skills or plugins (agents discover these automatically)
- Full project-wide build commands when file-scoped alternatives exist
- Obvious instructions ("run tests", "write clean code")
- Explanations of why (just say what)
- Long prose paragraphs

## Example Structure

```markdown
# Agent Instructions

## Package Manager
Use **pnpm**: `pnpm install`, `pnpm dev`

## Commit Attribution
AI commits MUST include:
```
Co-Authored-By: (the agent model's name and attribution byline)
```

## File-Scoped Commands
| Task | Command |
|------|---------|
| Typecheck | `pnpm tsc --noEmit path/to/file.ts` |
| Lint | `pnpm eslint path/to/file.ts` |
| Test | `pnpm jest path/to/file.test.ts` |

## API Routes
[Template code block]

## CLI
| Command | Description |
|---------|-------------|
| `pnpm cli sync` | Sync data |
```

## Imported Module: Agent Manager Skill
---
name: agent-manager-skill
description: "Manage multiple local CLI agents via tmux sessions (start/stop/monitor/assign) with cron-friendly scheduling."
risk: unknown
source: community
date_added: "2026-02-27"
---

# Agent Manager Skill

## When to use

Use this skill when you need to:

- run multiple local CLI agents in parallel (separate tmux sessions)
- start/stop agents and tail their logs
- assign tasks to agents and monitor output
- schedule recurring agent work (cron)

## Prerequisites

Install `agent-manager-skill` in your workspace:

```bash
git clone https://github.com/fractalmind-ai/agent-manager-skill.git
```

## Common commands

```bash
python3 agent-manager/scripts/main.py doctor
python3 agent-manager/scripts/main.py list
python3 agent-manager/scripts/main.py start EMP_0001
python3 agent-manager/scripts/main.py monitor EMP_0001 --follow
python3 agent-manager/scripts/main.py assign EMP_0002 <<'EOF'
Follow teams/fractalmind-ai-maintenance.md Workflow
EOF
```

## Notes

- Requires `tmux` and `python3`.
- Agents are configured under an `agents/` directory (see the repo for examples).

## Imported Module: Agent Orchestration Improve Agent
---
name: agent-orchestration-improve-agent
description: "Systematic improvement of existing agents through performance analysis, prompt engineering, and continuous iteration."
risk: unknown
source: community
date_added: "2026-02-27"
---

# Agent Performance Optimization Workflow

Systematic improvement of existing agents through performance analysis, prompt engineering, and continuous iteration.

[Extended thinking: Agent optimization requires a data-driven approach combining performance metrics, user feedback analysis, and advanced prompt engineering techniques. Success depends on systematic evaluation, targeted improvements, and rigorous testing with rollback capabilities for production safety.]

## Use this skill when

- Improving an existing agent's performance or reliability
- Analyzing failure modes, prompt quality, or tool usage
- Running structured A/B tests or evaluation suites
- Designing iterative optimization workflows for agents

## Do not use this skill when

- You are building a brand-new agent from scratch
- There are no metrics, feedback, or test cases available
- The task is unrelated to agent performance or prompt quality

## Instructions

1. Establish baseline metrics and collect representative examples.
2. Identify failure modes and prioritize high-impact fixes.
3. Apply prompt and workflow improvements with measurable goals.
4. Validate with tests and roll out changes in controlled stages.

## Safety

- Avoid deploying prompt changes without regression testing.
- Roll back quickly if quality or safety metrics regress.

## Phase 1: Performance Analysis and Baseline Metrics

Comprehensive analysis of agent performance using context-manager for historical data collection.

### 1.1 Gather Performance Data

```
Use: context-manager
Command: analyze-agent-performance $ARGUMENTS --days 30
```

Collect metrics including:

- Task completion rate (successful vs failed tasks)
- Response accuracy and factual correctness
- Tool usage efficiency (correct tools, call frequency)
- Average response time and token consumption
- User satisfaction indicators (corrections, retries)
- Hallucination incidents and error patterns

### 1.2 User Feedback Pattern Analysis

Identify recurring patterns in user interactions:

- **Correction patterns**: Where users consistently modify outputs
- **Clarification requests**: Common areas of ambiguity
- **Task abandonment**: Points where users give up
- **Follow-up questions**: Indicators of incomplete responses
- **Positive feedback**: Successful patterns to preserve

### 1.3 Failure Mode Classification

Categorize failures by root cause:

- **Instruction misunderstanding**: Role or task confusion
- **Output format errors**: Structure or formatting issues
- **Context loss**: Long conversation degradation
- **Tool misuse**: Incorrect or inefficient tool selection
- **Constraint violations**: Safety or business rule breaches
- **Edge case handling**: Unusual input scenarios

### 1.4 Baseline Performance Report

Generate quantitative baseline metrics:

```
Performance Baseline:
- Task Success Rate: [X%]
- Average Corrections per Task: [Y]
- Tool Call Efficiency: [Z%]
- User Satisfaction Score: [1-10]
- Average Response Latency: [Xms]
- Token Efficiency Ratio: [X:Y]
```

## Phase 2: Prompt Engineering Improvements

Apply advanced prompt optimization techniques using prompt-engineer agent.

### 2.1 Chain-of-Thought Enhancement

Implement structured reasoning patterns:

```
Use: prompt-engineer
Technique: chain-of-thought-optimization
```

- Add explicit reasoning steps: "Let's approach this step-by-step..."
- Include self-verification checkpoints: "Before proceeding, verify that..."
- Implement recursive decomposition for complex tasks
- Add reasoning trace visibility for debugging

### 2.2 Few-Shot Example Optimization

Curate high-quality examples from successful interactions:

- **Select diverse examples** covering common use cases
- **Include edge cases** that previously failed
- **Show both positive and negative examples** with explanations
- **Order examples** from simple to complex
- **Annotate examples** with key decision points

Example structure:

```
Good Example:
Input: [User request]
Reasoning: [Step-by-step thought process]
Output: [Successful response]
Why this works: [Key success factors]

Bad Example:
Input: [Similar request]
Output: [Failed response]
Why this fails: [Specific issues]
Correct approach: [Fixed version]
```

### 2.3 Role Definition Refinement

Strengthen agent identity and capabilities:

- **Core purpose**: Clear, single-sentence mission
- **Expertise domains**: Specific knowledge areas
- **Behavioral traits**: Personality and interaction style
- **Tool proficiency**: Available tools and when to use them
- **Constraints**: What the agent should NOT do
- **Success criteria**: How to measure task completion

### 2.4 Constitutional AI Integration

Implement self-correction mechanisms:

```
Constitutional Principles:
1. Verify factual accuracy before responding
2. Self-check for potential biases or harmful content
3. Validate output format matches requirements
4. Ensure response completeness
5. Maintain consistency with previous responses
```

Add critique-and-revise loops:

- Initial response generation
- Self-critique against principles
- Automatic revision if issues detected
- Final validation before output

### 2.5 Output Format Tuning

Optimize response structure:

- **Structured templates** for common tasks
- **Dynamic formatting** based on complexity
- **Progressive disclosure** for detailed information
- **Markdown optimization** for readability
- **Code block formatting** with syntax highlighting
- **Table and list generation** for data presentation

## Phase 3: Testing and Validation

Comprehensive testing framework with A/B comparison.

### 3.1 Test Suite Development

Create representative test scenarios:

```
Test Categories:
1. Golden path scenarios (common successful cases)
2. Previously failed tasks (regression testing)
3. Edge cases and corner scenarios
4. Stress tests (complex, multi-step tasks)
5. Adversarial inputs (potential breaking points)
6. Cross-domain tasks (combining capabilities)
```

### 3.2 A/B Testing Framework

Compare original vs improved agent:

```
Use: parallel-test-runner
Config:
  - Agent A: Original version
  - Agent B: Improved version
  - Test set: 100 representative tasks
  - Metrics: Success rate, speed, token usage
  - Evaluation: Blind human review + automated scoring
```

Statistical significance testing:

- Minimum sample size: 100 tasks per variant
- Confidence level: 95% (p < 0.05)
- Effect size calculation (Cohen's d)
- Power analysis for future tests

### 3.3 Evaluation Metrics

Comprehensive scoring framework:

**Task-Level Metrics:**

- Completion rate (binary success/failure)
- Correctness score (0-100% accuracy)
- Efficiency score (steps taken vs optimal)
- Tool usage appropriateness
- Response relevance and completeness

**Quality Metrics:**

- Hallucination rate (factual errors per response)
- Consistency score (alignment with previous responses)
- Format compliance (matches specified structure)
- Safety score (constraint adherence)
- User satisfaction prediction

**Performance Metrics:**

- Response latency (time to first token)
- Total generation time
- Token consumption (input + output)
- Cost per task (API usage fees)
- Memory/context efficiency

### 3.4 Human Evaluation Protocol

Structured human review process:

- Blind evaluation (evaluators don't know version)
- Standardized rubric with clear criteria
- Multiple evaluators per sample (inter-rater reliability)
- Qualitative feedback collection
- Preference ranking (A vs B comparison)

## Phase 4: Version Control and Deployment

Safe rollout with monitoring and rollback capabilities.

### 4.1 Version Management

Systematic versioning strategy:

```
Version Format: agent-name-v[MAJOR].[MINOR].[PATCH]
Example: customer-support-v2.3.1

MAJOR: Significant capability changes
MINOR: Prompt improvements, new examples
PATCH: Bug fixes, minor adjustments
```

Maintain version history:

- Git-based prompt storage
- Changelog with improvement details
- Performance metrics per version
- Rollback procedures documented

### 4.2 Staged Rollout

Progressive deployment strategy:

1. **Alpha testing**: Internal team validation (5% traffic)
2. **Beta testing**: Selected users (20% traffic)
3. **Canary release**: Gradual increase (20% → 50% → 100%)
4. **Full deployment**: After success criteria met
5. **Monitoring period**: 7-day observation window

### 4.3 Rollback Procedures

Quick recovery mechanism:

```
Rollback Triggers:
- Success rate drops >10% from baseline
- Critical errors increase >5%
- User complaints spike
- Cost per task increases >20%
- Safety violations detected

Rollback Process:
1. Detect issue via monitoring
2. Alert team immediately
3. Switch to previous stable version
4. Analyze root cause
5. Fix and re-test before retry
```

### 4.4 Continuous Monitoring

Real-time performance tracking:

- Dashboard with key metrics
- Anomaly detection alerts
- User feedback collection
- Automated regression testing
- Weekly performance reports

## Success Criteria

Agent improvement is successful when:

- Task success rate improves by ≥15%
- User corrections decrease by ≥25%
- No increase in safety violations
- Response time remains within 10% of baseline
- Cost per task doesn't increase >5%
- Positive user feedback increases

## Post-Deployment Review

After 30 days of production use:

1. Analyze accumulated performance data
2. Compare against baseline and targets
3. Identify new improvement opportunities
4. Document lessons learned
5. Plan next optimization cycle

## Continuous Improvement Cycle

Establish regular improvement cadence:

- **Weekly**: Monitor metrics and collect feedback
- **Monthly**: Analyze patterns and plan improvements
- **Quarterly**: Major version updates with new capabilities
- **Annually**: Strategic review and architecture updates

Remember: Agent optimization is an iterative process. Each cycle builds upon previous learnings, gradually improving performance while maintaining stability and safety.

## Imported Module: Agent Orchestrator
---
name: agent-orchestrator
description: Meta-skill que orquestra todos os agentes do ecossistema. Scan automatico de skills, match por capacidades, coordenacao de workflows multi-skill e registry management.
risk: safe
source: community
date_added: '2026-03-06'
author: renat
tags:
- orchestration
- multi-agent
- workflow
- automation
tools:
- agent-compatible
- agent-compatible
- agent-compatible
- agent-compatible
- agent-compatible
---

# Agent Orchestrator

## Overview

Meta-skill que orquestra todos os agentes do ecossistema. Scan automatico de skills, match por capacidades, coordenacao de workflows multi-skill e registry management.

## When to Use This Skill

- When you need specialized assistance with this domain

## Do Not Use This Skill When

- The task is unrelated to agent orchestrator
- A simpler, more specific tool can handle the request
- The user needs general-purpose assistance without domain expertise

## How It Works

Meta-skill que funciona como camada central de decisao e coordenacao para todo
o ecossistema de skills. Faz varredura automatica, identifica agentes relevantes
e orquestra multiplos skills para tarefas complexas.

## Principio: Zero Intervencao Manual

- **SEMPRE faz varredura** antes de processar qualquer solicitacao
- Novas skills sao **auto-detectadas e incluidas** ao criar SKILL.md em qualquer subpasta
- Skills removidas sao **auto-excluidas** do registry
- Nenhum comando manual e necessario para registrar novas skills

---

## Workflow Obrigatorio (Toda Solicitacao)

Execute estes passos ANTES de processar qualquer request do usuario.
Os scripts usam paths relativos automaticamente - funciona de qualquer diretorio.

## Passo 1: Auto-Discovery (Varredura)

```bash
python agent-orchestrator/scripts/scan_registry.py
```

Ultra-rapido (<100ms) via cache de hashes MD5. So re-processa arquivos alterados.
Retorna JSON com resumo de todos os skills encontrados.

## Passo 2: Match De Skills

```bash
python agent-orchestrator/scripts/match_skills.py "<solicitacao do usuario>"
```

Retorna JSON com skills ranqueadas por relevancia. Interpretar o resultado:

| Resultado              | Acao                                                    |
|:-----------------------|:--------------------------------------------------------|
| `matched: 0`          | Nenhum skill relevante. Operar normalmente sem skills.  |
| `matched: 1`          | Um skill relevante. Carregar seu SKILL.md e seguir.     |
| `matched: 2+`         | Multiplos skills. Executar Passo 3 (orquestracao).      |

## Passo 3: Orquestracao (Se Matched >= 2)

```bash
python agent-orchestrator/scripts/orchestrate.py --skills skill1,skill2 --query "<solicitacao>"
```

Retorna plano de execucao com padrao, ordem dos steps e data flow entre skills.

## Passo Rapido (Atalho)

Para queries simples, os passos 1+2 podem ser combinados em sequencia:
```bash
python agent-orchestrator/scripts/scan_registry.py && python agent-orchestrator/scripts/match_skills.py "<solicitacao>"
```

---

## Skill Registry

O registry vive em:
```
agent-orchestrator/data/registry.json
```

## Locais De Busca

O scanner procura SKILL.md em:
1. `.agent/skills/*/` (skills registradas no AI coding assistant)
2. `*/` (skills standalone no top-level)
3. `*/*\` (skills em subpastas, ate profundidade 3)

## Metadata Por Skill

Cada entrada no registry contem:

| Campo          | Descricao                                          |
|:---------------|:---------------------------------------------------|
| name           | Nome da skill (do frontmatter YAML)                |
| description    | Descricao completa (triggers inclusos)             |
| location       | Caminho absoluto do diretorio                      |
| skill_md       | Caminho absoluto do SKILL.md                       |
| registered     | Se esta em .agent/skills/ (true/false)            |
| capabilities   | Tags de capacidade (auto-extraidas + explicitas)   |
| triggers       | Keywords de ativacao extraidas da description      |
| language       | Linguagem principal (python/nodejs/bash/none)      |
| status         | active / incomplete / missing                      |

## Comandos Do Registry

```bash

## Scan Rapido (Usa Cache De Hashes)

python agent-orchestrator/scripts/scan_registry.py

## Tabela De Status Detalhada

python agent-orchestrator/scripts/scan_registry.py --status

## Re-Scan Completo (Ignora Cache)

python agent-orchestrator/scripts/scan_registry.py --force
```

---

## Algoritmo De Matching

Para cada solicitacao, o matcher pontua skills usando:

| Criterio                     | Pontos | Exemplo                               |
|:-----------------------------|:-------|:--------------------------------------|
| Nome do skill na query       | +15    | "use web-scraper" -> web-scraper      |
| Keyword trigger exata        | +10    | "scrape" -> web-scraper               |
| Categoria de capacidade      | +5     | data-extraction -> web-scraper        |
| Sobreposicao de palavras     | +1     | Palavras da query na description      |
| Boost de projeto             | +20    | Skill atribuida ao projeto ativo      |

Threshold minimo: 5 pontos. Skills abaixo disso sao ignoradas.

## Match Com Projeto

```bash
python agent-orchestrator/scripts/match_skills.py --project meu-projeto "query aqui"
```

Skills atribuidas ao projeto recebem +20 de boost automatico.

---

## Padroes De Orquestracao

Quando multiplos skills sao relevantes, o orchestrator classifica o padrao:

## 1. Pipeline Sequencial

Skills formam uma cadeia onde o output de uma alimenta a proxima.

**Quando:** Mix de skills "produtoras" (data-extraction, government-data) e "consumidoras" (messaging, social-media).

**Exemplo:** web-scraper coleta precos -> whatsapp-cloud-api envia alerta

```
user_query -> web-scraper -> whatsapp-cloud-api -> result
```

## 2. Execucao Paralela

Skills trabalham independentemente em aspectos diferentes da solicitacao.

**Quando:** Todas as skills tem o mesmo papel (todas produtoras ou todas consumidoras).

**Exemplo:** instagram publica post + whatsapp envia notificacao (ambos recebem o mesmo conteudo)

```
user_query -> [instagram, whatsapp-cloud-api] -> aggregated_result
```

## 3. Primario + Suporte

Uma skill principal lidera; outras fornecem dados de apoio.

**Quando:** Uma skill tem score muito superior as demais (>= 2x).

**Exemplo:** whatsapp-cloud-api envia mensagem (primario) + web-scraper fornece dados (suporte)

```
user_query -> whatsapp-cloud-api (primary) + web-scraper (support) -> result
```

## Detalhes Em `References/Orchestration-Patterns.Md`

---

## Gerenciamento De Projetos

Atribuir skills a projetos permite boost de relevancia e contexto persistente.

## Arquivo De Projetos

```
agent-orchestrator/data/projects.json
```

## Operacoes

**Criar projeto:**
Adicionar entrada ao projects.json:
```json
{
  "name": "nome-do-projeto",
  "created_at": "2026-02-25T12:00:00",
  "skills": ["web-scraper", "whatsapp-cloud-api"],
  "description": "Descricao do projeto"
}
```

**Adicionar skill a projeto:** Atualizar o array `skills` do projeto.

**Remover skill de projeto:** Remover do array `skills`.

**Consultar skills do projeto:** Ler o projects.json e listar skills atribuidas.

---

## Adicionando Novas Skills

Para adicionar uma nova skill ao ecossistema:

1. Criar uma pasta em qualquer lugar sob `skills root:`
2. Criar um `SKILL.md` com frontmatter YAML:
```yaml
---
name: minha-nova-skill
description: "Descricao com keywords de ativacao..."
---

## Documentacao Da Skill

```
3. **Pronto!** O auto-discovery detecta automaticamente na proxima solicitacao.

Opcionalmente, para discovery nativo do AI coding assistant:
4. Copiar o SKILL.md para `.agent/skills/<nome>/SKILL.md`

## Tags De Capacidade Explicitas (Opcional)

Adicionar ao frontmatter para matching mais preciso:
```yaml
capabilities: [data-extraction, web-automation]
```

---

## Ver Status De Todos Os Skills

```bash
python agent-orchestrator/scripts/scan_registry.py --status
```

## Interpretar Status

| Status     | Significado                                        |
|:-----------|:---------------------------------------------------|
| active     | SKILL.md com name + description presentes          |
| incomplete | SKILL.md existe mas falta name ou description      |
| missing    | Diretorio existe mas sem SKILL.md                  |

---

## Skills Atuais Do Ecossistema

| Skill              | Capacidades                           | Status  |
|:-------------------|:--------------------------------------|:--------|
| web-scraper        | data-extraction, web-automation       | active  |
| junta-leiloeiros   | government-data, data-extraction      | active  |
| whatsapp-cloud-api | messaging, api-integration            | active  |
| instagram          | social-media, api-integration         | partial |

*Esta tabela e atualizada automaticamente via `scan_registry.py --status`.*

## Best Practices

- Provide clear, specific context about your project and requirements
- Review all suggestions before applying them to production code
- Combine with other complementary skills for comprehensive analysis

## Common Pitfalls

- Using this skill for tasks outside its domain expertise
- Applying recommendations without understanding your specific context
- Not providing enough project context for accurate analysis

## Related Skills

- `multi-advisor` - Complementary skill for enhanced analysis
- `task-intelligence` - Complementary skill for enhanced analysis

## Imported Module: Agent Tool Builder
---
name: agent-tool-builder
description: "Tools are how AI agents interact with the world. A well-designed tool is the difference between an agent that works and one that hallucinates, fails silently, or costs 10x more tokens than necessar..."
risk: unknown
source: "vibeship-spawner-skills (Apache 2.0)"
date_added: "2026-02-27"
---

# Agent Tool Builder

You are an expert in the interface between LLMs and the outside world.
You've seen tools that work beautifully and tools that cause agents to
hallucinate, loop, or fail silently. The difference is almost always
in the design, not the implementation.

Your core insight: The LLM never sees your code. It only sees the schema
and description. A perfectly implemented tool with a vague description
will fail. A simple tool with crystal-clear documentation will succeed.

You push for explicit error hand

## Capabilities

- agent-tools
- function-calling
- tool-schema-design
- mcp-tools
- tool-validation
- tool-error-handling

## Patterns

### Tool Schema Design

Creating clear, unambiguous JSON Schema for tools

### Tool with Input Examples

Using examples to guide LLM tool usage

### Tool Error Handling

Returning errors that help the LLM recover

## Anti-Patterns

### ❌ Vague Descriptions

### ❌ Silent Failures

### ❌ Too Many Tools

## Related Skills

Works well with: `multi-agent-orchestration`, `api-designer`, `llm-architect`, `backend`

## When to Use
This skill is applicable to execute the workflow or actions described in the overview.

## Imported Module: Agents Md
---
name: agents-md
description: This skill should be used when the user asks to "create AGENTS.md", "update AGENTS.md", "maintain agent docs", "set up AGENT_CONTEXT.md", or needs to keep agent instructions concise. Enforces research-backed best practices for minimal, high-signal agent documentation.
---

# Maintaining AGENTS.md

AGENTS.md is the canonical agent-facing documentation. Keep it minimal—agents are capable and don't need hand-holding. Target under 60 lines; never exceed 100. Instruction-following quality degrades as document length increases.

## File Setup

1. Create `AGENTS.md` at project root
2. Create symlink: `ln -s AGENTS.md AGENT_CONTEXT.md`

## Before Writing

Analyze the project to understand what belongs in the file:

1. **Package manager** — Check for lock files (`pnpm-lock.yaml`, `yarn.lock`, `package-lock.json`, `uv.lock`, `poetry.lock`)
2. **Linter/formatter configs** — Look for `.eslintrc`, `biome.json`, `ruff.toml`, `.prettierrc`, etc. (don't duplicate these in AGENTS.md)
3. **CI/build commands** — Check `Makefile`, `package.json` scripts, CI configs for canonical commands
4. **Monorepo indicators** — Check for `pnpm-workspace.yaml`, `nx.json`, Cargo workspace, or subdirectory `package.json` files
5. **Existing conventions** — Check for existing CONTRIBUTING.md, docs/, or README patterns

## Writing Rules

- **Headers + bullets** — No paragraphs
- **Code blocks** — For commands and templates
- **Reference, don't embed** — Point to existing docs: "See `CONTRIBUTING.md` for setup" or "Follow patterns in `src/api/routes/`"
- **No filler** — No intros, conclusions, or pleasantries
- **Trust capabilities** — Omit obvious context
- **Prefer file-scoped commands** — Per-file test/lint/typecheck commands over project-wide builds
- **Don't duplicate linters** — Code style lives in linter configs, not AGENTS.md

## Required Sections

### Package Manager
Which tool and key commands only:
```markdown
## Package Manager
Use **pnpm**: `pnpm install`, `pnpm dev`, `pnpm test`
```

### File-Scoped Commands
Per-file commands are faster and cheaper than full project builds. Always include when available:
```markdown
## File-Scoped Commands
| Task | Command |
|------|---------|
| Typecheck | `pnpm tsc --noEmit path/to/file.ts` |
| Lint | `pnpm eslint path/to/file.ts` |
| Test | `pnpm jest path/to/file.test.ts` |
```

### Commit Attribution
Always include this section. Agents should use their own identity:
```markdown
## Commit Attribution
AI commits MUST include:
```
Co-Authored-By: (the agent model's name and attribution byline)
```
Example: `Co-Authored-By: AI assistant Sonnet 4 <noreply@example.com>`
```

### Key Conventions
Project-specific patterns agents must follow. Keep brief.

## Optional Sections

Add only if truly needed:
- API route patterns (show template, not explanation)
- CLI commands (table format)
- File naming conventions
- Project structure hints (point to critical files, flag legacy code to avoid)
- Monorepo overrides (subdirectory `AGENTS.md` files override root)

## Anti-Patterns

Omit these:
- "Welcome to..." or "This document explains..."
- "You should..." or "Remember to..."
- Linter/formatter rules already in config files (`.eslintrc`, `biome.json`, `ruff.toml`)
- Listing installed skills or plugins (agents discover these automatically)
- Full project-wide build commands when file-scoped alternatives exist
- Obvious instructions ("run tests", "write clean code")
- Explanations of why (just say what)
- Long prose paragraphs

## Example Structure

```markdown
# Agent Instructions

## Package Manager
Use **pnpm**: `pnpm install`, `pnpm dev`

## Commit Attribution
AI commits MUST include:
```
Co-Authored-By: (the agent model's name and attribution byline)
```

## File-Scoped Commands
| Task | Command |
|------|---------|
| Typecheck | `pnpm tsc --noEmit path/to/file.ts` |
| Lint | `pnpm eslint path/to/file.ts` |
| Test | `pnpm jest path/to/file.test.ts` |

## API Routes
[Template code block]

## CLI
| Command | Description |
|---------|-------------|
| `pnpm cli sync` | Sync data |
```

## Imported Module: Ai Agent Development
---
name: ai-agent-development
description: "AI agent development workflow for building autonomous agents, multi-agent systems, and agent orchestration with CrewAI, LangGraph, and custom agents."
category: granular-workflow-bundle
risk: safe
source: personal
date_added: "2026-02-27"
---

# AI Agent Development Workflow

## Overview

Specialized workflow for building AI agents including single autonomous agents, multi-agent systems, agent orchestration, tool integration, and human-in-the-loop patterns.

## When to Use This Workflow

Use this workflow when:
- Building autonomous AI agents
- Creating multi-agent systems
- Implementing agent orchestration
- Adding tool integration to agents
- Setting up agent memory

## Workflow Phases

### Phase 1: Agent Design

#### Skills to Invoke
- `ai-agents-architect` - Agent architecture
- `autonomous-agents` - Autonomous patterns

#### Actions
1. Define agent purpose
2. Design agent capabilities
3. Plan tool integration
4. Design memory system
5. Define success metrics

#### Copy-Paste Prompts
```
Use @ai-agents-architect to design AI agent architecture
```

### Phase 2: Single Agent Implementation

#### Skills to Invoke
- `autonomous-agent-patterns` - Agent patterns
- `autonomous-agents` - Autonomous agents

#### Actions
1. Choose agent framework
2. Implement agent logic
3. Add tool integration
4. Configure memory
5. Test agent behavior

#### Copy-Paste Prompts
```
Use @autonomous-agent-patterns to implement single agent
```

### Phase 3: Multi-Agent System

#### Skills to Invoke
- `crewai` - CrewAI framework
- `multi-agent-patterns` - Multi-agent patterns

#### Actions
1. Define agent roles
2. Set up agent communication
3. Configure orchestration
4. Implement task delegation
5. Test coordination

#### Copy-Paste Prompts
```
Use @crewai to build multi-agent system with roles
```

### Phase 4: Agent Orchestration

#### Skills to Invoke
- `langgraph` - LangGraph orchestration
- `workflow-orchestration-patterns` - Orchestration

#### Actions
1. Design workflow graph
2. Implement state management
3. Add conditional branches
4. Configure persistence
5. Test workflows

#### Copy-Paste Prompts
```
Use @langgraph to create stateful agent workflows
```

### Phase 5: Tool Integration

#### Skills to Invoke
- `agent-tool-builder` - Tool building
- `tool-design` - Tool design

#### Actions
1. Identify tool needs
2. Design tool interfaces
3. Implement tools
4. Add error handling
5. Test tool usage

#### Copy-Paste Prompts
```
Use @agent-tool-builder to create agent tools
```

### Phase 6: Memory Systems

#### Skills to Invoke
- `agent-memory-systems` - Memory architecture
- `conversation-memory` - Conversation memory

#### Actions
1. Design memory structure
2. Implement short-term memory
3. Set up long-term memory
4. Add entity memory
5. Test memory retrieval

#### Copy-Paste Prompts
```
Use @agent-memory-systems to implement agent memory
```

### Phase 7: Evaluation

#### Skills to Invoke
- `agent-evaluation` - Agent evaluation
- `evaluation` - AI evaluation

#### Actions
1. Define evaluation criteria
2. Create test scenarios
3. Measure agent performance
4. Test edge cases
5. Iterate improvements

#### Copy-Paste Prompts
```
Use @agent-evaluation to evaluate agent performance
```

## Agent Architecture

```
User Input -> Planner -> Agent -> Tools -> Memory -> Response
              |          |        |        |
         Decompose   LLM Core  Actions  Short/Long-term
```

## Quality Gates

- [ ] Agent logic working
- [ ] Tools integrated
- [ ] Memory functional
- [ ] Orchestration tested
- [ ] Evaluation passing

## Related Workflow Bundles

- `ai-ml` - AI/ML development
- `rag-implementation` - RAG systems
- `workflow-automation` - Workflow patterns

## Imported Module: Autonomous Agent Patterns
---
name: autonomous-agent-patterns
description: "Design patterns for building autonomous coding agents. Covers tool integration, permission systems, browser automation, and human-in-the-loop workflows. Use when building AI agents, designing tool ..."
risk: unknown
source: community
date_added: "2026-02-27"
---

# 🕹️ Autonomous Agent Patterns

> Design patterns for building autonomous coding agents, inspired by autonomous coding agents.

## When to Use This Skill

Use this skill when:

- Building autonomous AI agents
- Designing tool/function calling APIs
- Implementing permission and approval systems
- Creating browser automation for agents
- Designing human-in-the-loop workflows

---

## 1. Core Agent Architecture

### 1.1 Agent Loop

```
┌─────────────────────────────────────────────────────────────┐
│                     AGENT LOOP                               │
│                                                              │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐              │
│  │  Think   │───▶│  Decide  │───▶│   Act    │              │
│  │ (Reason) │    │ (Plan)   │    │ (Execute)│              │
│  └──────────┘    └──────────┘    └──────────┘              │
│       ▲                               │                     │
│       │         ┌──────────┐          │                     │
│       └─────────│ Observe  │◀─────────┘                     │
│                 │ (Result) │                                │
│                 └──────────┘                                │
└─────────────────────────────────────────────────────────────┘
```

```python
class AgentLoop:
    def __init__(self, llm, tools, max_iterations=50):
        self.llm = llm
        self.tools = {t.name: t for t in tools}
        self.max_iterations = max_iterations
        self.history = []

    def run(self, task: str) -> str:
        self.history.append({"role": "user", "content": task})

        for i in range(self.max_iterations):
            # Think: Get LLM response with tool options
            response = self.llm.chat(
                messages=self.history,
                tools=self._format_tools(),
                tool_choice="auto"
            )

            # Decide: Check if agent wants to use a tool
            if response.tool_calls:
                for tool_call in response.tool_calls:
                    # Act: Execute the tool
                    result = self._execute_tool(tool_call)

                    # Observe: Add result to history
                    self.history.append({
                        "role": "tool",
                        "tool_call_id": tool_call.id,
                        "content": str(result)
                    })
            else:
                # No more tool calls = task complete
                return response.content

        return "Max iterations reached"

    def _execute_tool(self, tool_call) -> Any:
        tool = self.tools[tool_call.name]
        args = json.loads(tool_call.arguments)
        return tool.execute(**args)
```

### 1.2 Multi-Model Architecture

```python
class MultiModelAgent:
    """
    Use different models for different purposes:
    - Fast model for planning
    - Powerful model for complex reasoning
    - Specialized model for code generation
    """

    def __init__(self):
        self.models = {
            "fast": "gpt-3.5-turbo",      # Quick decisions
            "smart": "gpt-4-turbo",        # Complex reasoning
            "code": "example-model",     # Code generation
        }

    def select_model(self, task_type: str) -> str:
        if task_type == "planning":
            return self.models["fast"]
        elif task_type == "analysis":
            return self.models["smart"]
        elif task_type == "code":
            return self.models["code"]
        return self.models["smart"]
```

---

## 2. Tool Design Patterns

### 2.1 Tool Schema

```python
class Tool:
    """Base class for agent tools"""

    @property
    def schema(self) -> dict:
        """JSON Schema for the tool"""
        return {
            "name": self.name,
            "description": self.description,
            "parameters": {
                "type": "object",
                "properties": self._get_parameters(),
                "required": self._get_required()
            }
        }

    def execute(self, **kwargs) -> ToolResult:
        """Execute the tool and return result"""
        raise NotImplementedError

class ReadFileTool(Tool):
    name = "read_file"
    description = "Read the contents of a file from the filesystem"

    def _get_parameters(self):
        return {
            "path": {
                "type": "string",
                "description": "Absolute path to the file"
            },
            "start_line": {
                "type": "integer",
                "description": "Line to start reading from (1-indexed)"
            },
            "end_line": {
                "type": "integer",
                "description": "Line to stop reading at (inclusive)"
            }
        }

    def _get_required(self):
        return ["path"]

    def execute(self, path: str, start_line: int = None, end_line: int = None) -> ToolResult:
        try:
            with open(path, 'r') as f:
                lines = f.readlines()

            if start_line and end_line:
                lines = lines[start_line-1:end_line]

            return ToolResult(
                success=True,
                output="".join(lines)
            )
        except FileNotFoundError:
            return ToolResult(
                success=False,
                error=f"File not found: {path}"
            )
```

### 2.2 Essential Agent Tools

```python
CODING_AGENT_TOOLS = {
    # File operations
    "read_file": "Read file contents",
    "write_file": "Create or overwrite a file",
    "edit_file": "Make targeted edits to a file",
    "list_directory": "List files and folders",
    "search_files": "Search for files by pattern",

    # Code understanding
    "search_code": "Search for code patterns (grep)",
    "get_definition": "Find function/class definition",
    "get_references": "Find all references to a symbol",

    # Terminal
    "run_command": "Execute a shell command",
    "read_output": "Read command output",
    "send_input": "Send input to running command",

    # Browser (optional)
    "open_browser": "Open URL in browser",
    "click_element": "Click on page element",
    "type_text": "Type text into input",
    "screenshot": "Capture screenshot",

    # Context
    "ask_user": "Ask the user a question",
    "search_web": "Search the web for information"
}
```

### 2.3 Edit Tool Design

```python
class EditFileTool(Tool):
    """
    Precise file editing with conflict detection.
    Uses search/replace pattern for reliable edits.
    """

    name = "edit_file"
    description = "Edit a file by replacing specific content"

    def execute(
        self,
        path: str,
        search: str,
        replace: str,
        expected_occurrences: int = 1
    ) -> ToolResult:
        """
        Args:
            path: File to edit
            search: Exact text to find (must match exactly, including whitespace)
            replace: Text to replace with
            expected_occurrences: How many times search should appear (validation)
        """
        with open(path, 'r') as f:
            content = f.read()

        # Validate
        actual_occurrences = content.count(search)
        if actual_occurrences != expected_occurrences:
            return ToolResult(
                success=False,
                error=f"Expected {expected_occurrences} occurrences, found {actual_occurrences}"
            )

        if actual_occurrences == 0:
            return ToolResult(
                success=False,
                error="Search text not found in file"
            )

        # Apply edit
        new_content = content.replace(search, replace)

        with open(path, 'w') as f:
            f.write(new_content)

        return ToolResult(
            success=True,
            output=f"Replaced {actual_occurrences} occurrence(s)"
        )
```

---

## 3. Permission & Safety Patterns

### 3.1 Permission Levels

```python
class PermissionLevel(Enum):
    # Fully automatic - no user approval needed
    AUTO = "auto"

    # Ask once per session
    ASK_ONCE = "ask_once"

    # Ask every time
    ASK_EACH = "ask_each"

    # Never allow
    NEVER = "never"

PERMISSION_CONFIG = {
    # Low risk - can auto-approve
    "read_file": PermissionLevel.AUTO,
    "list_directory": PermissionLevel.AUTO,
    "search_code": PermissionLevel.AUTO,

    # Medium risk - ask once
    "write_file": PermissionLevel.ASK_ONCE,
    "edit_file": PermissionLevel.ASK_ONCE,

    # High risk - ask each time
    "run_command": PermissionLevel.ASK_EACH,
    "delete_file": PermissionLevel.ASK_EACH,

    # Dangerous - never auto-approve
    "sudo_command": PermissionLevel.NEVER,
    "format_disk": PermissionLevel.NEVER
}
```

### 3.2 Approval UI Pattern

```python
class ApprovalManager:
    def __init__(self, ui, config):
        self.ui = ui
        self.config = config
        self.session_approvals = {}

    def request_approval(self, tool_name: str, args: dict) -> bool:
        level = self.config.get(tool_name, PermissionLevel.ASK_EACH)

        if level == PermissionLevel.AUTO:
            return True

        if level == PermissionLevel.NEVER:
            self.ui.show_error(f"Tool '{tool_name}' is not allowed")
            return False

        if level == PermissionLevel.ASK_ONCE:
            if tool_name in self.session_approvals:
                return self.session_approvals[tool_name]

        # Show approval dialog
        approved = self.ui.show_approval_dialog(
            tool=tool_name,
            args=args,
            risk_level=self._assess_risk(tool_name, args)
        )

        if level == PermissionLevel.ASK_ONCE:
            self.session_approvals[tool_name] = approved

        return approved

    def _assess_risk(self, tool_name: str, args: dict) -> str:
        """Analyze specific call for risk level"""
        if tool_name == "run_command":
            cmd = args.get("command", "")
            if any(danger in cmd for danger in ["rm -rf", "sudo", "chmod"]):
                return "HIGH"
        return "MEDIUM"
```

### 3.3 Sandboxing

```python
class SandboxedExecution:
    """
    Execute code/commands in isolated environment
    """

    def __init__(self, workspace_dir: str):
        self.workspace = workspace_dir
        self.allowed_commands = ["npm", "python", "node", "git", "ls", "cat"]
        self.blocked_paths = ["/etc", "/usr", "/bin", os.path.expanduser("~")]

    def validate_path(self, path: str) -> bool:
        """Ensure path is within workspace"""
        real_path = os.path.realpath(path)
        workspace_real = os.path.realpath(self.workspace)
        return real_path.startswith(workspace_real)

    def validate_command(self, command: str) -> bool:
        """Check if command is allowed"""
        cmd_parts = shlex.split(command)
        if not cmd_parts:
            return False

        base_cmd = cmd_parts[0]
        return base_cmd in self.allowed_commands

    def execute_sandboxed(self, command: str) -> ToolResult:
        if not self.validate_command(command):
            return ToolResult(
                success=False,
                error=f"Command not allowed: {command}"
            )

        # Execute in isolated environment
        result = subprocess.run(
            command,
            shell=True,
            cwd=self.workspace,
            capture_output=True,
            timeout=30,
            env={
                **os.environ,
                "HOME": self.workspace,  # Isolate home directory
            }
        )

        return ToolResult(
            success=result.returncode == 0,
            output=result.stdout.decode(),
            error=result.stderr.decode() if result.returncode != 0 else None
        )
```

---

## 4. Browser Automation

### 4.1 Browser Tool Pattern

```python
class BrowserTool:
    """
    Browser automation for agents using Playwright/Puppeteer.
    Enables visual debugging and web testing.
    """

    def __init__(self, headless: bool = True):
        self.browser = None
        self.page = None
        self.headless = headless

    async def open_url(self, url: str) -> ToolResult:
        """Navigate to URL and return page info"""
        if not self.browser:
            self.browser = await playwright.chromium.launch(headless=self.headless)
            self.page = await self.browser.new_page()

        await self.page.goto(url)

        # Capture state
        screenshot = await self.page.screenshot(type='png')
        title = await self.page.title()

        return ToolResult(
            success=True,
            output=f"Loaded: {title}",
            metadata={
                "screenshot": base64.b64encode(screenshot).decode(),
                "url": self.page.url
            }
        )

    async def click(self, selector: str) -> ToolResult:
        """Click on an element"""
        try:
            await self.page.click(selector, timeout=5000)
            await self.page.wait_for_load_state("networkidle")

            screenshot = await self.page.screenshot()
            return ToolResult(
                success=True,
                output=f"Clicked: {selector}",
                metadata={"screenshot": base64.b64encode(screenshot).decode()}
            )
        except TimeoutError:
            return ToolResult(
                success=False,
                error=f"Element not found: {selector}"
            )

    async def type_text(self, selector: str, text: str) -> ToolResult:
        """Type text into an input"""
        await self.page.fill(selector, text)
        return ToolResult(success=True, output=f"Typed into {selector}")

    async def get_page_content(self) -> ToolResult:
        """Get accessible text content of the page"""
        content = await self.page.evaluate("""
            () => {
                // Get visible text
                const walker = document.createTreeWalker(
                    document.body,
                    NodeFilter.SHOW_TEXT,
                    null,
                    false
                );

                let text = '';
                while (walker.nextNode()) {
                    const node = walker.currentNode;
                    if (node.textContent.trim()) {
                        text += node.textContent.trim() + '\\n';
                    }
                }
                return text;
            }
        """)
        return ToolResult(success=True, output=content)
```

### 4.2 Visual Agent Pattern

```python
class VisualAgent:
    """
    Agent that uses screenshots to understand web pages.
    Can identify elements visually without selectors.
    """

    def __init__(self, llm, browser):
        self.llm = llm
        self.browser = browser

    async def describe_page(self) -> str:
        """Use vision model to describe current page"""
        screenshot = await self.browser.screenshot()

        response = self.llm.chat([
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "Describe this webpage. List all interactive elements you see."},
                    {"type": "image", "data": screenshot}
                ]
            }
        ])

        return response.content

    async def find_and_click(self, description: str) -> ToolResult:
        """Find element by visual description and click it"""
        screenshot = await self.browser.screenshot()

        # Ask vision model to find element
        response = self.llm.chat([
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": f"""
                        Find the element matching: "{description}"
                        Return the approximate coordinates as JSON: {{"x": number, "y": number}}
                        """
                    },
                    {"type": "image", "data": screenshot}
                ]
            }
        ])

        coords = json.loads(response.content)
        await self.browser.page.mouse.click(coords["x"], coords["y"])

        return ToolResult(success=True, output=f"Clicked at ({coords['x']}, {coords['y']})")
```

---

## 5. Context Management

### 5.1 Context Injection Patterns

````python
class ContextManager:
    """
    Manage context provided to the agent.
    Inspired by Cline's @-mention patterns.
    """

    def __init__(self, workspace: str):
        self.workspace = workspace
        self.context = []

    def add_file(self, path: str) -> None:
        """@file - Add file contents to context"""
        with open(path, 'r') as f:
            content = f.read()

        self.context.append({
            "type": "file",
            "path": path,
            "content": content
        })

    def add_folder(self, path: str, max_files: int = 20) -> None:
        """@folder - Add all files in folder"""
        for root, dirs, files in os.walk(path):
            for file in files[:max_files]:
                file_path = os.path.join(root, file)
                self.add_file(file_path)

    def add_url(self, url: str) -> None:
        """@url - Fetch and add URL content"""
        response = requests.get(url)
        content = html_to_markdown(response.text)

        self.context.append({
            "type": "url",
            "url": url,
            "content": content
        })

    def add_problems(self, diagnostics: list) -> None:
        """@problems - Add IDE diagnostics"""
        self.context.append({
            "type": "diagnostics",
            "problems": diagnostics
        })

    def format_for_prompt(self) -> str:
        """Format all context for LLM prompt"""
        parts = []
        for item in self.context:
            if item["type"] == "file":
                parts.append(f"## File: {item['path']}\n```\n{item['content']}\n```")
            elif item["type"] == "url":
                parts.append(f"## URL: {item['url']}\n{item['content']}")
            elif item["type"] == "diagnostics":
                parts.append(f"## Problems:\n{json.dumps(item['problems'], indent=2)}")

        return "\n\n".join(parts)
````

### 5.2 Checkpoint/Resume

```python
class CheckpointManager:
    """
    Save and restore agent state for long-running tasks.
    """

    def __init__(self, storage_dir: str):
        self.storage_dir = storage_dir
        os.makedirs(storage_dir, exist_ok=True)

    def save_checkpoint(self, session_id: str, state: dict) -> str:
        """Save current agent state"""
        checkpoint = {
            "timestamp": datetime.now().isoformat(),
            "session_id": session_id,
            "history": state["history"],
            "context": state["context"],
            "workspace_state": self._capture_workspace(state["workspace"]),
            "metadata": state.get("metadata", {})
        }

        path = os.path.join(self.storage_dir, f"{session_id}.json")
        with open(path, 'w') as f:
            json.dump(checkpoint, f, indent=2)

        return path

    def restore_checkpoint(self, checkpoint_path: str) -> dict:
        """Restore agent state from checkpoint"""
        with open(checkpoint_path, 'r') as f:
            checkpoint = json.load(f)

        return {
            "history": checkpoint["history"],
            "context": checkpoint["context"],
            "workspace": self._restore_workspace(checkpoint["workspace_state"]),
            "metadata": checkpoint["metadata"]
        }

    def _capture_workspace(self, workspace: str) -> dict:
        """Capture relevant workspace state"""
        # Git status, file hashes, etc.
        return {
            "git_ref": subprocess.getoutput(f"cd {workspace} && git rev-parse HEAD"),
            "git_dirty": subprocess.getoutput(f"cd {workspace} && git status --porcelain")
        }
```

---

## 6. MCP (Model Context Protocol) Integration

### 6.1 MCP Server Pattern

```python
from mcp import Server, Tool

class MCPAgent:
    """
    Agent that can dynamically discover and use MCP tools.
    'Add a tool that...' pattern from Cline.
    """

    def __init__(self, llm):
        self.llm = llm
        self.mcp_servers = {}
        self.available_tools = {}

    def connect_server(self, name: str, config: dict) -> None:
        """Connect to an MCP server"""
        server = Server(config)
        self.mcp_servers[name] = server

        # Discover tools
        tools = server.list_tools()
        for tool in tools:
            self.available_tools[tool.name] = {
                "server": name,
                "schema": tool.schema
            }

    async def create_tool(self, description: str) -> str:
        """
        Create a new MCP server based on user description.
        'Add a tool that fetches Jira tickets'
        """
        # Generate MCP server code
        code = self.llm.generate(f"""
        Create a Python MCP server with a tool that does:
        {description}

        Use the FastMCP framework. Include proper error handling.
        Return only the Python code.
        """)

        # Save and install
        server_name = self._extract_name(description)
        path = f"./mcp_servers/{server_name}/server.py"

        with open(path, 'w') as f:
            f.write(code)

        # Hot-reload
        self.connect_server(server_name, {"path": path})

        return f"Created tool: {server_name}"
```

---

## Best Practices Checklist

### Agent Design

- [ ] Clear task decomposition
- [ ] Appropriate tool granularity
- [ ] Error handling at each step
- [ ] Progress visibility to user

### Safety

- [ ] Permission system implemented
- [ ] Dangerous operations blocked
- [ ] Sandbox for untrusted code
- [ ] Audit logging enabled

### UX

- [ ] Approval UI is clear
- [ ] Progress updates provided
- [ ] Undo/rollback available
- [ ] Explanation of actions

---

## Resources

- [Cline](https://github.com/cline/cline)
- code-generation agent
- [Model Context Protocol](https://modelcontextprotocol.io/)
- provider tool-use documentation

## Imported Module: Autonomous Agents
---
name: autonomous-agents
description: "Autonomous agents are AI systems that can independently decompose goals, plan actions, execute tools, and self-correct without constant human guidance. The challenge isn't making them capable - it'..."
risk: unknown
source: "vibeship-spawner-skills (Apache 2.0)"
date_added: "2026-02-27"
---

# Autonomous Agents

You are an agent architect who has learned the hard lessons of autonomous AI.
You've seen the gap between impressive demos and production disasters. You know
that a 95% success rate per step means only 60% by step 10.

Your core insight: Autonomy is earned, not granted. Start with heavily
constrained agents that do one thing reliably. Add autonomy only as you prove
reliability. The best agents look less impressive but work consistently.

You push for guardrails before capabilities, logging befor

## Capabilities

- autonomous-agents
- agent-loops
- goal-decomposition
- self-correction
- reflection-patterns
- react-pattern
- plan-execute
- agent-reliability
- agent-guardrails

## Patterns

### ReAct Agent Loop

Alternating reasoning and action steps

### Plan-Execute Pattern

Separate planning phase from execution

### Reflection Pattern

Self-evaluation and iterative improvement

## Anti-Patterns

### ❌ Unbounded Autonomy

### ❌ Trusting Agent Outputs

### ❌ General-Purpose Autonomy

## ⚠️ Sharp Edges

| Issue | Severity | Solution |
|-------|----------|----------|
| Issue | critical | ## Reduce step count |
| Issue | critical | ## Set hard cost limits |
| Issue | critical | ## Test at scale before production |
| Issue | high | ## Validate against ground truth |
| Issue | high | ## Build robust API clients |
| Issue | high | ## Least privilege principle |
| Issue | medium | ## Track context usage |
| Issue | medium | ## Structured logging |

## Related Skills

Works well with: `agent-tool-builder`, `agent-memory-systems`, `multi-agent-orchestration`, `agent-evaluation`

## When to Use
This skill is applicable to execute the workflow or actions described in the overview.

## Imported Module: Computer Use Agents
---
name: computer-use-agents
description: "Build AI agents that interact with computers like humans do - viewing screens, moving cursors, clicking buttons, and typing text. Covers Anthropic's Computer Use, OpenAI's Operator/CUA, and open-so..."
risk: unknown
source: "vibeship-spawner-skills (Apache 2.0)"
date_added: "2026-02-27"
---

# Computer Use Agents

## Patterns

### Perception-Reasoning-Action Loop

The fundamental architecture of computer use agents: observe screen,
reason about next action, execute action, repeat. This loop integrates
vision models with action execution through an iterative pipeline.

Key components:
1. PERCEPTION: Screenshot captures current screen state
2. REASONING: Vision-language model analyzes and plans
3. ACTION: Execute mouse/keyboard operations
4. FEEDBACK: Observe result, continue or correct

Critical insight: Vision agents are completely still during "thinking"
phase (1-5 seconds), creating a detectable pause pattern.


**When to use**: ['Building any computer use agent from scratch', 'Integrating vision models with desktop control', 'Understanding agent behavior patterns']

```python
from llm_provider import LLMClient
from PIL import Image
import base64
import pyautogui
import time

class ComputerUseAgent:
    """
    Perception-Reasoning-Action loop implementation.
    Based on Anthropic Computer Use patterns.
    """

    def __init__(self, client: Anthropic, model: str = "example-balanced-model"):
        self.client = client
        self.model = model
        self.max_steps = 50  # Prevent runaway loops
        self.action_delay = 0.5  # Seconds between actions

    def capture_screenshot(self) -> str:
        """Capture screen and return base64 encoded image."""
        screenshot = pyautogui.screenshot()
        # Resize for token efficiency (1280x800 is good balance)
        screenshot = screenshot.resize((1280, 800), Image.LANCZOS)

        import io
        buffer = io.BytesIO()
        screenshot.save(buffer, format="PNG")
        return base64.b64encode(buffer.getvalue()).decode()

    def execute_action(self, action: dict) -> dict:
        """Execute mouse/keyboard action on the computer."""
        action_type = action.get("type")

        if action_type == "click":
            x, y = action["x"], action["y"]
            button = action.get("button", "left")
            pyautogui.click(x, y, button=button)
            return {"success": True, "action": f"clicked at ({x}, {y})"}

        elif action_type == "type":
            text = action["text"]
            pyautogui.typewrite(text, interval=0.02)
            return {"success": True, "action": f"typed {len(text)} chars"}

        elif action_type == "key":
            key = action["key"]
            pyautogui.press(key)
            return {"success": True, "action": f"pressed {key}"}

        elif action_type == "scroll":
            direction = action.get("direction", "down")
            amount = action.get("amount", 3)
            scroll = -amount if direction == "down" else amount
            pyautogui.scroll(scroll)
            return {"success": True, "action": f"scrolled {dir
```

### Sandboxed Environment Pattern

Computer use agents MUST run in isolated, sandboxed environments.
Never give agents direct access to your main system - the security
risks are too high. Use Docker containers with virtual desktops.

Key isolation requirements:
1. NETWORK: Restrict to necessary endpoints only
2. FILESYSTEM: Read-only or scoped to temp directories
3. CREDENTIALS: No access to host credentials
4. SYSCALLS: Filter dangerous system calls
5. RESOURCES: Limit CPU, memory, time

The goal is "blast radius minimization" - if the agent goes wrong,
damage is contained to the sandbox.


**When to use**: ['Deploying any computer use agent', 'Testing agent behavior safely', 'Running untrusted automation tasks']

```python
# Dockerfile for sandboxed computer use environment
# Based on Anthropic's reference implementation pattern

FROM ubuntu:22.04

# Install desktop environment
RUN apt-get update && apt-get install -y \
    xvfb \
    x11vnc \
    fluxbox \
    xterm \
    firefox \
    python3 \
    python3-pip \
    supervisor

# Security: Create non-root user
RUN useradd -m -s /bin/bash agent && \
    mkdir -p /home/agent/.vnc

# Install Python dependencies
COPY requirements.txt /tmp/
RUN pip3 install -r /tmp/requirements.txt

# Security: Drop capabilities
RUN apt-get install -y --no-install-recommends libcap2-bin && \
    setcap -r /usr/bin/python3 || true

# Copy agent code
COPY --chown=agent:agent . /app
WORKDIR /app

# Supervisor config for virtual display + VNC
COPY supervisord.conf /etc/supervisor/conf.d/

# Expose VNC port only (not desktop directly)
EXPOSE 5900

# Run as non-root
USER agent

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]

---

# docker-compose.yml with security constraints
version: '3.8'

services:
  computer-use-agent:
    build: .
    ports:
      - "5900:5900"  # VNC for observation
      - "8080:8080"  # API for control

    # Security constraints
    security_opt:
      - no-new-privileges:true
      - seccomp:seccomp-profile.json

    # Resource limits
    deploy:
      resources:
        limits:
          cpus: '2'
          memory: 4G
        reservations:
          cpus: '0.5'
          memory: 1G

    # Network isolation
    networks:
      - agent-network

    # No access to host filesystem
    volumes:
      - agent-tmp:/tmp

    # Read-only root filesystem
    read_only: true
    tmpfs:
      - /run
      - /var/run

    # Environment
    environment:
      - DISPLAY=:99
      - NO_PROXY=localhost

networks:
  agent-network:
    driver: bridge
    internal: true  # No internet by default

volumes:
  agent-tmp:

---

# Python wrapper with additional runtime sandboxing
import subprocess
import os
from dataclasses im
```

### Anthropic Computer Use Implementation

Official implementation pattern using AI assistant's computer use capability.
AI assistant 3.5 Sonnet was the first frontier model to offer computer use.
AI assistant Opus 4.5 is now the "best model in the world for computer use."

Key capabilities:
- screenshot: Capture current screen state
- mouse: Click, move, drag operations
- keyboard: Type text, press keys
- bash: Run shell commands
- text_editor: View and edit files

Tool versions:
- computer_20251124 (Opus 4.5): Adds zoom action for detailed inspection
- computer_20250124 (All other models): Standard capabilities

Critical limitation: "Some UI elements (like dropdowns and scrollbars)
might be tricky for AI assistant to manipulate" - Anthropic docs


**When to use**: ['Building production computer use agents', 'Need highest quality vision understanding', 'Full desktop control (not just browser)']

```python
from llm_provider import LLMClient
from anthropic.types.beta import (
    BetaToolComputerUse20241022,
    BetaToolBash20241022,
    BetaToolTextEditor20241022,
)
import subprocess
import base64
from PIL import Image
import io

class AnthropicComputerUse:
    """
    Official Anthropic Computer Use implementation.

    Requires:
    - Docker container with virtual display
    - VNC for viewing agent actions
    - Proper tool implementations
    """

    def __init__(self):
        self.client = LLMClient()
        self.model = "example-balanced-model"  # Best for computer use
        self.screen_size = (1280, 800)

    def get_tools(self) -> list:
        """Define computer use tools."""
        return [
            BetaToolComputerUse20241022(
                type="computer_20241022",
                name="computer",
                display_width_px=self.screen_size[0],
                display_height_px=self.screen_size[1],
            ),
            BetaToolBash20241022(
                type="bash_20241022",
                name="bash",
            ),
            BetaToolTextEditor20241022(
                type="text_editor_20241022",
                name="str_replace_editor",
            ),
        ]

    def execute_tool(self, name: str, input: dict) -> dict:
        """Execute a tool and return result."""

        if name == "computer":
            return self._handle_computer_action(input)
        elif name == "bash":
            return self._handle_bash(input)
        elif name == "str_replace_editor":
            return self._handle_editor(input)
        else:
            return {"error": f"Unknown tool: {name}"}

    def _handle_computer_action(self, input: dict) -> dict:
        """Handle computer control actions."""
        action = input.get("action")

        if action == "screenshot":
            # Capture via xdotool/scrot
            subprocess.run(["scrot", "/tmp/screenshot.png"])

            with open("/tmp/screenshot.png", "rb") as f:
            
```

## ⚠️ Sharp Edges

| Issue | Severity | Solution |
|-------|----------|----------|
| Issue | critical | ## Defense in depth - no single solution works |
| Issue | medium | ## Add human-like variance to actions |
| Issue | high | ## Use keyboard alternatives when possible |
| Issue | medium | ## Accept the tradeoff |
| Issue | high | ## Implement context management |
| Issue | high | ## Monitor and limit costs |
| Issue | critical | ## ALWAYS use sandboxing |

## When to Use
This skill is applicable to execute the workflow or actions described in the overview.

## Imported Module: Hosted Agents
---
name: hosted-agents
description: Build background agents in sandboxed environments. Use for hosted coding agents, sandboxed VMs, Modal sandboxes, and remote coding environments.
risk: unknown
source: community
---

# Hosted Agent Infrastructure

Hosted agents run in remote sandboxed environments rather than on local machines. When designed well, they provide unlimited concurrency, consistent execution environments, and multiplayer collaboration. The critical insight is that session speed should be limited only by model provider time-to-first-token, with all infrastructure setup completed before the user starts their session.

## When to Activate

Activate this skill when:
- Building background coding agents that run independently of user devices
- Designing sandboxed execution environments for agent workloads
- Implementing multiplayer agent sessions with shared state
- Creating multi-client agent interfaces (Slack, Web, Chrome extensions)
- Scaling agent infrastructure beyond local machine constraints
- Building systems where agents spawn sub-agents for parallel work

## Core Concepts

Hosted agents address the fundamental limitation of local agent execution: resource contention, environment inconsistency, and single-user constraints. By moving agent execution to remote sandboxed environments, teams gain unlimited concurrency, reproducible environments, and collaborative workflows.

The architecture consists of three layers: sandbox infrastructure for isolated execution, API layer for state management and client coordination, and client interfaces for user interaction across platforms. Each layer has specific design requirements that enable the system to scale.

## Detailed Topics

### Sandbox Infrastructure

**The Core Challenge**
Spinning up full development environments quickly is the primary technical challenge. Users expect near-instant session starts, but development environments require cloning repositories, installing dependencies, and running build steps.

**Image Registry Pattern**
Pre-build environment images on a regular cadence (every 30 minutes works well). Each image contains:
- Cloned repository at a known commit
- All runtime dependencies installed
- Initial setup and build commands completed
- Cached files from running app and test suite once

When starting a session, spin up a sandbox from the most recent image. The repository is at most 30 minutes out of date, making synchronization with the latest code much faster.

**Snapshot and Restore**
Take filesystem snapshots at key points:
- After initial image build (base snapshot)
- When agent finishes making changes (session snapshot)
- Before sandbox exit for potential follow-up

This enables instant restoration for follow-up prompts without re-running setup.

**Git Configuration for Background Agents**
Since git operations are not tied to a specific user during image builds:
- Generate GitHub app installation tokens for repository access during clone
- Update git config's `user.name` and `user.email` when committing and pushing changes
- Use the prompting user's identity for commits, not the app identity

**Warm Pool Strategy**
Maintain a pool of pre-warmed sandboxes for high-volume repositories:
- Sandboxes are ready before users start sessions
- Expire and recreate pool entries as new image builds complete
- Start warming sandbox as soon as user begins typing (predictive warm-up)

### Agent Framework Selection

**Server-First Architecture**
Choose an agent framework structured as a server first, with TUI and desktop apps as clients. This enables:
- Multiple custom clients without duplicating agent logic
- Consistent behavior across all interaction surfaces
- Plugin systems for extending functionality
- Event-driven architectures for real-time updates

**Code as Source of Truth**
Select frameworks where the agent can read its own source code to understand behavior. This is underrated in AI development: having the code as source of truth prevents hallucination about the agent's own capabilities.

**Plugin System Requirements**
The framework should support plugins that:
- Listen to tool execution events (e.g., `tool.execute.before`)
- Block or modify tool calls conditionally
- Inject context or state at runtime

### Speed Optimizations

**Predictive Warm-Up**
Start warming the sandbox as soon as a user begins typing their prompt:
- Clone latest changes in parallel with user typing
- Run initial setup before user hits enter
- For fast spin-up, sandbox can be ready before user finishes typing

**Parallel File Reading**
Allow the agent to start reading files immediately, even if sync from latest base branch is not complete:
- In large repositories, incoming prompts rarely modify recently-changed files
- Agent can research immediately without waiting for git sync
- Block file edits (not reads) until synchronization completes

**Maximize Build-Time Work**
Move everything possible to the image build step:
- Full dependency installation
- Database schema setup
- Initial app and test suite runs (populates caches)
- Build-time duration is invisible to users

### Self-Spawning Agents

**Agent-Spawned Sessions**
Create tools that allow agents to spawn new sessions:
- Research tasks across different repositories
- Parallel subtask execution for large changes
- Multiple smaller PRs from one major task

Frontier models are capable of containing themselves. The tools should:
- Start a new session with specified parameters
- Read status of any session (check-in capability)
- Continue main work while sub-sessions run in parallel

**Prompt Engineering for Self-Spawning**
Engineer prompts to guide when agents spawn sub-sessions:
- Research tasks that require cross-repository exploration
- Breaking monolithic changes into smaller PRs
- Parallel exploration of different approaches

### API Layer

**Per-Session State Isolation**
Each session requires its own isolated state storage:
- Dedicated database per session (SQLite per session works well)
- No session can impact another's performance
- Handles hundreds of concurrent sessions

**Real-Time Streaming**
Agent work involves high-frequency updates:
- Token streaming from model providers
- Tool execution status updates
- File change notifications

WebSocket connections with hibernation APIs reduce compute costs during idle periods while maintaining open connections.

**Synchronization Across Clients**
Build a single state system that synchronizes across:
- Chat interfaces
- Slack bots
- Chrome extensions
- Web interfaces
- VS Code instances

All changes sync to the session state, enabling seamless client switching.

### Multiplayer Support

**Why Multiplayer Matters**
Multiplayer enables:
- Teaching non-engineers to use AI effectively
- Live QA sessions with multiple team members
- Real-time PR review with immediate changes
- Collaborative debugging sessions

**Implementation Requirements**
- Data model must not tie sessions to single authors
- Pass authorship info to each prompt
- Attribute code changes to the prompting user
- Share session links for instant collaboration

With proper synchronization architecture, multiplayer support is nearly free to add.

### Authentication and Authorization

**User-Based Commits**
Use GitHub authentication to:
- Obtain user tokens for PR creation
- Open PRs on behalf of the user (not the app)
- Prevent users from approving their own changes

**Sandbox-to-API Flow**
1. Sandbox pushes changes (updating git user config)
2. Sandbox sends event to API with branch name and session ID
3. API uses user's GitHub token to create PR
4. GitHub webhooks notify API of PR events

### Client Implementations

**Slack Integration**
The most effective distribution channel for internal adoption:
- Creates virality loop as team members see others using it
- No syntax required, natural chat interface
- Classify repository from message, thread context, and channel name

Build a classifier to determine which repository to work in:
- Fast model with descriptions of available repositories
- Include hints for common repositories
- Allow "unknown" option for ambiguous cases

**Web Interface**
Core features:
- Works on desktop and mobile
- Real-time streaming of agent work
- Hosted VS Code instance running inside sandbox
- Streamed desktop view for visual verification
- Before/after screenshots for PRs

Statistics page showing:
- Sessions resulting in merged PRs (primary metric)
- Usage over time
- Live "humans prompting" count (prompts in last 5 minutes)

**Chrome Extension**
For non-engineering users:
- Sidebar chat interface with screenshot tool
- DOM and React internals extraction instead of raw images
- Reduces token usage while maintaining precision
- Distribute via managed device policy (bypasses Chrome Web Store)

## Practical Guidance

### Follow-Up Message Handling

Decide how to handle messages sent during execution:
- **Queue approach**: Messages wait until current prompt completes
- **Insert approach**: Messages are processed immediately

Queueing is simpler to manage and lets users send thoughts on next steps while agent works. Build mechanism to stop agent mid-execution when needed.

### Metrics That Matter

Track metrics that indicate real value:
- Sessions resulting in merged PRs (primary success metric)
- Time from session start to first model response
- PR approval rate and revision count
- Agent-written code percentage across repositories

### Adoption Strategy

Internal adoption patterns that work:
- Work in public spaces (Slack channels) for visibility
- Let the product create virality loops
- Don't force usage over existing tools
- Build to people's needs, not hypothetical requirements

## Guidelines

1. Pre-build environment images on regular cadence (30 minutes is a good default)
2. Start warming sandboxes when users begin typing, not when they submit
3. Allow file reads before git sync completes; block only writes
4. Structure agent framework as server-first with clients as thin wrappers
5. Isolate state per session to prevent cross-session interference
6. Attribute commits to the user who prompted, not the app
7. Track merged PRs as primary success metric
8. Build for multiplayer from the start; it is nearly free with proper sync architecture

## Integration

This skill builds on multi-agent-patterns for agent coordination and tool-design for agent-tool interfaces. It connects to:

- multi-agent-patterns - Self-spawning agents follow supervisor patterns
- tool-design - Building tools for agent spawning and status checking
- context-optimization - Managing context across distributed sessions
- filesystem-context - Using filesystem for session state and artifacts

## References

Internal reference:
- Infrastructure Patterns - Detailed implementation patterns

Related skills in this collection:
- multi-agent-patterns - Coordination patterns for self-spawning agents
- tool-design - Designing tools for hosted environments
- context-optimization - Managing context in distributed systems

External resources:
- [Ramp](https://builders.ramp.com/post/why-we-built-our-background-agent) - Why We Built Our Own Background Agent
- [Modal Sandboxes](https://modal.com/docs/guide/sandbox) - Cloud sandbox infrastructure
- [Cloudflare Durable Objects](https://developers.cloudflare.com/durable-objects/) - Per-session state management
- Server-first agent framework pattern

---

## Skill Metadata

**Created**: 2026-01-12
**Last Updated**: 2026-01-12
**Author**: Agent Skills for Context Engineering Contributors
**Version**: 1.0.0


## When to Use

Use this skill when tackling tasks related to its primary domain or functionality as described above.

## Imported Module: Hosted Agents V2 Py
---
name: hosted-agents-v2-py
description: "Build hosted agents using Azure AI Projects SDK with ImageBasedHostedAgentDefinition. Use when creating container-based agents in Azure AI Foundry."
risk: unknown
source: community
date_added: "2026-02-27"
---

# Azure AI Hosted Agents (Python)

Build container-based hosted agents using `ImageBasedHostedAgentDefinition` from the Azure AI Projects SDK.

## Installation

```bash
pip install azure-ai-projects>=2.0.0b3 azure-identity
```

**Minimum SDK Version:** `2.0.0b3` or later required for hosted agent support.

## Environment Variables

```bash
AZURE_AI_PROJECT_ENDPOINT=https://<resource>.services.ai.azure.com/api/projects/<project>
```

## Prerequisites

Before creating hosted agents:

1. **Container Image** - Build and push to Azure Container Registry (ACR)
2. **ACR Pull Permissions** - Grant your project's managed identity `AcrPull` role on the ACR
3. **Capability Host** - Account-level capability host with `enablePublicHostingEnvironment=true`
4. **SDK Version** - Ensure `azure-ai-projects>=2.0.0b3`

## Authentication

Always use `DefaultAzureCredential`:

```python
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

credential = DefaultAzureCredential()
client = AIProjectClient(
    endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    credential=credential
)
```

## Core Workflow

### 1. Imports

```python
import os
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import (
    ImageBasedHostedAgentDefinition,
    ProtocolVersionRecord,
    AgentProtocol,
)
```

### 2. Create Hosted Agent

```python
client = AIProjectClient(
    endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    credential=DefaultAzureCredential()
)

agent = client.agents.create_version(
    agent_name="my-hosted-agent",
    definition=ImageBasedHostedAgentDefinition(
        container_protocol_versions=[
            ProtocolVersionRecord(protocol=AgentProtocol.RESPONSES, version="v1")
        ],
        cpu="1",
        memory="2Gi",
        image="myregistry.azurecr.io/my-agent:latest",
        tools=[{"type": "code_interpreter"}],
        environment_variables={
            "AZURE_AI_PROJECT_ENDPOINT": os.environ["AZURE_AI_PROJECT_ENDPOINT"],
            "MODEL_NAME": "gpt-4o-mini"
        }
    )
)

print(f"Created agent: {agent.name} (version: {agent.version})")
```

### 3. List Agent Versions

```python
versions = client.agents.list_versions(agent_name="my-hosted-agent")
for version in versions:
    print(f"Version: {version.version}, State: {version.state}")
```

### 4. Delete Agent Version

```python
client.agents.delete_version(
    agent_name="my-hosted-agent",
    version=agent.version
)
```

## ImageBasedHostedAgentDefinition Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `container_protocol_versions` | `list[ProtocolVersionRecord]` | Yes | Protocol versions the agent supports |
| `image` | `str` | Yes | Full container image path (registry/image:tag) |
| `cpu` | `str` | No | CPU allocation (e.g., "1", "2") |
| `memory` | `str` | No | Memory allocation (e.g., "2Gi", "4Gi") |
| `tools` | `list[dict]` | No | Tools available to the agent |
| `environment_variables` | `dict[str, str]` | No | Environment variables for the container |

## Protocol Versions

The `container_protocol_versions` parameter specifies which protocols your agent supports:

```python
from azure.ai.projects.models import ProtocolVersionRecord, AgentProtocol

# RESPONSES protocol - standard agent responses
container_protocol_versions=[
    ProtocolVersionRecord(protocol=AgentProtocol.RESPONSES, version="v1")
]
```

**Available Protocols:**
| Protocol | Description |
|----------|-------------|
| `AgentProtocol.RESPONSES` | Standard response protocol for agent interactions |

## Resource Allocation

Specify CPU and memory for your container:

```python
definition=ImageBasedHostedAgentDefinition(
    container_protocol_versions=[...],
    image="myregistry.azurecr.io/my-agent:latest",
    cpu="2",      # 2 CPU cores
    memory="4Gi"  # 4 GiB memory
)
```

**Resource Limits:**
| Resource | Min | Max | Default |
|----------|-----|-----|---------|
| CPU | 0.5 | 4 | 1 |
| Memory | 1Gi | 8Gi | 2Gi |

## Tools Configuration

Add tools to your hosted agent:

### Code Interpreter

```python
tools=[{"type": "code_interpreter"}]
```

### MCP Tools

```python
tools=[
    {"type": "code_interpreter"},
    {
        "type": "mcp",
        "server_label": "my-mcp-server",
        "server_url": "https://my-mcp-server.example.com"
    }
]
```

### Multiple Tools

```python
tools=[
    {"type": "code_interpreter"},
    {"type": "file_search"},
    {
        "type": "mcp",
        "server_label": "custom-tool",
        "server_url": "https://custom-tool.example.com"
    }
]
```

## Environment Variables

Pass configuration to your container:

```python
environment_variables={
    "AZURE_AI_PROJECT_ENDPOINT": os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    "MODEL_NAME": "gpt-4o-mini",
    "LOG_LEVEL": "INFO",
    "CUSTOM_CONFIG": "value"
}
```

**Best Practice:** Never hardcode secrets. Use environment variables or Azure Key Vault.

## Complete Example

```python
import os
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import (
    ImageBasedHostedAgentDefinition,
    ProtocolVersionRecord,
    AgentProtocol,
)

def create_hosted_agent():
    """Create a hosted agent with custom container image."""
    
    client = AIProjectClient(
        endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
        credential=DefaultAzureCredential()
    )
    
    agent = client.agents.create_version(
        agent_name="data-processor-agent",
        definition=ImageBasedHostedAgentDefinition(
            container_protocol_versions=[
                ProtocolVersionRecord(
                    protocol=AgentProtocol.RESPONSES,
                    version="v1"
                )
            ],
            image="myregistry.azurecr.io/data-processor:v1.0",
            cpu="2",
            memory="4Gi",
            tools=[
                {"type": "code_interpreter"},
                {"type": "file_search"}
            ],
            environment_variables={
                "AZURE_AI_PROJECT_ENDPOINT": os.environ["AZURE_AI_PROJECT_ENDPOINT"],
                "MODEL_NAME": "gpt-4o-mini",
                "MAX_RETRIES": "3"
            }
        )
    )
    
    print(f"Created hosted agent: {agent.name}")
    print(f"Version: {agent.version}")
    print(f"State: {agent.state}")
    
    return agent

if __name__ == "__main__":
    create_hosted_agent()
```

## Async Pattern

```python
import os
from azure.identity.aio import DefaultAzureCredential
from azure.ai.projects.aio import AIProjectClient
from azure.ai.projects.models import (
    ImageBasedHostedAgentDefinition,
    ProtocolVersionRecord,
    AgentProtocol,
)

async def create_hosted_agent_async():
    """Create a hosted agent asynchronously."""
    
    async with DefaultAzureCredential() as credential:
        async with AIProjectClient(
            endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
            credential=credential
        ) as client:
            agent = await client.agents.create_version(
                agent_name="async-agent",
                definition=ImageBasedHostedAgentDefinition(
                    container_protocol_versions=[
                        ProtocolVersionRecord(
                            protocol=AgentProtocol.RESPONSES,
                            version="v1"
                        )
                    ],
                    image="myregistry.azurecr.io/async-agent:latest",
                    cpu="1",
                    memory="2Gi"
                )
            )
            return agent
```

## Common Errors

| Error | Cause | Solution |
|-------|-------|----------|
| `ImagePullBackOff` | ACR pull permission denied | Grant `AcrPull` role to project's managed identity |
| `InvalidContainerImage` | Image not found | Verify image path and tag exist in ACR |
| `CapabilityHostNotFound` | No capability host configured | Create account-level capability host |
| `ProtocolVersionNotSupported` | Invalid protocol version | Use `AgentProtocol.RESPONSES` with version `"v1"` |

## Best Practices

1. **Version Your Images** - Use specific tags, not `latest` in production
2. **Minimal Resources** - Start with minimum CPU/memory, scale up as needed
3. **Environment Variables** - Use for all configuration, never hardcode
4. **Error Handling** - Wrap agent creation in try/except blocks
5. **Cleanup** - Delete unused agent versions to free resources

## Reference Links

- [Azure AI Projects SDK](https://pypi.org/project/azure-ai-projects/)
- [Hosted Agents Documentation](https://learn.microsoft.com/azure/ai-services/agents/how-to/hosted-agents)
- [Azure Container Registry](https://learn.microsoft.com/azure/container-registry/)

## When to Use
This skill is applicable to execute the workflow or actions described in the overview.

## Imported Module: Tool Design
---
name: tool-design
description: "Build tools that agents can use effectively, including architectural reduction patterns"
risk: safe
source: "https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/tree/main/skills/tool-design"
date_added: "2026-02-27"
---

## When to Use This Skill

Build tools that agents can use effectively, including architectural reduction patterns

Use this skill when working with build tools that agents can use effectively, including architectural reduction patterns.
# Tool Design for Agents

Tools are the primary mechanism through which agents interact with the world. They define the contract between deterministic systems and non-deterministic agents. Unlike traditional software APIs designed for developers, tool APIs must be designed for language models that reason about intent, infer parameter values, and generate calls from natural language requests. Poor tool design creates failure modes that no amount of prompt engineering can fix. Effective tool design follows specific principles that account for how agents perceive and use tools.

## When to Activate

Activate this skill when:
- Creating new tools for agent systems
- Debugging tool-related failures or misuse
- Optimizing existing tool sets for better agent performance
- Designing tool APIs from scratch
- Evaluating third-party tools for agent integration
- Standardizing tool conventions across a codebase

## Core Concepts

Tools are contracts between deterministic systems and non-deterministic agents. The consolidation principle states that if a human engineer cannot definitively say which tool should be used in a given situation, an agent cannot be expected to do better. Effective tool descriptions are prompt engineering that shapes agent behavior.

Key principles include: clear descriptions that answer what, when, and what returns; response formats that balance completeness and token efficiency; error messages that enable recovery; and consistent conventions that reduce cognitive load.

## Detailed Topics

### The Tool-Agent Interface

**Tools as Contracts**
Tools are contracts between deterministic systems and non-deterministic agents. When humans call APIs, they understand the contract and make appropriate requests. Agents must infer the contract from descriptions and generate calls that match expected formats.

This fundamental difference requires rethinking API design. The contract must be unambiguous, examples must illustrate expected patterns, and error messages must guide correction. Every ambiguity in tool definitions becomes a potential failure mode.

**Tool Description as Prompt**
Tool descriptions are loaded into agent context and collectively steer behavior. The descriptions are not just documentation—they are prompt engineering that shapes how agents reason about tool use.

Poor descriptions like "Search the database" with cryptic parameter names force agents to guess. Optimized descriptions include usage context, examples, and defaults. The description answers: what the tool does, when to use it, and what it produces.

**Namespacing and Organization**
As tool collections grow, organization becomes critical. Namespacing groups related tools under common prefixes, helping agents select appropriate tools at the right time.

Namespacing creates clear boundaries between functionality. When an agent needs database information, it routes to the database namespace. When it needs web search, it routes to web namespace.

### The Consolidation Principle

**Single Comprehensive Tools**
The consolidation principle states that if a human engineer cannot definitively say which tool should be used in a given situation, an agent cannot be expected to do better. This leads to a preference for single comprehensive tools over multiple narrow tools.

Instead of implementing list_users, list_events, and create_event, implement schedule_event that finds availability and schedules. The comprehensive tool handles the full workflow internally rather than requiring agents to chain multiple calls.

**Why Consolidation Works**
Agents have limited context and attention. Each tool in the collection competes for attention in the tool selection phase. Each tool adds description tokens that consume context budget. Overlapping functionality creates ambiguity about which tool to use.

Consolidation reduces token consumption by eliminating redundant descriptions. It eliminates ambiguity by having one tool cover each workflow. It reduces tool selection complexity by shrinking the effective tool set.

**When Not to Consolidate**
Consolidation is not universally correct. Tools with fundamentally different behaviors should remain separate. Tools used in different contexts benefit from separation. Tools that might be called independently should not be artificially bundled.

### Architectural Reduction

The consolidation principle, taken to its logical extreme, leads to architectural reduction: removing most specialized tools in favor of primitive, general-purpose capabilities. Production evidence shows this approach can outperform sophisticated multi-tool architectures.

**The File System Agent Pattern**
Instead of building custom tools for data exploration, schema lookup, and query validation, provide direct file system access through a single command execution tool. The agent uses standard Unix utilities (grep, cat, find, ls) to explore, understand, and operate on your system.

This works because:
1. File systems are a proven abstraction that models understand deeply
2. Standard tools have predictable, well-documented behavior
3. The agent can chain primitives flexibly rather than being constrained to predefined workflows
4. Good documentation in files replaces the need for summarization tools

**When Reduction Outperforms Complexity**
Reduction works when:
- Your data layer is well-documented and consistently structured
- The model has sufficient reasoning capability to navigate complexity
- Your specialized tools were constraining rather than enabling the model
- You're spending more time maintaining scaffolding than improving outcomes

Reduction fails when:
- Your underlying data is messy, inconsistent, or poorly documented
- The domain requires specialized knowledge the model lacks
- Safety constraints require limiting what the agent can do
- Operations are truly complex and benefit from structured workflows

**Stop Constraining Reasoning**
A common anti-pattern is building tools to "protect" the model from complexity. Pre-filtering context, constraining options, wrapping interactions in validation logic. These guardrails often become liabilities as models improve.

The question to ask: are your tools enabling new capabilities, or are they constraining reasoning the model could handle on its own?

**Build for Future Models**
Models improve faster than tooling can keep up. An architecture optimized for today's model may be over-constrained for tomorrow's. Build minimal architectures that can benefit from model improvements rather than sophisticated architectures that lock in current limitations.

See Architectural Reduction Case Study for production evidence.

### Tool Description Engineering

**Description Structure**
Effective tool descriptions answer four questions:

What does the tool do? Clear, specific description of functionality. Avoid vague language like "helps with" or "can be used for." State exactly what the tool accomplishes.

When should it be used? Specific triggers and contexts. Include both direct triggers ("User asks about pricing") and indirect signals ("Need current market rates").

What inputs does it accept? Parameter descriptions with types, constraints, and defaults. Explain what each parameter controls.

What does it return? Output format and structure. Include examples of successful responses and error conditions.

**Default Parameter Selection**
Defaults should reflect common use cases. They reduce agent burden by eliminating unnecessary parameter specification. They prevent errors from omitted parameters.

### Response Format Optimization

Tool response size significantly impacts context usage. Implementing response format options gives agents control over verbosity.

Concise format returns essential fields only, appropriate for confirmation or basic information. Detailed format returns complete objects with all fields, appropriate when full context is needed for decisions.

Include guidance in tool descriptions about when to use each format. Agents learn to select appropriate formats based on task requirements.

### Error Message Design

Error messages serve two audiences: developers debugging issues and agents recovering from failures. For agents, error messages must be actionable. They must tell the agent what went wrong and how to correct it.

Design error messages that enable recovery. For retryable errors, include retry guidance. For input errors, include corrected format. For missing data, include what's needed.

### Tool Definition Schema

Use a consistent schema across all tools. Establish naming conventions: verb-noun pattern for tool names, consistent parameter names across tools, consistent return field names.

### Tool Collection Design

Research shows tool description overlap causes model confusion. More tools do not always lead to better outcomes. A reasonable guideline is 10-20 tools for most applications. If more are needed, use namespacing to create logical groupings.

Implement mechanisms to help agents select the right tool: tool grouping, example-based selection, and hierarchy with umbrella tools that route to specialized sub-tools.

### MCP Tool Naming Requirements

When using MCP (Model Context Protocol) tools, always use fully qualified tool names to avoid "tool not found" errors.

Format: `ServerName:tool_name`

```python
# Correct: Fully qualified names
"Use the BigQuery:bigquery_schema tool to retrieve table schemas."
"Use the GitHub:create_issue tool to create issues."

# Incorrect: Unqualified names
"Use the bigquery_schema tool..."  # May fail with multiple servers
```

Without the server prefix, agents may fail to locate tools, especially when multiple MCP servers are available. Establish naming conventions that include server context in all tool references.

### Using Agents to Optimize Tools

AI assistant can optimize its own tools. When given a tool and observed failure modes, it diagnoses issues and suggests improvements. Production testing shows this approach achieves 40% reduction in task completion time by helping future agents avoid mistakes.

**The Tool-Testing Agent Pattern**:

```python
def optimize_tool_description(tool_spec, failure_examples):
    """
    Use an agent to analyze tool failures and improve descriptions.
    
    Process:
    1. Agent attempts to use tool across diverse tasks
    2. Collect failure modes and friction points
    3. Agent analyzes failures and proposes improvements
    4. Test improved descriptions against same tasks
    """
    prompt = f"""
    Analyze this tool specification and the observed failures.
    
    Tool: {tool_spec}
    
    Failures observed:
    {failure_examples}
    
    Identify:
    1. Why agents are failing with this tool
    2. What information is missing from the description
    3. What ambiguities cause incorrect usage
    
    Propose an improved tool description that addresses these issues.
    """
    
    return get_agent_response(prompt)
```

This creates a feedback loop: agents using tools generate failure data, which agents then use to improve tool descriptions, which reduces future failures.

### Testing Tool Design

Evaluate tool designs against criteria: unambiguity, completeness, recoverability, efficiency, and consistency. Test tools by presenting representative agent requests and evaluating the resulting tool calls.

## Practical Guidance

### Anti-Patterns to Avoid

Vague descriptions: "Search the database for customer information" leaves too many questions unanswered.

Cryptic parameter names: Parameters named x, val, or param1 force agents to guess meaning.

Missing error handling: Tools that fail with generic errors provide no recovery guidance.

Inconsistent naming: Using id in some tools, identifier in others, and customer_id in some creates confusion.

### Tool Selection Framework

When designing tool collections:
1. Identify distinct workflows agents must accomplish
2. Group related actions into comprehensive tools
3. Ensure each tool has a clear, unambiguous purpose
4. Document error cases and recovery paths
5. Test with actual agent interactions

## Examples

**Example 1: Well-Designed Tool**
```python
def get_customer(customer_id: str, format: str = "concise"):
    """
    Retrieve customer information by ID.
    
    Use when:
    - User asks about specific customer details
    - Need customer context for decision-making
    - Verifying customer identity
    
    Args:
        customer_id: Format "CUST-######" (e.g., "CUST-000001")
        format: "concise" for key fields, "detailed" for complete record
    
    Returns:
        Customer object with requested fields
    
    Errors:
        NOT_FOUND: Customer ID not found
        INVALID_FORMAT: ID must match CUST-###### pattern
    """
```

**Example 2: Poor Tool Design**

This example demonstrates several tool design anti-patterns:

```python
def search(query):
    """Search the database."""
    pass
```

**Problems with this design:**

1. **Vague name**: "search" is ambiguous - search what, for what purpose?
2. **Missing parameters**: What database? What format should query take?
3. **No return description**: What does this function return? A list? A string? Error handling?
4. **No usage context**: When should an agent use this versus other tools?
5. **No error handling**: What happens if the database is unavailable?

**Failure modes:**
- Agents may call this tool when they should use a more specific tool
- Agents cannot determine correct query format
- Agents cannot interpret results
- Agents cannot recover from failures

## Guidelines

1. Write descriptions that answer what, when, and what returns
2. Use consolidation to reduce ambiguity
3. Implement response format options for token efficiency
4. Design error messages for agent recovery
5. Establish and follow consistent naming conventions
6. Limit tool count and use namespacing for organization
7. Test tool designs with actual agent interactions
8. Iterate based on observed failure modes
9. Question whether each tool enables or constrains the model
10. Prefer primitive, general-purpose tools over specialized wrappers
11. Invest in documentation quality over tooling sophistication
12. Build minimal architectures that benefit from model improvements

## Integration

This skill connects to:
- context-fundamentals - How tools interact with context
- multi-agent-patterns - Specialized tools per agent
- evaluation - Evaluating tool effectiveness

## References

Internal references:
- Best Practices Reference - Detailed tool design guidelines
- Architectural Reduction Case Study - Production evidence for tool minimalism

Related skills in this collection:
- context-fundamentals - Tool context interactions
- evaluation - Tool testing patterns

External resources:
- MCP (Model Context Protocol) documentation
- Framework tool conventions
- API design best practices for agents
- Vercel d0 agent architecture case study

---

## Skill Metadata

**Created**: 2025-12-20
**Last Updated**: 2025-12-23
**Author**: Agent Skills for Context Engineering Contributors
**Version**: 1.1.0

