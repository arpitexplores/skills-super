## Source: references/skills/healthcare-workflows/SKILL.md

---
name: healthcare-workflows
description: "A health assistant skill for medical information analysis, symptom tracking, and wellness guidance."
risk: safe
source: "https://github.com/huifer/Healthcare-Workflows"
date_added: "2026-02-27"
---

# Healthcare Workflows

## Overview

A health assistant skill for medical information analysis, symptom tracking, and wellness guidance.

## When to Use This Skill

Use this skill when you need to work with a health assistant skill for medical information analysis, symptom tracking, and wellness guidance..

## Instructions

This skill provides guidance and patterns for a health assistant skill for medical information analysis, symptom tracking, and wellness guidance..

For more information, see the [source repository](https://github.com/huifer/Healthcare-Workflows).

---

## Merged Reference (legacy variant)

---
name: ai-analyzer
description: AI驱动的综合健康分析系统，整合多维度健康数据、识别异常模式、预测健康风险、提供个性化建议。支持智能问答和AI健康报告生成。
allowed-tools: Read, Grep, Glob, Write
---

# AI健康分析器

基于AI技术的综合健康分析系统，提供智能健康洞察、风险预测和个性化建议。

## 核心功能

### 1. 智能健康分析
- **多维度数据整合**: 整合基础指标、生活方式、心理健康、医疗历史等4类数据源
- **异常模式识别**: 使用CUSUM、Z-score等算法检测异常值和变化点
- **相关性分析**: 计算不同健康指标之间的相关性（皮尔逊、斯皮尔曼）
- **趋势预测**: 基于历史数据进行趋势分析和预测

### 2. 健康风险预测
- **高血压风险**: 基于Framingham风险评分模型
- **糖尿病风险**: 基于ADA糖尿病风险评分标准
- **心血管疾病风险**: 基于ACC/AHA ASCVD指南
- **营养缺乏风险**: 基于RDA达成率和饮食模式分析
- **睡眠障碍风险**: 基于PSQI和睡眠模式分析

### 3. 个性化建议引擎
- **基础个性化**: 基于年龄、性别、BMI、活动水平等静态档案
- **建议分级**: Level 1（一般性）、Level 2（参考性）、Level 3（医疗建议）
- **循证依据**: 基于医学指南和循证医学证据
- **可操作性**: 提供具体、可行的改进建议

### 4. 自然语言交互
- **智能问答**: 支持健康数据查询、趋势分析、相关性查询等
- **上下文理解**: 维护对话历史，支持多轮对话
- **意图识别**: 识别用户查询意图，提供精准回复

### 5. AI健康报告生成
- **综合报告**: 包含所有维度健康数据、AI洞察、风险评估
- **快速摘要**: 关键指标概览、异常警示、主要建议
- **风险评估报告**: 各类疾病风险、风险因素分析、预防措施
- **趋势分析报告**: 多维度趋势、变化点识别、预测分析
- **HTML交互式报告**: ECharts图表、Tailwind CSS样式

## 使用说明

### 触发条件

当用户提到以下场景时，使用此技能：

**通用询问**:
- ✅ "AI分析我的健康状况"
- ✅ "我的健康有什么风险？"
- ✅ "生成AI健康报告"
- ✅ "AI分析所有数据"

**风险预测**:
- ✅ "预测我的高血压风险"
- ✅ "我有糖尿病风险吗？"
- ✅ "评估我的心血管风险"
- ✅ "AI预测健康风险"

**智能问答**:
- ✅ "我的睡眠怎么样？"
- ✅ "运动对我的健康有什么影响？"
- ✅ "我应该如何改善健康状况？"
- ✅ "AI健康助手问答"

**报告生成**:
- ✅ "生成AI健康报告"
- ✅ "创建综合分析报告"
- ✅ "AI风险评估报告"

### 执行步骤

#### 步骤 1: 读取AI配置

```javascript
const aiConfig = readFile('data/ai-config.json');
const aiHistory = readFile('data/ai-history.json');
```

检查AI功能是否启用，验证数据源配置。

#### 步骤 2: 读取用户档案

```javascript
const profile = readFile('data/profile.json');
```

获取基础信息：年龄、性别、身高、体重、BMI等。

#### 步骤 3: 读取健康数据

根据配置的数据源读取相关数据：

```javascript
// 基础健康指标
const indexData = readFile('data/index.json');

// 生活方式数据
const fitnessData = readFile('data-example/fitness-tracker.json');
const sleepData = readFile('data-example/sleep-tracker.json');
const nutritionData = readFile('data-example/nutrition-tracker.json');

// 心理健康数据
const mentalHealthData = readFile('data-example/mental-health-tracker.json');

// 医疗历史
const medications = exists('data/medications.json') ? readFile('data/medications.json') : null;
const allergies = exists('data/allergies.json') ? readFile('data/allergies.json') : null;
```

#### 步骤 4: 数据整合和预处理

整合所有数据源，进行数据清洗、时间对齐和缺失值处理。

#### 步骤 5: 多维度分析

**相关性分析**: 计算睡眠↔情绪、运动↔体重、营养↔生化指标等关联

**趋势分析**: 使用线性回归、移动平均等方法识别趋势方向

**异常检测**: 使用CUSUM、Z-score算法检测异常值和变化点

#### 步骤 6: 风险预测

基于Framingham、ADA、ACC/AHA等标准进行风险预测：

- 高血压风险（10年概率）
- 糖尿病风险（10年概率）
- 心血管疾病风险（10年概率）
- 营养缺乏风险
- 睡眠障碍风险

#### 步骤 7: 生成个性化建议

根据分析结果生成三级建议：

- **Level 1**: 一般性建议（基于标准指南）
- **Level 2**: 参考性建议（基于个人数据）
- **Level 3**: 医疗建议（需医生确认，包含免责声明）

#### 步骤 8: 生成分析报告

**文本报告**: 包含总体评估、风险预测、关键趋势、相关性发现、个性化建议

**HTML报告**: 调用 `scripts/generate_ai_report.py` 生成包含ECharts图表的交互式报告

#### 步骤 9: 更新AI历史记录

记录分析结果到 `data/ai-history.json`

## 数据源

| 数据源 | 文件路径 | 数据内容 |
|--------|---------|---------|
| 用户档案 | `data/profile.json` | 年龄、性别、身高、体重、BMI |
| 医疗记录 | `data/index.json` | 生化指标、影像检查 |
| 运动追踪 | `data-example/fitness-tracker.json` | 运动类型、时长、强度、MET值 |
| 睡眠追踪 | `data-example/sleep-tracker.json` | 睡眠时长、质量、PSQI评分 |
| 营养追踪 | `data-example/nutrition-tracker.json` | 饮食记录、营养素摄入、RDA达成率 |
| 心理健康 | `data-example/mental-health-tracker.json` | PHQ-9、GAD-7评分 |
| 用药记录 | `data/medications.json` | 药物名称、剂量、用法、依从性 |
| 过敏史 | `data/allergies.json` | 过敏原、严重程度 |

## 算法说明

### 相关性分析
- **皮尔逊相关系数**: 连续变量（如睡眠时长与情绪评分）
- **斯皮尔曼相关系数**: 有序变量（如症状严重程度）

### 异常检测
- **CUSUM算法**: 时间序列变化点检测
- **Z-score方法**: 统计异常值检测（|z| > 2）
- **IQR方法**: 四分位数异常值检测

### 风险预测
- **Framingham风险评分**: 高血压、心血管疾病风险
- **ADA风险评分**: 2型糖尿病风险
- **ASCVD计算器**: 动脉粥样硬化心血管病风险

## 安全与合规

### 必须遵循
- ❌ 不给出医疗诊断
- ❌ 不给出具体用药剂量建议
- ❌ 不判断生死预后
- ❌ 不替代医生建议
- ✅ 所有分析必须标注"仅供参考"
- ✅ Level 3建议必须包含免责声明
- ✅ 高风险预测必须建议咨询医生

### 隐私保护
- ✅ 所有数据保持本地
- ✅ 无外部API调用
- ✅ HTML报告独立运行

## 相关命令

- `/ai analyze` - AI综合分析
- `/ai predict [risk_type]` - 健康风险预测
- `/ai chat [query]` - 自然语言问答
- `/ai report generate [type]` - 生成AI健康报告
- `/ai status` - 查看AI功能状态

## 技术实现

### 工具限制
此Skill仅使用以下工具：
- **Read**: 读取JSON数据文件
- **Grep**: 搜索特定模式
- **Glob**: 按模式查找数据文件
- **Write**: 生成HTML报告和更新历史记录

### 性能优化
- 增量读取：仅读取指定时间范围的数据文件
- 数据缓存：避免重复读取同一文件
- 延迟计算：按需生成图表数据

---

## Merged Reference (legacy variant)

---
name: bdi-mental-states
description: This skill should be used when the user asks to "model agent mental states", "implement BDI architecture", "create belief-desire-intention models", "transform RDF to beliefs", "build cognitive agent", or mentions BDI ontology, mental state modeling, rational agency, or neuro-symbolic AI integration.
---

# BDI Mental State Modeling

Transform external RDF context into agent mental states (beliefs, desires, intentions) using formal BDI ontology patterns. This skill enables agents to reason about context through cognitive architecture, supporting deliberative reasoning, explainability, and semantic interoperability within multi-agent systems.

## When to Activate

Activate this skill when:
- Processing external RDF context into agent beliefs about world states
- Modeling rational agency with perception, deliberation, and action cycles
- Enabling explainability through traceable reasoning chains
- Implementing BDI frameworks (SEMAS, JADE, JADEX)
- Augmenting LLMs with formal cognitive structures (Logic Augmented Generation)
- Coordinating mental states across multi-agent platforms
- Tracking temporal evolution of beliefs, desires, and intentions
- Linking motivational states to action plans

## Core Concepts

### Mental Reality Architecture

**Mental States (Endurants)**: Persistent cognitive attributes
- `Belief`: What the agent believes to be true about the world
- `Desire`: What the agent wishes to bring about
- `Intention`: What the agent commits to achieving

**Mental Processes (Perdurants)**: Events that modify mental states
- `BeliefProcess`: Forming/updating beliefs from perception
- `DesireProcess`: Generating desires from beliefs
- `IntentionProcess`: Committing to desires as actionable intentions

### Cognitive Chain Pattern

```turtle
:Belief_store_open a bdi:Belief ;
    rdfs:comment "Store is open" ;
    bdi:motivates :Desire_buy_groceries .

:Desire_buy_groceries a bdi:Desire ;
    rdfs:comment "I desire to buy groceries" ;
    bdi:isMotivatedBy :Belief_store_open .

:Intention_go_shopping a bdi:Intention ;
    rdfs:comment "I will buy groceries" ;
    bdi:fulfils :Desire_buy_groceries ;
    bdi:isSupportedBy :Belief_store_open ;
    bdi:specifies :Plan_shopping .
```

### World State Grounding

Mental states reference structured configurations of the environment:

```turtle
:Agent_A a bdi:Agent ;
    bdi:perceives :WorldState_WS1 ;
    bdi:hasMentalState :Belief_B1 .

:WorldState_WS1 a bdi:WorldState ;
    rdfs:comment "Meeting scheduled at 10am in Room 5" ;
    bdi:atTime :TimeInstant_10am .

:Belief_B1 a bdi:Belief ;
    bdi:refersTo :WorldState_WS1 .
```

### Goal-Directed Planning

Intentions specify plans that address goals through task sequences:

```turtle
:Intention_I1 bdi:specifies :Plan_P1 .

:Plan_P1 a bdi:Plan ;
    bdi:addresses :Goal_G1 ;
    bdi:beginsWith :Task_T1 ;
    bdi:endsWith :Task_T3 .

:Task_T1 bdi:precedes :Task_T2 .
:Task_T2 bdi:precedes :Task_T3 .
```

## T2B2T Paradigm

Triples-to-Beliefs-to-Triples implements bidirectional flow between RDF knowledge graphs and internal mental states:

**Phase 1: Triples-to-Beliefs**
```turtle
# External RDF context triggers belief formation
:WorldState_notification a bdi:WorldState ;
    rdfs:comment "Push notification: Payment request $250" ;
    bdi:triggers :BeliefProcess_BP1 .

:BeliefProcess_BP1 a bdi:BeliefProcess ;
    bdi:generates :Belief_payment_request .
```

**Phase 2: Beliefs-to-Triples**
```turtle
# Mental deliberation produces new RDF output
:Intention_pay a bdi:Intention ;
    bdi:specifies :Plan_payment .

:PlanExecution_PE1 a bdi:PlanExecution ;
    bdi:satisfies :Plan_payment ;
    bdi:bringsAbout :WorldState_payment_complete .
```

## Notation Selection by Level

| C4 Level | Notation | Mental State Representation |
|----------|----------|----------------------------|
| L1 Context | ArchiMate | Agent boundaries, external perception sources |
| L2 Container | ArchiMate | BDI reasoning engine, belief store, plan executor |
| L3 Component | UML | Mental state managers, process handlers |
| L4 Code | UML/RDF | Belief/Desire/Intention classes, ontology instances |

## Justification and Explainability

Mental entities link to supporting evidence for traceable reasoning:

```turtle
:Belief_B1 a bdi:Belief ;
    bdi:isJustifiedBy :Justification_J1 .

:Justification_J1 a bdi:Justification ;
    rdfs:comment "Official announcement received via email" .

:Intention_I1 a bdi:Intention ;
    bdi:isJustifiedBy :Justification_J2 .

:Justification_J2 a bdi:Justification ;
    rdfs:comment "Location precondition satisfied" .
```

## Temporal Dimensions

Mental states persist over bounded time periods:

```turtle
:Belief_B1 a bdi:Belief ;
    bdi:hasValidity :TimeInterval_TI1 .

:TimeInterval_TI1 a bdi:TimeInterval ;
    bdi:hasStartTime :TimeInstant_9am ;
    bdi:hasEndTime :TimeInstant_11am .
```

Query mental states active at specific moments:

```sparql
SELECT ?mentalState WHERE {
    ?mentalState bdi:hasValidity ?interval .
    ?interval bdi:hasStartTime ?start ;
              bdi:hasEndTime ?end .
    FILTER(?start <= "2025-01-04T10:00:00"^^xsd:dateTime && 
           ?end >= "2025-01-04T10:00:00"^^xsd:dateTime)
}
```

## Compositional Mental Entities

Complex mental entities decompose into constituent parts for selective updates:

```turtle
:Belief_meeting a bdi:Belief ;
    rdfs:comment "Meeting at 10am in Room 5" ;
    bdi:hasPart :Belief_meeting_time , :Belief_meeting_location .

# Update only location component
:BeliefProcess_update a bdi:BeliefProcess ;
    bdi:modifies :Belief_meeting_location .
```

## Integration Patterns

### Logic Augmented Generation (LAG)

Augment LLM outputs with ontological constraints:

```python
def augment_llm_with_bdi_ontology(prompt, ontology_graph):
    ontology_context = serialize_ontology(ontology_graph, format='turtle')
    augmented_prompt = f"{ontology_context}\n\n{prompt}"
    
    response = llm.generate(augmented_prompt)
    triples = extract_rdf_triples(response)
    
    is_consistent = validate_triples(triples, ontology_graph)
    return triples if is_consistent else retry_with_feedback()
```

### SEMAS Rule Translation

Map BDI ontology to executable production rules:

```prolog
% Belief triggers desire formation
[HEAD: belief(agent_a, store_open)] / 
[CONDITIONALS: time(weekday_afternoon)] » 
[TAIL: generate_desire(agent_a, buy_groceries)].

% Desire triggers intention commitment
[HEAD: desire(agent_a, buy_groceries)] / 
[CONDITIONALS: belief(agent_a, has_shopping_list)] » 
[TAIL: commit_intention(agent_a, buy_groceries)].
```

## Guidelines

1. Model world states as configurations independent of agent perspectives, providing referential substrate for mental states.

2. Distinguish endurants (persistent mental states) from perdurants (temporal mental processes), aligning with DOLCE ontology.

3. Treat goals as descriptions rather than mental states, maintaining separation between cognitive and planning layers.

4. Use `hasPart` relations for meronymic structures enabling selective belief updates.

5. Associate every mental entity with temporal constructs via `atTime` or `hasValidity`.

6. Use bidirectional property pairs (`motivates`/`isMotivatedBy`, `generates`/`isGeneratedBy`) for flexible querying.

7. Link mental entities to `Justification` instances for explainability and trust.

8. Implement T2B2T through: (1) translate RDF to beliefs, (2) execute BDI reasoning, (3) project mental states back to RDF.

9. Define existential restrictions on mental processes (e.g., `BeliefProcess ⊑ ∃generates.Belief`).

10. Reuse established ODPs (EventCore, Situation, TimeIndexedSituation, BasicPlan, Provenance) for interoperability.

## Competency Questions

Validate implementation against these SPARQL queries:

```sparql
# CQ1: What beliefs motivated formation of a given desire?
SELECT ?belief WHERE {
    :Desire_D1 bdi:isMotivatedBy ?belief .
}

# CQ2: Which desire does a particular intention fulfill?
SELECT ?desire WHERE {
    :Intention_I1 bdi:fulfils ?desire .
}

# CQ3: Which mental process generated a belief?
SELECT ?process WHERE {
    ?process bdi:generates :Belief_B1 .
}

# CQ4: What is the ordered sequence of tasks in a plan?
SELECT ?task ?nextTask WHERE {
    :Plan_P1 bdi:hasComponent ?task .
    OPTIONAL { ?task bdi:precedes ?nextTask }
} ORDER BY ?task
```

## Anti-Patterns

1. **Conflating mental states with world states**: Mental states reference world states, they are not world states themselves.

2. **Missing temporal bounds**: Every mental state should have validity intervals for diachronic reasoning.

3. **Flat belief structures**: Use compositional modeling with `hasPart` for complex beliefs.

4. **Implicit justifications**: Always link mental entities to explicit justification instances.

5. **Direct intention-to-action mapping**: Intentions specify plans which contain tasks; actions execute tasks.

## Integration

- **RDF Processing**: Apply after parsing external RDF context to construct cognitive representations
- **Semantic Reasoning**: Combine with ontology reasoning to infer implicit mental state relationships
- **Multi-Agent Communication**: Integrate with FIPA ACL for cross-platform belief sharing
- **Temporal Context**: Coordinate with temporal reasoning for mental state evolution
- **Explainable AI**: Feed into explanation systems tracing perception through deliberation to action
- **Neuro-Symbolic AI**: Apply in LAG pipelines to constrain LLM outputs with cognitive structures

## References

See `references/` folder for detailed documentation:
- `bdi-ontology-core.md` - Core ontology patterns and class definitions
- `rdf-examples.md` - Complete RDF/Turtle examples
- `sparql-competency.md` - Full competency question SPARQL queries
- `framework-integration.md` - SEMAS, JADE, LAG integration patterns

Primary sources:
- Zuppiroli et al. "The Belief-Desire-Intention Ontology" (2025)
- Rao & Georgeff "BDI agents: From theory to practice" (1995)
- Bratman "Intention, plans, and practical reason" (1987)

---

## Merged Reference (legacy variant)

---
name: behavioral-modes
description: "AI operational modes (brainstorm, implement, debug, review, teach, ship, orchestrate). Use to adapt behavior based on task type."
risk: unknown
source: community
date_added: "2026-02-27"
---

# Behavioral Modes - Adaptive AI Operating Modes

## Purpose
This skill defines distinct behavioral modes that optimize AI performance for specific tasks. Modes change how the AI approaches problems, communicates, and prioritizes.

---

## Available Modes

### 1. 🧠 BRAINSTORM Mode

**When to use:** Early project planning, feature ideation, architecture decisions

**Behavior:**
- Ask clarifying questions before assumptions
- Offer multiple alternatives (at least 3)
- Think divergently - explore unconventional solutions
- No code yet - focus on ideas and options
- Use visual diagrams (mermaid) to explain concepts

**Output style:**
```
"Let's explore this together. Here are some approaches:

Option A: [description]
  ✅ Pros: ...
  ❌ Cons: ...

Option B: [description]
  ✅ Pros: ...
  ❌ Cons: ...

What resonates with you? Or should we explore a different direction?"
```

---

### 2. ⚡ IMPLEMENT Mode

**When to use:** Writing code, building features, executing plans

**Behavior:**
- **CRITICAL: Use `clean-code` skill standards** - concise, direct, no verbose explanations
- Fast execution - minimize questions
- Use established patterns and best practices
- Write complete, production-ready code
- Include error handling and edge cases
- **NO tutorial-style explanations** - just code
- **NO unnecessary comments** - let code self-document
- **NO over-engineering** - solve the problem directly
- **NO RUSHING** - Quality > Speed. Read ALL references before coding.

**Output style:**
```
[Code block]

[Brief summary, max 1-2 sentences]
```

**NOT:**
```
"Building [feature]...

✓ Created [file1]
✓ Created [file2]
✓ Updated [file3]

[long explanation]

Run `npm run dev` to test."
```

---

### 3. 🔍 DEBUG Mode

**When to use:** Fixing bugs, troubleshooting errors, investigating issues

**Behavior:**
- Ask for error messages and reproduction steps
- Think systematically - check logs, trace data flow
- Form hypothesis → test → verify
- Explain the root cause, not just the fix
- Prevent future occurrences

**Output style:**
```
"Investigating...

🔍 Symptom: [what's happening]
🎯 Root cause: [why it's happening]
✅ Fix: [the solution]
🛡️ Prevention: [how to avoid in future]
```

---

### 4. 📋 REVIEW Mode

**When to use:** Code review, architecture review, security audit

**Behavior:**
- Be thorough but constructive
- Categorize by severity (Critical/High/Medium/Low)
- Explain the "why" behind suggestions
- Offer improved code examples
- Acknowledge what's done well

**Output style:**
```
## Code Review: [file/feature]

### 🔴 Critical
- [issue with explanation]

### 🟠 Improvements
- [suggestion with example]

### 🟢 Good
- [positive observation]
```

---

### 5. 📚 TEACH Mode

**When to use:** Explaining concepts, documentation, onboarding

**Behavior:**
- Explain from fundamentals
- Use analogies and examples
- Progress from simple to complex
- Include practical exercises
- Check understanding

**Output style:**
```
## Understanding [Concept]

### What is it?
[Simple explanation with analogy]

### How it works
[Technical explanation with diagram]

### Example
[Code example with comments]

### Try it yourself
[Exercise or task]
```

---

### 6. 🚀 SHIP Mode

**When to use:** Production deployment, final polish, release preparation

**Behavior:**
- Focus on stability over features
- Check for missing error handling
- Verify environment configs
- Run all tests
- Create deployment checklist

**Output style:**
```
## Pre-Ship Checklist

### ✅ Code Quality
- [ ] No TypeScript errors
- [ ] ESLint passing
- [ ] All tests passing

### ✅ Security
- [ ] No exposed secrets
- [ ] Input validation complete

### ✅ Performance
- [ ] Bundle size acceptable
- [ ] No console.logs

### 🚀 Ready to deploy
```

---

## Mode Detection

The AI should automatically detect the appropriate mode based on:

| Trigger | Mode |
|---------|------|
| "what if", "ideas", "options" | BRAINSTORM |
| "build", "create", "add" | IMPLEMENT |
| "not working", "error", "bug" | DEBUG |
| "review", "check", "audit" | REVIEW |
| "explain", "how does", "learn" | TEACH |
| "deploy", "release", "production" | SHIP |

---

## Multi-Agent Collaboration Patterns (2025)

Modern architectures optimized for agent-to-agent collaboration:

### 1. 🔭 EXPLORE Mode
**Role:** Discovery and Analysis (Explorer Agent)
**Behavior:** Socratic questioning, deep-dive code reading, dependency mapping.
**Output:** `discovery-report.json`, architectural visualization.

### 2. 🗺️ PLAN-EXECUTE-CRITIC (PEC)
Cyclic mode transitions for high-complexity tasks:
1. **Planner:** Decomposes the task into atomic steps (`task.md`).
2. **Executor:** Performs the actual coding (`IMPLEMENT`).
3. **Critic:** Reviews the code, performs security and performance checks (`REVIEW`).

### 3. 🧠 MENTAL MODEL SYNC
Behavior for creating and loading "Mental Model" summaries to preserve context between sessions.

---

## Combining Modes

---

## Manual Mode Switching

Users can explicitly request a mode:

```
/brainstorm new feature ideas
/implement the user profile page
/debug why login fails
/review this pull request
```

## When to Use
This skill is applicable to execute the workflow or actions described in the overview.

---

## Merged Reference (legacy variant)

---
name: emergency-card
description: 生成紧急情况下快速访问的医疗信息摘要卡片。当用户需要旅行、就诊准备、紧急情况或询问"紧急信息"、"医疗卡片"、"急救信息"时使用此技能。提取关键信息（过敏、用药、急症、植入物），支持多格式输出（JSON、文本、二维码），用于急救或快速就医。
risk: unknown
source: community
---

# 紧急医疗信息卡生成器

生成紧急情况下快速访问的医疗信息摘要，用于急救或就医。

## 核心功能

### 1. 紧急信息提取
从用户的健康数据中提取最关键的信息：
- **严重过敏**：优先提取4级（过敏性休克）和3级过敏
- **当前用药**：活跃药物的名称、剂量、频率
- **急症情况**：需要紧急处理的医疗状况
- **植入物**：心脏起搏器、支架等（影响检查和治疗）
- **紧急联系人**：快速联系的家属信息

### 2. 信息优先级排序
按照医疗紧急程度对信息排序：
1. **P0 - 危急信息**：过敏性休克、严重药物过敏、危及生命的疾病
2. **P1 - 重要信息**：当前用药、慢性病、植入物
3. **P2 - 一般信息**：血型、年龄、体重、最近检查

### 3. 多格式输出
支持多种输出格式以适应不同场景：
- **HTML格式**：可打印网页，使用Tailwind CSS和Lucide图标（推荐）
- **JSON格式**：结构化数据，便于系统集成
- **文本格式**：简洁可读，适合打印携带
- **PDF格式**：专业打印，适合长期保存

#### HTML格式（新增）
生成独立的HTML文件，包含：
- Tailwind CSS样式（通过CDN）
- Lucide图标（通过CDN）
- 响应式设计
- 打印优化
- 多种尺寸变体（A4、钱包卡、大字版）
- 自动卡片类型检测（标准、儿童、老年、严重过敏）

使用方式：
```bash
# 生成标准卡片
python scripts/generate_emergency_card.py

# 指定卡片类型
python scripts/generate_emergency_card.py standard
python scripts/generate_emergency_card.py child
python scripts/generate_emergency_card.py elderly
python scripts/generate_emergency_card.py severe

# 指定打印尺寸
python scripts/generate_emergency_card.py standard a4       # A4标准
python scripts/generate_emergency_card.py standard wallet   # 钱包卡
python scripts/generate_emergency_card.py standard large    # 大字版（老年）
```

输出文件：`emergency-cards/emergency-card-{variant}-{YYYY-MM-DD}.html`

### 4. 离线可用
- 支持手机保存（相册、文件）
- 支持打印携带（钱包、包）
- 支持云端备份（可选）

## 使用说明

### 触发条件
当用户提到以下场景时，使用此技能：
- ✅ "生成紧急医疗信息卡"
- ✅ "我需要旅行，如何快速提供医疗信息"
- ✅ "把我的过敏信息整理成卡片"
- ✅ "紧急情况急救信息"
- ✅ "就医准备资料"
- ✅ "医疗信息摘要"

### 执行步骤

#### 步骤 1: 读取用户基础数据
从以下数据源读取信息：

```javascript
// 1. 用户档案
const profile = readFile('data/profile.json');

// 2. 过敏史
const allergies = readFile('data/allergies.json');

// 3. 当前用药
const medications = readFile('data/medications/medications.json');

// 4. 辐射记录
const radiation = readFile('data/radiation-records.json');

// 5. 手术记录（查找植入物）
const surgeries = glob('data/手术记录/**/*.json');

// 6. 出院小结（查找急症）
const dischargeSummaries = glob('data/出院小结/**/*.json');
```

#### 步骤 2: 提取关键信息

##### 2.1 基础信息
```javascript
const basicInfo = {
  name: profile.basic_info?.name || "未设置",
  age: calculateAge(profile.basic_info?.birth_date),
  gender: profile.basic_info?.gender || "未设置",
  blood_type: profile.basic_info?.blood_type || "未知",
  weight: `${profile.basic_info?.weight} ${profile.basic_info?.weight_unit}`,
  height: `${profile.basic_info?.height} ${profile.basic_info?.height_unit}`,
  bmi: profile.calculated?.bmi,
  emergency_contacts: profile.emergency_contacts || []
};
```

#### 2.2 严重过敏
```javascript
// 过滤出3-4级严重过敏
const criticalAllergies = allergies.allergies
  .filter(a => a.severity_level >= 3 && a.current_status.status === 'active')
  .map(a => ({
    allergen: a.allergen.name,
    severity: `过敏${getSeverityLabel(a.severity_level)}（${a.severity_level}级）`,
    reaction: a.reaction_description,
    diagnosed_date: a.diagnosis_date
  }));
```

#### 2.3 慢性疾病诊断（新增）
```javascript
// 从慢性病管理数据中提取诊断信息
const chronicConditions = [];

// 高血压
try {
  const hypertensionData = readFile('data/hypertension-tracker.json');
  if (hypertensionData.hypertension_management?.diagnosis_date) {
    chronicConditions.push({
      condition: '高血压',
      diagnosis_date: hypertensionData.hypertension_management.diagnosis_date,
      classification: hypertensionData.hypertension_management.classification,
      current_bp: hypertensionData.hypertension_management.average_bp,
      risk_level: hypertensionData.hypertension_management.cardiovascular_risk?.risk_level
    });
  }
} catch (e) {
  // 文件不存在或读取失败，跳过
}

// 糖尿病
try {
  const diabetesData = readFile('data/diabetes-tracker.json');
  if (diabetesData.diabetes_management?.diagnosis_date) {
    chronicConditions.push({
      condition: diabetesData.diabetes_management.type === 'type_1' ? '1型糖尿病' : '2型糖尿病',
      diagnosis_date: diabetesData.diabetes_management.diagnosis_date,
      duration_years: diabetesData.diabetes_management.duration_years,
      hba1c: diabetesData.diabetes_management.hba1c?.history?.[0]?.value,
      control_status: diabetesData.diabetes_management.hba1c?.achievement ? '控制良好' : '需改善'
    });
  }
} catch (e) {
  // 文件不存在或读取失败，跳过
}

// COPD
try {
  const copdData = readFile('data/copd-tracker.json');
  if (copdData.copd_management?.diagnosis_date) {
    chronicConditions.push({
      condition: '慢阻肺（COPD）',
      diagnosis_date: copdData.copd_management.diagnosis_date,
      gold_grade: `GOLD ${copdData.copd_management.gold_grade}级`,
      cat_score: copdData.copd_management.symptom_assessment?.cat_score?.total_score,
      exacerbations_last_year: copdData.copd_management.exacerbations?.last_year
    });
  }
} catch (e) {
  // 文件不存在或读取失败，跳过
}
```

#### 2.4 当前用药
```javascript
// 只包含活跃的药物
const currentMedications = medications.medications
  .filter(m => m.active === true)
  .map(m => ({
    name: m.name,
    dosage: `${m.dosage.value}${m.dosage.unit}`,
    frequency: getFrequencyLabel(m.frequency),
    instructions: m.instructions,
    warnings: m.warnings || []
  }));
```

##### 2.4 医疗状况
从出院小结中提取诊断信息：
```javascript
const medicalConditions = dischargeSummaries
  .flatMap(ds => {
    const data = readFile(ds.file_path);
    return data.diagnoses || [];
  })
  .map(d => ({
    condition: d.condition,
    diagnosis_date: d.date,
    status: d.status || "随访中"
  }));
```

##### 2.5 植入物
从手术记录中提取植入物信息：
```javascript
const implants = surgeries
  .flatMap(s => {
    const data = readFile(s.file_path);
    return data.procedure?.implants || [];
  })
  .map(i => ({
    type: i.type,
    implant_date: i.date,
    hospital: i.hospital,
    notes: i.notes
  }));
```

##### 2.6 近期辐射暴露
```javascript
const recentRadiation = {
  total_dose_last_year: calculateTotalDose(radiation.records, 'last_year'),
  last_exam: radiation.records[radiation.records.length - 1]
};
```

#### 步骤 3: 生成信息卡片

按照优先级组织信息：
```javascript
const emergencyCard = {
  version: "1.0",
  generated_at: new Date().toISOString(),
  basic_info: basicInfo,
  critical_allergies: criticalAllergies.sort(bySeverityDesc),
  current_medications: currentMedications,
  medical_conditions: [...medicalConditions, ...chronicConditions], // 合并急症和慢性病
  implants: implants,
  recent_radiation_exposure: recentRadiation,
  disclaimer: "此信息卡仅供参考，不替代专业医疗诊断",
  data_source: "my-his个人健康信息系统",
  chronic_conditions: chronicConditions // 单独字段便于访问
};
```

#### 步骤 4: 格式化输出

##### JSON格式
直接输出结构化JSON数据。

##### 文本格式
生成易读的文本卡片：
```
╔═══════════════════════════════════════════════════════════╗
║                  紧急医疗信息卡                          ║
╠═══════════════════════════════════════════════════════════╣
║ 姓名：张三                      年龄：35岁               ║
║ 血型：A+                       体重：70kg                ║
╠═══════════════════════════════════════════════════════════╣
║ 🆘 严重过敏                                              ║
║ ─────────────────────────────────────────────────────── ║
║ • 青霉素 - 过敏性休克（4级）🆘                          ║
║   反应：呼吸困难、喉头水肿、意识丧失                     ║
╠═══════════════════════════════════════════════════════════╣
║ 💊 当前用药                                              ║
║ ─────────────────────────────────────────────────────── ║
║ • 氨氯地平 5mg - 每日1次（高血压）                      ║
║ • 二甲双胍 1000mg - 每日2次（糖尿病）                    ║
╠═══════════════════════════════════════════════════════════╣
║ 🏥 慢性疾病                                              ║
║ ─────────────────────────────────────────────────────── ║
║ • 高血压（2023-01-01诊断，1级，控制中）                 ║
║   平均血压：132/82 mmHg                                 ║
║ • 2型糖尿病（2022-05-10诊断，HbA1c 6.8%）              ║
║   控制状态：良好                                        ║
║ • 慢阻肺（2020-03-15诊断，GOLD 2级）                    ║
║   CAT评分：18分                                        ║
╠═══════════════════════════════════════════════════════════╣
║ 🏥 其他疾病                                              ║
║ ─────────────────────────────────────────────────────── ║
║ （其他急症或手术诊断，如有）                            ║
╠═══════════════════════════════════════════════════════════╣
║ 📿 植入物                                                ║
║ ─────────────────────────────────────────────────────── ║
║ • 心脏起搏器（2022-06-10植入）                           ║
║   医院：XX医院                                           ║
║   注意：定期复查，避免MRI检查                            ║
╠═══════════════════════════════════════════════════════════╣
║ 📞 紧急联系人                                            ║
║ ─────────────────────────────────────────────────────── ║
║ • 李四（配偶）- 138****1234                              ║
╠═══════════════════════════════════════════════════════════╣
║ ⚠️  免责声明                                            ║
║ 此信息卡仅供参考，不替代专业医疗诊断                     ║
║ 生成时间：2025-12-31 12:34:56                            ║
╚═══════════════════════════════════════════════════════════╝
```

##### 二维码格式
将JSON数据转换为二维码图片：
```javascript
const qrCode = generateQRCode(JSON.stringify(emergencyCard));
emergencyCard.qr_code = qrCode;
```

#### 步骤 5: 保存文件

根据用户选择的格式保存文件：
```javascript
// JSON格式
saveFile('emergency-card.json', JSON.stringify(emergencyCard, null, 2));

// 文本格式
saveFile('emergency-card.txt', generateTextCard(emergencyCard));

// 二维码格式
saveFile('emergency-card-qr.png', emergencyCard.qr_code);
```

#### 步骤 6: 输出确认信息

```
✅ 紧急医疗信息卡已生成

文件位置：data/emergency-cards/emergency-card-2025-12-31.json
生成时间：2025-12-31 12:34:56

包含信息：
━━━━━━━━━━━━━━━━━━━━━━━━━━
✓ 基础信息（姓名、年龄、血型）
✓ 严重过敏（1项4级过敏）
✓ 当前用药（2种药物）
✓ 医疗状况（2种疾病）
✓ 植入物（1项）
✓ 紧急联系人（1人）

💡 使用建议：
━━━━━━━━━━━━━━━━━━━━━━━━━━
• 将JSON文件保存到手机云盘
• 将二维码保存到手机相册
• 打印文本版随身携带
• 旅行前更新信息

⚠️  注意事项：
━━━━━━━━━━━━━━━━━━━━━━━━━━
• 此信息卡仅供参考，不替代专业医疗诊断
• 定期更新（建议每3个月或健康信息变化后）
• 如有严重过敏，请随身携带过敏急救卡
```

## 数据源

### 主要数据源
- **data/profile.json**：用户基础信息、血型、紧急联系人
- **data/allergies.json**：过敏史和严重程度分级
- **data/medications/medications.json**：当前用药计划和剂量

### 慢性病数据源（新增）
- **data/hypertension-tracker.json**：高血压管理数据（诊断日期、分级、血压控制、靶器官损害、心血管风险）
- **data/diabetes-tracker.json**：糖尿病管理数据（类型、HbA1c、血糖控制、并发症筛查）
- **data/copd-tracker.json**：COPD管理数据（GOLD分级、CAT评分、急性加重史、肺功能）

### 辅助数据源
- **data/radiation-records.json**：近期辐射暴露记录
- **data/手术记录/**/*.json**：手术植入物信息
- **data/出院小结/**/*.json**：医疗诊断信息

### 可选数据源
- **data/index.json**：全局数据索引

## 安全性原则

### 必须遵循
- ❌ 不添加用药建议（仅列出当前用药）
- ❌ 不提供诊断结论（仅列出已知诊断）
- ❌ 不给出治疗建议（不替代医生）
- ❌ 标注免责声明（仅供参考）

### 信息准确度
- ✅ 仅提取已记录的信息（不推测或推断）
- ✅ 标注信息来源和更新时间
- ✅ 建议定期更新信息

### 隐私保护
- ✅ 敏感信息可选隐藏
- ✅ 电话号码部分隐藏（如：138****1234）
- ✅ 所有数据仅保存在本地

## 错误处理

### 数据缺失
- **过敏数据缺失**：输出"未记录过敏史"
- **用药数据缺失**：输出"未记录当前用药"
- **植入物数据缺失**：输出"无植入物"

### 文件读取失败
- **无法读取profile.json**：使用默认值（姓名：未设置）
- **无法读取allergies.json**：跳过过敏信息
- **继续生成其他信息**：不因单个文件失败而中断

### 二维码生成失败
- 降级为文本格式输出
- 提示用户手动记录信息

## 示例输出

完整示例请参考相关文档。

## 测试数据

测试数据请参考相关文档。

## 格式说明

详细格式请参考相关文档。


## When to Use

Use this skill when tackling tasks related to its primary domain or functionality as described above.

---

## Merged Reference (legacy variant)

---
name: family-health-analyzer
description: 分析家族病史、评估遗传风险、识别家庭健康模式、提供个性化预防建议
allowed-tools: Read, Write, Grep, Glob
---

# 家庭健康分析技能

## 技能概述

本技能提供家庭健康数据的深度分析,包括:
- 遗传风险评估
- 家族疾病模式识别
- 家庭共同问题分析
- 个性化预防建议
- 可视化报告生成

## 触发条件

当用户请求以下内容时,使用此技能:
- "家庭健康报告"
- "家族病史分析"
- "遗传风险评估"
- "家庭健康趋势"
- 执行 `/family report` 命令
- 执行 `/family risk` 命令

## 分析步骤

### 步骤1: 确定分析目标

识别用户请求类型:
- 家族病史分析
- 遗传风险评估
- 家庭健康趋势
- 家庭健康报告

### 步骤2: 读取家庭数据

**数据源:**
1. 主数据文件: `data/family-health-tracker.json`
2. 集成模块数据:
   - `data/hypertension-tracker.json`
   - `data/diabetes-tracker.json`
   - `data/profile.json`

### 步骤3: 数据验证与清洗

**验证项目:**
- 关系完整性
- 年龄合理性
- 数据一致性

### 步骤4: 遗传模式识别

**识别算法:**
1. 家族聚集性分析
2. 遗传模式识别
3. 早发病例识别(通常<50岁)

### 步骤5: 风险计算算法

**加权计算:**
```python
遗传风险评分 = (一级亲属患病数 × 0.4) +
              (早发病例数 × 0.3) +
              (家族聚集度 × 0.3)

风险等级:
- 高风险: ≥70%
- 中风险: 40%-69%
- 低风险: <40%
```

### 步骤6: 生成预防建议

**建议分类:**
- 筛查建议:定期检查项目
- 生活方式建议:饮食、运动、作息
- 就医建议:何时就医、咨询专科

**示例:**
```json
{
  "category": "screening",
  "action": "定期血压监测",
  "frequency": "每周3次",
  "start_age": 35,
  "priority": "high"
}
```

### 步骤7: 生成可视化报告

**HTML报告组件:**
1. 家谱树(ECharts树图)
2. 遗传风险热力图
3. 疾病分布饼图
4. 预防建议时间线

### 步骤8: 输出结果

**输出格式:**
1. 文本报告(简洁版):命令行输出
2. HTML报告(完整版):可视化图表

## 安全原则

### 医学安全边界
- ✅ 仅基于家族病史进行统计分析
- ✅ 提供预防建议和筛查提醒
- ✅ 明确标注不确定性
- ❌ 不进行遗传疾病诊断
- ❌ 不预测个体发病概率
- ❌ 不推荐具体治疗方案

### 免责声明
每次分析输出必须包含:
```
⚠️ 免责声明:
1. 本分析基于家族病史统计,仅供参考
2. 遗传风险评估不预测个体发病
3. 所有医疗决策请咨询专业医师
4. 遗传咨询建议咨询专业遗传咨询师
```

## 集成现有模块

- 读取高血压管理数据
- 读取糖尿病管理数据
- 关联用药记录

---

**技能版本**: v1.0
**最后更新**: 2025-01-08
**维护者**: WellAlly Tech

---

## Merged Reference (legacy variant)

---
name: fitness-analyzer
description: 分析运动数据、识别运动模式、评估健身进展，并提供个性化训练建议。支持与慢性病数据的关联分析。
allowed-tools: Read, Grep, Glob, Write
---

# 运动分析器技能

分析运动数据，识别运动模式，评估健身进展，并提供个性化训练建议。

## 功能

### 1. 运动趋势分析
分析运动量、频率、强度的变化趋势，识别改善或需要调整的方面。

**分析维度**：
- 运动量趋势（时长、距离、卡路里）
- 运动频率趋势（每周运动天数）
- 强度分布变化（低/中/高强度占比）
- 运动类型偏好变化

**输出**：
- 趋势方向（改善/稳定/下降）
- 变化幅度和百分比
- 趋势显著性
- 改进建议

### 2. 运动进步追踪
追踪特定运动类型的进步情况，量化健身效果。

**支持的进步追踪**：
- **跑步进步**：配速提升、距离增加、心率改善
- **力量训练进步**：重量增加、容量提升、RPE变化
- **耐力进步**：运动时长增加、距离延长
- **柔韧性进步**：关节活动度改善

**输出**：
- 开始值 vs 当前值
- 改善百分比
- 进步可视化
- 达成的里程碑

### 3. 运动习惯分析
识别用户的运动习惯和模式。

**分析内容**：
- 常用运动时间（早晨/下午/晚上）
- 运动频率模式（每周几天）
- 运动类型偏好
- 休息日分布
- 运动一致性评分

**输出**：
- 习惯总结
- 一致性评分（0-100）
- 优化建议
- 习惯养成建议

### 4. 相关性分析
分析运动与其他健康指标的相关性。

**支持的相关性分析**：
- **运动 ↔ 体重**：运动消耗与体重变化的关系
- **运动 ↔ 血压**：运动对血压的长期影响
- **运动 ↔ 血糖**：运动对血糖控制的效果
- **运动 ↔ 情绪/睡眠**：运动对情绪和睡眠的影响

**输出**：
- 相关系数（-1到1）
- 相关性强度（弱/中/强）
- 统计显著性
- 因果关系推断
- 实践建议

### 5. 个性化建议生成
基于用户数据生成个性化运动建议。

**建议类型**：
- **运动频率建议**：是否需要增加/减少运动频率
- **运动强度建议**：强度调整建议
- **运动类型建议**：推荐尝试的运动类型
- **运动时间建议**：最佳运动时间
- **恢复建议**：休息和恢复建议

**建议依据**：
- WHO/ACSM/AHA运动指南
- 用户运动历史数据
- 用户健康状况
- 用户健身目标

## 输出格式

### 趋势分析报告

```markdown
# 运动趋势分析报告

## 分析周期
2025-03-20 至 2025-06-20（3个月）

## 运动量趋势

### 运动时长
- 趋势：⬆️ 上升
- 开始：平均120分钟/周
- 当前：平均180分钟/周
- 变化：+50%（+60分钟/周）
- 解读：运动量显著增加，表现优秀

### 卡路里消耗
- 趋势：⬆️ 上升
- 开始：平均960卡/周
- 当前：平均1440卡/周
- 变化：+50%
- 解读：运动消耗增加，有助于体重管理

### 运动距离
- 趋势：⬆️ 上升
- 开始：平均10公里/周
- 当前：平均20公里/周
- 变化：+100%
- 解读：耐力显著提升

## 运动频率

- 当前频率：4天/周
- 目标频率：4-5天/周
- 状态：✅ 达标
- 建议：保持当前频率

## 强度分布

| 强度 | 占比 | 变化 |
|------|------|------|
| 低强度 | 25% | +5% |
| 中等强度 | 55% | -10% |
| 高强度 | 20% | +5% |

**分析**：强度分布合理，中等强度占主导，符合有氧运动建议。

## 运动类型分布

| 运动类型 | 占比 |
|---------|------|
| 跑步 | 50% |
| 瑜伽 | 25% |
| 力量训练 | 25% |

**建议**：可以适当增加力量训练比例至30-40%。

## 洞察与建议

### 优势
1. ✅ 运动量稳定增长，(+50%)
2. ✅ 运动频率稳定，每周4天
3. ✅ 休息日充足，恢复良好

### 改进建议
1. 📈 每周增加2次力量训练
2. 📈 尝试不同运动类型避免单调
3. 📈 适当增加高强度间歇训练(HIIT)

### 警示
1. ⚠️ 注意运动强度不宜过高，控制在中等强度为主
```

### 相关性分析报告

```markdown
# 运动与血压相关性分析

## 数据来源
- 运动数据：fitness-logs (2025-03-20 至 2025-06-20)
- 血压数据：hypertension-tracker (同期)

## 分析结果

### 相关系数
- 变量：每周运动时长 ↔ 收缩压
- 相关系数：r = -0.68
- 相关性强度：**强负相关**
- 统计显著性：p < 0.01 **高度显著**

### 解读
运动时长与收缩压呈强负相关，意味着：
- 运动越多，血压越低
- 每增加30分钟运动，收缩压平均下降3-5 mmHg

### 实践建议
1. ✅ 继续保持规律运动，每周5-7天
2. ✅ 每次运动30-60分钟，中等强度
3. ✅ 优先选择有氧运动（快走、慢跑、骑行）
4. ⚠️ 避免憋气动作和突然爆发性运动

### 医学参考
- AHA声明：规律有氧运动可降低收缩压5-7 mmHg
- 您的运动效果：降低约10 mmHg，效果显著！
```

### 进步追踪报告

```markdown
# 跑步进步追踪

## 分析周期
2025-01-01 至 2025-06-20（6个月）

## 配速进步

| 指标 | 开始 | 当前 | 改善 |
|------|------|------|------|
| 平均配速 | 7:30 min/km | 6:00 min/km | +20% ⬆️ |
| 最快配速 | 7:00 min/km | 5:30 min/km | +22% ⬆️ |
| 5公里用时 | 37:30 | 30:00 | +20% ⬆️ |

**趋势**：配速持续稳定提升，进步显著！

## 距离进步

| 指标 | 开始 | 当前 | 改善 |
|------|------|------|------|
| 最长单次距离 | 3 km | 12 km | +300% ⬆️ |
| 月度总距离 | 40 km | 86 km | +115% ⬆️ |
| 平均距离 | 5 km | 6 km | +20% ⬆️ |

**趋势**：耐力大幅提升，可以完成更长距离。

## 心率改善

| 指标 | 开始 | 当前 | 改善 |
|------|------|------|------|
| 静息心率 | 78 bpm | 72 bpm | -6 bpm ⬇️ |
| 相同配速心率 | 155 bpm | 145 bpm | -10 bpm ⬇️ |

**分析**：心肺功能显著改善，相同配速下心率降低。

## 里程碑

- ✅ 2025-03-15：首次完成5公里跑
- ✅ 2025-05-20：首次完成10公里跑
- ✅ 2025-06-10：配速突破6:00 min/km

## 下一步目标

- 🎯 完成半程马拉松（21公里）
- 🎯 配速提升至5:30 min/km
- 🎯 尝试间歇训练提升速度
```

## 数据源

### 主要数据源

1. **运动日志**
   - 路径：`data/fitness-logs/YYYY-MM/YYYY-MM-DD.json`
   - 内容：运动记录（类型、时长、强度、心率、距离等）
   - 频率：每次运动后更新

2. **用户档案**
   - 路径：`data/fitness-tracker.json`
   - 内容：用户档案、健身目标、统计数据
   - 更新：定期更新

3. **健康数据关联**
   - `data/hypertension-tracker.json`（血压数据）
   - `data/diabetes-tracker.json`（血糖数据）
   - `data/profile.json`（体重、BMI等）

### 数据质量检查

- 数据完整性：检查必要字段是否存在
- 数据合理性：检查数值是否在合理范围内
- 时间一致性：检查时间戳是否合理
- 重复数据：检测并处理重复记录

## 算法说明

### 1. 线性回归趋势分析

使用线性回归分析运动数据的时间趋势。

**公式**：
y = a + bx

其中：
- y：运动指标（时长、卡路里、距离等）
- x：时间
- a：截距
- b：斜率（趋势方向和速度）

**解释**：
- b > 0：上升趋势
- b < 0：下降趋势
- b ≈ 0：稳定

### 2. Pearson相关系数

用于分析两个变量之间的线性相关性。

**公式**：
r = Σ[(xi - x̄)(yi - ȳ)] / √[Σ(xi - x̄)² × Σ(yi - ȳ)²]

**范围**：-1 ≤ r ≤ 1

**解释**：
- r = 1：完全正相关
- r = -1：完全负相关
- r = 0：无线性相关

**强度判断**：
- |r| < 0.3：弱相关
- 0.3 ≤ |r| < 0.7：中等相关
- |r| ≥ 0.7：强相关

### 3. 配速计算

**配速** = 运动时长 / 距离

单位：min/km 或 min/mile

**示例**：
- 30分钟跑5公里
- 配速 = 30 / 5 = 6 min/km

### 4. MET能量代谢计算

**卡路里消耗** = MET × 体重(kg) × 时间(小时)

**常见运动的MET值**：
- 走路（3-5 km/h）：3.5-5 MET
- 慢跑（8 km/h）：8 MET
- 快跑（10 km/h）：10 MET
- 游泳：6-10 MET
- 骑行（休闲）：4 MET
- 力量训练：5 MET
- 瑜伽：3 MET

## 医学安全边界

⚠️ **重要声明**
本分析仅供健康参考，不构成医疗建议。

### 分析能力范围

✅ **能做到**：
- 运动数据统计和分析
- 趋势识别和可视化
- 相关性计算和解释
- 一般性运动建议

❌ **不做到**：
- 疾病诊断
- 运动风险评估
- 具体运动处方设计
- 运动损伤诊断和治疗

### 危险信号检测

在分析过程中检测以下危险信号：

1. **心率异常**
   - 运动心率 > 95%最大心率
   - 静息心率 > 100 bpm

2. **血压异常**
   - 收缩压 ≥ 180 mmHg
   - 舒张压 ≥ 110 mmHg

3. **过度训练迹象**
   - 连续7天高强度运动
   - 运动感受持续下降（RPE > 17）

4. **体重快速下降**
   - 每周减重 > 1kg（可能不健康）

### 建议分级

**Level 1: 一般性建议**
- 基于WHO/ACSM指南
- 适用于一般人群

**Level 2: 参考性建议**
- 基于用户数据
- 需结合个人情况

**Level 3: 医疗建议**
- 涉及疾病管理
- 需医生确认

## 使用示例

### 示例1：生成运动趋势报告

```bash
/fitness trend 3months
```

输出：
- 3个月运动趋势分析
- 运动量、频率、强度变化
- 洞察和建议

### 示例2：追踪跑步进步

```bash
/fitness analysis progress running
```

输出：
- 配速进步
- 距离进步
- 心率改善
- 里程碑达成

### 示例3：分析运动与血压相关性

```bash
/fitness analysis correlation blood_pressure
```

输出：
- 相关系数
- 相关性强度
- 显著性检验
- 实践建议

---

**技能版本**: v1.0
**最后更新**: 2026-01-02
**维护者**: WellAlly Tech

---

## Merged Reference (legacy variant)

---
name: geo-fundamentals
description: "Generative Engine Optimization for AI search engines (AI answer engines)."
risk: unknown
source: community
date_added: "2026-02-27"
---

# GEO Fundamentals

> Optimization for AI-powered search engines.

---

## 1. What is GEO?

**GEO** = Generative Engine Optimization

| Goal | Platform |
|------|----------|
| Be cited in AI responses | AI answer engines, Gemini |

### SEO vs GEO

| Aspect | SEO | GEO |
|--------|-----|-----|
| Goal | #1 ranking | AI citations |
| Platform | Google | AI engines |
| Metrics | Rankings, CTR | Citation rate |
| Focus | Keywords | Entities, data |

---

## 2. AI Engine Landscape

| Engine | Citation Style | Opportunity |
|--------|----------------|-------------|
| **Perplexity** | Numbered [1][2] | Highest citation rate |
| **ChatGPT** | Inline/footnotes | Custom GPTs |
| **AI assistant** | Contextual | Long-form content |
| **Gemini** | Sources section | SEO crossover |

---

## 3. RAG Retrieval Factors

How AI engines select content to cite:

| Factor | Weight |
|--------|--------|
| Semantic relevance | ~40% |
| Keyword match | ~20% |
| Authority signals | ~15% |
| Freshness | ~10% |
| Source diversity | ~15% |

---

## 4. Content That Gets Cited

| Element | Why It Works |
|---------|--------------|
| **Original statistics** | Unique, citable data |
| **Expert quotes** | Authority transfer |
| **Clear definitions** | Easy to extract |
| **Step-by-step guides** | Actionable value |
| **Comparison tables** | Structured info |
| **FAQ sections** | Direct answers |

---

## 5. GEO Content Checklist

### Content Elements

- [ ] Question-based titles
- [ ] Summary/TL;DR at top
- [ ] Original data with sources
- [ ] Expert quotes (name, title)
- [ ] FAQ section (3-5 Q&A)
- [ ] Clear definitions
- [ ] "Last updated" timestamp
- [ ] Author with credentials

### Technical Elements

- [ ] Article schema with dates
- [ ] Person schema for author
- [ ] FAQPage schema
- [ ] Fast loading (< 2.5s)
- [ ] Clean HTML structure

---

## 6. Entity Building

| Action | Purpose |
|--------|---------|
| Google Knowledge Panel | Entity recognition |
| Wikipedia (if notable) | Authority source |
| Consistent info across web | Entity consolidation |
| Industry mentions | Authority signals |

---

## 7. AI Crawler Access

### Key AI User-Agents

| Crawler | Engine |
|---------|--------|
| GPTBot | ChatGPT/OpenAI |
| AI-Assistant-Web | AI assistant |
| PerplexityBot | Perplexity |
| Googlebot | Gemini (shared) |

### Access Decision

| Strategy | When |
|----------|------|
| Allow all | Want AI citations |
| Block GPTBot | Don't want OpenAI training |
| Selective | Allow some, block others |

---

## 8. Measurement

| Metric | How to Track |
|--------|--------------|
| AI citations | Manual monitoring |
| "According to [Brand]" mentions | Search in AI |
| Competitor citations | Compare share |
| AI-referred traffic | UTM parameters |

---

## 9. Anti-Patterns

| ❌ Don't | ✅ Do |
|----------|-------|
| Publish without dates | Add timestamps |
| Vague attributions | Name sources |
| Skip author info | Show credentials |
| Thin content | Comprehensive coverage |

---

> **Remember:** AI cites content that's clear, authoritative, and easy to extract. Be the best answer.

---

## Script

| Script | Purpose | Command |
|--------|---------|---------|
| `scripts/geo_checker.py` | GEO audit (AI citation readiness) | `python scripts/geo_checker.py <project_path>` |


## When to Use
This skill is applicable to execute the workflow or actions described in the overview.

---

## Merged Reference (legacy variant)

---
name: goal-analyzer
description: 分析健康目标数据、识别目标模式、评估目标进度,并提供个性化目标管理建议。支持与营养、运动、睡眠等健康数据的关联分析。
allowed-tools: Read, Grep, Glob, Write
---

# 健康目标分析器技能

分析健康目标数据,识别目标模式和进度,评估目标达成情况,并提供个性化目标管理建议。

## 功能

### 1. SMART目标验证

验证设定的新目标是否符合SMART原则。

**验证维度**:
- **S**pecific(具体性)
  - 目标是否明确具体
  - 是否有清晰的定义
  - 是否避免模糊表述

- **M**easurable(可衡量性)
  - 是否有可量化的指标
  - 是否有明确的衡量标准
  - 是否可以追踪进度

- **A**chievable(可实现性)
  - 目标是否现实可行
  - 是否考虑了当前状况
  - 是否在合理时间范围内
  - 减重目标:建议每周0.5-1公斤
  - 运动目标:建议每周3-5次,每次30-60分钟

- **R**elevant(相关性)
  - 目标是否与健康相关
  - 是否符合用户整体健康计划
  - 是否与现有目标协调

- **T**ime-bound(有时限)
  - 是否有明确的截止日期
  - 时间框架是否合理
  - 是否有阶段性里程碑

**输出**:
- SMART评分(每个维度1-5分)
- 总体评分和等级(S级/A级/B级/C级)
- 改进建议
- 目标优化方案

**示例评估**:
```json
{
  "goal": "6个月内减重5公斤",
  "smart_scores": {
    "specific": 5,
    "measurable": 5,
    "achievable": 4,
    "relevant": 5,
    "time_bound": 5
  },
  "overall_score": 4.8,
  "grade": "A",
  "assessment": "优秀的SMART目标",
  "suggestions": [
    "建议设定阶段性里程碑(每2个月减重1.5-2公斤)",
    "建议配合运动计划和饮食调整"
  ]
}
```

---

### 2. 目标进度追踪

追踪和分析目标的完成进度。

**追踪内容**:
- **当前进度**
  - 完成百分比
  - 当前数值vs目标数值
  - 剩余差距

- **时间进度**
  - 已用时间占比
  - 剩余时间
  - 进度超前/落后判断

- **速度分析**
  - 平均进度速度(每周/每月)
  - 预计完成时间
  - 是否需要调整计划

- **趋势识别**
  - 进度趋势(加速/稳定/减速)
  - 周期性模式
  - 异常波动检测

**输出**:
- 进度可视化(进度条、百分比)
- 完成概率预测
- 时间预估(乐观/中性/悲观)
- 调整建议

**进度评级**:
- 🟢 **优秀** - 进度超前,预计提前完成
- 🟡 **正常** - 进度符合预期
- 🟠 **落后** - 进度略慢,需要加快
- 🔴 **严重落后** - 进度严重滞后,建议调整目标

---

### 3. 习惯养成分析

分析习惯的养成情况和连续性。

**分析内容**:
- **连续天数追踪**
  - 当前连续天数
  - 历史最长连续天数
  - 平均连续天数

- **完成率统计**
  - 总体完成率
  - 每周完成率
  - 每月完成率
  - 特定星期几完成率

- **习惯强度评估**
  - 习惯固化程度(1-10分)
  - 习惯稳定性评分
  - 自动化程度评估

- **习惯模式识别**
  - 最佳触发时间
  - 常见中断原因
  - 成功因素识别

**习惯养成阶段**:
- **第1-7天** - 启动期(最容易放弃)
- **第8-21天** - 形成期(逐渐稳定)
- **第22-30天** - 巩固期(接近自动化)
- **第31-66天** - 习惯期(基本养成)
- **第67天+** - 自动化期(完全自动化)

**输出**:
- 习惯热图(日历视图)
- 连续天数统计
- 完成率趋势图
- 习惯强度评分
- 习惯堆叠建议

**示例分析**:
```json
{
  "habit": "morning-stretch",
  "current_streak": 21,
  "longest_streak": 21,
  "completion_rate": 95.2,
  "strength_score": 7.5,
  "stage": "巩固期",
  "assessment": "习惯即将形成,继续保持!",
  "next_milestone": 30,
  "suggestions": [
    "继续保持,即将达到30天里程碑",
    "可以尝试添加新的相关习惯"
  ]
}
```

---

### 4. 动机评估与管理

评估和管理用户的动机水平。

**评估内容**:
- **动机评分追踪**
  - 当前动机水平(1-10分)
  - 动机变化趋势
  - 动机波动周期

- **动机因素分析**
  - 内在动机(健康、自我实现)
  - 外在动机(奖励、认可)
  - 社会支持(家人朋友鼓励)

- **动机低谷识别**
  - 动机下降信号
  - 常见低谷时间点
  - 风险时段预警

**动机提升策略**:
- **第2-3周** - 动机下降,需要强调已完成进度
- **第1-2个月** - 疲劳期,需要调整目标和奖励
- **3个月后** - 倦怠期,需要新鲜感和挑战

**输出**:
- 动机趋势图
- 动机低谷预警
- 个性化激励建议
- 奖励机制建议

**激励建议示例**:
- 当动机<5分:回顾初心,降低短期目标
- 当动机5-7分:强调进步,设置小奖励
- 当动机>7分:设定挑战,追求卓越

---

### 5. 成就系统管理

管理基础成就系统的解锁和进度。

**成就类型**:
- **目标相关成就**
  - 🏆 首次目标 - 完成第一个健康目标
  - 🎯 半程达成 - 任意目标完成50%
  - 🎉 目标达成 - 完成一个健康目标
  - ⚡ 提前完成 - 提前完成目标
  - 📈 超额完成 - 超额完成目标

- **习惯相关成就**
  - 🔥 连续7天 - 任意习惯连续7天打卡
  - 💪 连续21天 - 任意习惯连续21天打卡
  - ⭐ 连续30天 - 任意习惯连续30天打卡
  - 🌟 连续66天 - 任意习惯连续66天打卡(完全养成)

- **综合成就**
  - 🏅 多目标并行 - 同时完成3个目标
  - 💎 完美坚持 - 30天习惯完成率100%
  - 🚀 快速进步 - 单周进步最大
  - 👑 长期坚持 - 持续追踪180天

**成就追踪**:
- 已解锁成就列表
- 未解锁成就进度
- 成就解锁时间
- 成就相关建议

**输出**:
- 成就徽章展示
- 成就完成进度
- 下一个可解锁成就
- 成就达成建议

---

### 6. 障碍识别与建议

识别阻碍目标达成的因素,提供解决方案。

**障碍类型**:
- **时间障碍**
  - 忙碌、时间不足
  - 建议:缩短单次时长,增加频率;利用碎片时间

- **动机障碍**
  - 缺乏动力、拖延
  - 建议:设置提醒;寻找伙伴;调整目标

- **环境障碍**
  - 缺乏支持、诱惑过多
  - 建议:改变环境;寻找替代方案;建立支持系统

- **能力障碍**
  - 目标太难、缺乏知识
  - 建议:降低难度;学习知识;寻求专业帮助

- **身体障碍**
  - 疲劳、不适、受伤
  - 建议:休息恢复;调整计划;咨询医生

**输出**:
- 主要障碍识别
- 障碍频率统计
- 个性化解决方案
- 预防性建议

---

### 7. 数据关联分析

将健康目标与其他健康数据进行关联分析。

**关联维度**:
- **减重目标关联**
  - 营养摄入(卡路里、宏量营养素)
  - 运动消耗(频率、强度、时长)
  - 睡眠质量(时长、深度)
  - 体重变化趋势

- **运动目标关联**
  - 睡眠质量(恢复情况)
  - 营养摄入(蛋白质、碳水)
  - 身体指标(体重、体脂率)

- **饮食目标关联**
  - 营养素摄入(维生素、矿物质)
  - 身体指标(血压、血糖)
  - 运动表现

- **睡眠目标关联**
  - 运动时间(晚间运动影响)
  - 饮食时间(晚餐时间、咖啡因)
  - 屏幕时间(蓝光影响)

**分析方法**:
- 相关性分析(Pearson相关系数)
- 回归分析(预测模型)
- 趋势匹配(趋势同步性)
- 因果推断(潜在因果关系)

**输出**:
- 关联强度(强/中/弱)
- 正/负相关关系
- 因果关系推断
- 优化建议

**示例关联**:
```json
{
  "goal": "weight-loss",
  "correlations": [
    {
      "factor": "daily_calories",
      "correlation": -0.75,
      "strength": "强负相关",
      "insight": "每日卡路里摄入与减重进度呈强负相关,降低摄入加速进度"
    },
    {
      "factor": "exercise_frequency",
      "correlation": 0.68,
      "strength": "强正相关",
      "insight": "运动频率与减重进度呈强正相关,建议保持每周4次以上"
    },
    {
      "factor": "sleep_duration",
      "correlation": 0.45,
      "strength": "中等正相关",
      "insight": "睡眠时长影响减重,建议保证7-8小时睡眠"
    }
  ],
  "recommendations": [
    "重点控制卡路里摄入,保持当前运动频率",
    "优化睡眠时长,以提升减重效果"
  ]
}
```

---

### 8. 可视化报告生成

生成包含ECharts图表的HTML交互式报告。

**报告类型**:

#### A. 进度趋势报告
- 折线图展示目标进度随时间变化
- 里程碑标注
- 预测完成时间区间
- 进度速度分析

#### B. 习惯热图报告
- 日历热图展示习惯完成情况
- 颜色深浅表示完成频率
- 连续天数标注
- 完成率统计

#### C. 多目标对比报告
- 环形图展示多个目标完成率
- 优先级排序
- 资源分配建议
- 进度同步性分析

#### D. 动机趋势报告
- 折线图展示动机变化
- 动机与进度相关性
- 动机低谷预警
- 激励建议

#### E. 综合报告
- 包含以上所有图表
- 整体健康状况评估
- 综合改进建议
- 下阶段目标建议

**报告特点**:
- 响应式设计,支持移动端
- 深色/浅色主题切换
- 交互式图表(缩放、筛选)
- 数据表格展示
- 导出PDF功能
- 完全本地化,无需联网

**ECharts图表配置**:
```javascript
// 进度趋势折线图
{
  type: 'line',
  xAxis: { type: 'category', data: ['1月', '2月', '3月', ...] },
  yAxis: { type: 'value', name: '完成%' },
  series: [{
    name: '目标进度',
    type: 'line',
    data: [0, 15, 35, 50, 70, 85, 100],
    smooth: true,
    markLine: {
      data: [{ yAxis: 50, name: '50%里程碑' }]
    }
  }]
}

// 习惯热图
{
  type: 'heatmap',
  xAxis: { type: 'category', data: ['周一', '周二', ...] },
  yAxis: { type: 'category', data: ['第1周', '第2周', ...] },
  visualMap: {
    min: 0, max: 1,
    inRange: { color: ['#ebedf0', '#216e39'] }
  },
  series: [{
    type: 'heatmap',
    data: [[0, 0, 1], [1, 0, 1], [2, 0, 0], ...]
  }]
}

// 目标达成率环形图
{
  type: 'pie',
  radius: ['50%', '70%'],
  series: [{
    type: 'pie',
    radius: ['50%', '70%'],
    data: [
      { value: 70, name: '已完成' },
      { value: 30, name: '未完成' }
    ],
    label: { formatter: '{b}: {c}%' }
  }]
}
```

**输出**:
- HTML文件(包含完整的CSS、JS、ECharts)
- 图表交互功能
- 数据表格
- 分析文本
- 建议列表

---

## 医学安全边界

### 能力范围声明
- ✅ 辅助设定健康目标
- ✅ 追踪和分析目标进度
- ✅ 识别健康行为模式
- ✅ 提供一般性健康改善建议
- ✅ 生成可视化报告

- ❌ 不提供医疗诊断
- ❌ 不开具治疗处方
- ❌ 不替代专业医疗建议
- ❌ 不处理进食障碍或强迫行为

### 危险信号识别
**极端目标警告**:
- 减重目标>每周1公斤
- 增重目标>每周0.5公斤
- 极端卡路里限制(<1200卡/天)
- 过度运动(>2小时/天,7天/周)

**不健康行为迹象**:
- 完成率<30%持续3周
- 动机评分<3分持续2周
- 身体不适报告
- 强迫性行为模式

**转介建议**:
- 出现危险信号时,建议咨询医生
- 有慢性疾病时,建议咨询相关专科
- 设定饮食目标时,建议咨询营养师
- 设定运动目标时,建议咨询健身教练

---

## 输出格式

### 目标分析报告
```markdown
# 健康目标分析报告

## 目标概览
- 目标: 6个月内减重5公斤
- 开始日期: 2025-01-01
- 目标日期: 2025-06-30
- 当前日期: 2025-03-20

## SMART评估
- 具体性: ⭐⭐⭐⭐⭐ (5/5)
- 可衡量性: ⭐⭐⭐⭐⭐ (5/5)
- 可实现性: ⭐⭐⭐⭐ (4/5)
- 相关性: ⭐⭐⭐⭐⭐ (5/5)
- 有时限: ⭐⭐⭐⭐⭐ (5/5)

**总体评分: A (4.8/5)**

## 进度分析
- 当前进度: 70%
- 已完成: 3.5公斤 / 5.0公斤
- 时间进度: 27% (79天/180天)
- 进度评级: 🟢 优秀 (进度超前)

### 趋势分析
- 平均速度: 0.77公斤/月
- 预计完成: 2025-05-20 (提前40天)
- 进度趋势: 稳定上升

## 习惯追踪
### 早上拉伸习惯
- 当前连续: 21天 🔥
- 历史最长: 21天
- 完成率: 95.2%
- 习惯阶段: 巩固期
- 下一个里程碑: 30天 ⭐

## 动机评估
- 当前动机: 8/10
- 动机趋势: 稳定
- 动机状态: 良好

## 数据关联分析
### 强相关因素(影响度>60%)
1. 每日卡路里摄入 (负相关 -0.75)
2. 每周运动频次 (正相关 +0.68)
3. 睡眠时长 (正相关 +0.45)

### 建议
- 保持当前卡路里摄入水平
- 继续保持每周4次运动频率
- 优化睡眠时长至7-8小时

## 障碍识别
主要障碍: 社交活动饮食控制

解决方案:
- 社交活动前提前规划饮食
- 选择健康餐厅
- 适量控制份量

## 成就解锁
🔥 连续21天 - 早上拉伸习惯达成!
🎯 半程达成 - 减重目标完成50%!

## 下一步行动
1. 保持当前进度
2. 关注社交活动饮食控制
3. 继续养成早操习惯
4. 准备达成30天里程碑
```

---

## 技术实现要点

### 数据读取
- 读取主数据文件: `data-example/health-goals-tracker.json`
- 读取日志文件: `data-example/health-goals-logs/YYYY-MM/YYYY-MM-DD.json`
- 关联数据: `data-example/nutrition-tracker.json`, `fitness-tracker.json` 等

### 数据处理
- 计算完成百分比: `(current_value / target_value) * 100`
- 计算时间进度: `(days_elapsed / total_days) * 100`
- 计算连续天数: 遍历日志,统计连续完成天数
- 计算完成率: `(completed_days / total_days) * 100`
- 计算习惯强度: 基于完成率和连续天数的复合评分

### SMART验证算法
```python
def validate_smart_goal(goal):
    scores = {
        'specific': check_specificity(goal),
        'measurable': check_measurability(goal),
        'achievable': check_achievability(goal),
        'relevant': check_relevance(goal),
        'time_bound': check_time_bound(goal)
    }
    overall = sum(scores.values()) / len(scores)
    grade = get_grade(overall)
    return scores, overall, grade
```

### HTML报告生成
- 使用ECharts 5.x CDN
- 响应式CSS布局
- JavaScript处理图表交互
- 支持深色/浅色主题切换
- 数据从JSON文件动态加载

---

**使用此技能时,始终优先考虑用户的健康和安全!**

---

## Merged Reference (legacy variant)

---
name: mental-health-analyzer
description: 分析心理健康数据、识别心理模式、评估心理健康状况、提供个性化心理健康建议。支持与睡眠、运动、营养等其他健康数据的关联分析。
allowed-tools: Read, Grep, Glob, Write, Edit
---

# 心理健康分析技能

## 核心功能

心理健康分析技能提供全面的心理健康数据分析功能，帮助用户追踪心理状态、识别情绪模式、监测危机风险和优化应对策略。

**主要功能模块：**

1. **心理健康评估分析** - PHQ-9/GAD-7等量表评分趋势分析
2. **情绪模式识别** - 识别常见情绪、触发因素和应对方式效果
3. **心理治疗进展追踪** - 治疗目标达成和症状改善评估
4. **危机风险评估** - 多级危机风险检测（高/中/低）和预警
5. **睡眠-心理关联分析** - 睡眠质量与心理状态的关联性分析
6. **运动-情绪关联分析** - 运动与情绪改善的关系分析
7. **营养-心理关联分析** - 饮食对情绪和焦虑的影响分析
8. **慢性病-心理关联分析** - 慢性疾病与心理健康的关系分析

## 触发条件

技能在以下情况下自动触发：

1. 用户使用 `/mental trend` 查看心理状况趋势
2. 用户使用 `/mental pattern` 分析情绪模式
3. 用户使用 `/mental therapy progress` 查看治疗进展
4. 用户使用 `/crisis assessment` 进行危机风险评估
5. 用户使用 `/mental report` 生成心理健康报告

## 医学安全边界

**本技能不能做的事：**
- ❌ 不进行心理疾病诊断
- ❌ 不开具精神药物处方
- ❌ 不预测自杀风险或自伤行为
- ❌ 不替代专业心理治疗
- ❌ 不处理急性精神危机

**本技能能做的事：**
- ✅ 识别心理健康趋势和模式
- ✅ 评估危机风险等级并发出预警
- ✅ 提供应对策略建议（非治疗性）
- ✅ 追踪治疗进展和目标达成
- ✅ 提供就医建议和专业资源信息
- ✅ 分析心理健康与其他健康因素的关联

## 执行步骤

### 第1步：数据读取

读取心理健康数据文件：
- `data-example/mental-health-tracker.json` - 主心理健康档案
- `data-example/mental-health-logs/.index.json` - 日志索引
- `data-example/mental-health-logs/YYYY-MM/YYYY-MM-DD.json` - 每日情绪日记

**数据验证：**
- 检查文件是否存在
- 验证数据结构完整性
- 确认有足够的数据点进行分析（建议至少3次PHQ-9/GAD-7评估，或7天情绪日记）

### 第2步：心理健康评估趋势分析

**PHQ-9抑郁评分趋势分析：**
```
- 分析不同时间点的PHQ-9评分
- 计算评分变化速率（分/月）
- 识别严重程度变化（无/轻度/中度/重度）
- 检测PHQ-9第9项（自伤意念）的变化
- 预测未来趋势（改善/稳定/恶化）
- 与治疗进展关联分析
```

**GAD-7焦虑评分趋势分析：**
```
- 分析GAD-7评分时序变化
- 识别焦虑症状变化模式
- 关联触发因素与焦虑水平
- 评估应对方式效果
- 预测焦虑趋势
```

**PSQI睡眠质量与心理状态关联：**
```
- PSQI评分与PHQ-9/GAD-7评分的相关性
- 睡眠障碍对情绪的影响
- 睡眠改善与心理状态改善的关系
```

**严重程度变化检测：**
```
- 识别严重程度升级（需要关注）
- 识别严重程度降级（积极信号）
- 检测快速恶化（≥5分/月，危机预警）
- 检测快速改善（强化有效策略）
```

### 第3步：情绪模式识别

**常见情绪统计：**
```
- 统计最常见的主要情绪（top 5）
- 计算平均情绪强度
- 识别情绪分布模式
- 分析情绪多样性
```

**时间模式分析：**
```
- 一天中的情绪变化模式（早/中/晚）
- 一周中的情绪变化模式（周一至周日）
- 情绪波动程度（方差/标准差）
- 情绪稳定性评估
```

**触发因素分析：**
```
- 统计高频触发因素（top 10）
- 计算每个触发因素的平均影响
- 识别高危触发因素（高影响+高频）
- 触发因素与情绪类型的关联
```

**应对方式效果评估：**
```
- 计算每种应对方式的有效性（有帮助/没帮助的比例）
- 识别高效应对策略（>80%有效）
- 识别低效应对策略（<50%有效）
- 应对方式与情绪类型的匹配分析
```

### 第4步：心理治疗进展追踪

**治疗目标达成评估：**
```
- 计算每个目标的完成百分比
- 评估症状改善程度（基线→当前→目标）
- 预估目标达成时间
- 识别滞后目标（需要调整）
```

**治疗过程分析：**
```
- 治疗频率和依从性
- 作业完成率和质量
- 治疗联盟强度
- 咨询前后情绪变化
```

**症状改善评估：**
```
- PHQ-9/GAD-7评分变化（治疗前→治疗后）
- 症状缓解百分比
- 功能水平改善
- 生活质量变化
```

### 第5步：危机风险评估（优先级：最高）

**多级风险检测机制：**

```
风险等级计算（总分0-20+）：

1. PHQ-9第9项检测（最高优先级）
   - 得分=2（经常）：+10分，直接判定高风险
   - 得分=1（有时）：+5分
   - 得分=0（完全不会）：+0分

2. 症状快速恶化检测
   - 快速恶化（≥5分/月）：+5分
   - 恶化（2-4分/月）：+3分
   - 稳定（-1至1分/月）：+0分
   - 改善（≤-2分/月）：-2分

3. 高强度负面情绪占比检测
   - 占比>70%：+3分
   - 占比50-70%：+2分
   - 占比<50%：+0分

4. 情绪波动检测
   - 方差>6（波动大）：+2分
   - 方差4-6（波动中）：+1分
   - 方差<4（波动小）：+0分

5. 危机计划预警信号检测
   - 每出现一个预警信号：+2分

6. 社会退缩检测
   - 严重退缩（独处时间>80%）：+3分
   - 中度退缩（独处时间50-80%）：+2分
   - 轻度/无退缩：+0分

7. 功能受损检测
   - 严重受损（≥5天/周）：+4分
   - 中度受损（3-4天/周）：+2分
   - 轻度/无受损：+0分

风险等级判定：
- 高风险（≥10分）：立即就医，启动危机干预
- 中风险（5-9分）：密切关注，考虑就医（48小时内）
- 低风险（0-4分）：继续监测，定期评估
```

**危机预警信号检测：**
```
- 绝望感（hopelessness）
- 社会退缩（social_withdrawal）
- 极端情绪波动（extreme_mood_swings）
- 谈论死亡（talk_of_death）
- 送走财物（giving_away_possessions）
- 自伤意念（self_harm）
- 自杀想法（suicidal_thoughts）
- 物质滥用（substance_abuse）
```

**紧急行动触发条件：**
```
立即就医（24小时内）：
- PHQ-9第9项得分≥2
- 总风险评分≥10分
- 出现幻觉或妄想
- 有自伤或自杀计划

尽快就医（48小时内）：
- PHQ-9≥15分或GAD-7≥15分
- 总风险评分5-9分
- 症状快速恶化（≥5分/月）
- 严重影响功能

定期就医（1个月内）：
- PHQ-9 10-14分或GAD-7 10-14分
- 总风险评分<5分但症状持续
- 需要专业支持
```

### 第6步：睡眠-心理关联分析

**数据来源：**
- 读取 `data-example/sleep-tracker.json`
- 提取睡眠时长、睡眠质量（PSQI）、入睡时间等数据

**关联分析：**
```
- 睡眠时长与PHQ-9评分的相关性
- 睡眠质量与GAD-7评分的相关性
- 失眠症状与情绪稳定性的关系
- 睡眠改善与心理状态改善的时间关系
- 睡眠障碍类型与特定心理症状的关联
```

**分析输出：**
```
- 相关性系数和统计显著性
- 睡眠对心理状态的影响程度（高/中/低）
- 睡眠改善建议
- 睡眠与情绪的双向关系分析
```

### 第7步：运动-情绪关联分析

**数据来源：**
- 读取 `data-example/fitness-tracker.json`
- 提取运动频率、运动类型、运动强度、运动时长等数据

**关联分析：**
```
- 运动频率与平均情绪强度的关系
- 运动类型与情绪改善效果的关系
- 运动强度与焦虑水平的关系
- 运动时长与情绪持续时间的关系
- 运动后的情绪变化模式
- 运动习惯与抑郁症状的关系
```

**分析输出：**
```
- 运动对情绪的积极影响程度
- 最有效的运动类型推荐
- 最佳运动频率建议
- 运动与应对方式的关系
```

### 第8步：营养-心理关联分析

**数据来源：**
- 读取 `data-example/nutrition-tracker.json`
- 提取咖啡因摄入、糖分摄入、饮食习惯等数据

**关联分析：**
```
- 咖啡因摄入量与GAD-7焦虑评分的关系
- 糖分摄入与情绪波动的关联
- 饮食规律性与情绪稳定性的关系
- 特定营养素缺乏（维生素D、Omega-3）与抑郁症状
- 饮食模式与整体心理健康
```

**分析输出：**
```
- 饮食对心理状态的影响程度
- 营养建议（如减少咖啡因、均衡饮食）
- 可能的营养缺乏提示
- 饮食调整建议
```

### 第9步：慢性病-心理关联分析

**数据来源：**
- 读取相关慢性病数据文件（如 `diabetes-tracker.json`, `hypertension-tracker.json`）
- 提取疾病控制情况、症状负担、功能受限等数据

**关联分析：**
```
- 慢性疼痛与抑郁症状的关系
- 疾病控制情况与心理状态的关系
- 功能受限与心理健康的关系
- 疾病负担与焦虑水平的关系
- 共病模式识别
- 药物副作用对情绪的影响
- 药物依从性与症状改善的关系
```
```

**分析输出：**
```
- 慢性疾病对心理健康的影响程度
- 需要特别关注的心理问题
- 整体健康管理建议
- 心理支持对疾病管理的益处
```

### 第10步：生成报告

输出包括：
- 心理健康状况摘要
- 评估量表趋势分析
- 情绪模式和触发因素
- 治疗进展评估
- 危机风险等级和建议
- 与其他健康因素的关联分析
- 个性化建议和行动计划

## 输出格式

### 心理健康分析报告结构

```markdown
# 心理健康分析报告

**报告日期**: YYYY-MM-DD
**分析周期**: YYYY-MM-DD 至 YYYY-MM-DD
**数据完整性**: 良好

⚠️ **重要提示**：本报告仅供参考，不构成医学诊断。如有严重心理困扰，请寻求专业心理医生帮助。

---

## 危机风险预警

**当前风险等级**: 🟢 低风险 | 🟡 中风险 | 🔴 高风险

**风险评分**: X/20

**风险因素**:
- [列出检测到的风险因素]

**建议行动**:
- [根据风险等级提供具体建议]

---

## 1. 心理健康状况摘要

[整体评价：优秀/良好/一般/需改进/危机]
- PHQ-9评分：X分（严重程度）
- GAD-7评分：X分（严重程度）
- 睡眠质量：X分（PSQI）
- 整体趋势：改善/稳定/恶化

## 2. 心理评估趋势分析

### PHQ-9抑郁评分趋势
- 当前评分：X分
- 基线评分：X分
- 变化：±X分
- 变化速率：X分/月
- 趋势：改善/稳定/恶化
- 严重程度变化：[严重程度1] → [严重程度2]

**图表描述**：
- [折线图展示PHQ-9评分变化]
- [标记严重程度分界线：5, 10, 15]

**特别关注**：
- 第9项（自伤意念）得分：X
- 最高分项：[条目名称]
- 持续存在问题：[列出条目]

### GAD-7焦虑评分趋势
- 当前评分：X分
- 基线评分：X分
- 变化：±X分
- 变化速率：X分/月
- 趋势：改善/稳定/恶化

**图表描述**：
- [折线图展示GAD-7评分变化]
- [标记严重程度分界线：5, 10, 15]

**主要焦虑症状**：
- 最高分项：[条目名称]
- 主要触发因素：[列出]

### PSQI睡眠质量
- 总分：X分
- 睡眠质量：[评价]
- 主要问题：[列出问题成分]

## 3. 情绪模式分析

### 常见情绪
1. [情绪1] - 占比X%，平均强度X/10
2. [情绪2] - 占比X%，平均强度X/10
3. [情绪3] - 占比X%，平均强度X/10

**图表描述**：
- [饼图展示情绪分布]
- [雷达图展示多维度情绪]

### 时间模式
- 早晨：主要情绪[情绪]，平均强度X/10
- 下午：主要情绪[情绪]，平均强度X/10
- 晚上：主要情绪[情绪]，平均强度X/10

### 周模式
- 周一至周五：主要情绪[情绪]，平均强度X/10
- 周末：主要情绪[情绪]，平均强度X/10

### 情绪稳定性
- 波动程度：高/中/低
- 情绪方差：X

**图表描述**：
- [折线图展示情绪强度时序变化]
- [波动范围可视化]

## 4. 触发因素分析

### 高频触发因素（Top 10）
| 排名 | 触发因素 | 频次 | 平均影响 |
|------|----------|------|----------|
| 1 | [触发因素1] | X次 | 高/中/低 |
| 2 | [触发因素2] | X次 | 高/中/低 |
| ... |

### 高危触发因素（高影响+高频）
- [触发因素1] - 频次X，影响高，建议：[应对建议]
- [触发因素2] - 频次X，影响高，建议：[应对建议]

**图表描述**：
- [柱状图展示触发因素频次]
- [热图展示触发因素与情绪类型的关联]

## 5. 应对方式效果评估

### 应对方式排名（按效果）
| 应对方式 | 有效次数 | 无效次数 | 有效率 | 排名 |
|----------|----------|----------|--------|------|
| [应对方式1] | X次 | X次 | XX% | 1 |
| [应对方式2] | X次 | X次 | XX% | 2 |
| ... |

### 高效应对策略（>80%有效）
- [策略1] - 有效率XX%，推荐使用
- [策略2] - 有效率XX%，推荐使用

### 低效应对策略（<50%有效）
- [策略1] - 有效率XX%，建议调整或停止
- [策略2] - 有效率XX%，建议调整或停止

**图表描述**：
- [条形图展示应对方式效果排名]
- [饼图展示有效/无效比例]

## 6. 心理治疗进展

### 治疗概况
- 治疗类型：[CBT/心理动力学/人本主义等]
- 治疗频率：[每周/每两周等]
- 已进行咨询次数：X次
- 治疗时长：X个月

### 治疗目标进展
| 目标 | 基线 | 当前 | 目标 | 进展 | 预计达成时间 |
|------|------|------|------|------|--------------|
| [目标1] | X分 | X分 | X分 | XX% | YYYY-MM-DD |
| [目标2] | X分 | X分 | X分 | XX% | YYYY-MM-DD |

**整体进展评价**：[优秀/良好/一般/需改进]

### 症状改善
- PHQ-9评分变化：X分 → X分，改善XX%
- GAD-7评分变化：X分 → X分，改善XX%
- 整体功能水平：[改善/稳定/恶化]

### 作业完成情况
- 平均完成率：XX%
- 高质量完成：XX%
- 需要加强的方面：[列出]

## 7. 危机风险评估

### 风险等级
**当前风险等级**: 🟢 低风险 | 🟡 中风险 | 🔴 高风险

**风险评分**: X/20

### 风险因素分析
| 风险因素 | 得分 | 详情 |
|----------|------|------|
| PHQ-9第9项 | X分 | 得分X，[详情] |
| 症状变化 | X分 | [快速恶化/恶化/稳定/改善] |
| 情绪强度 | X分 | 高强度负面情绪占比XX% |
| 情绪波动 | X分 | 波动[大/中/小] |
| 预警信号 | X分 | 出现X个预警信号：[列出] |
| 社会退缩 | X分 | [严重/中度/轻度/无]退缩 |
| 功能受损 | X分 | [严重/中度/轻度/无]受损 |

### 检测到的预警信号
- [如有列出]

### 建议行动
- [根据风险等级提供具体行动建议]

### 紧急资源
- 心理危机热线：400-xxx-xxxx（24小时）
- 精神科急诊：就近三甲医院
- 急救电话：120

## 8. 与其他健康因素的关联分析

### 睡眠-心理关联
**关联强度**: 高/中/低

**主要发现**:
- 睡眠时长与PHQ-9评分的相关性：r=X.XX
- 睡眠质量与情绪稳定性的关系：[描述]
- 主要睡眠问题：[列出]
- 改善睡眠对心理状态的潜在益处：[描述]

**建议**:
- [具体的睡眠改善建议]

### 运动-情绪关联
**关联强度**: 高/中/低

**主要发现**:
- 运动频率与情绪改善的关系：[描述]
- 最有效的运动类型：[列出]
- 运动后的情绪变化：[描述]

**建议**:
- [具体的运动建议]

### 营养-心理关联
**关联强度**: 高/中/低

**主要发现**:
- 咖啡因摄入与焦虑的关系：[描述]
- 糖分摄入与情绪波动的关系：[描述]
- 可能的营养缺乏：[列出]

**建议**:
- [具体的营养建议]

### 慢性病-心理关联
**关联强度**: 高/中/低

**主要发现**:
- [慢性病]与心理状态的关系：[描述]
- 疾病负担对心理健康的影响：[描述]
- 功能受限与情绪的关系：[描述]

**建议**:
- [具体的整体健康管理建议]

## 9. 综合建议

### 立即行动（如适用）
- [如有紧急问题，列出立即需要采取的行动]

### 本周行动计划
1. [行动项1] - 优先级：高/中/低
2. [行动项2] - 优先级：高/中/低
3. ...

### 本月目标
1. [目标1]
2. [目标2]
3. ...

### 继续保持的方面
- [列出做得好的方面，鼓励继续保持]

### 需要改进的方面
- [列出需要改进的方面，提供具体建议]

### 推荐资源
- [书籍/APP/支持团体/在线资源等]

## 10. 数据质量说明

- 数据完整性：[优秀/良好/一般/需改进]
- PHQ-9评估次数：X次
- GAD-7评估次数：X次
- 情绪日记条目：X条
- 时间跨度：X天

---

**报告生成时间**: YYYY-MM-DD HH:MM:SS
**下次评估建议时间**: YYYY-MM-DD

⚠️ **免责声明**：本报告由心理健康分析技能自动生成，仅供参考，不构成医学诊断或治疗建议。如有任何心理健康问题，请寻求专业心理医生或精神科医生的帮助。
```

## 使用示例

### 示例1：趋势分析

**用户输入**：
```
/mental trend 3months
```

**技能执行**：
1. 读取最近3个月的PHQ-9和GAD-7评估数据
2. 计算评分变化速率和趋势
3. 分析严重程度变化
4. 检测PHQ-9第9项变化
5. 生成趋势报告

**输出**：
```markdown
# 心理健康趋势分析（近3个月）

## 整体趋势
- PHQ-9：14分 → 8分，改善6分，趋势：改善 ✓
- GAD-7：12分 → 6分，改善6分，趋势：改善 ✓
- 变化速率：约2分/月

## 严重程度变化
- PHQ-9：中度抑郁 → 轻度抑郁 ✓
- GAD-7：中度焦虑 → 轻度焦虑 ✓

## 积极信号
- 症状持续改善
- PHQ-9第9项得分：1 → 0 ✓
- 治疗效果良好

## 建议
- 继续当前治疗
- 保持运动和睡眠习惯
- 下次评估：1个月后
```

### 示例2：情绪模式分析

**用户输入**：
```
/mental pattern
```

**技能执行**：
1. 读取情绪日记数据
2. 统计常见情绪和时间模式
3. 分析触发因素和应对方式
4. 生成模式识别报告

**输出**：
```markdown
# 情绪模式分析

## 常见情绪（Top 3）
1. 焦虑 - 占比35%，平均强度7/10
2. 疲劳 - 占比25%，平均强度6/10
3. 平静 - 占比20%，平均强度7/10

## 时间模式
- 早晨：平静（强度7/10）😌
- 下午：焦虑（强度7/10）😰
- 晚上：疲劳（强度6/10）😴

## 主要触发因素（Top 5）
1. 工作压力 - 12次，影响高
2. 睡眠不足 - 8次，影响中
3. 运动 - 6次，影响积极
4. 社交 - 5次，影响积极
5. 交通拥堵 - 4次，影响中

## 高效应对策略
1. 运动 - 有效率90% ✓
2. 冥想 - 有效率85% ✓
3. 深呼吸 - 有效率75% ✓

## 建议
- 下午工作压力大时，可使用深呼吸或短暂散步
- 保持规律运动，对情绪改善效果显著
- 改善睡眠有助于减轻焦虑和疲劳
```

### 示例3：危机风险评估

**用户输入**：
```
/crisis assessment
```

**技能执行**：
1. 读取最近的PHQ-9/GAD-7评估
2. 读取最近的情绪日记
3. 执行危机风险检测算法
4. 计算风险评分和等级
5. 生成危机风险报告

**输出**：
```markdown
# 危机风险评估

## 当前风险等级：🟢 低风险

**风险评分**: 3/20

## 风险因素分析
| 风险因素 | 得分 | 详情 |
|----------|------|------|
| PHQ-9第9项 | 0分 | 得分0，无自伤意念 ✓ |
| 症状变化 | -2分 | 改善趋势 ✓ |
| 情绪强度 | 2分 | 高强度负面情绪占比45% |
| 情绪波动 | 1分 | 波动中等 |
| 预警信号 | 0分 | 未检测到 ✓ |
| 社会退缩 | 0分 | 社交活动良好 ✓ |
| 功能受损 | 0分 | 功能正常 ✓ |
| **总分** | **3分** | **低风险** ✓ |

## 建议行动
- 继续监测心理状态
- 保持健康的生活习惯
- 定期进行心理评估（每月1次）
- 继续心理治疗（如有）

## 紧急资源（备用）
- 心理危机热线：400-xxx-xxxx（24小时）
- 精神科急诊：就近三甲医院
- 急救电话：120

⚠️ 如出现以下情况，请立即寻求专业帮助：
- 有自伤或自杀想法或计划
- 幻觉、妄想
- 完全失去功能
- 无法控制的情绪爆发
```

### 示例4：治疗进展分析

**用户输入**：
```
/mental therapy progress
```

**技能执行**：
1. 读取治疗记录和目标
2. 计算目标完成百分比
3. 分析症状改善程度
4. 评估作业完成情况
5. 生成治疗进展报告

**输出**：
```markdown
# 心理治疗进展分析

## 治疗概况
- 治疗类型：CBT（认知行为治疗）
- 治疗频率：每周1次
- 已进行咨询：24次
- 治疗时长：5个月

## 治疗目标进展
| 目标 | 基线 | 当前 | 目标 | 进展 | 预计达成时间 |
|------|------|------|------|------|--------------|
| 降低焦虑水平 | 14分 | 8分 | 5分 | 57% | 2025-08-01 |
| 改善睡眠质量 | 10分 | 6分 | 4分 | 60% | 2025-07-15 |
| 增加愉快活动 | 2次/周 | 5次/周 | 7次/周 | 50% | 2025-07-01 |

**整体进展评价**: 良好 ✓

## 症状改善
- PHQ-9评分：14分 → 8分，改善43% ✓
- GAD-7评分：14分 → 6分，改善57% ✓
- 整体功能水平：显著改善 ✓

## 作业完成情况
- 平均完成率：85%
- 高质量完成：60%
- 需要加强：认知重构练习

## 治疗亮点
- 焦虑症状显著改善
- 睡眠质量明显提升
- 行为激活效果良好
- 认知扭曲识别能力提升

## 继续保持
- 每周心理咨询
- 每日放松练习
- 行为激活（运动、社交）
- 思维记录

## 需要加强
- 认知重构练习
- 应对技巧应用
- 睡眠卫生维持
```

### 示例5：关联分析

**用户输入**：
```
/mental analysis correlations
```

**技能执行**：
1. 读取心理健康、睡眠、运动、营养、慢性病数据
2. 计算相关性系数
3. 分析影响程度
4. 生成关联分析报告

**输出**：
```markdown
# 心理健康关联分析

## 睡眠-心理关联（关联强度：高）

### 主要发现
- 睡眠时长与PHQ-9评分呈负相关（r=-0.72, p<0.01）
- 睡眠质量与情绪稳定性呈正相关（r=0.68, p<0.01）
- PSQI评分每改善1分，PHQ-9评分平均降低1.2分

### 睡眠问题影响
- 入睡困难 → 次日焦虑增加40%
- 夜间易醒 → 次日情绪低落增加35%
- 睡眠不足 → 注意力不集中，情绪波动加大

### 建议
- 保持规律作息，每晚23:00前入睡
- 改善睡眠卫生：避免咖啡因下午摄入
- 继续放松练习，促进睡眠

## 运动-情绪关联（关联强度：高）

### 主要发现
- 运动频率与积极情绪占比呈正相关（r=0.75, p<0.01）
- 运动日情绪平均强度比非运动日高1.5分
- 运动后焦虑感平均降低50%

### 最有效的运动类型
1. 有氧运动（跑步、游泳）- 改善率85%
2. 瑜伽 - 改善率80%
3. 户外散步 - 改善率75%

### 建议
- 保持每周3-5次运动，每次30分钟以上
- 优先选择有氧运动
- 焦虑时可进行户外散步

## 营养-心理关联（关联强度：中）

### 主要发现
- 咖啡因摄入与GAD-7评分呈正相关（r=0.52, p<0.05）
- 高糖饮食与情绪波动呈正相关（r=0.48, p<0.05）
- Omega-3摄入不足可能与抑郁症状相关

### 建议
- 减少咖啡因摄入（每天≤2杯）
- 减少添加糖摄入
- 考虑补充Omega-3（咨询医生）

## 综合建议
基于关联分析，以下生活方式对改善心理健康最有效：
1. **规律运动**（每周3-5次，30分钟+）
2. **充足睡眠**（7-8小时，23:00前入睡）
3. **均衡饮食**（减少咖啡因和糖分）
4. **持续治疗**（CBT心理治疗）

这4个方面的综合干预对您的心理健康改善贡献率为**75%**。
```

### 示例6：完整报告生成

**用户输入**：
```
/mental report
```

**技能执行**：
1. 读取所有相关数据
2. 执行完整分析流程
3. 生成交互式HTML报告
4. 包含危机警告和建议

**输出**：
生成完整的心理健康分析报告HTML文件，包含：
- 所有图表（ECharts交互式图表）
- 危机风险警告（如适用）
- 详细分析和建议
- 可下载或打印

---

## 错误处理

### 数据文件不存在
```
错误：未找到心理健康数据文件
建议：请先使用 /mental assess 或 /mental mood 命令创建数据
```

### 数据不足
```
警告：数据不足以进行趋势分析
建议：至少需要3次PHQ-9/GAD-7评估或7天情绪日记
当前数据：PHQ-9评估X次，情绪日记X条
```

### 危机风险高
```
🔴 危机警告：检测到高风险因素

立即行动：
1. 联系心理危机热线：400-xxx-xxxx（24小时）
2. 前往最近的精神科急诊
3. 拨打急救电话：120
4. 联系家人或朋友陪伴

检测到的风险因素：
- [列出高风险因素]

不要犹豫，立即寻求专业帮助！
```

## 数据源说明

**主要数据源**：
- `data-example/mental-health-tracker.json` - 心理健康主数据
- `data-example/mental-health-logs/` - 情绪日记日志

**关联数据源**：
- `data-example/sleep-tracker.json` - 睡眠数据
- `data-example/fitness-tracker.json` - 运动数据
- `data-example/nutrition-tracker.json` - 营养数据
- `data-example/diabetes-tracker.json` - 糖尿病数据（如适用）
- `data-example/hypertension-tracker.json` - 高血压数据（如适用）
- `data-example/medication-tracker.json` - 用药数据

## 性能优化

对于大量数据（如>6个月的情绪日记），采用以下优化策略：
- 数据聚合：按周/月聚合情绪数据
- 抽样分析：随机抽样代表性数据点
- 增量分析：仅分析新增数据
- 缓存中间结果

---

**技能版本**: v1.0.0
**最后更新**: 2025-01-06
**维护者**: WellAlly Tech

---

## Merged Reference (legacy variant)

---
name: nutrition-analyzer
description: 分析营养数据、识别营养模式、评估营养状况，并提供个性化营养建议。支持与运动、睡眠、慢性病数据的关联分析。
allowed-tools: Read, Grep, Glob, Write
---

# 营养分析器技能

分析饮食和营养数据，识别营养模式，评估营养状况，并提供个性化营养改善建议。

## 功能

### 1. 营养趋势分析

分析营养素摄入的变化趋势，识别改善或需要关注的方面。

**分析维度**：
- 宏量营养素趋势（蛋白质、碳水、脂肪、纤维、卡路里）
- 微量营养素趋势（维生素、矿物质）
- 热量来源分布变化
- 餐食模式（饮食时间、频率）
- 食物类别偏好

**输出**：
- 趋势方向（改善/稳定/下降）
- 变化幅度和百分比
- 趋势显著性
- 改进建议

### 2. 营养素摄入评估

评估营养素摄入是否达到推荐标准（RDA/AI）。

**评估内容**：
- **宏量营养素评估**：
  - 蛋白质摄入量和质量
  - 碳水化合物类型分布（精制 vs 复杂碳水）
  - 脂肪类型分布（饱和/单不饱和/多不饱和/反式脂肪）
  - 膳食纤维摄入量

- **维生素评估**：
  - 维生素A、C、D、E、K
  - 维生素B族（B1、B2、B3、B6、B12、叶酸、泛酸、生物素）
  - 与RDA对比
  - 缺乏风险评估

- **矿物质评估**：
  - 常量矿物质：钙、磷、镁、钠、钾、氯、硫
  - 微量矿物质：铁、锌、铜、锰、碘、硒、铬、钼
  - 与RDA对比
  - 缺乏风险评估

- **特殊营养素评估**：
  - Omega-3脂肪酸（EPA、DHA、ALA）
  - 胆碱
  - 辅酶Q10
  - 植物化学物（类黄酮、类胡萝卜素等）

**输出**：
- 每种营养素的达成率
- 缺乏/不足/充足/过量分级
- 缺乏风险识别
- 优先改善建议

### 3. 营养状况评估

综合评估用户的营养状况。

**评估内容**：
- **整体营养质量评分**：
  - 营养密度评分
  - 食物多样性评分
  - 均衡饮食评分

- **营养模式识别**：
  - 饮食模式类型（地中海式、DASH、素食等）
  - 饮食时间模式（进食频率、进食窗口）
  - 零食和加餐模式

- **营养风险识别**：
  - 营养缺乏风险（如维生素D缺乏、铁缺乏）
  - 营养过量风险（如维生素A过量、钠过量）
  - 不健康饮食习惯（高糖、高脂、高钠）

**输出**：
- 营养状况等级（优秀/良好/一般/较差）
- 主要营养问题识别
- 风险因素列表
- 改善优先级

### 4. 相关性分析

分析营养与其他健康指标的相关性。

**支持的相关性分析**：
- **营养 ↔ 体重**：
  - 卡路里摄入与体重变化的关系
  - 宏量营养素比例与体重管理
  - 进食时间与代谢关系

- **营养 ↔ 运动**：
  - 营养摄入对运动表现的影响
  - 运动日vs休息日的营养需求
  - 蛋白质摄入与肌肉恢复

- **营养 ↔ 睡眠**：
  - 咖啡因摄入与睡眠质量
  - 晚餐时间与入睡时间
  - 特定营养素（如镁、色氨酸）与睡眠

- **营养 ↔ 血压**：
  - 钠摄入与血压
  - 钾/钠比值与血压
  - DASH饮食依从性与血压控制

- **营养 ↔ 血糖**：
  - 碳水化合物类型与血糖波动
  - 膳食纤维与血糖控制
  - 进食时间与血糖曲线

**输出**：
- 相关系数（-1到1）
- 相关性强度（弱/中/强）
- 统计显著性
- 因果关系推断
- 实践建议

### 5. 个性化建议生成

基于用户数据生成个性化营养改善建议。

**建议类型**：
- **营养素调整建议**：
  - 增加缺乏的营养素
  - 减少过量的营养素
  - 优化营养素比例

- **食物选择建议**：
  - 推荐特定食物类别
  - 食物替换建议（更健康的选择）
  - 食物搭配建议（促进吸收）

- **饮食习惯建议**：
  - 进食时间调整
  - 餐食频率调整
  - 烹饪方式建议

- **补充剂建议**（仅供参考）：
  - 基于缺乏风险的补充剂建议
  - 补充剂剂量和时机
  - 相互作用警示

**建议依据**：
- DRIs/RDA标准
- 用户营养历史数据
- 用户健康状况和目标
- 循证营养学证据

---

## 使用说明

### 触发条件

当用户请求以下内容时触发本技能：
- 营养趋势分析
- 营养素摄入评估
- 营养状况评估
- 营养改善建议
- 营养与其他健康指标的关联分析

### 执行步骤

#### 步骤 1: 确定分析范围

明确用户请求的分析类型和时间范围：
- 分析类型：趋势/评估/相关性/建议
- 时间范围：周/月/季度/自定义
- 分析深度：宏量营养素/微量营养素/全面分析

#### 步骤 2: 读取数据

**主要数据源**：
1. `data-example/nutrition-tracker.json` - 营养追踪主数据
2. `data-example/nutrition-logs/YYYY-MM/YYYY-MM-DD.json` - 每日饮食记录

**关联数据源**：
1. `data-example/profile.json` - 体重、BMI等基础数据
2. `data-example/fitness-tracker.json` - 运动数据
3. `data-example/sleep-tracker.json` - 睡眠数据
4. `data-example/hypertension-tracker.json` - 血压数据
5. `data-example/diabetes-tracker.json` - 血糖数据

#### 步骤 3: 数据分析

根据分析类型执行相应的分析算法：

**趋势分析算法**：
- 线性回归计算趋势斜率
- 移动平均平滑波动
- 统计显著性检验

**RDA达成率计算**：
```python
rda_achievement = (actual_intake / rda_value) * 100

status_classification:
- < 50%: 严重缺乏
- 50-75%: 不足
- 75-100%: 接近目标
- 100-150%: 充足（理想范围）
- > 150%: 过量（注意安全上限UL）
```

**营养密度评分**：
```python
nutrient_density_score = (
    (vitamins_achieved / total_vitamins) * 40 +
    (minerals_achieved / total_minerals) * 30 +
    (fiber_achieved / fiber_rda) * 30
)
```

**相关性分析算法**：
- Pearson相关系数计算
- 滞后相关性分析（考虑时间延迟效应）
- 多变量回归分析

#### 步骤 4: 生成报告

按照标准格式输出分析报告（见"输出格式"部分）

---

## 输出格式

### 营养趋势分析报告

```markdown
# 营养摄入趋势分析报告

## 分析周期
2025-03-20 至 2025-06-20（3个月，90天记录）

## 宏量营养素趋势

### 卡路里摄入
- **趋势**：⬇️ 下降
- **开始**：平均2100卡/天
- **当前**：平均1950卡/天
- **变化**：-150卡/天 (-7.1%)
- **解读**：卡路里摄入适度减少，与减重目标一致

**趋势线**：
```
2100 ┤ ╭╮
2050 ┤ ╭╯╰╮
2000 ┼─╯   ╰╮
1950 ┤      ╰
1900 └───────────
     3月  4月  5月  6月
```

### 蛋白质
- **趋势**：➡️ 稳定
- **平均**：82g/天（范围：70-95g）
- **目标**：80g/天
- **达标率**：93%（84/90天达标）
- **解读**：蛋白质摄入稳定，基本达标

### 膳食纤维
- **趋势**：⬆️ 改善
- **开始**：平均18g/天
- **当前**：平均22g/天
- **变化**：+4g/天 (+22%)
- **目标**：30g/天
- **解读**：纤维摄入显著增加，但仍需继续努力

### 脂肪
- **趋势**：⬇️ 下降
- **开始**：平均75g/天
- **当前**：平均68g/天
- **变化**：-7g/天 (-9.3%)
- **目标**：≤65g/天
- **解读**：脂肪摄入减少，接近目标

**脂肪类型分布变化**：
| 脂肪类型 | 开始 | 当前 | 目标 | 趋势 |
|---------|------|------|------|------|
| 饱和脂肪 | 25g | 20g | <20g | ⬇️ 改善 |
| 单不饱和 | 30g | 32g | >35g | ⬆️ 略增 |
| 多不饱和 | 15g | 12g | 15-20g | ⬇️ 需增加 |
| 反式脂肪 | 2g | 0.5g | 0g | ⬇️ 改善 |

## 维生素状况趋势

### 维生素D
- **摄入趋势**：⬆️ 增加（补充剂开始）
- **开始**：平均2μg/天（饮食来源）
- **当前**：平均52μg/天（含2000IU补充剂）
- **RDA**：15μg/天
- **血清水平变化**：
  - 基线（2025-05）：18 ng/mL
  - 当前（2025-06）：22 ng/mL
  - 目标：30-100 ng/mL
- **解读**：✅ 补充剂起效，但需继续监测

### 维生素C
- **趋势**：⬆️ 改善
- **开始**：平均65mg/天
- **当前**：平均85mg/天
- **RDA**：100mg/天
- **达标率**：从65% → 85%
- **建议**：增加柑橘类、奇异果、草莓等水果

### B族维生素
- **维生素B12**：✅ 充足（平均2.5μg，RDA 2.4μg）
- **叶酸**：⚠️ 不足（平均320μg，RDA 400μg）
- **B6**：✅ 充足（平均1.5mg，RDA 1.3mg）

## 矿物质趋势

### 钙
- **趋势**：➡️ 稳定
- **平均**：850mg/天
- **RDA**：1000mg/天
- **达标率**：85%
- **主要来源**：乳制品40%、豆腐25%、绿叶蔬菜20%

### 铁
- **趋势**：✅ 充足
- **平均**：12mg/天
- **RDA**：8mg/天（男性）
- **达标率**：150%
- **主要来源**：肉类、蛋类、豆类、绿叶蔬菜

### 钠
- **趋势**：⬇️ 改善
- **开始**：平均2800mg/天
- **当前**：平均2100mg/天
- **目标**：<2300mg/天（理想<1500mg）
- **解读**：✅ 达到一般目标，⚠️ 理想目标仍需努力

### 钾
- **趋势**：⬆️ 改善
- **开始**：平均2800mg/天
- **当前**：平均3200mg/天
- **目标**：3500-4700mg/天
- **钾/钠比值**：从1.0 → 1.5（目标>2）
- **建议**：继续增加水果和蔬菜

## 特殊营养素趋势

### Omega-3
- **趋势**：⬆️ 增加（鱼油补充剂）
- **开始**：平均150mg/天
- **当前**：平均850mg/天（含补充剂）
- **推荐量**：500-1000mg/天
- **状态**：✅ 达标

### 胆碱
- **趋势**：➡️ 稳定
- **平均**：350mg/天
- **AI（适宜摄入量）**：425mg/天
- **达标率**：82%
- **主要来源**：鸡蛋（60%）、肉类（25%）、豆类（15%）

## 饮食模式分析

### 食物类别分布
| 食物类别 | 占比 | 变化 | 评价 |
|---------|------|------|------|
| 蔬菜水果 | 35% | +8% | ✅ 增加 |
| 全谷物 | 20% | +5% | ✅ 改善 |
| 精制谷物 | 15% | -7% | ✅ 减少 |
| 蛋白质来源 | 20% | 稳定 | ✅ 充足 |
| 添加脂肪 | 8% | -3% | ✅ 减少 |
| 添加糖 | 2% | -2% | ✅ 减少 |

### 进食时间模式
- **平均进食窗口**：12.5小时（07:30 - 20:00）
- **进食频率**：平均4.2次/天
- **最常见餐食时间**：
  - 早餐：07:30（90%天数）
  - 午餐：12:15（95%天数）
  - 晚餐：18:45（98%天数）
  - 加餐：15:30（60%天数）

### 饮食质量评分
- **营养密度评分**：7.2/10（从6.5提升）
- **食物多样性评分**：6.8/10
- **均衡饮食评分**：7.5/10
- **综合评分**：7.2/10 → **良好**

## 洞察与建议

### 关键洞察

1. **膳食纤维持续改善但仍不足**
   - 从18g增至22g，但仍低于目标30g
   - 影响：饱腹感、肠道健康、血糖控制
   - 建议：每餐至少包含5g纤维

2. **脂肪质量改善**
   - 饱和脂肪减少，反式脂肪几乎消除
   - 多不饱和脂肪略低，需增加Omega-3食物
   - 建议：增加深海鱼类、坚果、亚麻籽

3. **钠摄入改善但钾/钠比仍低**
   - 钠减少33%，钾增加14%
   - 钾/钠比从1.0升至1.5，仍低于目标2.0
   - 建议：继续增加高钾食物（香蕉、橙子、土豆、菠菜）

4. **维生素D补充剂有效**
   - 血清水平从18升至22 ng/mL（4周+4ng）
   - 预计3-4个月可达目标范围
   - 建议：继续补充，定期监测

### 优先级行动计划

#### Priority 1：提升膳食纤维至30g/天（2周）

**具体行动**：
1. 早餐：全谷物（燕麦/全麦面包）+ 水果（9g）
2. 午餐：糙米/全麦面 + 2份蔬菜（8g）
3. 晚餐：红薯/杂粮 + 2份蔬菜（8g）
4. 加餐：水果 + 坚果（5g）
**总计**：30g ✅

#### Priority 2：优化钾/钠比值至2.0（4周）

**具体行动**：
1. 减少加工食品（主要钠源）
2. 每日2-3份高钾水果（香蕉、橙子、猕猴桃）
3. 蔬菜选择菠菜、土豆、蘑菇、番茄
4. 使用香料替代盐调味

#### Priority 3：维持维生素D补充（长期）

**监测计划**：
- 3个月后复查血清水平
- 目标：40-60 ng/mL
- 根据结果调整剂量

## 营养目标进度

| 目标 | 开始 | 当前 | 目标值 | 进度 | 状态 |
|------|------|------|--------|------|------|
| 卡路里 | 2100 | 1950 | 1800-2000 | 100% | ✅ 达标 |
| 蛋白质 | 75g | 82g | 80g | 100% | ✅ 达标 |
| 膳食纤维 | 18g | 22g | 30g | 73% | ⚠️ 进行中 |
| 维生素D | 18 ng/mL | 22 ng/mL | 30-100 | 20% | ⚠️ 改善中 |
| 钠摄入 | 2800mg | 2100mg | <2300 | 100% | ✅ 达标 |
| Omega-3 | 150mg | 850mg | 500-1000mg | 100% | ✅ 达标 |

---

**报告生成时间**：2025-06-20
**分析周期**：2025-03-20 至 2025-06-20（90天）
**数据记录数**：90天
**营养分析器版本**：v1.0
```

---

## 数据结构

### 饮食记录数据

```json
{
  "date": "2025-06-20",
  "meals": [
    {
      "type": "breakfast",
      "time": "07:30",
      "foods": ["鸡蛋", "牛奶", "全麦面包"],
      "calories": 450,
      "macronutrients": {
        "protein_g": 20,
        "carbs_g": 55,
        "fat_g": 15,
        "fiber_g": 5,
        "saturated_fat_g": 5,
        "monounsaturated_fat_g": 6,
        "polyunsaturated_fat_g": 3,
        "trans_fat_g": 0.1
      },
      "micronutrients": {
        "vitamin_a_mcg": 150,
        "vitamin_c_mg": 5,
        "vitamin_d_mcg": 1.5,
        "vitamin_e_mg": 1,
        "vitamin_k_mcg": 5,
        "thiamine_mg": 0.3,
        "riboflavin_mg": 0.4,
        "niacin_mg": 4,
        "vitamin_b6_mg": 0.1,
        "folate_mcg": 30,
        "vitamin_b12_mcg": 0.6,
        "calcium_mg": 250,
        "iron_mg": 2,
        "magnesium_mg": 40,
        "phosphorus_mg": 200,
        "zinc_mg": 2,
        "selenium_mcg": 10,
        "potassium_mg": 350,
        "sodium_mg": 300
      },
      "special_nutrients": {
        "omega_3_g": 0.1,
        "choline_mg": 150
      }
    }
  ],
  "daily_summary": {
    "total_calories": 2000,
    "total_macronutrients": {
      "protein_g": 80,
      "carbs_g": 250,
      "fat_g": 65,
      "fiber_g": 30
    },
    "rda_achievement": {
      "protein": 100,
      "vitamin_c": 85,
      "vitamin_d": 35,
      "calcium": 90,
      "iron": 75
    },
    "goal_achieved": true
  }
}
```

---

## 算法说明

### RDA达成率计算

```python
def calculate_rda_achievement(actual_intake, rda_value, ul_value=None):
    """
    计算RDA达成率和状态

    参数：
    - actual_intake: 实际摄入量
    - rda_value: 推荐膳食供给量
    - ul_value: 可耐受最高摄入量（可选）

    返回：
    - achievement_rate: 达成率百分比
    - status: 状态标签
    """
    achievement_rate = (actual_intake / rda_value) * 100

    if ul_value and actual_intake > ul_value:
        status = "exceeds_ul"
        category = "过量（危险）"
    elif achievement_rate < 50:
        status = "severe_deficiency"
        category = "严重缺乏"
    elif achievement_rate < 75:
        status = "insufficient"
        category = "不足"
    elif achievement_rate < 100:
        status = "approaching_target"
        category = "接近目标"
    elif achievement_rate <= 150:
        status = "adequate"
        category = "充足"
    else:
        status = "high_intake"
        category = "较高"

    return {
        'achievement_rate': round(achievement_rate, 1),
        'status': status,
        'category': category
    }
```

### 营养密度评分

```python
def calculate_nutrient_density_score(meal_data):
    """
    计算食物营养密度评分（0-10分）

    因素权重：
    - 维生素达成率：40%
    - 矿物质达成率：30%
    - 膳食纤维：20%
    - 限制性营养素（饱和脂肪、钠、添加糖）：10%
    """
    score = 0

    # 维生素评分
    vitamin_achievements = [
        meal_data['micronutrients'][v] / RDA[v]
        for v in ['vitamin_a', 'vitamin_c', 'vitamin_d', 'vitamin_e', 'vitamin_k']
    ]
    vitamin_score = min(sum(vitamin_achievements) / len(vitamin_achievements), 1.5) * 10
    score += min(vitamin_score, 10) * 0.40

    # 矿物质评分
    mineral_achievements = [
        meal_data['micronutrients'][m] / RDA[m]
        for m in ['calcium', 'iron', 'magnesium', 'zinc']
    ]
    mineral_score = min(sum(mineral_achievements) / len(mineral_achievements), 1.5) * 10
    score += min(mineral_score, 10) * 0.30

    # 膳食纤维评分
    fiber_score = min(meal_data['macronutrients']['fiber_g'] / 5, 2) * 10
    score += min(fiber_score, 10) * 0.20

    # 限制性营养素扣分
    penalty = 0
    if meal_data['macronutrients']['saturated_fat_g'] > 10:
        penalty += 2
    if meal_data['micronutrients']['sodium_mg'] > 600:
        penalty += 2
    if meal_data.get('added_sugars_g', 0) > 10:
        penalty += 2

    score = max(0, score - penalty * 0.10)

    return round(score, 1)
```

### 健康饮食指数评分

```python
def calculate_healthy_eating_index(daily_data):
    """
    计算健康饮食指数（HEI-2015改编）

    评分范围：0-100分
    """
    score = 0

    # 充足性成分（满分50分）
    # 1. 水果（5分）
    fruit_servings = daily_data['fruit_servings']
    score += min(fruit_servings, 2.5) * 2

    # 2. 蔬菜（5分）
    veg_servings = daily_data['vegetable_servings']
    score += min(veg_servings, 3) * 1.67

    # 3. 全谷物（10分）
    whole_grains_oz = daily_data['whole_grains_oz']
    score += min(whole_grains_oz, 3) * 3.33

    # 4. 乳制品（10分）
    dairy_servings = daily_data['dairy_servings']
    score += min(dairy_servings, 3) * 3.33

    # 5. 蛋白质（5分）
    protein_oz = daily_data['protein_oz']
    score += min(protein_oz, 5) * 1

    # 6. 海鲜/植物蛋白（5分）
    plant_protein_oz = daily_data['plant_protein_oz']
    score += min(plant_protein_oz, 2) * 2.5

    # 7. 脂肪酸比例（10分）
    fat_ratio = daily_data['unsaturated_fat_g'] / max(daily_data['saturated_fat_g'], 1)
    score += min(fat_ratio, 2.5) * 4

    # 适度性成分（满分40分，反向计分）
    # 8. 精制谷物（10分，越少越好）
    refined_grains_oz = daily_data['refined_grains_oz']
    score += max(10 - refined_grains_oz * 2, 0)

    # 9. 钠（10分，越少越好）
    sodium_g = daily_data['sodium_mg'] / 1000
    score += max(10 - sodium_g * 2, 0)

    # 10. 添加糖（10分，越少越好）
    added_sugars_pct = daily_data['added_sugars_g'] / (daily_data['total_calories'] / 100)
    score += max(10 - added_sugars_pct * 10, 0)

    # 11. 饱和脂肪（10分，越少越好）
    saturated_fat_pct = daily_data['saturated_fat_g'] / (daily_data['total_calories'] / 100)
    score += max(10 - saturated_fat_pct * 10, 0)

    return round(score, 1)
```

---

## 医学安全边界

⚠️ **重要声明**

本分析仅供健康参考，不构成医疗诊断或营养处方。

### 分析能力范围

✅ **能做到**：
- 营养数据统计和分析
- 趋势识别和可视化
- RDA达成率计算
- 营养缺乏风险评估
- 一般性营养建议
- 补充剂相互作用检查

❌ **不做到**：
- 诊断营养缺乏疾病
- 开具补充剂处方
- 替代注册营养师
- 处理严重营养不良
- 评估食物过敏

### 危险信号检测

在分析过程中检测以下危险信号：

1. **营养素过量**：
   - 维生素A > 3000μg（长期）
   - 维生素D > 100μg（长期）
   - 铁 > 45mg（长期）
   - 硒 > 400μg
   - 钠 > 2300mg（持续）

2. **营养素缺乏**：
   - 维生素D < 10μg/天（血清<12 ng/mL）
   - 维生素B12 < 1.5μg/天（素食者）
   - 铁 < 6mg/天（育龄女性）
   - 钙 < 500mg/天

3. **能量摄入异常**：
   - 持续<1200卡/天（可能营养不良）
   - 持续>3500卡/天（可能超重）

4. **饮食模式异常**：
   - 膳食纤维<10g/天
   - 添加糖>25%热量
   - 饱和脂肪>15%热量

### 建议分级

**Level 1: 一般性建议**
- 基于DRIs/RDA标准
- 适用于一般人群
- 无需医疗监督

**Level 2: 参考性建议**
- 基于用户数据和健康状况
- 需结合个人情况
- 建议咨询营养师

**Level 3: 医疗建议**
- 涉及疾病管理或补充剂
- 需医生确认
- 不得自行调整药物剂量

---

## 参考资源

- 中国居民膳食营养素参考摄入量 (DRIs)：http://www.cnsoc.org/
- 美国膳食指南：https://www.dietaryguidelines.gov/
- USDA FoodData Central：https://fooddatacentral.usda.gov/
- WHO营养建议：https://www.who.int/nutrition/
- 补充剂相互作用数据库：https://naturalmedicines.therapeuticresearch.com/

---

**技能版本**: v1.0
**创建日期**: 2026-01-06
**维护者**: WellAlly Tech

---

## Merged Reference (legacy variant)

---
name: occupational-health-analyzer
description: 分析职业健康数据、识别工作相关健康风险、评估职业健康状况、提供个性化职业健康建议。支持与睡眠、运动、心理健康等其他健康数据的关联分析。
allowed-tools: Read, Grep, Glob, Write, Edit
---

# 职业健康分析技能

## 核心功能

职业健康分析技能提供全面的职业健康数据分析功能，帮助用户追踪工作相关健康问题、识别职业健康风险、评估工作环境人机工程水平和优化职业健康。

**主要功能模块：**

1. **职业健康风险评估** - 久坐、视屏终端、倒班工作、重复性劳损、工作压力等多维度风险评估
2. **工作相关问题追踪** - 颈肩腰腿痛、眼疲劳、腕管综合征等症状监测
3. **人机工程评估** - 工作站、椅子、显示器、键盘、环境等全方位评估
4. **职业病筛查** - 基于工作类型的职业病风险评估和筛查建议
5. **趋势分析** - 症状发展、改善效果、风险变化趋势
6. **关联分析** - 与睡眠、运动、心理健康、慢性病模块的关联分析
7. **个性化建议** - 工作姿势、休息提醒、设备建议、环境优化
8. **预警系统** - 高风险模式、症状恶化、职业病风险预警

## 触发条件

技能在以下情况下自动触发：

1. 用户使用 `/work trend` 查看职业健康趋势
2. 用户使用 `/work status` 查看综合健康状态
3. 用户使用 `/work recommend` 获取改进建议
4. 用户使用 `/work assess` 进行综合评估
5. 用户使用 `/work issue` 记录问题后的分析
6. 用户使用 `/work ergonomic` 进行人机工程评估后的分析

## 医学安全边界

**本技能不能做的事：**
- ❌ 不进行职业病诊断
- ❌ 不出具职业病诊断证明
- ❌ 不替代工作场所健康监护
- ❌ 不预测疾病发展
- ❌ 不处理急性健康危机

**本技能能做的事：**
- ✅ 职业健康风险评估和筛查
- ✅ 工作相关症状识别和追踪
- ✅ 人机工程评估和改进建议
- ✅ 职业病风险预警
- ✅ 工作环境改善建议
- ✅ 健康记录保存（就医时参考）
- ✅ 与其他健康数据的关联分析

## 执行步骤

### 第1步：数据读取

读取职业健康数据文件：
- `data-example/occupational-health-tracker.json` - 主职业健康档案

**数据验证：**
- 检查文件是否存在
- 验证数据结构完整性
- 确认有足够的数据点进行分析

### 第2步：职业健康风险评估

#### 久坐风险评估（Sedentary Risk Score）

**评分维度（每个维度0-10分）**：

1. **每天久坐时间** (sedentary_time_daily)
   - >8小时：10分
   - 6-8小时：7分
   - 4-6小时：4分
   - <4小时：1分

2. **休息频率** (break_frequency)
   - 无休息：10分
   - 每3小时+：8分
   - 每2小时：5分
   - 每小时：2分

3. **每周运动时间** (weekly_exercise_minutes)
   - 0分钟：10分
   - <60分钟：7分
   - 60-150分钟：4分
   - >150分钟：1分

4. **现有症状** (existing_symptoms_severity)
   - 严重症状：10分
   - 中度症状：7分
   - 轻度症状：4分
   - 无症状：1分

**总分计算**：
```
总分 = 久坐时间 + 休息频率 + 运动时间 + 现有症状
范围：4-40分
```

**风险等级判定**：
- 低风险：4-13分
- 中风险：14-26分
- 高风险：27-40分

#### 视屏终端风险评估（VDT Risk Score）

**评分维度（每个维度0-10分）**：

1. **每天屏幕时间** (screen_time_daily)
   - >8小时：10分
   - 6-8小时：7分
   - 4-6小时：4分
   - <4小时：1分

2. **20-20-20法则遵守** (rule_20_20_20_compliance)
   - 从不遵守：10分
   - 偶尔遵守：6分
   - 经常遵守：3分
   - 总是遵守：1分

3. **照明条件** (lighting_quality)
   - 很差：10分
   - 较差：7分
   - 一般：4分
   - 良好：1分

4. **眼部症状** (eye_symptoms_severity)
   - 严重症状：10分
   - 中度症状：7分
   - 轻度症状：4分
   - 无症状：1分

**总分计算和风险等级判定同久坐风险**

#### 综合风险评估

**综合风险等级计算**：
```
综合风险分数 = max(久坐风险, 视屏风险, 倒班风险, 劳损风险, 压力风险)

如果有多个高风险因素（≥27分），综合风险等级上调一级
如果有3个及以上中风险因素（14-26分），综合风险等级上调一级
```

### 第3步：人机工程评估

#### 评估维度和评分

**椅子评估**（0-20分）：
```
- 可调节性（0-5分）
- 腰椎支撑（0-5分）
- 座椅深度（0-5分）
- 扶手（0-5分）
```

**显示器评估**（0-20分）：
```
- 高度（0-7分）
- 距离（0-7分）
- 角度（0-6分）
```

**键盘和鼠标评估**（0-20分）：
```
- 键盘位置（0-5分）
- 鼠标位置（0-5分）
- 手腕支撑（0-10分）
```

**工作台评估**（0-20分）：
```
- 高度（0-10分）
- 空间（0-10分）
```

**环境评估**（0-20分）：
```
- 照明（0-7分）
- 噪音（0-7分）
- 温度（0-6分）
```

**总分计算**：
```
总分 = 椅子 + 显示器 + 键盘鼠标 + 工作台 + 环境
范围：0-100分

评分等级：
- 优秀：0-20分
- 良好：21-40分
- 一般：41-60分
- 较差：61-80分
- 差：81-100分
```

### 第4步：职业病筛查

#### 基于工作类型的筛查推荐

**办公室工作**：
```
必查项目：
- 视力测试（每年1次）
- 肌肉骨骼评估（每年1次）
```

**体力劳动**：
```
必查项目：
- 肌肉骨骼评估（每年1次）
- 肺功能检查（粉尘环境每年1次）
```

**倒班工作**：
```
必查项目：
- 睡眠质量评估（每6个月1次）
- 心理健康筛查（每年1次）
```

**噪音环境工作**：
```
必查项目：
- 听力测试（每年1次）
```

**粉尘/化学环境工作**：
```
必查项目：
- 肺功能检查（每年1次）
- 皮肤病筛查（每年1次）
```

### 第5步：关联分析

#### 睡眠-职业健康关联
- 倒班工作与睡眠质量的相关性
- 睡眠不足与工作相关症状的关系

#### 运动-职业健康关联
- 久坐工作与运动量的关系
- 运动与肌肉骨骼症状的关系

#### 心理健康-职业健康关联
- 工作压力与心理状态的关系
- 职业健康问题与心理症状的关联

### 第6步：生成报告

输出包括：
- 职业健康状况摘要
- 风险评估结果和趋势
- 工作相关问题分析
- 人机工程评估结果
- 职业病筛查建议
- 与其他健康因素的关联分析
- 预警信息（如适用）
- 个性化建议和行动计划

## 输出格式

### 职业健康分析报告结构

```markdown
# 职业健康分析报告

**报告日期**: YYYY-MM-DD
**分析周期**: YYYY-MM-DD 至 YYYY-MM-DD
**数据完整性**: 良好

⚠️ **重要提示**：本报告仅供参考，不构成职业病诊断。

---

## 1. 职业健康状况摘要

[整体评价：优秀/良好/一般/需改进/高风险]
- 综合风险等级：[低/中/高]
- 职业健康评分：X/100
- 人机工程评分：X/100
- 活跃问题数：X个
- 整体趋势：改善/稳定/恶化

## 2. 风险评估结果

### 久坐风险评估
**风险等级**: 🟢 低风险 | 🟡 中风险 | 🔴 高风险
**风险评分**: X/40

**建议**: [具体建议]

### 视屏终端风险评估
**风险等级**: 🟢 低风险 | 🟡 中风险 | 🔴 高风险
**风险评分**: X/40

**建议**: [具体建议]

## 3. 工作相关问题分析

### 当前活跃问题
- [问题1]: 严重程度、频率、持续时间
- [问题2]: 严重程度、频率、持续时间

### 症状趋势
- 改善的问题
- 稳定的问题
- 恶化的问题 ⚠️

## 4. 人机工程评估

**人机工程评分**: X/100
**评分等级**: 优秀/良好/一般/较差/差

### 改进建议
- 高优先级建议
- 中优先级建议
- 低优先级建议

## 5. 职业病筛查

### 推荐筛查
- [筛查项目1] - 建议时间
- [筛查项目2] - 建议时间

## 6. 综合建议

### 立即行动
- [行动项]

### 本周行动计划
- [行动项1]
- [行动项2]

### 预防措施
- [预防措施列表]

---

**报告生成时间**: YYYY-MM-DD HH:MM:SS
⚠️ **免责声明**：本报告仅供参考，不构成职业病诊断或治疗建议。
```

## 错误处理

### 数据文件不存在
```
错误：未找到职业健康数据文件
建议：请先使用 /work assess 命令创建数据
```

### 数据不足
```
警告：数据不足以进行趋势分析
建议：至少需要3次评估记录
```

### 高风险预警
```
🔴 职业病高风险警告

检测到以下高风险因素：
- [列出高风险因素]

建议行动：
1. 立即就医，进行职业病诊断
2. 咨询职业医学专科医生
3. 考虑工作调整
```

## 数据源说明

**主要数据源**：
- `data-example/occupational-health-tracker.json` - 职业健康主数据

**关联数据源**：
- `data-example/sleep-tracker.json` - 睡眠数据
- `data-example/fitness-tracker.json` - 运动数据
- `data-example/mental-health-tracker.json` - 心理健康数据

---

**技能版本**: v1.0.0
**最后更新**: 2025-01-08
**维护者**: WellAlly Tech

---

## Merged Reference (legacy variant)

---
name: oral-health-analyzer
description: 分析口腔健康数据、识别口腔问题模式、评估口腔健康状况、提供个性化口腔健康建议。支持与营养、慢性病、用药等其他健康数据的关联分析。
---
name: oral-health-analyzer

# 口腔健康分析技能

## 技能概述

本技能提供全面的口腔健康数据分析功能，包括趋势识别、风险评估、问题诊断和个性化建议生成。

## 医学免责声明

⚠️ **重要提示**：本技能提供的数据分析和建议仅供参考，不构成医学诊断或治疗建议。

- 所有口腔问题应由专业牙科医生诊断和治疗
- 分析结果不能替代专业口腔检查
- 紧急情况应立即就医
- 请遵循牙科医生的专业建议

## 核心功能

### 1. 趋势分析

#### 龋齿发展趋势
- 识别龋齿发生的模式和频率
- 分析龋齿在不同牙位的分布
- 评估龋齿发展速度
- 预测未来龋齿风险

**输出内容**：
- 龋齿数量变化曲线
- 高风险牙位识别
- 发展趋势预测
- 预防建议

#### 牙周健康变化
- 牙周出血频率统计
- 牙周袋深度变化
- 附着丧失监测
- 牙龈退缩进展

**输出内容**：
- 牙周健康评分趋势
- 疾病进展预警
- 治疗效果评估
- 维护建议

#### 卫生习惯改善
- 刷牙频率变化
- 牙线使用频率变化
- 洁牙记录追踪
- 卫生习惯评分

**输出内容**：
- 习惯改善曲线
- 评分变化趋势
- 目标达成情况
- 激励建议

### 2. 风险评估

#### 龋齿风险评估
基于以下因素进行综合评估：
- 饮食习惯（糖分摄入）
- 口腔卫生习惯
- 氟化物使用
- 唾液分泌情况
- 既往龋齿史
- 家族史

**风险等级**：
- **低风险**：良好的卫生习惯+低糖饮食+定期检查
- **中风险**：中等糖摄入+一般卫生习惯
- **高风险**：高糖饮食+差卫生习惯+不定期检查+龋齿史

**输出内容**：
- 风险等级（低/中/高）
- 主要风险因素
- 量化风险评分
- 降低风险建议

#### 牙周病风险评估
基于以下因素进行综合评估：
- 牙龈出血频率
- 牙周袋深度
- 附着丧失程度
- 吸烟状况
- 糖尿病控制情况
- 压力水平
- 家族史

**风险等级**：
- **健康**：无出血，探诊深度1-3mm
- **牙龈炎**：探诊出血，探诊深度3-4mm
- **轻度牙周炎**：探诊深度4-5mm，轻度附着丧失
- **中度牙周炎**：探诊深度5-6mm，中度附着丧失
- **重度牙周炎**：探诊深度>6mm，重度附着丧失

**输出内容**：
- 疾病分期
- 风险因素列表
- 进展风险预测
- 管理建议

#### 口腔癌风险评估
基于以下因素进行综合评估：
- 吸烟史
- 饮酒习惯
- 槟榔咀嚼
- HPV感染
- 日晒暴露（唇癌）
- 营养状况
- 口腔卫生

**风险等级**：
- **低风险**：无危险因素
- **中风险**：1-2个危险因素
- **高风险**：3个以上危险因素或既往病变

**输出内容**：
- 风险等级
- 主要危险因素
- 筛查建议
- 预防策略

### 3. 关联分析

#### 与营养模块的关联
**糖分摄入与龋齿风险**：
- 分析每日糖分摄入量
- 评估进食频率对龋齿的影响
- 识别高糖食物类型
- 推荐低糖替代食物

**钙和维生素D与牙齿健康**：
- 评估钙摄入量是否充足
- 分析维生素D水平
- 评估对牙齿强度的影响
- 推荐补充剂（如需要）

**营养缺乏的口腔表现**：
- 维生素C缺乏：牙龈出血
- 维生素B缺乏：口腔溃疡
- 铁缺乏：舌头炎症
- 蛋白质缺乏：黏膜萎缩

#### 与慢性病模块的关联
**糖尿病与牙周病**：
- 分析血糖控制与牙周健康的关系
- 评估糖尿病并发症风险
- 提供牙周病对血糖影响的说明
- 联合管理建议

**心血管疾病与牙周病**：
- 分析牙周炎对心血管疾病的影响
- 评估炎症指标关联
- 提供预防性治疗建议
- 联合监测建议

**妊娠期口腔健康**：
- 妊娠期牙龈炎风险评估
- 牙齿治疗时机建议
- 药物使用安全性评估
- 孕期口腔护理指导

**骨质疏松与牙齿健康**：
- 评估骨密度对牙齿的影响
- 分析抗骨吸收药物的副作用
- 提供牙齿保护建议

#### 与用药模块的关联
**药物引起的口干**：
- 识别导致口干的药物
- 评估口干严重程度
- 提供缓解建议
- 与医生沟通用药调整

**药物引起的牙龈增生**：
- 识别导致牙龈增生的药物
- 评估增生程度
- 提供管理建议
- 与医生沟通替代用药

**药物对牙齿颜色的影响**：
- 识别导致牙齿变色的药物
- 提供美容解决方案
- 预防措施建议

#### 与眼健康模块的关联
**干燥综合征**：
- 口干与眼干的联合分析
- 评估全身性自身免疫病
- 多系统症状追踪
- 专科转诊建议

**自身免疫病的口腔表现**：
- 狼疮的口腔病变
- 类风湿关节炎的颞下颌关节影响
- 其他免疫病的口腔表现

### 4. 个性化建议

#### 预防建议
**龋齿预防**：
- 刷牙技巧指导（巴氏刷牙法）
- 牙线使用方法
- 含氟产品推荐
- 饮食调整建议
- 定期检查提醒

**牙周病预防**：
- 改善口腔卫生习惯
- 戒烟支持
- 压力管理
- 血糖控制（糖尿病患者）
- 定期洁牙建议

**口腔癌预防**：
- 戒烟限酒
- 避免槟榔
- 防晒（唇部）
- 营养均衡
- 定期自查方法

#### 治疗建议
**根据问题类型提供**：
- 常规检查建议（每6个月）
- 紧急情况处理指导
- 专科转诊建议（如需要）
- 治疗时机建议
- 费用预估参考

#### 生活方式建议
**饮食调整**：
- 减少游离糖摄入
- 增加钙和维生素D摄入
- 多喝水（预防口干）
- 避免过硬食物（保护牙冠）

**习惯改善**：
- 制定个性化刷牙计划
- 逐步增加牙线使用频率
- 建立口腔卫生常规
- 设置提醒系统

**风险因素管理**：
- 戒烟策略
- 限酒建议
- 压力管理技巧
- 夜磨牙管理

### 5. 目标管理

#### 目标设定
- 与用户协商设定现实目标
- 分解为可实现的步骤
- 设定时间节点
- 建立评估标准

**常见目标类型**：
- 提高牙线使用频率
- 改善刷牙技巧
- 减少糖分摄入
- 定期口腔检查
- 戒烟

#### 进度追踪
- 定期评估目标达成情况
- 提供激励和反馈
- 调整目标（如需要）
- 庆祝里程碑达成

#### 障碍识别
- 识别阻碍目标达成的因素
- 提供克服障碍的策略
- 调整计划以适应实际情况
- 提供持续支持

### 6. 统计分析

#### 综合健康评分
基于以下因素计算：
- 口腔卫生习惯（40%）
- 检查频率（20%）
- 治疗完成情况（20%）
- 问题控制情况（10%）
- 目标达成情况（10%）

**评分范围**：0-100分
- **优秀**：90-100分
- **良好**：75-89分
- **一般**：60-74分
- **较差**：<60分

#### 口腔健康年龄
- 基于牙齿状态、牙周健康、卫生习惯计算
- 与实际年龄对比
- 提供改善建议

#### 治疗统计
- 治疗类型分布
- 治疗费用统计
- 治疗频率分析
- 牙医就诊记录

#### 问题统计
- 问题类型分布
- 问题发生频率
- 问题持续时间
- 解决率统计

### 7. 预警系统

#### 定期检查提醒
- 距离下次检查30天：温馨提醒
- 距离下次检查7天：紧急提醒
- 超过检查时间：逾期提醒

#### 问题预警
- 牙痛超过3天：建议就医
- 牙龈出血持续1周：建议检查
- 口腔溃疡超过2周：建议活检
- 新增肿块/白斑：立即就医

#### 趋势预警
- 龋齿数量快速增加：风险升级
- 牙周指标恶化：转诊牙周专科
- 卫生习惯下降：干预建议
- 治疗频率增加：深度评估

## 使用场景

### 场景1：定期健康评估
**用户请求**：分析最近6个月的口腔健康状况

**分析流程**：
1. 读取最近6个月的所有口腔健康记录
2. 分析检查记录、治疗记录、问题记录
3. 评估卫生习惯变化
4. 计算健康评分变化
5. 识别改善或恶化的趋势
6. 生成综合评估报告

**输出内容**：
- 健康评分变化趋势
- 主要改善点
- 需要关注的问题
- 下一步行动建议

### 场景2：问题诊断辅助
**用户请求**：我最近刷牙时牙龈出血，持续1周了

**分析流程**：
1. 检索最近的口腔检查记录
2. 分析牙周状况历史
3. 评估当前卫生习惯
4. 检查是否有相关用药记录
5. 分析营养数据（如维生素C摄入）
6. 生成诊断辅助报告

**输出内容**：
- 可能的原因分析
- 严重程度评估
- 就医建议
- 家庭护理方法
- 预防措施

### 场景3：治疗规划
**用户请求**：我想改善口腔卫生，降低龋齿风险

**分析流程**：
1. 评估当前龋齿风险
2. 分析主要风险因素
3. 评估当前卫生习惯
4. 识别需要改善的领域
5. 设定阶段性目标
6. 制定个性化计划

**输出内容**：
- 当前风险评估
- 改善目标
- 行动计划
- 时间表
- 进度追踪方法

### 场景4：多学科联合分析
**用户请求**：我有糖尿病，这对我的口腔健康有什么影响？

**分析流程**：
1. 读取糖尿病管理数据
2. 分析血糖控制情况
3. 评估牙周健康状况
4. 分析两者关联性
5. 评估并发症风险
6. 生成联合管理建议

**输出内容**：
- 糖尿病对口腔的影响
- 口腔健康对血糖的影响
- 并发症风险评估
- 联合管理策略
- 监测指标建议

### 场景5：预防性指导
**用户请求**：我准备怀孕，应该注意哪些口腔问题？

**分析流程**：
1. 评估当前口腔健康状况
2. 识别潜在风险
3. 分析当前用药安全性
4. 评估治疗紧迫性
5. 生成孕期口腔管理计划

**输出内容**：
- 孕前口腔检查建议
- 孕期常见口腔问题
- 药物使用安全性
- 治疗时机建议
- 孕期护理指导

## 数据分析方法

### 定量分析
- 统计描述（均值、中位数、标准差）
- 趋势分析（线性回归、移动平均）
- 相关性分析（Pearson/Spearman相关）
- 风险评分计算（多因素加权）

### 定性分析
- 文本描述分析
- 症状模式识别
- 主诉内容分类
- 满意度评估

### 可视化输出
- 时间序列图表
- 牙位分布图
- 风险评估雷达图
- 进度追踪仪表板
- 对比分析柱状图

## 质量保证

### 数据验证
- 检查数据完整性
- 验证数据一致性
- 识别异常值
- 处理缺失数据

### 结果验证
- 医学逻辑检查
- 与临床指南对照
- 专家审查（如有）
- 用户反馈收集

### 持续改进
- 定期更新分析算法
- 引入新的科学证据
- 优化用户体验
- 扩展功能范围

## 参考资源

### 临床指南
- 美国牙科协会（ADA）指南
- 世界卫生组织（WHO）口腔健康指南
- 中华口腔医学会临床指南
- Cochrane口腔健康组系统评价

### 评估工具
- DMFT指数（龋失补指数）
- CPI指数（社区牙周指数）
- 口腔健康影响.profile（OHIP-14）
- 龋齿风险评估工具（CAT）

### 数据源
- 用户记录数据
- 营养模块数据
- 慢性病模块数据
- 用药模块数据
- 眼健康模块数据

## 局限性

### 系统局限
- 不能替代专业口腔检查
- 不能进行影像学检查
- 不能进行实验室检测
- 分析结果受数据质量影响

### 数据局限
- 依赖用户记录准确性
- 可能存在遗漏记录
- 主观评估存在偏差
- 时间跨度可能不足

### 建议局限
- 不能考虑所有个体因素
- 不能预测所有并发症
- 需要结合临床判断
- 不能保证100%准确性

## 未来扩展

### 计划功能
- AI影像识别（牙片分析）
- 语音记录录入
- 智能提醒系统
- 社区支持功能
- 与牙医系统对接

### 研究方向
- 机器学习预测模型
- 个性化预防策略
- 基因风险分析
- 微生物组分析

---
name: oral-health-analyzer

**版本**: v1.0.0
**最后更新**: 2025-01-06
**维护者**: WellAlly Tech

---

## Merged Reference (legacy variant)

---
name: rehabilitation-analyzer
description: 分析康复训练数据、识别康复模式、评估康复进展，并提供个性化康复建议
allowed-tools: Read, Grep, Glob, Write, Edit
---

# 康复训练分析技能

## 核心功能

康复训练分析技能提供全面的康复数据分析功能，帮助用户追踪康复进展、识别改善模式和优化训练计划。

**主要功能模块：**

1. **康复进展分析** - 评估功能改善趋势和康复效果
2. **功能改善曲线** - 可视化ROM、肌力、平衡等功能指标变化
3. **疼痛模式识别** - 分析疼痛评分变化趋势和触发因素
4. **目标达成率评估** - 追踪康复目标完成情况
5. **康复阶段分析** - 评估当前阶段进展和阶段转换准备度
6. **训练依从性评估** - 分析训练计划执行情况

## 触发条件

技能在以下情况下自动触发：

1. 用户使用 `/rehab progress` 查看康复进展
2. 用户使用 `/rehab analysis` 进行康复分析
3. 用户使用 `/rehab trends` 查看趋势分析
4. 用户使用 `/rehab report` 生成康复报告

## 执行步骤

### 第1步：数据读取
读取康复数据文件：
- `data/rehabilitation-tracker.json` - 主康复档案
- `data/rehabilitation-logs/YYYY-MM/YYYY-MM-DD.json` - 每日训练日志

**数据验证：**
- 检查文件是否存在
- 验证数据结构完整性
- 确认有足够的数据点进行分析（建议至少3次评估或10天训练记录）

### 第2步：功能评估趋势分析

**关节活动度（ROM）分析：**
```
- 分析不同时间点的ROM测量值
- 计算ROM改善速率（度/周）
- 识别ROM平台期或倒退
- 预测达到目标ROM的时间
- 与目标范围对比
```

**肌力改善分析：**
```
- 追踪肌力等级变化（MMT评分）
- 识别肌力提升模式
- 比较不同肌群恢复速度
- 评估肌力不平衡情况
```

**平衡功能分析：**
```
- 平衡测试分数趋势
- 单腿站立时间改善
- 平衡稳定性评估
- 跌倒风险变化
```

### 第3步：疼痛模式分析

**疼痛时序分析：**
```
- 分析晨起疼痛趋势
- 分析活动后疼痛趋势
- 识别疼痛加重/缓解模式
- 关联疼痛与训练强度
```

**疼痛触发因素识别：**
```
- 特定训练项目与疼痛关系
- 训练强度与疼痛相关性
- 活动类型与疼痛关系
- 时间因素对疼痛影响
```

### 第4步：训练依从性计算

**依从性指标：**
```
依从性 = (实际训练次数 / 计划训练次数) × 100%
```

**分析维度：**
- 周依从性
- 月依从性
- 整体依从性
- 不同训练类型的依从性

### 第5步：目标达成评估

**目标进度追踪：**
- 计算每个目标的完成百分比
- 预估目标达成时间
- 识别滞后目标
- 提供目标调整建议

### 第6步：康复阶段评估

**当前阶段分析：**
- 阶段目标完成情况
- 是否准备好进入下一阶段
- 阶段转换建议

### 第7步：生成报告

输出包括：
- 康复进展摘要
- 功能改善趋势
- 疼痛控制情况
- 训练依从性评价
- 目标达成评估
- 阶段进展建议
- 个性化建议

## 输出格式

### 康复进展报告结构

```markdown
# 康复进展报告
**报告日期**: YYYY-MM-DD
**康复时长**: X天
**当前阶段**: 第X阶段 - 阶段名称

## 1. 康复进展摘要

[整体进展评价：优秀/良好/一般/需改进]
- 康复时长：X天（第X周）
- 完成训练：X次
- 训练依从性：X%
- 当前阶段进展：X%

## 2. 功能改善趋势

### 关节活动度（ROM）
- [关节名] [活动类型]: 基线X° → 当前X° → 改善X°
- 改善速率：X°/周
- 达到目标时间预估：X周
- 趋势分析：[改善趋势描述]

### 肌力评估
- [肌群名]: 基线X/5 → 当前X/5 → 改善X级
- 肌力提升模式：[描述]
- 肌力平衡：[评估]

### 平衡功能
- [测试类型]: 基线X → 当前X → 改善X
- 平衡稳定性：[评估]
- 跌倒风险：[评估]

## 3. 疼痛控制情况

- 平均疼痛水平：X/10
- 疼痛趋势：[改善/稳定/加重]
- 疼痛模式：[描述]
- 触发因素：[识别出的触发因素]
- 疼痛控制建议：[建议]

## 4. 训练依从性

- 整体依从性：X%
- 计划训练：X次
- 实际训练：X次
- 依从性评价：[优秀/良好/一般/需改进]
- 缺训原因分析：[如有]

## 5. 目标达成情况

### 已达成目标（X个）
- 目标1：[描述] - 达成日期：YYYY-MM-DD
- ...

### 进行中目标（X个）
- 目标1：[描述] - 当前进度：X% - 预计达成：YYYY-MM-DD
- ...

### 滞后目标（X个）
- 目标1：[描述] - 当前进度：X% - 需要关注

## 6. 康复阶段进展

**当前阶段**: 第X阶段 - [阶段名称]
- 阶段目标完成：X/X
- 阶段进度：X%
- 阶段持续时间：X周
- **阶段评价**: [评价]

**是否准备好进入下一阶段**: [是/否]
- [准备好的理由] / [需要继续努力的项目]

## 7. 个性化建议

### 训练建议
- [具体训练建议]

### 目标调整建议
- [目标调整建议]

### 阶段转换建议
- [阶段转换建议]

### 注意事项
- [需要注意的事项]

## 8. 下次评估

**下次评估日期**: YYYY-MM-DD
**评估重点**: [重点评估项目]
```

### 简要进展报告

```markdown
## 康复进展简报

📊 **整体进展**: 良好
⏱️ **康复时长**: 第X周（X天）
🎯 **阶段**: 第X阶段 - [阶段名称]

**功能改善**:
- ROM: +X°（改善速率X°/周）✅
- 肌力: 提升X级 ✅
- 平衡: 改善X% ✅

**疼痛控制**: 平均X/10（[趋势]）
**训练依从性**: X%（[评价]）
**目标达成**: X/X（X%）

**当前阶段**: X/X目标完成
**下一阶段准备**: [是/否]

💡 **建议**: [1-2条核心建议]
```

## 数据源

### 主数据文件
- **文件路径**: `data/rehabilitation-tracker.json`
- **读取字段**:
  - `user_profile` - 用户档案和康复基本信息
  - `rehabilitation_goals` - 康复目标列表
  - `exercise_log` - 训练日志
  - `functional_assessments` - 功能评估记录
  - `phase_progression` - 阶段进展记录
  - `pain_diary` - 疼痛日记
  - `statistics` - 统计数据

### 日志数据文件
- **文件路径**: `data/rehabilitation-logs/YYYY-MM/YYYY-MM-DD.json`
- **读取字段**:
  - `daily_summary` - 日训练摘要
  - `exercise_sessions` - 训练详情
  - `pain_entries` - 疼痛记录
  - `assessments` - 评估记录
  - `notes` - 每日备注

## 分析算法

### 1. 改善趋势分析

**线性回归分析：**
```
使用最小二乘法拟合功能改善趋势
改善速率 = (当前值 - 基线值) / 时间间隔
```

**改善模式识别：**
- 线性改善：稳定持续改善
- 阶梯式改善：平台期后快速改善
- 平台期：改善停滞
- 倒退：功能下降（需要关注）

### 2. 疼痛时序分析

**移动平均计算：**
```
7日移动平均疼痛 = sum(近7天疼痛) / 7
```

**疼痛趋势判断：**
- 改善：疼痛评分下降≥20%
- 稳定：疼痛评分变化<20%
- 加重：疼痛评分上升≥20%

### 3. 依从性计算

```
总体依从性 = (实际训练天数 / 计划训练天数) × 100%

训练类型依从性 = (某类型实际完成 / 某类型计划完成) × 100%
```

**依从性评价：**
- 优秀：≥90%
- 良好：75-89%
- 一般：60-74%
- 需改进：<60%

### 4. 目标达成预测

**线性外推：**
```
预测时间 = 当前日期 + ((目标值 - 当前值) / 改善速率)
```

**考虑因素：**
- 近期改善速率
- 平台期历史
- 训练依从性

### 5. 阶段转换准备度评估

**准备度评分：**
```
准备度 = (已达成阶段目标数 / 阶段目标总数) × 100%

准备度 ≥ 80%: 建议进入下一阶段
准备度 60-79%: 可考虑进入下一阶段，需谨慎
准备度 < 60%: 建议继续当前阶段
```

## 安全与隐私

### 数据安全原则

1. **本地存储**
   - 所有康复数据仅存储在用户本地设备
   - 不上传至任何云端服务器
   - 不与第三方共享数据

2. **隐私保护**
   - 个人健康信息严格保密
   - 数据文件不包含个人身份信息
   - 用户完全控制数据访问权限

3. **数据完整性**
   - 原始数据不被修改
   - 分析结果基于真实数据
   - 支持数据导出和备份

### 医学安全边界

**系统不能做的事：**
- ❌ 不提供具体康复训练处方
- ❌ 不替代康复师专业指导
- ❌ 不诊断损伤或并发症
- ❌ 不调整康复阶段计划
- ❌ 不预测康复预后时间
- ❌ 不处理急性疼痛或损伤

**系统能做的事：**
- ✅ 提供数据分析和趋势识别
- ✅ 提供进展追踪和目标管理
- ✅ 提供一般性康复建议
- ✅ 提供专业康复就医提醒
- ✅ 记录训练和评估数据
- ✅ 生成康复进展报告

**重要提示：**
- 所有康复训练计划应遵循康复师指导
- 任何疼痛加重或功能倒退应及时就医
- 定期专业评估是康复成功的关键
- 系统建议仅供参考，不替代专业判断

## 错误处理

### 数据读取错误

**错误类型1：文件不存在**
```
错误信息: "未找到康复数据文件，请先使用 /rehab start 开始康复追踪"
处理建议: 引导用户开始康复记录
```

**错误类型2：数据不足**
```
错误信息: "数据不足，至少需要3次功能评估或10天训练记录才能生成分析报告"
当前数据: X次评估，X天训练记录
处理建议: 建议用户继续记录更多数据
```

**错误类型3：数据结构错误**
```
错误信息: "数据文件结构异常，请检查数据完整性"
处理建议: 建议用户重新初始化康复档案
```

### 分析过程错误

**错误类型：计算异常**
```
错误信息: "数据分析过程中出现异常，请稍后重试"
处理建议: 记录错误日志，提供基础数据展示
```

### 输出生成错误

**错误类型：报告生成失败**
```
错误信息: "报告生成失败，请尝试简化查询条件或联系技术支持"
处理建议: 提供简化版报告或原始数据导出
```

## 使用示例

### 示例1：查看康复进展

**用户输入：**
```
/rehab progress
```

**技能执行：**
1. 读取 rehabilitation-tracker.json
2. 读取近30天的康复日志
3. 分析功能改善趋势
4. 计算训练依从性
5. 评估目标达成情况
6. 生成进展报告

**输出：**
```
# 康复进展报告

## 康复进展摘要
📊 整体进展: 良好
⏱️ 康复时长: 第6周（36天）
🎯 当前阶段: 第3阶段 - 强化期

## 功能改善
- 膝关节屈曲: 30° → 120° (+90°) ✅
- 膝关节伸直: -10° → 0° (+10°) ✅
- 股四头肌肌力: 3/5 → 4/5 (提升1级) ✅
- 单腿站立: 5秒 → 30秒 (+25秒) ✅

## 疼痛控制
- 平均疼痛: 1.5/10（良好控制）
- 疼痛趋势: 稳定 ✅

## 训练依从性: 92%（优秀）

## 目标达成: 8/14（57%）
- ✅ 已达成: 8个
- 🔄 进行中: 5个
- ⚠️ 滞后: 1个

## 阶段进展
第3阶段进度: 2/5目标完成（40%）
下一阶段准备: 需要继续努力

💡 建议: 继续当前训练强度，重点关注股四头肌强化训练
```

### 示例2：分析功能改善趋势

**用户输入：**
```
/rehab trends rom
```

**技能执行：**
1. 提取所有ROM评估记录
2. 绘制ROM改善曲线（文字描述）
3. 计算改善速率
4. 预测达到目标时间
5. 识别改善模式

**输出：**
```
# 关节活动度（ROM）趋势分析

## 膝关节屈曲
📈 改善趋势: 良好

时间线:
- 5/15: 30° (基线)
- 5/30: 70° (+40°)
- 6/15: 100° (+30°)
- 6/20: 120° (+20°)

改善速率: 8.6°/周
目标: 135°
预计达成: 2025-08-01（还需2周）
趋势: 持续改善 ✅

## 膝关节伸直
✅ 已达成目标

时间线:
- 5/15: -10° (基线)
- 6/10: 0° (达成目标) ✅
- 6/20: 0° (维持)

改善速率: 2.5°/周
目标: 0°
达成日期: 2025-06-10
趋势: 维持目标 ✅

## 建议
- 膝关节屈曲进展良好，继续保持
- 注意伸直维持训练，避免屈曲挛缩
- 预计2周内可达到屈曲目标
```

### 示例3：评估疼痛模式

**用户输入：**
```
/rehab analysis pain
```

**技能执行：**
1. 提取所有疼痛记录
2. 分析疼痛时序变化
3. 识别疼痛触发因素
4. 评估疼痛控制效果

**输出：**
```
# 疼痛模式分析

## 疼痛趋势
📉 总体趋势: 改善中

- 基线疼痛: 5/10
- 当前疼痛: 2/10
- 改善: 3分（60%改善）✅

## 时序模式
- 晨起疼痛: 1/10（轻度）
- 活动后疼痛: 2/10（轻度）
- 休息时疼痛: 0/10（无痛）

## 触发因素识别
- 主要触发因素: 延长坐姿、上下楼梯
- 疼痛加剧活动: 下楼梯、深蹲
- 缓解因素: 休息、冰敷、抬高

## 训练相关疼痛
- 训练时平均疼痛: 1.2/10（安全范围）
- 训练后疼痛: 2/10（快速缓解）
- 训练依从性不受疼痛影响 ✅

## 建议
- 疼痛控制良好，继续当前训练强度
- 注意训练后休息和冰敷
- 避免疼痛加剧活动（深蹲、下楼梯）
- 如疼痛>4/10，及时就医评估
```

## 相关性分析

### 与运动模块关联

**关联分析：**
- 康复训练与运动能力恢复的关联
- 康复训练强度与心率变化的关系
- 功能改善与日常活动量的关联

**示例：**
```
用户使用 /rehab analysis correlation fitness
技能读取:
- rehabilitation-tracker.json
- fitness-tracker.json
- 分析康复训练与运动指标的相关性
```

### 与睡眠模块关联

**关联分析：**
- 训练强度与睡眠质量的关系
- 疼痛水平与睡眠时长的关系
- 恢复期睡眠需求分析

### 与用药模块关联

**关联分析：**
- 止痛药使用趋势
- 用药与训练强度的关系
- 疼痛控制与用药依从性

## 使用示例

### 场景1：新用户开始康复
```
用户: /rehab start acl-surgery 2025-05-01
系统: 初始化康复档案，设置基础目标，提供初始建议
技能: rehabilitation-analyzer（可选，用于初步评估）
```

### 场景2：记录每日训练
```
用户: /rehab exercise slr 3x15 pain2
系统: 记录训练数据，更新训练日志
技能: 不触发（仅记录）
```

### 场景3：查看进展报告
```
用户: /rehab progress
系统: 调用 rehabilitation-analyzer 技能
技能: 完整分析，生成进展报告
```

### 场景4：分析特定功能
```
用户: /rehab trends rom
系统: 调用 rehabilitation-analyzer 技能
技能: ROM专项分析，生成趋势报告
```

### 场景5：评估疼痛模式
```
用户: /rehab analysis pain
系统: 调用 rehabilitation-analyzer 技能
技能: 疼痛专项分析，识别模式和触发因素
```

---

**技能版本**: v1.0
**最后更新**: 2026-01-06
**维护者**: WellAlly Tech

---

## Merged Reference (legacy variant)

---
name: sexual-health-analyzer
description: Sexual Health Analyzer
---

# 性健康分析技能

## 技能概述

本技能提供全面的性健康数据分析功能,包括IIEF-5评分分析、STD筛查管理、避孕效果评估、性活动统计以及与用药、慢性病、心理、营养、运动等模块的深度关联分析。

## 医学免责声明

⚠️ **重要提示**:本技能提供的数据分析和建议仅供参考,不构成医学诊断或治疗建议。

- 所有性健康问题应由专业医生诊断和治疗
- 分析结果不能替代专业医疗检查
- 紧急情况应立即就医
- 请遵循医生的专业建议

## 核心功能

### 1. IIEF-5 评分分析

#### 1.1 交互式问卷

**问卷结构**:
- 5个问题,每个问题0-5分
- 总分范围:0-25分
- 评估时间范围:过去6个月

**问题详解**:

**问题1**:勃起信心
- 评估用户对获得和维持勃起的信心程度
- 反映心理因素对性功能的影响
- 低分可能提示表现焦虑

**问题2**:勃起获得
- 评估受到性刺激时获得勃起的能力
- 反映血管和神经功能
- 低分可能提示器质性ED

**问题3**:插入能力
- 评估勃起硬度是否足够插入
- 临床相关的勃起质量指标
- 低分通常需要医疗干预

**问题4**:勃起维持
- 评估完成性交过程中维持勃起的能力
- 反映静脉闭塞功能
- 与问题3联合分析可确定ED类型

**问题5**:性交满意度
- 评估性交过程的主观满意度
- 受硬度、持续时间、伴侣满意度等多因素影响
- 综合性功能的最终指标

#### 1.2 ED严重程度评估

| 总分 | ED严重程度 | 临床意义 | 推荐措施 |
|------|-----------|----------|----------|
| 22-25 | 正常 | 勃起功能良好 | 继续健康生活方式 |
| 17-21 | 轻度ED | 轻度功能障碍 | 生活方式调整,定期评估 |
| 12-16 | 轻中度ED | 中度功能障碍 | 建议就医评估 |
| 8-11 | 中度ED | 明显功能障碍 | 需要医疗干预 |
| 5-7 | 重度ED | 严重功能障碍 | 全面医疗评估和治疗 |

#### 1.3 趋势分析

**分析维度**:
- 总分变化趋势(改善/稳定/恶化)
- 各问题得分变化模式
- ED严重程度变化轨迹
- 治疗干预效果评估

**输出内容**:
- IIEF-5评分时间序列图表
- 改善/恶化趋势标识
- 变化速率计算
- 与其他健康指标的相关性分析

#### 1.4 风险因素分析

**生理因素**:
- 年龄:每增加10年,ED风险增加约20%
- 糖尿病:ED风险增加3倍
- 心血管疾病:ED风险增加2-3倍
- 高血压:ED风险增加1.5-2倍
- 肥胖:BMI>30增加ED风险
- 荷尔蒙异常:低睾酮水平

**心理因素**:
- 表现焦虑
- 抑郁症状
- 压力水平
- 伴侣关系问题

**生活方式因素**:
- 吸烟:增加ED风险1.5倍
- 酗酒:长期影响性功能
- 缺乏运动:心血管健康下降
- 睡眠质量:影响荷尔蒙分泌

**药物因素**:
- 抗抑郁药(SSRIs等)
- 抗高血压药(β受体阻滞剂、噻嗪类)
- 抗精神病药
- 激素类药物

#### 1.5 改善建议

**生活方式干预**:
- **戒烟**:显著改善血管健康
- **限酒**:男性每日<2杯
- **减重**:BMI控制在18.5-24.9
- **规律运动**:
  - 每周150分钟中等强度有氧运动
  - 每周2-3次力量训练
  - 每日盆底肌训练(凯格尔运动)
- **健康饮食**:
  - 地中海饮食模式
  - 增加水果蔬菜摄入
  - 减少饱和脂肪和加工食品
  - 适量坚果和全谷物

**心理干预**:
- 性治疗师咨询
- 认知行为疗法
- 伴侣治疗
- 压力管理技术(冥想、瑜伽)

**医疗干预**:
- PDE5抑制剂(需医生处方)
- 睾酮补充疗法(如睾酮低)
- 真空勃起装置
- 阴茎注射疗法
- 手术治疗(血管手术、假体)

### 2. STD 筛查管理

#### 2.1 筛查项目详解

**HIV (艾滋病病毒)**:
- **检测方法**:血液检测(抗体+抗原组合)
- **窗口期**:1-3个月
- **高危人群**:MSM、性工作者、多性伴侣者
- **筛查频率**:高风险每3-6个月,一般风险每年

**梅毒 (Syphilis)**:
- **检测方法**:血液检测(RPR/VDRL+TPPA确认)
- **窗口期**:10-90天
- **分期**:一期、二期、潜伏期、三期
- **治疗**:青霉素有效,早期治愈率高

**衣原体 (Chlamydia)**:
- **检测方法**:尿液检测或拭子
- **窗口期**:1-3周
- **特点**:常无症状,但可导致不孕
- **治疗**:阿奇霉素或多西环素

**淋病 (Gonorrhea)**:
- **检测方法**:尿液检测或拭子
- **窗口期**:1-14天
- **特点**:男性症状明显,女性常无症状
- **治疗**:头孢曲松+阿奇霉素(考虑耐药性)

**HPV (人乳头瘤病毒)**:
- **检测方法**:拭子DNA检测
- **窗口期**:1个月-数年
- **特点**:非常常见,大多数自愈
- **高危型**:HPV 16/18与宫颈癌相关
- **预防**:HPV疫苗有效

**乙肝 (Hepatitis B)**:
- **检测方法**:血液检测(HBsAg+抗HBs)
- **窗口期**:1-6个月
- **预防**:乙肝疫苗有效
- **治疗**:抗病毒药物

**生殖器疱疹 (Herpes)**:
- **检测方法**:拭子PCR或血液抗体
- **窗口期**:2-12天
- **特点**:无治愈方法,可控制症状
- **治疗**:抗病毒药物(阿昔洛韦等)

#### 2.2 风险评估

**行为风险因素**:
- 性伴侣数量(>3个/年 = 高风险)
- 保护措施使用频率
- 性伴侣的STD状况
- 性工作或性工作者接触史
- MSM人群
- 注射吸毒史

**动态风险评分**:
- **低风险**(<10分):单一稳定伴侣,坚持保护
- **中风险**(10-30分):2-3个性伴侣,偶尔保护
- **高风险**(30-50分):多性伴侣,保护不一致
- **极高风险**(>50分):性工作者,MSM,无保护

#### 2.3 筛查频率建议

基于风险等级的个性化筛查计划:

| 风险等级 | HIV/梅毒 | 衣原体/淋病 | HPV | 乙肝 |
|----------|---------|------------|-----|------|
| 低风险 | 每1-2年 | 每1-2年 | 每3年 | 已免疫无需检测 |
| 中风险 | 每年 | 每年 | 每3年 | 每1-2年 |
| 高风险 | 每3-6月 | 每3-6月 | 每年 | 每年 |
| 极高风险 | 每3月 | 每3月 | 每6月 | 每6月 |

#### 2.4 阳性结果管理

**立即行动**:
- 开始治疗(遵医嘱)
- 通知性伴侣并进行检测
- 暂停性生活或严格保护
- 避免传播风险

**治疗追踪**:
- 治疗后检测以确认治愈
- 监测药物副作用
- 评估治疗依从性
- 记录治疗过程和结果

**预防再感染**:
- 性伴侣同时治疗
- 治愈后重新开始保护措施
- 定期复查
- 风险教育

#### 2.5 统计分析

- 筛查频率趋势
- 阳性率变化
- 感染类型分布
- 治愈率统计
- 再感染率分析

### 3. 避孕管理

#### 3.1 避孕方法详细分析

**避孕套 (男/女)**:
- **典型使用有效率**:85%
- **完美使用有效率**:98%
- **优点**:
  - 唯一防孕又防病的方法
  - 无激素副作用
  - 易于获取
  - 即刻起效
- **缺点**:
  - 需要每次使用
  - 可能影响性快感
  - 可能破裂或滑落
- **满意度影响因素**:
  - 尺寸是否合适
  - 润滑剂使用
  - 佩戴技巧
  - 品牌偏好

**口服避孕药**:
- **典型使用有效率**:91%
- **完美使用有效率**:99.7%
- **类型**:
  - 复方避孕药(雌激素+孕激素)
  - 单纯孕激素药(适合哺乳期)
  - 24/4方案 vs 21/7方案
- **优点**:
  - 高效避孕
  - 可调节月经周期
  - 改善痤疮和经前综合症
  - 降低卵巢癌和子宫内膜癌风险
- **缺点**:
  - 需要每日服用
  - 激素副作用
  - 不适合吸烟女性>35岁
  - 不能预防STD
- **副作用追踪**:
  - 恶心、乳房胀痛
  - 情绪变化
  - 性欲改变
  - 体重变化
  - 月经间期出血

**宫内节育器 (IUD)**:
- **有效率**:99%+
- **类型**:
  - 铜IUD(10-12年)
  - 左炔诺孕酮IUD(3-8年)
- **优点**:
  - 长效可逆
  - 即刻起效
  - 可随时取出
  - 激素IUD可减轻月经
- **缺点**:
  - 需要医生放置
  - 放置时不适
  - 可能增加月经量和痛经(铜IUD)
  - 不能预防STD
- **副作用追踪**:
  - 放置后疼痛
  - 月经变化
  - 点滴出血
  - 穿孔风险(罕见)

**皮下埋植**:
- **有效率**:99%+
- **持续时间**:3-5年
- **优点**:
  - 长效可逆
  - 放置简单
  - 可随时取出
  - 隐蔽性好
- **缺点**:
  - 激素副作用
  - 可能导致月经紊乱
  - 放置部位可能瘢痕
  - 不能预防STD

**避孕针**:
- **典型使用有效率**:94%
- **完美使用有效率**:99%+
- **频率**:每3个月一次
- **优点**:
  - 不需要每日服用
  - 隐蔽性好
- **缺点**:
  - 需要定期注射
  - 体重增加常见
  - 生育力恢复可能延迟
  - 不能预防STD

**体外射精**:
- **典型使用有效率**:78%
- **完美使用有效率**:96%
- **风险**:
  - 需要高度自控
  - 射精前可能有精子溢出
  - 增加性焦虑
  - 不能预防STD
- **不推荐**:失败率较高

**安全期法**:
- **典型使用有效率**:76-88%
- **完美使用有效率**:95-99%
- **方法**:
  - 日历法
  - 基础体温法
  - 宫颈黏液法
  - 症状体温法
- **风险**:
  - 月经不规律时不可靠
  - 需要严格记录
  - 排卵期可能不规律
  - 不能预防STD
- **不推荐**:失败率较高

**结扎手术**:
- **有效率**:99%+
- **类型**:
  - 输精管结扎(男性)
  - 输卵管结扎(女性)
- **优点**:
  - 永久性避孕
  - 高效
  - 无激素影响
- **缺点**:
  - 通常不可逆
  - 需要手术
  - 术后恢复期
  - 不能预防STD

#### 3.2 效果评估

**避孕失败率分析**:
- Pearl指数(每100女性年失败数)
- 典型使用 vs 完美使用差异
- 使用错误分析
- 失败原因追踪

**满意度评分**:
- 易用性(1-10分)
- 舒适度(1-10分)
- 对性生活影响(1-10分)
- 副作用可接受度(1-10分)
- 整体满意度(1-10分)

#### 3.3 副作用追踪

**荷尔蒙相关副作用**:
- 月经模式改变
- 情绪波动
- 性欲变化
- 体重变化
- 乳房胀痛

**非荷尔蒙副作用**:
- 疼痛或不适(IUD)
- 过敏反应(避孕套)
- 疤痕形成(埋植、结扎)

**严重副作用**:
- 血栓栓塞风险(激素类)
- 异位妊娠风险(IUD失败时)
- 感染风险(IUD放置)

#### 3.4 切换历史

**切换原因分析**:
- 副作用不耐受
- 效果不满意
- 生活方式改变
- 健康状况变化
- 经济原因
- 伴侣偏好

**切换建议**:
- 基于副作用史选择
- 考虑年龄和生育计划
- 评估健康风险因素
- 伴侣讨论

### 4. 性活动日志

#### 4.1 记录内容

**基础信息**:
- 日期和时间
- 活动类型(性交、口交、手交等)
- 持续时间
- 伴侣类型(固定、新伴侣等)

**保护措施**:
- 避孕方法(避孕套、口服避孕药等)
- 是否正确使用
- 是否破损或失败

**主观体验**:
- 满意度评分(1-10分)
- 性欲水平(1-10分)
- 疼痛或不适(有/无,程度)
- 是否达到高潮

**特殊情况**:
- 异常症状
- 避孕失败
- 意外情况
- 备注

#### 4.2 隐私保护

**数据标记**:
- 敏感数据标记
- 加密建议
- 访问权限设置
- 数据匿名化选项

**用户控制**:
- 可选功能,完全自主决定
- 可随时删除记录
- 可选择性导出数据
- 就医时可选择性展示

#### 4.3 统计分析

**频率统计**:
- 每周/每月/每年性活动次数
- 频率变化趋势
- 与年龄/关系阶段对比

**满意度分析**:
- 平均满意度评分
- 满意度趋势变化
- 影响满意度的因素分析
- 与IIEF-5/FSFI评分相关性

**保护措施统计**:
- 保护措施使用率
- 各避孕方法使用频率
- 避孕失败次数和原因
- 保护措施与满意度关系

**模式识别**:
- 性活动时间模式
- 与生理周期关系(女性)
- 与情绪/压力相关性
- 与药物使用相关性

### 5. 关联分析

#### 5.1 与用药模块的关联

**PDE5抑制剂效果追踪**:
- 药物名称和剂量
- 服用频率和时机
- 效果评分(1-10分)
- 副作用记录
- 效果随时间变化
- 与IIEF-5评分相关性
- 成本效益分析

**抗抑郁药对性功能的影响**:
- 药物类别(SSRIs, SNRIs, TCAs等)
- 性功能副作用类型
- 严重程度评估
- 发生时间(用药初期/长期)
- 与性欲、勃起、高潮的关系
- 换药或加药建议

**降压药对性功能的影响**:
- 药物类别(β受体阻滞剂、噻嗪类等)
- ED发生率
- 性欲影响
- 替代药物选择建议

**激素类药物**:
- 睾酮补充治疗
- 雌激素/孕激素
- 性功能影响
- 剂量调整建议

**其他药物**:
- 抗精神病药
- 抗组胺药
- 化疗药物
- 对性功能的影响

#### 5.2 与慢性病模块的关联

**糖尿病与ED**:
- **病理机制**:
  - 血管内皮损伤
  - 神经病变
  - 荷尔蒙异常
- **血糖控制与ED关系**:
  - HbA1c <7%:ED风险较低
  - HbA1c 7-9%:中度风险
  - HbA1c >9%:高度风险
- **糖尿病病程与ED**:
  - <5年:ED风险增加2倍
  - 5-10年:ED风险增加3倍
  - >10年:ED风险增加4-5倍
- **管理建议**:
  - 严格控制血糖
  - 定期ED筛查
  - 早期干预
  - 综合管理(血压、血脂)

**高血压与性功能**:
- **病理机制**:
  - 血管损伤
  - 内皮功能障碍
- **降压药的影响**:
  - β受体阻滞剂:增加ED风险
  - 噻嗪类利尿剂:可能引起ED
  - ACEI/ARB:中性或有益
  - 钙通道阻滞剂:中性
- **管理建议**:
  - 控制血压至目标值
  - 选择对性功能影响小的药物
  - 定期评估性功能

**心血管疾病与性功能**:
- **ED作为预警信号**:
  - ED可能早于心绞痛症状2-3年
  - ED是心血管疾病的独立预测因子
  - 建议ED患者进行心血管评估
- **性生活安全评估**:
  - 心功能分级评估
  - 运动耐量评估
  - 药物使用(硝酸酯类药物禁用PDE5抑制剂)
- **心肌梗死后性生活指导**:
  - 通常2-4周后可恢复
  - 逐步增加强度
  - 监测症状

**肥胖与性功能**:
- **影响机制**:
  - 荷尔蒙变化(睾酮降低,雌激素升高)
  - 血管内皮功能障碍
  - 心理因素(身体意象)
- **减重效果**:
  - 减重5-10%可显著改善
  - 减重后IIEF-5评分平均提高3-5分
  - 运动结合饮食效果最佳

#### 5.3 与心理健康模块的关联

**焦虑与性功能**:
- **表现焦虑**:
  - 担心性表现
  - 害怕不能满足伴侣
  - 导致勃起困难或早泄
- **广泛性焦虑**:
  - 性欲下降
  - 难以放松享受
  - 分心难以集中
- **干预**:
  - 认知行为疗法
  - 放松训练
  - 感觉集中训练

**抑郁与性功能**:
- **抑郁症状与性欲**:
  - 性欲丧失常见症状
  - 性兴趣显著下降
  - 可能是最早出现的症状之一
- **抗抑郁药的双重影响**:
  - 改善抑郁可能恢复性欲
  - 但药物本身可能引起性功能障碍
- **管理策略**:
  - 选择对性功能影响小的抗抑郁药(安非他酮)
  - 加用药物(如丁螺环酮)
  - 剂量调整
  - 心理治疗

**创伤后应激障碍(PTSD)**:
- 性回避
- 性唤起困难
- 闪回影响
- 需要专业创伤治疗

**身体意象**:
- 对自己身体的不满
- 影响性自信
- 导致回避亲密关系
- 身体积极性训练

**伴侣关系**:
- 关系质量与性生活满意度高度相关
- 沟通问题影响性满足
- 冲突未解决影响性欲
- 伴侣治疗可能有益

#### 5.4 与营养模块的关联

**关键营养素**:

**锌**:
- **功能**:睾酮合成必需元素
- **缺乏表现**:性欲下降,ED
- **推荐摄入**:男性11mg/天
- **食物来源**:牡蛎、牛肉、南瓜子、腰果
- **补充建议**:如缺乏可补充15-30mg/天

**精氨酸**:
- **功能**:促进一氧化氮生成,改善血流
- **对ED的潜在益处**:可能轻度改善勃起功能
- **推荐剂量**:3-5g/天
- **食物来源**:坚果、种子、肉类、鱼类
- **注意事项**:可能与某些药物相互作用

**维生素D**:
- **功能**:支持睾酮合成
- **缺乏表现**:低维生素D水平与ED相关
- **目标水平**:血清25(OH)D >30 ng/mL
- **补充建议**:如缺乏可补充1000-2000 IU/天

**镁**:
- **功能**:支持睾酮合成,改善血流
- **推荐摄入**:男性400-420mg/天
- **食物来源**:绿叶蔬菜、坚果、全谷物
- **补充建议**:如缺乏可补充200-400mg/天

**Omega-3脂肪酸**:
- **功能**:改善心血管健康,间接改善性功能
- **推荐摄入**:1-2g EPA+DHA/天
- **食物来源**:深海鱼类、亚麻籽、核桃

**抗氧化物质**:
- **功能**:保护血管内皮
- **重要抗氧化剂**:维生素C、维生素E、硒、番茄红素
- **食物来源**:水果、蔬菜、坚果

**膳食模式**:

**地中海饮食**:
- **特点**:高水果蔬菜、全谷物、橄榄油、鱼类
- **研究证据**:改善ED,降低心血管风险
- **机制**:改善血管健康,降低炎症

**限制**:
- **饱和脂肪**:减少红肉和全脂乳制品
- **反式脂肪**:避免加工食品
- **添加糖**:控制糖分摄入,特别是糖尿病患者
- **酒精**:男性每日<2杯

**营养状况评估**:
- 评估营养素缺乏
- 提供个性化营养建议
- 推荐补充剂(如需要)
- 监测营养改善效果

#### 5.5 与运动模块的关联

**有氧运动**:
- **类型**:快走、跑步、游泳、骑行
- **推荐量**:每周150分钟中等强度
- **对ED的益处**:
  - 改善心血管健康
  - 增强血流
  - 降低ED风险约40%
  - IIEF-5评分平均提高2-4分
- **机制**:
  - 改善内皮功能
  - 增加一氧化氮生物利用度
  - 降低血压和血糖

**力量训练**:
- **类型**:重量训练、抗阻训练
- **推荐量**:每周2-3次
- **对性功能的益处**:
  - 提高睾酮水平
  - 增强肌肉力量和耐力
  - 改善身体意象和自信
- **注意事项**:
  - 避免过度训练
  - 充分恢复

**盆底肌训练(凯格尔运动)**:
- **功能**:
  - 增强勃起硬度和维持能力
  - 改善射精控制
  - 对ED和早泄均有益
- **方法**:
  - 收缩盆底肌肉(如中断排尿)
  - 保持5秒,放松5秒
  - 每日3组,每组10-15次
- **效果**:
  - 6-12周后显著改善
  - IIEF-5评分平均提高3-5分

**瑜伽**:
- **益处**:
  - 改善身体意象和性自信
  - 增强柔韧性和身体意识
  - 降低压力和焦虑
  - 某些体式增强盆底肌
- **推荐**:
  - 每周2-3次
  - 结合冥想和呼吸练习

**运动与性欲**:
- 适度运动提高性欲
- 过度运动可能降低性欲(女运动员三联征)
- 找到平衡点

**运动处方**:
- 基于年龄、健康状况、兴趣
- 渐进式增加
- 结合有氧、力量、柔韧性训练
- 盆底肌训练作为补充

### 6. 风险评估

#### 6.1 ED风险评分

**风险因素加权**:

| 风险因素 | 权重 | 评分 |
|----------|------|------|
| 年龄 | 15% | <40:0, 40-49:1, 50-59:2, 60+:3 |
| 糖尿病 | 20% | 无:0, 控制:1, 未控制:3 |
| 心血管疾病 | 15% | 无:0, 稳定:1, 不稳定:3 |
| 高血压 | 10% | 无:0, 控制:1, 未控制:2 |
| 吸烟 | 10% | 从不:0, 已戒烟:1, 吸烟:2 |
| 酗酒 | 5% | 无:0, 偶尔:1, 经常:2 |
| 肥胖 | 10% | BMI<25:0, 25-30:1, >30:2 |
| 缺乏运动 | 5% | 规律:0, 偶尔:1, 缺乏:2 |
| 压力/焦虑 | 5% | 无:0, 轻度:1, 中重度:2 |
| 药物副作用 | 5% | 无:0, 轻度:1, 明显:2 |

**风险等级**:
- **低风险**(0-20分):ED可能性低
- **中风险**(21-40分):ED风险增加
- **高风险**(41-60分):ED高度可能
- **极高风险**(>60分):几乎肯定有ED

#### 6.2 STD风险评分

**行为因素**:

| 风险因素 | 评分 |
|----------|------|
| 性伴侣数量 | 单一:0, 2-3:5, 4-10:15, >10:30 |
| 保护措施使用 | 总是:0, 通常:5, 有时:15, 从不:30 |
| 性伴侣类型 | 固定:0, 新伴侣/偶尔:10, 性工作者:30 |
| MSM | 否:0, 是:20 |
| 已知伴侣感染 | 无:0, 有:50 |
| 注射吸毒 | 否:0, 是:30 |
| 既往STD史 | 无:0, 1次:10, >1次:20 |

**风险等级**:
- **低风险**(0-10分):STD可能性低
- **中风险**(11-30分):STD风险增加
- **高风险**(31-50分):STD高度可能
- **极高风险**(>50分):需要立即筛查

### 7. 个性化建议

#### 7.1 基于IIEF-5评分的建议

**正常(22-25分)**:
- 继续健康生活方式
- 定期评估(每年)
- 预防性措施

**轻度ED(17-21分)**:
- 生活方式干预优先
- 压力管理
- 限制酒精和戒烟
- 3-6个月后重新评估

**轻中度ED(12-16分)**:
- 生活方式干预
- 考虑PDE5抑制剂
- 心理因素评估
- 建议就医

**中度ED(8-11分)**:
- 积极医疗干预
- PDE5抑制剂
- 考虑其他治疗选项
- 心理咨询

**重度ED(5-7分)**:
- 全面医疗评估
- 多学科治疗
- 可能需要专科转诊
- 伴侣参与

#### 7.2 基于风险评估的建议

**高风险ED**:
- 定期筛查(每3-6个月)
- 积极控制危险因素
- 预防性干预
- 早期治疗

**高风险STD**:
- 频繁筛查(每3个月)
- PrEP(暴露前预防)考虑
- 疫苗接种(HPV、乙肝)
- 风险降低咨询

#### 7.3 生活方式处方

**运动处方**:
- 有氧运动:每周150分钟
- 力量训练:每周2-3次
- 盆底肌训练:每日
- 灵活性训练:每周2-3次

**饮食处方**:
- 地中海饮食模式
- 增加水果蔬菜至5-9份/天
- 全谷物替代精制谷物
- 每周2次深海鱼类
- 限制加工食品和添加糖

**行为处方**:
- 戒烟计划
- 限酒:男性<2杯/天
- 睡眠改善:7-9小时/天
- 压力管理:每日放松练习
- 体重管理:BMI 18.5-24.9

### 8. 预警系统

#### 8.1 定期检查提醒

**IIEF-5评估**:
- 正常:每年
- 轻度ED:每6个月
- 中度以上:每3-6个月

**STD筛查**:
- 基于风险等级个性化设置
- 高风险:每3个月
- 一般风险:每年
- 低风险:每1-2年

**性健康检查**:
- 40岁以下:每1-2年
- 40岁以上:每年
- 慢性病患者:每年

#### 8.2 问题预警

**IIEF-5评分下降**:
- 连续2次评估下降>3分
- 一个月内下降>5分
- ED严重程度升级

**STD高风险行为**:
- 无保护性行为增加
- 性伴侣数量增加
- 已知暴露后未筛查

**避孕失效**:
- 避孕套破裂>2次/月
- 漏服避孕药>2次/月
- IUD位置异常

#### 8.3 趋势预警

**性欲显著下降**:
- 持续>3个月
- 影响生活质量
- 伴侣关系受影响

**满意度持续降低**:
- 平均满意度<5分
- 持续下降趋势
- 需要专业评估

## 使用场景

### 场景1:定期性健康评估

**用户请求**:分析最近6个月的性健康状况

**分析流程**:
1. 读取最近6个月的所有性健康记录
2. 分析IIEF-5评分变化趋势
3. 评估STD筛查历史
4. 检查避孕方法有效性
5. 分析用药效果
6. 评估生活方式因素

**输出内容**:
- IIEF-5评分变化曲线
- ED严重程度变化
- 主要风险因素
- 改善建议
- 下次检查时间

### 场景2:ED诊断辅助

**用户请求**:我最近勃起困难,IIEF-5评分15分,什么原因?

**分析流程**:
1. 检索最近IIEF-5评分历史
2. 分析用药记录
3. 评估慢性病控制情况
4. 检查心理状态记录
5. 分析生活方式因素
6. 识别主要原因

**输出内容**:
- ED严重程度:轻中度
- 主要风险因素(如糖尿病控制不佳)
- 可修改因素(如吸烟、缺乏运动)
- 药物影响分析
- 个性化改善计划

### 场景3:避孕方法选择

**用户请求**:我想换一种避孕方法,当前口服避孕药有副作用

**分析流程**:
1. 评估当前避孕方法满意度和副作用
2. 分析健康史和风险因素
3. 考虑年龄和生育计划
4. 对比各种避孕方法的优缺点
5. 识别适合的替代方案

**输出内容**:
- 当前方法问题分析
- 适合的替代方案
- 各方案优缺点对比
- 推荐方案及理由
- 切换时间建议

### 场景4:STD风险评估

**用户请求**:我最近有新伴侣,需要STD筛查吗?

**分析流程**:
1. 评估性行为模式
2. 识别风险因素
3. 计算风险评分
4. 确定需要筛查的项目
5. 设置筛查时间表

**输出内容**:
- 当前风险等级
- 推荐筛查项目
- 筛查时间建议
- 风险降低措施
- 随访计划

### 场景5:多学科联合分析

**用户请求**:我有糖尿病,这对性功能有什么影响?

**分析流程**:
1. 读取糖尿病管理数据
2. 分析血糖控制情况
3. 评估性功能状态
4. 分析两者关联性
5. 评估并发症风险
6. 生成联合管理建议

**输出内容**:
- 糖尿病对性功能的影响机制
- 当前血糖控制与ED风险
- 综合管理策略
- 监测指标建议
- 生活方式干预重点

## 数据分析方法

### 定量分析
- 统计描述(均值、中位数、标准差)
- 趋势分析(线性回归、移动平均)
- 相关性分析(Pearson/Spearman相关)
- 风险评分计算(多因素加权)

### 定性分析
- 文本描述分析
- 症状模式识别
- 主诉内容分类
- 满意度评估

### 可视化输出
- IIEF-5评分时间序列图表
- ED严重程度变化图
- STD筛查历史时间线
- 避孕方法效果对比
- 性活动频率统计图
- 风险因素雷达图

## 质量保证

### 数据验证
- 检查数据完整性
- 验证数据一致性
- 识别异常值
- 处理缺失数据

### 结果验证
- 医学逻辑检查
- 与临床指南对照
- 专家审查(如有)
- 用户反馈收集

### 持续改进
- 定期更新分析算法
- 引入新的科学证据
- 优化用户体验
- 扩展功能范围

## 参考资源

### 临床指南
- WHO性健康指南
- EAU(欧洲泌尿协会)ED指南
- AUA(美国泌尿协会)性功能障碍指南
- CDCSTD筛查和治疗指南
- 中华医学会男科学指南

### 评估工具
- IIEF-5(国际勃起功能指数-5)
- FSFI(女性性功能指数)
- SHEF(性健康评估框架)

### 数据源
- 用户记录数据
- 用药模块数据
- 慢性病模块数据
- 心理模块数据
- 营养模块数据
- 运动模块数据

## 局限性

### 系统局限
- 不能替代专业医疗检查
- 不能进行实验室检测
- 不能进行体格检查
- 分析结果受数据质量影响

### 数据局限
- 依赖用户记录准确性
- 可能存在遗漏记录
- 主观评估存在偏差
- 时间跨度可能不足

### 建议局限
- 不能考虑所有个体因素
- 不能预测所有并发症
- 需要结合临床判断
- 不能保证100%准确性

## 未来扩展

### 计划功能
- AI辅助诊断
- 个性化治疗方案生成
- 伴侣健康关联分析
- 生殖健康追踪(生育规划)
- 性教育模块

### 研究方向
- 机器学习预测模型
- 基因风险分析
- 个性化预防策略
- 远程医疗集成

---

**版本**: v1.0.0
**最后更新**: 2025-01-06
**维护者**: WellAlly Tech

---

## Merged Reference (legacy variant)

---
name: skin-health-analyzer
description: Analyze skin health data, identify skin problem patterns, assess skin health status. Supports correlation analysis with nutrition, chronic diseases, and medication data.
risk: unknown
source: community
---

# 皮肤健康分析技能

## 技能概述

本技能提供全面的皮肤健康数据分析功能，包括趋势识别、风险评估、问题诊断和个性化建议生成。特别强调痣的监测和皮肤癌预防。

## 医学免责声明

⚠️ **重要提示**：本技能提供的数据分析和建议仅供参考，不构成医学诊断或治疗建议。

- 所有皮肤问题应由专业皮肤科医生诊断和治疗
- 痣的异常变化必须立即就医检查
- 皮肤癌需要专业诊断，不能仅依靠自我评估
- 分析结果不能替代专业皮肤科检查
- 紧急情况应立即就医
- 请遵循皮肤科医生的专业建议

## 核心功能

### 1. 趋势分析

#### 皮肤问题发展趋势
- 识别痤疮、湿疹等问题的发生模式
- 分析问题的季节性和周期性
- 评估问题严重程度的变化
- 预测未来发作风险

**输出内容**：
- 问题发生频率曲线
- 严重程度变化趋势
- 诱发因素分析
- 预防建议

#### 痣的变化监测
- 新增痣的位置和数量追踪
- 已有痣的大小变化监测
- ABCDE特征变化记录
- 高风险痣识别

**输出内容**：
- 痣的分布图
- 变化预警报告
- 需要关注的美容痣列表
- 就医建议

#### 护肤效果评估
- 护肤程序使用频率分析
- 产品效果评估
- 皮肤状态改善情况
- 不良反应监测

**输出内容**：
- 护肤效果评分
- 产品推荐
- 程序优化建议
- 成本效益分析

#### 日晒防护效果分析
- 防晒霜使用情况统计
- 日晒伤发生频率
- 光老化迹象评估
- 防护习惯改进建议

**输出内容**：
- 防护评分趋势
- 风险评估
- 改进建议
- 产品推荐

### 2. 风险评估

#### 皮肤癌风险评估
基于以下因素进行综合评估：
- 皮肤类型（Fitzpatrick分型）
- 日晒暴露史
- 痣的数量和特征
- 日晒伤历史
- 家族史
- 使用日光浴床历史

**风险等级**：
- **低风险**：深色皮肤、少日晒、无痣异常
- **中风险**：浅色皮肤、中度日晒、有痣异常
- **高风险**：浅色皮肤、大量日晒、多个异常痣、家族史

**输出内容**：
- 风险等级（低/中/高）
- 主要风险因素
- 量化风险评分
- 降低风险策略
- 筛查建议

#### 痤疮严重程度评估
基于以下因素进行综合评估：
- 痤疮类型（黑头、白头、炎性丘疹、结节、囊肿）
- 病灶数量和分布
- 炎症程度
- 瘢痕形成风险

**严重程度分级**：
- **轻度**：主要是黑头和白头，少量炎性病灶
- **中度**：较多炎性病灶，可能形成轻微瘢痕
- **重度**：结节和囊肿，高瘢痕风险

**输出内容**：
- 严重程度分级
- 主要诱因分析
- 治疗建议参考
- 护肤建议
- 就医建议

#### 过敏风险识别
基于以下因素进行综合评估：
- 已知过敏原
- 皮肤敏感史
- 产品使用历史
- 季节性过敏模式
- 家族过敏史

**输出内容**：
- 过敏原列表
- 风险评估
- 避免建议
- 替代产品推荐

#### 光老化风险预测
基于以下因素进行综合评估：
- 日晒暴露总量
- 防护习惯
- 皮肤类型
- 年龄
- 生活方式

**输出内容**：
- 光老化风险等级
- 当前光老化迹象
- 预防建议
- 治疗选择参考

### 3. 关联分析

#### 与营养模块的关联
**营养素对皮肤健康的影响**：
- 维生素A：皮肤细胞更新、视力
- 维生素C：胶原蛋白合成、抗氧化
- 维生素E：抗氧化、保护细胞膜
- Omega-3脂肪酸：抗炎作用
- 锌：伤口愈合、油脂控制
- 水：皮肤水合作用

**食物对皮肤问题的影响**：
- 高糖食物：痤疮加重
- 乳制品：部分人群痤疮诱发因素
- 辛辣食物：玫瑰痤疮加重
- 酒精：皮肤脱水、潮红

**营养缺乏的皮肤表现**：
- 维生素A缺乏：皮肤干燥、角化
- 维生素C缺乏：伤口愈合慢、易淤青
- 维生素B缺乏：皮炎、口角炎
- 铁缺乏：苍白、脆弱
- 蛋白质缺乏：皮肤松弛、水肿

**输出内容**：
- 营养状况评估
- 缺乏风险识别
- 饮食调整建议
- 补充剂建议（如需要）

#### 与慢性病模块的关联
**糖尿病与皮肤**：
- 糖尿病皮肤病（糖尿病性皮肤病）
- 伤口愈合延迟
- 真菌感染风险增加
- 黑棘皮病
- 脂质性渐进性坏死

**自身免疫病与皮肤**：
- 狼疮：蝶形红斑、光敏感
- 类风湿关节炎：类风湿结节、血管炎
- 银屑病关节炎：银屑病皮损
- 皮肌炎：Gottron征、向阳性皮疹

**甲状腺疾病与皮肤**：
- 甲亢：皮肤湿润、头发变细、指甲松动
- 甲减：皮肤干燥、毛发粗燥、水肿

**肝脏疾病与皮肤**：
- 黄疸：皮肤和巩膜黄染
- 蜘蛛痣：血管性蜘蛛状病变
- 掌红斑：手掌红斑
- 皮肤瘙痒：胆汁淤积

**输出内容**：
- 皮肤症状与疾病关联分析
- 并发症风险评估
- 综合管理建议
- 专科转诊建议

#### 与用药模块的关联
**药物疹（药物过敏）**：
- 常见致敏药物：抗生素、抗癫痫药、NSAIDs
- 皮疹类型：麻疹样、荨麻疹、固定药疹
- 严重反应：Stevens-Johnson综合征

**光敏性药物**：
- 四环素类抗生素
- 噻嗪类利尿剂
- NSAIDs
- 某些抗精神病药

**药物引起的色素沉着**：
- 米诺环素：蓝色灰色色素沉着
- 胺碘酮：蓝灰色色素沉着
- 某些化疗药物

**药物引起的皮肤干燥**：
- 维A酸类
- 苯二氮卓类
- 抗组胺药（长期使用）

**输出内容**：
- 药物风险识别
- 相互作用分析
- 替代药物建议（需与医生讨论）
- 监测建议

#### 与内分泌模块的关联
**激素变化对皮肤的影响**：
- 青春期：雄激素增加，痤疮
- 妊娠期：色素沉着、妊娠纹、皮肤血管变化
- 更年期：雌激素下降，皮肤干燥、皱纹
- 月经周期：周期性痤疮加重

**多囊卵巢综合征（PCOS）**：
- 痤疮
- 多毛症
- 雄激素性脱发
- 黑棘皮病

**库欣综合征**：
- 月亮脸、水牛背
- 皮肤变薄、紫纹
- 痤疮、多毛

**输出内容**：
- 激素对皮肤的影响分析
- 周期性症状识别
- 管理建议
- 治疗时机建议

### 4. 个性化建议

#### 护肤程序优化
**根据皮肤类型定制**：
- 干性皮肤：加强保湿，避免过度清洁
- 油性皮肤：控油，保持清洁，水油平衡
- 混合性皮肤：分区护理，T区控油，U区保湿
- 中性皮肤：维持现状，基础护理
- 敏感性皮肤：温和产品，避免刺激

**根据主要问题定制**：
- 痤疮：清洁、控油、抗炎、避免致痘成分
- 色斑：防晒、美白成分、抗氧化
- 抗衰老：抗氧化、修复、防晒
- 敏感：舒缓、修复、屏障保护

**输出内容**：
- 早晨护肤程序建议
- 晚间护肤程序建议
- 每周护理建议
- 产品选择指导
- 预算范围建议

#### 生活方式调整
**饮食调整**：
- 低升糖指数饮食（痤疮）
- 抗炎饮食（湿疹、银屑病）
- 抗氧化食物（抗衰老）
- 充足水分摄入

**睡眠管理**：
- 保证7-9小时睡眠
- 规律作息时间
- 睡前护肤程序
- 枕头清洁（痤疮）

**压力管理**：
- 识别压力诱发的皮肤问题
- 学习放松技巧
- 规律运动
- 兴爱好

**环境调整**：
- 室内湿度控制（干燥皮肤）
- 避免过敏原（过敏肌肤）
- 工作环境防护（职业性皮肤问题）

**输出内容**：
- 个性化生活方式建议
- 目标设定
- 进度追踪方法
- 激励机制

#### 预防措施建议
**皮肤癌预防**：
- 每日防晒（SPF 30+）
- 避免日光浴床
- 定期皮肤检查
- 保护儿童免受日晒
- 早期发现异常痣

**痤疮预防**：
- 正确清洁皮肤
- 避免触摸面部
- 清洁手机和眼镜
- 更换枕套频率
- 非致痘性化妆品

**湿疹预防**：
- 保持皮肤保湿
- 避免已知诱因
- 使用温和洗涤剂
- 穿着棉质衣物
- 控制室内温度和湿度

**光老化预防**：
- 全年防晒
- 抗氧化护肤品
- 不吸烟
- 充足睡眠
- 健康饮食

**输出内容**：
- 针对性预防策略
- 优先级排序
- 实施步骤
- 效果评估方法

#### 产品选择建议
**成分知识**：
- 痤疮治疗：水杨酸、过氧化苯甲酰、维A酸
- 美白：维生素C、烟酰胺、熊果苷
- 抗衰老：视黄醇、肽类、透明质酸
- 保湿：透明质酸、甘油、神经酰胺
- 舒缓：芦荟、积雪草、燕麦

**产品选择原则**：
- 根据皮肤类型选择
- 避免已知过敏原
- 成分简单优于复杂
- 无香料配方更安全
- 先试用小包装

**阅读产品标签**：
- 识别致痘成分
- 识别过敏原
- 理解活性成分浓度
- 理解产品功效宣称

**输出内容**：
- 成分教育
- 产品推荐框架（非具体品牌）
- 避免成分列表
- 产品试用建议

### 5. 目标管理

#### 目标设定
- 与用户协商设定现实目标
- 分解为可实现的步骤
- 设定时间节点
- 建立评估标准

**常见目标类型**：
- 改善痤疮状况
- 建立规律护肤习惯
- 增加防晒使用频率
- 减少色斑
- 改善皮肤干燥
- 建立定期自查习惯

#### 进度追踪
- 定期评估目标达成情况
- 提供激励和反馈
- 调整目标（如需要）
- 庆祝里程碑达成
- 记录改进过程

#### 障碍识别
- 识别阻碍目标达成的因素
- 提供克服障碍的策略
- 调整计划以适应实际情况
- 提供持续支持
- 连接资源和支持网络

### 6. 统计分析

#### 综合健康评分
基于以下因素计算：
- 皮肤问题控制情况（30%）
- 护肤习惯（25%）
- 日晒防护（20%）
- 定期检查（15%）
- 目标达成（10%）

**评分范围**：0-100分
- **优秀**：90-100分
- **良好**：75-89分
- **一般**：60-74分
- **较差**：<60分

#### 皮肤健康年龄
- 基于皮肤状态、问题情况、防护习惯计算
- 与实际年龄对比
- 提供改善建议

#### 问题统计
- 问题类型分布
- 问题发生频率
- 问题持续时间
- 解决率统计
- 复发率分析

#### 护肤统计
- 护肤程序执行率
- 产品使用频率
- 护肤花费统计
- 产品更换频率
- 不良反应统计

### 7. 预警系统

#### 痣的变化预警
- 新增痣数量异常增加
- 已有痣快速增大
- ABCDE特征出现异常
- 颜色或形态改变
- 出现症状（瘙痒、出血）

**预警级别**：
- **黄色预警**：需要观察，下次检查时咨询医生
- **橙色预警**：需要尽快就医（1周内）
- **红色预警**：需要立即就医

#### 皮肤问题预警
- 痤疮突然恶化
- 新出现严重皮疹
- 药物反应迹象
- 感染征象（红肿热痛）
- 慢性病皮肤表现

#### 护肤预警
- 产品不良反应
- 护肤程序不当
- 过度护肤征象
- 过期产品使用
- 产品相互作用

#### 检查提醒
- 定期皮肤自查提醒（每月）
- 皮肤科检查提醒（每年）
- 痣监测提醒（每月）
- 防晒补涂提醒

## 使用场景

### 场景1：定期健康评估
**用户请求**：分析最近6个月的皮肤健康状况

**分析流程**：
1. 读取最近6个月的所有皮肤健康记录
2. 分析问题记录、痣监测、护肤记录
3. 评估防护习惯变化
4. 计算健康评分变化
5. 识别改善或恶化的趋势
6. 生成综合评估报告

**输出内容**：
- 健康评分变化趋势
- 主要改善点
- 需要关注的问题
- 下一步行动建议

### 场景2：痣的监测评估
**用户请求**：我发现背部有个痣有些变化，帮我评估一下

**分析流程**：
1. 检索该痣的历史记录
2. 对比ABCDE特征变化
3. 评估风险等级
4. 检查是否有其他异常痣
5. 分析个人风险因素
6. 生成评估报告

**输出内容**：
- ABCDE评估结果
- 变化程度分析
- 风险等级
- 就医建议（强烈建议/建议/观察）
- 监测频率建议

### 场景3：痤疮管理规划
**用户请求**：我想改善痤疮问题，制定一个管理计划

**分析流程**：
1. 评估当前痤疮严重程度
2. 分析主要诱发因素
3. 评估当前护肤和饮食习惯
4. 识别需要改善的领域
5. 设定阶段性目标
6. 制定个性化计划

**输出内容**：
- 当前严重程度评估
- 主要诱因分析
- 护肤程序建议
- 饮食和生活方式建议
- 目标和时间表
- 何时就医建议

### 场景4：防晒改进计划
**用户请求**：我的防晒习惯不好，帮我制定改进计划

**分析流程**：
1. 评估当前防晒习惯
2. 分析日晒暴露模式
3. 评估皮肤类型和风险
4. 识别主要障碍
5. 设定可达成的目标
6. 制定渐进式改进计划

**输出内容**：
- 当前防晒评分
- 风险评估
- 改进目标
- 产品选择建议
- 使用习惯建立策略
- 进度追踪方法

### 场景5：多学科联合分析
**用户请求**：我有糖尿病，这对我的皮肤有什么影响？

**分析流程**：
1. 读取糖尿病管理数据
2. 分析血糖控制情况
3. 评估皮肤并发症风险
4. 识别潜在的糖尿病皮肤问题
5. 分析两者关联性
6. 生成联合管理建议

**输出内容**：
- 糖尿病对皮肤的影响
- 常见糖尿病皮肤问题
- 并发症风险评估
- 联合管理策略
- 监测指标建议
- 何时就医

### 场景6：抗衰老规划
**用户请求**：我想预防皮肤老化，从现在开始应该注意什么？

**分析流程**：
1. 评估当前皮肤状态
2. 分析生活方式和习惯
3. 评估光老化风险
4. 识别可改变的风险因素
5. 制定预防策略
6. 建立监测指标

**输出内容**：
- 当前皮肤年龄评估
- 主要老化风险因素
- 预防策略（防晒、护肤、生活方式）
- 护肤程序建议
- 定期评估建议
- 投资回报分析

## 数据分析方法

### 定量分析
- 统计描述（均值、中位数、标准差）
- 趋势分析（线性回归、移动平均）
- 相关性分析（Pearson/Spearman相关）
- 风险评分计算（多因素加权）
- 时间序列分析

### 定性分析
- 文本描述分析
- 症状模式识别
- 主诉内容分类
- 满意度评估
- 图片分析（如可用）

### ABCDE评估算法
- 不对称性评分（0-2分）
- 边缘规则性评分（0-2分）
- 颜色均匀性评分（0-2分）
- 直径评分（0-2分）
- 变化评分（0-2分）
- 总分≥4分：建议就医

### 可视化输出
- 时间序列图表
- 身体部位分布图
- 痣的位置地图
- 风险评估雷达图
- 进度追踪仪表板
- 对比分析柱状图

## 质量保证

### 数据验证
- 检查数据完整性
- 验证数据一致性
- 识别异常值
- 处理缺失数据
- 交叉验证不同来源数据

### 结果验证
- 医学逻辑检查
- 与临床指南对照
- 专家审查（如有）
- 用户反馈收集
- 定期更新算法

### 持续改进
- 定期更新分析算法
- 引入新的科学证据
- 优化用户体验
- 扩展功能范围
- 提高准确性

## 参考资源

### 临床指南
- 美国皮肤病学会（AAD）指南
- 欧洲皮肤病学会（EADV）指南
- 中华皮肤科分会临床指南
- 皮肤癌基金会（SCF）指南

### 评估工具
- ABCDE法则（黑色素瘤筛查）
- Glasgow七点清单（黑色素瘤评估）
- 痤疮严重程度评分系统
- 湿疹面积和严重程度指数（EASI）
- 皮肤病生活质量指数（DLQI）

### 数据源
- 用户记录数据
- 营养模块数据
- 慢性病模块数据
- 用药模块数据
- 内分泌模块数据
- 环境数据（紫外线指数）

## 局限性

### 系统局限
- 不能替代专业皮肤科检查
- 不能进行皮肤镜检查
- 不能进行病理检查
- 分析结果受数据质量影响
- 不能进行生物活检

### 数据局限
- 依赖用户记录准确性
- 可能存在遗漏记录
- 主观评估存在偏差
- 时间跨度可能不足
- 照片质量影响评估

### 建议局限
- 不能考虑所有个体因素
- 不能预测所有并发症
- 需要结合临床判断
- 不能保证100%准确性
- 产品建议可能存在个体差异

## 未来扩展

### 计划功能
- AI图像识别（痣和皮肤病变分析）
- 语音记录录入
- 智能提醒系统
- 与皮肤科医生系统对接
- 远程皮肤病学支持

### 研究方向
- 机器学习预测模型
- 个性化预防策略
- 基因风险分析
- 皮肤微生物组分析
- 环境因素影响分析

---

**版本**: v1.0.0
**最后更新**: 2025-01-06
**维护者**: WellAlly Tech


## When to Use

Use this skill when tackling tasks related to its primary domain or functionality as described above.

---

## Merged Reference (legacy variant)

---
name: sleep-analyzer
description: 分析睡眠数据、识别睡眠模式、评估睡眠质量，并提供个性化睡眠改善建议。支持与其他健康数据的关联分析。
allowed-tools: Read, Grep, Glob, Write
---

# 睡眠分析器技能

分析睡眠数据，识别睡眠模式，评估睡眠质量，并提供个性化睡眠改善建议。

## 功能

### 1. 睡眠趋势分析

分析睡眠时长、质量、效率的变化趋势，识别改善或需要关注的方面。

**分析维度**：
- 睡眠时长趋势（平均睡眠时长变化）
- 睡眠效率趋势（睡眠效率百分比变化）
- 入睡时间模式（上床时间、入睡时间、起床时间）
- 作息规律性评分（sleep consistency score）
- 周末vs工作日对比（social jetlag）

**输出**：
- 趋势方向（改善/稳定/下降）
- 变化幅度和百分比
- 趋势显著性评估
- 最佳睡眠时间窗口识别
- 改进建议

### 2. 睡眠质量评估

综合评估睡眠质量，识别影响睡眠质量的关键因素。

**评估内容**：
- PSQI分数追踪和趋势
- 主观睡眠质量分布（好/中/差）
- 夜间觉醒分析（次数、时长、原因）
- 睡眠阶段分析（深睡、浅睡、REM比例）
- 睡后恢复感评估

**输出**：
- 睡眠质量等级（优秀/良好/一般/较差）
- 质量变化趋势
- 主要影响因素识别
- 质量改善优先级建议

### 3. 睡眠问题识别

识别常见的睡眠问题和风险因素。

**识别内容**：
- **失眠模式**：
  - 入睡困难（sleep latency >30分钟）
  - 睡眠维持困难（夜间觉醒>2次或总觉醒时间>30分钟）
  - 早醒（比预期提前醒来>30分钟）
  - 混合型失眠

- **呼吸暂停风险**：
  - STOP-BANG问卷评分
  - 症状分析（打鼾、憋醒、白天嗜睡）
  - 风险等级（低/中/高）

- **其他问题**：
  - 作息不规律检测
  - 睡眠债计算（理想时长vs实际时长）
  - 社交时差评估

**输出**：
- 问题存在与否
- 问题类型和严重程度
- 风险因素列表
- 是否需要就医建议

### 4. 相关性分析

分析睡眠与其他健康指标的相关性。

**支持的相关性分析**：
- **睡眠 ↔ 运动**：
  - 运动日vs休息日的睡眠差异
  - 运动时间对睡眠的影响（早晨/下午/晚间运动）
  - 运动强度与睡眠质量的相关性

- **睡眠 ↔ 饮食**：
  - 咖啡因摄入与睡眠时长、入睡时间的关系
  - 酒精摄入对睡眠结构的影响
  - 晚餐时间与睡眠质量的关系

- **睡眠 ↔ 情绪**：
  - 睡眠与情绪的双向关系分析
  - 压力水平对睡眠质量的影响
  - 睡眠剥夺对日间情绪的影响

- **睡眠 ↔ 慢性病**：
  - 睡眠与高血压的关系
  - 睡眠与血糖控制的关联
  - 睡眠与体重变化的关系

**输出**：
- 相关系数（-1到1）
- 相关性强度（弱/中/强）
- 统计显著性
- 因果关系推断
- 实践建议

### 5. 个性化建议生成

基于用户数据生成个性化睡眠改善建议。

**建议类型**：
- **作息调整建议**：
  - 最佳上床/起床时间
  - 作息一致性改善方案
  - 午睡管理建议

- **睡前准备建议**：
  - 睡前例行程序设计
  - 放松技巧推荐
  - 屏幕时间管理

- **睡眠环境优化**：
  - 温度、湿度、光线、噪音优化
  - 床品舒适度建议

- **生活方式调整**：
  - 运动、饮食、咖啡因、酒精管理
  - 压力管理建议

- **CBT-I元素**：
  - 刺激控制建议
  - 睡眠限制建议
  - 认知重构建议

**输出**：
- 优先级排序的建议列表
- 具体实施步骤
- 预期效果说明
- 实施时间线

---

## 使用说明

### 触发条件

当用户请求以下内容时触发本技能：
- 睡眠趋势分析
- 睡眠质量评估
- 睡眠问题识别
- 睡眠改善建议
- 睡眠与其他健康指标的关联分析

### 执行步骤

#### 步骤 1: 确定分析范围

明确用户请求的分析类型和时间范围：
- 分析类型：趋势/质量/问题/相关性/建议
- 时间范围：周/月/季度/自定义

#### 步骤 2: 读取数据

**主要数据源**：
1. `data-example/sleep-tracker.json` - 睡眠追踪主数据
2. `data-example/sleep-logs/YYYY-MM/YYYY-MM-DD.json` - 每日睡眠记录

**关联数据源**：
1. `data-example/fitness-tracker.json` - 运动数据
2. `data-example/hypertension-tracker.json` - 血压数据
3. `data-example/diabetes-tracker.json` - 血糖数据
4. `data-example/diet-records/` - 饮食记录
5. `data-example/mood-tracker.json` - 情绪数据

#### 步骤 3: 数据分析

根据分析类型执行相应的分析算法：

**趋势分析算法**：
- 线性回归计算趋势斜率
- 移动平均平滑波动
- 统计显著性检验

**相关性分析算法**：
- Pearson相关系数计算
- 滞后相关性分析（考虑时间延迟效应）
- 多变量回归分析

**模式识别算法**：
- 时间序列模式识别
- 异常值检测
- 周期性分析

#### 步骤 4: 生成报告

按照标准格式输出分析报告（见"输出格式"部分）

---

## 输出格式

### 睡眠质量分析报告

```markdown
# 睡眠质量分析报告

## 分析周期
2025-03-20 至 2025-06-20（3个月）

---

## 睡眠时长趋势

- **趋势**：⬆️ 改善
- **开始**：平均6.2小时/晚
- **当前**：平均7.1小时/晚
- **变化**：+0.9小时 (+14.5%)
- **解读**：睡眠时长显著增加，接近理想目标（7.5小时）

**趋势线**：
```
6.5h ┤     ╭╮
6.0h ┤   ╭─╯╰╮
5.5h ┤ ╭─╯   ╰─╮
5.0h ┼─┘       ╰─
     └───────────
     3月  4月  5月  6月
```

---

## 睡眠效率

- **平均睡眠效率**：85.3%
- **效率范围**：78%-92%
- **达标率**：63%（>85%为达标）
- **解读**：睡眠效率正常，仍有提升空间

**效率分布**：
- 优秀（>90%）：15晚
- 良好（85-90%）：28晚
- 需改善（<85%）：47晚

---

## 作息规律性

- **平均上床时间**：23:15（范围：22:30-01:00）
- **平均起床时间**：07:05（范围：06:30-08:30）
- **作息一致性评分**：72/100
- **社交时差**：45分钟（周末比工作日晚睡晚起）
- **解读**：作息基本规律，但周末波动较大

**建议**：
- 🎯 保持一致的起床时间，包括周末
- 🎯 逐步调整上床时间，避免周末过度延迟

---

## 睡眠质量分布

| 质量等级 | 天数 | 占比 | 趋势 |
|---------|------|------|------|
| 优秀 | 8 | 9% | ⬆️ |
| 很好 | 12 | 13% | ➡️ |
| 好 | 15 | 17% | ⬆️ |
| 一般 | 42 | 47% | ⬇️ |
| 差 | 10 | 11% | ⬇️ |
| 很差 | 3 | 3% | ➡️ |

**解读**：睡眠质量以"一般"为主，但"好"及以上质量的天数在增加

---

## 夜间觉醒分析

- **平均觉醒次数**：1.8次/晚
- **平均觉醒时长**：18分钟
- **主要原因**：
  1. 尿意（45%）
  2. 噪音（25%）
  3. 温度过热（15%）
  4. 其他（15%）

**建议**：
- 🎯 睡前2小时限制液体摄入
- 🎯 优化卧室温度（18-22℃）
- 🎯 使用白噪音机器遮蔽背景噪音

---

## PSQI 评估趋势

- **最新分数**：8分（睡眠质量一般）
- **上次分数**：10分（2025-03-20）
- **变化**：-2分（改善）
- **趋势**：⬆️ 持续改善

**历史趋势**：
```
12 ┤ ●
10 ┤  ●
 8 ┤    ●
 6 ┤
   └──────
   12月 3月 6月
```

**各成分变化**：
- 主观睡眠质量：2→2（稳定）
- 入睡时间：2→2（稳定）
- 睡眠时长：2→1（改善）
- 睡眠效率：2→1（改善）
- 睡眠障碍：2→1（改善）

---

## 睡眠问题识别

### 失眠评估

- **类型**：混合型失眠
- **频率**：4-5晚/周
- **持续时间**：18个月
- **主要症状**：
  - ✗ 入睡困难（潜伏期>30分钟）
  - ✗ 睡眠维持困难（夜间觉醒>2次）
  - ✓ 无早醒问题

- **影响**：
  - 白天疲劳：中度
  - 情绪烦躁：是
  - 注意力困难：是
  - 工作表现：轻度影响

- **建议**：🏥 持续>3个月，建议就医咨询睡眠专科

### 呼吸暂停筛查（STOP-BANG）

- **评分**：3/8
- **风险等级**：中等风险
- **阳性项目**：
  - ✗ Snoring（打鼾）
  - ✗ Tired（白天疲劳）
  - ✓ Observed apnea（未观察到呼吸暂停）
  - ✗ Pressure（高血压）
  - ✓ BMI > 28
  - ✓ Age > 50
  - ✗ Neck size > 40cm
  - ✓ Gender = male

- **建议**：⚠️ 建议进行睡眠检查（PSG）

---

## 相关性分析

### 睡眠 ↔ 运动

**运动日 vs 休息日**：
- 运动日平均睡眠：7.3小时
- 休息日平均睡眠：6.8小时
- 差异：+0.5小时（+7.4%）

**运动时间对睡眠的影响**：
- 早晨运动：睡眠时长7.5小时，质量评分7.8/10
- 下午运动：睡眠时长7.2小时，质量评分7.5/10
- 晚间运动：睡眠时长6.8小时，质量评分6.8/10

**相关性**：中等正相关（r = 0.42）
**结论**：规律运动有助于改善睡眠，但应避免睡前2-3小时剧烈运动

**建议**：
- 🎯 保持规律运动习惯
- 🎯 将运动时间移至早晨或下午
- 🎯 睡前2-3小时避免剧烈运动

---

### 睡眠 ↔ 咖啡因

**咖啡因摄入时间分析**：
- 下午2点前摄入：平均睡眠7.2小时，入睡潜伏期25分钟
- 下午2点后摄入：平均睡眠6.7小时，入睡潜伏期40分钟
- 差异：-0.5小时时长，+15分钟潜伏期

**相关性**：中等负相关（r = -0.38）
**结论**：下午2点后摄入咖啡因显著影响睡眠

**建议**：
- 🎯 避免下午2点后摄入咖啡因
- 🎯 睡前6小时完全避免咖啡因

---

### 睡眠 ↔ 情绪

**睡眠质量对次日情绪的影响**：
- 睡眠好：次日情绪积极概率82%
- 睡眠一般：次日情绪积极概率45%
- 睡眠差：次日情绪积极概率18%

**睡前情绪对入睡的影响**：
- 睡前压力高：入睡潜伏期45分钟
- 睡前压力低：入睡潜伏期20分钟
- 差异：+25分钟

**相关性**：强双向相关（r = 0.65）
**结论**：睡眠与情绪存在显著的相互影响

**建议**：
- 🎯 睡前进行压力管理（冥想、深呼吸）
- 🎯 建立放松的睡前例行程序
- 🎯 记录情绪日记，识别压力模式

---

## 洞察与建议

### 关键洞察

1. **作息不一致是主要问题**
   - 社交时差45分钟
   - 周末作息显著偏离工作日
   - 影响：生物钟紊乱，周一"时差反应"

2. **晚间运动影响入睡**
   - 晚间运动日入睡潜伏期延长15分钟
   - 建议：调整运动时间

3. **睡眠环境可优化**
   - 噪音觉醒占25%
   - 温度过热占15%
   - 建议针对性改善

---

### 优先级行动计划

#### Priority 1：建立一致作息（2周）

**目标**：提高作息一致性评分至85分

**具体行动**：
1. 固定起床时间07:00（包括周末）
2. 固定上床时间23:00
3. 限制午睡<30分钟，且下午3点前
4. 逐步调整周末作息（每次提前15分钟）

**预期效果**：
- 作息一致性评分：72 → 85
- 睡眠效率提升：+3-5%
- 周一疲劳感减轻

---

#### Priority 2：创建睡前例行程序（3周）

**目标**：建立稳定的睡前例行程序

**具体行动**：
1. 提前1小时开始例行程序（22:00）
2. 关闭电子设备（22:30）
3. 调暗卧室灯光
4. 进行放松活动（阅读、冥想、温水澡）
5. 保持卧室安静、黑暗、凉爽（18-22℃）

**预期效果**：
- 入睡潜伏期缩短：30 → 20分钟
- 睡眠质量提升：一般 → 好
- 睡前压力降低

---

#### Priority 3：优化睡眠环境（1周）

**目标**：消除环境对睡眠的干扰

**具体行动**：
1. 安装遮光窗帘
2. 使用白噪音机器遮蔽背景噪音
3. 优化温度至18-22℃
4. 移除卧室时钟
5. 更换舒适的枕头和床垫

**预期效果**：
- 夜间觉醒减少：1.8 → 1.2次/晚
- 睡眠连续性提升
- 晨起状态改善

---

#### Priority 4：生活方式调整（4周）

**目标**：消除影响睡眠的生活习惯

**具体行动**：
1. 将运动移至早晨或下午
2. 下午2点后停止咖啡因摄入
3. 睡前3小时避免酒精
4. 睡前2小时避免大餐
5. 睡前1小时避免工作相关讨论

**预期效果**：
- 睡眠时长增加：+0.3小时
- 睡眠质量评分提升：+1分
- PSQI分数改善：8 → 6

---

## 长期目标

- **睡眠时长**：达到7.5小时/晚（当前7.1小时）
- **睡眠效率**：提升至>90%（当前85%）
- **PSQI分数**：降至≤5分（当前8分）
- **作息一致性**：提升至≥85分（当前72分）
- **入睡潜伏期**：缩短至<20分钟（当前28分钟）

---

## 医学安全提醒

⚠️ **就医建议**：
- 🏥 失眠持续>3个月，建议咨询睡眠专科
- 🏥 STOP-BANG≥3分，建议进行睡眠检查（PSG）
- 🏥 严重嗜睡影响驾驶安全，需立即就医

---

**报告生成时间**：2025-06-20
**分析周期**：2025-03-20 至 2025-06-20（90天）
**数据记录数**：90晚
**睡眠分析器版本**：v1.0
```

---

## 数据结构

### 睡眠记录数据

```json
{
  "sleep_records": [
    {
      "id": "sleep_20250620001",
      "date": "2025-06-20",
      "sleep_times": {
        "bedtime": "23:00",
        "sleep_onset_time": "23:30",
        "wake_time": "07:00",
        "out_of_bed_time": "07:15"
      },
      "sleep_metrics": {
        "sleep_duration_hours": 7.0,
        "time_in_bed_hours": 8.25,
        "sleep_latency_minutes": 30,
        "sleep_efficiency": 84.8
      },
      "sleep_quality": {
        "subjective_quality": "fair",
        "quality_score": 5,
        "rested_feeling": "somewhat"
      },
      "factors": {
        "exercise": true,
        "exercise_time": "evening",
        "caffeine_after_2pm": false,
        "screen_time_before_bed_minutes": 60
      }
    }
  ]
}
```

---

## 算法说明

### 睡眠质量评分算法

```python
def calculate_sleep_quality_score(record):
    """
    计算睡眠质量评分（0-10分）

    因素权重：
    - 睡眠时长：30%
    - 睡眠效率：25%
    - 入睡潜伏期：20%
    - 夜间觉醒：15%
    - 主观质量：10%
    """
    score = 0

    # 睡眠时长评分（理想7-9小时）
    duration = record['sleep_duration_hours']
    if 7 <= duration <= 9:
        duration_score = 10
    elif 6 <= duration < 7 or 9 < duration <= 10:
        duration_score = 7
    else:
        duration_score = 4
    score += duration_score * 0.30

    # 睡眠效率评分（>90%优秀）
    efficiency = record['sleep_efficiency']
    efficiency_score = min(efficiency / 90 * 10, 10)
    score += efficiency_score * 0.25

    # 入睡潜伏期评分（<15分钟优秀）
    latency = record['sleep_latency_minutes']
    if latency <= 15:
        latency_score = 10
    elif latency <= 30:
        latency_score = 7
    elif latency <= 45:
        latency_score = 4
    else:
        latency_score = 1
    score += latency_score * 0.20

    # 夜间觉醒评分（0次优秀）
    awakenings = record['awakenings']['count']
    awakening_score = max(10 - awakenings * 2, 0)
    score += awakening_score * 0.15

    # 主观质量评分
    quality_map = {
        'excellent': 10,
        'very_good': 8,
        'good': 7,
        'fair': 5,
        'poor': 3,
        'very_poor': 1
    }
    subjective_score = quality_map.get(
        record['sleep_quality']['subjective_quality'],
        5
    )
    score += subjective_score * 0.10

    return round(score, 1)
```

### 作息规律性评分算法

```python
def calculate_sleep_consistency_score(records):
    """
    计算作息规律性评分（0-100分）

    因素：
    - 上床时间标准差
    - 起床时间标准差
    - 睡眠时长标准差
    - 工作日vs周末差异
    """
    # 提取时间数据
    bedtimes = [r['bedtime'] for r in records]
    wake_times = [r['wake_time'] for r in records]
    durations = [r['sleep_duration_hours'] for r in records]

    # 计算标准差（分钟）
    bedtime_std = time_to_minutes_std(bedtimes)
    wake_std = time_to_minutes_std(wake_times)
    duration_std = statistics.stdev(durations)

    # 计算工作日vs周末差异
    weekday_avg = avg([r['sleep_duration_hours']
                       for r in records if is_weekday(r)])
    weekend_avg = avg([r['sleep_duration_hours']
                       for r in records if is_weekend(r)])
    diff = abs(weekday_avg - weekend_avg)

    # 综合评分
    score = 100
    score -= bedtime_std * 0.5  # 上床时间标准差影响
    score -= wake_std * 0.5     # 起床时间标准差影响
    score -= duration_std * 2   # 睡眠时长标准差影响
    score -= diff * 10          # 工作日周末差异影响

    return max(0, min(100, round(score)))
```

### 相关性分析算法

```python
def calculate_correlation(sleep_data, other_data, lag_days=0):
    """
    计算睡眠与其他指标的相关性

    参数：
    - sleep_data: 睡眠数据列表
    - other_data: 其他指标数据列表
    - lag_days: 滞后天数（考虑延迟效应）

    返回：
    - correlation_coefficient: 相关系数
    - p_value: 统计显著性
    - interpretation: 相关性解释
    """
    # 对齐数据（考虑滞后）
    aligned = align_data_with_lag(sleep_data, other_data, lag_days)

    # 计算Pearson相关系数
    from scipy import stats
    corr, p_value = stats.pearsonr(
        aligned['sleep_values'],
        aligned['other_values']
    )

    # 解释相关性
    if abs(corr) < 0.3:
        strength = "弱"
    elif abs(corr) < 0.7:
        strength = "中等"
    else:
        strength = "强"

    direction = "正相关" if corr > 0 else "负相关"
    significant = p_value < 0.05

    interpretation = f"{strength}{direction}"
    if significant:
        interpretation += "（统计学显著）"

    return {
        'correlation_coefficient': round(corr, 3),
        'p_value': round(p_value, 4),
        'interpretation': interpretation,
        'significant': significant
    }
```

---

## 医学安全声明

本技能提供的分析和建议仅供参考，不构成医疗诊断或治疗方案。

**本技能能够做到的**：
- ✅ 分析睡眠数据和模式
- ✅ 识别睡眠问题风险
- ✅ 提供睡眠卫生建议
- ✅ 评估与其他健康指标的相关性

**本技能不能做的**：
- ❌ 诊断失眠、睡眠呼吸暂停等疾病
- ❌ 开具助眠药物或治疗
- ❌ 替代专业睡眠医学治疗
- ❌ 处理严重睡眠障碍

**何时需要就医**：
- 🏥 失眠持续>3个月
- 🏥 疑似睡眠呼吸暂停（STOP-BANG≥3）
- 🏥 严重嗜睡影响安全
- 🏥 突发严重睡眠问题

---

## 参考资源

- AASM 睡眠评分标准：https://aasm.org/
- PSQI 量表：https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3455216/
- STOP-BANG 问卷：https://www.stopbang.ca/
- CBT-I 治疗：https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3455216/

---

**技能版本**: v1.0
**创建日期**: 2026-01-02
**维护者**: WellAlly Tech

---

## Merged Reference (legacy variant)

---
name: tcm-constitution-analyzer
description: 分析中医体质数据、识别体质类型、评估体质特征,并提供个性化养生建议。支持与营养、运动、睡眠等健康数据的关联分析。
allowed-tools: Read, Grep, Glob, Write
---

# 中医体质辨识分析器技能

分析中医体质数据,识别体质类型,评估体质特征,并提供个性化养生改善建议。

## 功能

### 1. 体质辨识评估

基于《中医体质分类与判定》标准进行体质辨识。

**评估维度**:
- 9种体质类型评分(平和质、气虚质、阳虚质、阴虚质、痰湿质、湿热质、血瘀质、气郁质、特禀质)
- 主体质判定
- 兼夹体质识别
- 体质特征分析

**评估方法**:
- 60题标准化问卷
- 5分制评分(没有/很少/有时/经常/总是)
- 转化分数计算(0-100分)

**输出**:
- 体质类型判定结果
- 各体质评分
- 体质特征描述
- 个体化养生建议

### 2. 体质特征分析

综合评估用户的体质特征。

**分析内容**:
- **形体特征**:
  - 体型特点
  - 面色表现
  - 舌象脉象

- **心理特征**:
  - 性格特点
  - 情绪倾向

- **发病倾向**:
  - 易感疾病
  - 健康风险

- **适应能力**:
  - 环境适应
  - 季节适应

**输出**:
- 体质类型分类
- 特征描述
- 风险评估
- 调理优先级

### 3. 体质变化趋势分析

追踪体质变化,评估调理效果。

**分析内容**:
- 多次评估对比
- 评分变化趋势
- 体质稳定性分析
- 调理效果评估

**输出**:
- 趋势图表
- 改善幅度
- 稳定性评估
- 继续调理建议

### 4. 相关性分析

分析体质与其他健康指标的相关性。

**支持的相关性分析**:
- **体质 ↔ 营养**:
  - 体质类型与饮食偏好的关系
  - 营养状况对体质的影响
  - 个性化饮食建议

- **体质 ↔ 运动**:
  - 不同体质适合的运动类型
  - 运动对体质改善的作用

- **体质 ↔ 睡眠**:
  - 体质与睡眠质量的关系
  - 睡眠对体质的影响

- **体质 ↔ 慢性病**:
  - 不同体质易患疾病
  - 体质与疾病的关系

**输出**:
- 相关系数
- 相关性强度
- 统计显著性
- 实践建议

### 5. 个性化建议生成

基于体质类型生成个性化养生建议。

**建议类型**:
- **饮食调养**:
  - 宜食食物清单
  - 忌食食物清单
  - 推荐食谱
  - 饮食原则

- **起居调摄**:
  - 作息建议
  - 环境要求
  - 生活习惯

- **运动锻炼**:
  - 推荐运动类型
  - 运动频次和强度
  - 注意事项

- **情志调摄**:
  - 情绪管理
  - 心理调节

- **穴位保健**:
  - 推荐穴位
  - 按摩方法
  - 艾灸建议

- **中药调理**:
  - 推荐方剂
  - 方剂组成
  - 用法用量
  - 注意事项

**建议依据**:
- 中医体质理论
- 用户体质类型
- 季节因素
- 用户健康状况

---

## 使用说明

### 触发条件

当用户请求以下内容时触发本技能:
- 中医体质辨识评估
- 体质类型查询
- 体质特征分析
- 中医养生建议
- 体质趋势分析
- 体质与其他健康指标的关联分析

### 执行步骤

#### 步骤 1: 确定分析范围

明确用户请求的分析类型:
- 体质辨识评估
- 体质特征查询
- 养生建议获取
- 趋势分析
- 相关性分析

#### 步骤 2: 读取数据

**主要数据源**:
1. `data/constitutions.json` - 体质知识库
2. `data/constitution-recommendations.json` - 养生建议库
3. `data-example/tcm-constitution-tracker.json` - 体质追踪主数据
4. `data-example/tcm-constitution-logs/YYYY-MM/YYYY-MM-DD.json` - 每日评估记录

**关联数据源**:
1. `data-example/profile.json` - 基础信息
2. `data-example/nutrition-tracker.json` - 营养数据
3. `data-example/fitness-tracker.json` - 运动数据
4. `data-example/sleep-tracker.json` - 睡眠数据

#### 步骤 3: 数据分析

根据分析类型执行相应的分析算法:

**体质评分算法**:
```python
def calculate_constitution_scores(answers):
    """
    基于《中医体质分类与判定》标准

    计算公式:
    转化分数 = [(原始分数 - 题目数) / (题目数 × 4)] × 100

    其中:
    - 原始分数 = 各题目得分之和
    - 题目数 = 该体质的问题数量
    """
    scores = {}
    for constitution, questions in CONSTITUTION_QUESTIONS.items():
        original_score = sum(answers[q] for q in questions)
        question_count = len(questions)
        converted_score = ((original_score - question_count) / (question_count * 4)) * 100
        scores[constitution] = round(converted_score, 1)
    return scores
```

**体质判定算法**:
```python
def determine_constitution_type(scores):
    """
    判定逻辑:
    1. 平和质判定:
       - 得分 ≥ 60分
       - 其他8种体质得分均 < 40分

    2. 偏颇体质判定:
       - 得分最高的体质为判定结果

    3. 兼夹体质判定:
       - 次高分的体质得分 ≥ 40分
       - 则为兼夹体质
    """
    peaceful_score = scores['平和质']
    other_scores = {k: v for k, v in scores.items() if k != '平和质'}

    # 判定是否为平和质
    if peaceful_score >= 60 and all(s < 40 for s in other_scores.values()):
        return {
            'primary': '平和质',
            'secondary': [],
            'type': 'balanced'
        }

    # 偏颇体质判定
    sorted_scores = sorted(other_scores.items(), key=lambda x: x[1], reverse=True)
    primary = sorted_scores[0][0]

    # 判断兼夹体质
    secondary = [k for k, v in sorted_scores[1:3] if v >= 40]

    return {
        'primary': primary,
        'secondary': secondary,
        'type': 'compound' if secondary else 'single'
    }
```

**趋势分析算法**:
- 线性回归计算趋势
- 移动平均平滑波动
- 统计显著性检验

#### 步骤 4: 生成报告

按照标准格式输出分析报告(见"输出格式"部分)

---

## 输出格式

### 体质辨识评估报告

```markdown
# 中医体质辨识评估报告

## 评估日期
2025-06-20

## 评估结果

### 体质类型判定
- **主体质**: 气虚质
- **兼夹体质**: 阳虚质
- **体质类型**: 兼夹体质

### 各体质评分

| 体质类型 | 评分 | 判定 |
|---------|------|------|
| 气虚质 | 78.5 | ⚠️ 偏颇 |
| 阳虚质 | 62.3 | ⚠️ 偏颇 |
| 平和质 | 42.1 | 正常 |
| 痰湿质 | 38.7 | 正常 |
| 气郁质 | 35.2 | 正常 |
| 阴虚质 | 32.1 | 正常 |
| 湿热质 | 28.4 | 正常 |
| 血瘀质 | 25.6 | 正常 |
| 特禀质 | 18.3 | 正常 |

---

## 体质特征分析

### 气虚质特征

**形体特征**:
- 肌肉松软
- 容易疲乏
- 声音低弱
- 喜静懒言
- 容易出汗

**心理特征**:
- 性格内向
- 不喜冒险
- 情绪不稳定

**发病倾向**:
- 易感冒
- 易内脏下垂
- 易疲劳

**适应能力**:
- 不耐受风、寒、暑、湿邪
- 秋季易发病

### 阳虚质特征

**形体特征**:
- 畏寒怕冷
- 手足不温
- 喜热饮食

**心理特征**:
- 性格多沉静
- 内向

**发病倾向**:
- 易患痰饮、肿胀、腹泻
- 易感寒邪

**适应能力**:
- 不耐寒邪,耐受夏热
- 冬季易发病

---

## 养生建议

### 饮食调养

**原则**: 补气健脾,温补肾阳

**宜食食物**:
- 补气类: 山药、大枣、黄芪、人参、白术
- 温阳类: 羊肉、韭菜、花椒、生姜、桂圆
- 健脾类: 薏苡仁、茯苓、扁豆

**忌食食物**:
- 生冷寒凉: 冰淇淋、冰镇饮料、生鱼片
- 油腻厚味: 油炸食品、肥肉
- 辛辣燥热: 辣椒、花椒

**推荐食谱**:
1. 黄芪炖鸡
2. 山药粥
3. 红枣茯苓粥
4. 当归生姜羊肉汤

**饮食建议**:
- 少食多餐,细嚼慢咽
- 饮食宜温热,忌生冷
- 饭后适当休息

### 起居调摄

**作息建议**:
- 保证充足睡眠(8小时以上)
- 早睡晚起
- 避免熬夜

**环境要求**:
- 保持环境温暖干燥
- 避免受风寒
- 注意保暖,特别是腰腹部和脚部

**生活习惯**:
- 避免过度劳累
- 劳逸结合
- 可适当晒太阳
- 温水泡脚

### 运动锻炼

**原则**: 温和运动,避免剧烈

**推荐运动**:
- 太极拳
- 八段锦
- 散步
- 气功
- 瑜伽

**运动建议**:
- 频率: 每日1-2次
- 时长: 每次20-30分钟
- 强度: 低至中等强度
- 注意: 以不感到过度疲劳为宜

**注意事项**:
- 避免剧烈运动
- 运动后及时休息
- 循序渐进
- 避免在寒冷环境中运动

### 情志调摄

**原则**: 保持心情舒畅,避免过度思虑

**调摄方法**:
- 保持积极乐观
- 避免过度思虑
- 适当参加社交活动
- 学会放松

**情绪管理**:
- 培养兴趣爱好
- 保持社交活动
- 学会调节情绪

### 穴位保健

**推荐穴位**:

#### 1. 足三里
- **位置**: 小腿外侧,膝眼下3寸
- **功效**: 健脾益气,强壮身体
- **方法**: 每日按揉3-5分钟,可艾灸

#### 2. 气海
- **位置**: 肚脐下1.5寸
- **功效**: 培补元气
- **方法**: 每日按揉3-5分钟,可艾灸

#### 3. 关元
- **位置**: 肚脐下3寸
- **功效**: 培元固本,温补肾阳
- **方法**: 每日按揉3-5分钟,可艾灸10-15分钟

### 中药调理

⚠️ **重要提醒**: 以下内容仅供中医师参考,不可自行抓药服用

**推荐方剂**: 四君子汤加减

**方源**: 《太平惠民和剂局方》

**方剂组成**:
- 人参: 9-15g, 大补元气
- 白术: 9-12g, 健脾益气
- 茯苓: 9-15g, 健脾渗湿
- 甘草: 6-9g, 调和诸药

**随症加减**:
- 气虚重者: 加黄芪 15-30g
- 脾虚湿盛者: 加薏苡仁 15-30g, 扁豆 10-15g
- 食少腹胀者: 加陈皮 6-9g, 砂仁 3-6g

**用法**: 水煎服,日一剂,分早晚两次温服

**注意事项**:
- ⚠️ 需经专业中医师辨证后使用
- ⚠️ 孕妇、儿童、体弱者需医师指导
- ⚠️ 服药期间忌食生冷、油腻、辛辣食物
- ⚠️ 感冒发烧时暂停服用
- ⚠️ 服用期间出现不良反应立即停用并就医

---

## 季节调养建议

### 春季调养
- 养阳为主,顺应生发之气
- 多食韭菜、菠菜、山药
- 保持心情舒畅,适当运动
- 注意防风保暖

### 夏季调养
- 清暑热,养心神
- 多食绿豆、冬瓜、苦瓜
- 注意防暑降温
- 保持心情平和

### 秋季调养
- 养收润燥,养肺
- 多食银耳、百合、梨
- 注意保暖,避免受凉
- 保持情绪稳定

### 冬季调养
- 养藏为主,温补肾阳
- 多食羊肉、核桃、栗子
- 注意保暖,特别是腰腹部
- 早睡晚起,避免过度劳累

---

## 与其他健康指标的关联

### 体质与营养
- 气虚质、阳虚质: 宜温补饮食
- 阴虚质、湿热质: 宜清淡饮食
- 痰湿质: 宜低脂低糖,控制体重

### 体质与运动
- 气虚质、阳虚质: 温和运动为主
- 湿热质、痰湿质: 适度加强运动强度
- 阴虚质: 避免剧烈运动

### 体质与睡眠
- 气虚质、阳虚质: 保证充足睡眠
- 阴虚质: 避免熬夜
- 气郁质: 疏肝解郁,改善睡眠质量

### 体质与慢性病
- 痰湿质: 易患高血压、糖尿病、高脂血症
- 湿热质: 易患代谢综合征
- 血瘀质: 易患心血管疾病
- 气郁质: 易患抑郁症、焦虑症

---

## 医学安全边界

⚠️ **重要声明**

本分析仅供健康参考,不构成医疗诊断或治疗建议。

### 分析能力范围

✅ **能做到**:
- 中医体质辨识评估
- 体质特征分析
- 一般性养生建议
- 中医知识普及
- 体质趋势追踪

❌ **不做到**:
- 中医疾病诊断
- 中药处方开具
- 替代中医师诊疗
- 针灸等治疗操作
- 处理严重健康问题

### 危险信号检测

在分析过程中检测以下危险信号:

1. **严重体质偏颇**:
   - 单一偏颇体质得分 > 80分
   - 多种偏颇体质兼夹

2. **健康风险提示**:
   - 痰湿质 → 高血压、糖尿病风险
   - 湿热质 → 代谢综合征风险
   - 血瘀质 → 心血管疾病风险
   - 气郁质 → 抑郁症风险

3. **就医引导**:
   - 疑似疾病症状 → 建议就医
   - 需要中药治疗 → 咨询中医师
   - 体质调理无效 → 寻求专业帮助

### 建议分级

**Level 1: 一般性建议**
- 基于中医体质理论
- 适用于一般人群
- 无需医疗监督

**Level 2: 参考性建议**
- 基于用户体质和健康状况
- 需结合个人情况
- 建议咨询中医师

**Level 3: 医疗建议**
- 涉及中药调理
- 需中医师确认
- 不得自行服用中药

---

## 数据结构

### 体质评估记录

```json
{
  "date": "2025-06-20",
  "questionnaire": {
    "questions": [
      {
        "id": 1,
        "constitution": "气虚质",
        "question": "您容易疲乏吗?",
        "answer": 4,
        "weight": 1.0
      }
    ],
    "total_questions": 60
  },
  "results": {
    "primary_constitution": "气虚质",
    "secondary_constitutions": ["阳虚质"],
    "constitution_scores": {
      "平和质": 42.1,
      "气虚质": 78.5,
      "阳虚质": 62.3,
      "阴虚质": 32.1,
      "痰湿质": 38.7,
      "湿热质": 28.4,
      "血瘀质": 25.6,
      "气郁质": 35.2,
      "特禀质": 18.3
    },
    "constitution_type": "compound"
  },
  "characteristics": {
    "physical": ["容易疲劳", "气短", "自汗"],
    "psychological": ["性格内向", "不喜欢说话"]
  },
  "recommendations": {
    "diet": {
      "principles": ["补气健脾", "温补肾阳"],
      "beneficial": ["山药", "大枣", "黄芪"],
      "avoid": ["生冷寒凉", "油腻厚味"]
    },
    "exercise": "温和运动,如太极拳、散步",
    "lifestyle": "规律作息,避免过度劳累",
    "acupoints": ["足三里", "气海", "关元"]
  }
}
```

---

## 参考资源

### 中医体质理论
- 《中医体质分类与判定》标准
- 王琦九种体质学说
- 《中医体质学》教材

### 养生原则
- 中医基础理论
- 四季养生原则
- 辨证施治原则

### 中药方剂
- 《方剂学》教材
- 《太平惠民和剂局方》
- 《金匮要略》

---

**技能版本**: v1.0
**创建日期**: 2026-01-08
**维护者**: WellAlly Tech

---

## Merged Reference (legacy variant)

---
name: threejs-fundamentals
description: Three.js scene setup, cameras, renderer, Object3D hierarchy, coordinate systems. Use when setting up 3D scenes, creating cameras, configuring renderers, managing object hierarchies, or working with transforms.
---

# Three.js Fundamentals

## Quick Start

```javascript
import * as THREE from "three";

// Create scene, camera, renderer
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(
  75,
  window.innerWidth / window.innerHeight,
  0.1,
  1000,
);
const renderer = new THREE.WebGLRenderer({ antialias: true });

renderer.setSize(window.innerWidth, window.innerHeight);
renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
document.body.appendChild(renderer.domElement);

// Add a mesh
const geometry = new THREE.BoxGeometry(1, 1, 1);
const material = new THREE.MeshStandardMaterial({ color: 0x00ff00 });
const cube = new THREE.Mesh(geometry, material);
scene.add(cube);

// Add light
scene.add(new THREE.AmbientLight(0xffffff, 0.5));
const dirLight = new THREE.DirectionalLight(0xffffff, 1);
dirLight.position.set(5, 5, 5);
scene.add(dirLight);

camera.position.z = 5;

// Animation loop
function animate() {
  requestAnimationFrame(animate);
  cube.rotation.x += 0.01;
  cube.rotation.y += 0.01;
  renderer.render(scene, camera);
}
animate();

// Handle resize
window.addEventListener("resize", () => {
  camera.aspect = window.innerWidth / window.innerHeight;
  camera.updateProjectionMatrix();
  renderer.setSize(window.innerWidth, window.innerHeight);
});
```

## Core Classes

### Scene

Container for all 3D objects, lights, and cameras.

```javascript
const scene = new THREE.Scene();
scene.background = new THREE.Color(0x000000); // Solid color
scene.background = texture; // Skybox texture
scene.background = cubeTexture; // Cubemap
scene.environment = envMap; // Environment map for PBR
scene.fog = new THREE.Fog(0xffffff, 1, 100); // Linear fog
scene.fog = new THREE.FogExp2(0xffffff, 0.02); // Exponential fog
```

### Cameras

**PerspectiveCamera** - Most common, simulates human eye.

```javascript
// PerspectiveCamera(fov, aspect, near, far)
const camera = new THREE.PerspectiveCamera(
  75, // Field of view (degrees)
  window.innerWidth / window.innerHeight, // Aspect ratio
  0.1, // Near clipping plane
  1000, // Far clipping plane
);

camera.position.set(0, 5, 10);
camera.lookAt(0, 0, 0);
camera.updateProjectionMatrix(); // Call after changing fov, aspect, near, far
```

**OrthographicCamera** - No perspective distortion, good for 2D/isometric.

```javascript
// OrthographicCamera(left, right, top, bottom, near, far)
const aspect = window.innerWidth / window.innerHeight;
const frustumSize = 10;
const camera = new THREE.OrthographicCamera(
  (frustumSize * aspect) / -2,
  (frustumSize * aspect) / 2,
  frustumSize / 2,
  frustumSize / -2,
  0.1,
  1000,
);
```

**ArrayCamera** - Multiple viewports with sub-cameras.

```javascript
const cameras = [];
for (let i = 0; i < 4; i++) {
  const subcamera = new THREE.PerspectiveCamera(40, 1, 0.1, 100);
  subcamera.viewport = new THREE.Vector4(
    Math.floor(i % 2) * 0.5,
    Math.floor(i / 2) * 0.5,
    0.5,
    0.5,
  );
  cameras.push(subcamera);
}
const arrayCamera = new THREE.ArrayCamera(cameras);
```

**CubeCamera** - Renders environment maps for reflections.

```javascript
const cubeRenderTarget = new THREE.WebGLCubeRenderTarget(256);
const cubeCamera = new THREE.CubeCamera(0.1, 1000, cubeRenderTarget);
scene.add(cubeCamera);

// Use for reflections
material.envMap = cubeRenderTarget.texture;

// Update each frame (expensive!)
cubeCamera.position.copy(reflectiveMesh.position);
cubeCamera.update(renderer, scene);
```

### WebGLRenderer

```javascript
const renderer = new THREE.WebGLRenderer({
  canvas: document.querySelector("#canvas"), // Optional existing canvas
  antialias: true, // Smooth edges
  alpha: true, // Transparent background
  powerPreference: "high-performance", // GPU hint
  preserveDrawingBuffer: true, // For screenshots
});

renderer.setSize(width, height);
renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));

// Tone mapping
renderer.toneMapping = THREE.ACESFilmicToneMapping;
renderer.toneMappingExposure = 1.0;

// Color space (Three.js r152+)
renderer.outputColorSpace = THREE.SRGBColorSpace;

// Shadows
renderer.shadowMap.enabled = true;
renderer.shadowMap.type = THREE.PCFSoftShadowMap;

// Clear color
renderer.setClearColor(0x000000, 1);

// Render
renderer.render(scene, camera);
```

### Object3D

Base class for all 3D objects. Mesh, Group, Light, Camera all extend Object3D.

```javascript
const obj = new THREE.Object3D();

// Transform
obj.position.set(x, y, z);
obj.rotation.set(x, y, z); // Euler angles (radians)
obj.quaternion.set(x, y, z, w); // Quaternion rotation
obj.scale.set(x, y, z);

// Local vs World transforms
obj.getWorldPosition(targetVector);
obj.getWorldQuaternion(targetQuaternion);
obj.getWorldDirection(targetVector);

// Hierarchy
obj.add(child);
obj.remove(child);
obj.parent;
obj.children;

// Visibility
obj.visible = false;

// Layers (for selective rendering/raycasting)
obj.layers.set(1);
obj.layers.enable(2);
obj.layers.disable(0);

// Traverse hierarchy
obj.traverse((child) => {
  if (child.isMesh) child.material.color.set(0xff0000);
});

// Matrix updates
obj.matrixAutoUpdate = true; // Default: auto-update matrices
obj.updateMatrix(); // Manual matrix update
obj.updateMatrixWorld(true); // Update world matrix recursively
```

### Group

Empty container for organizing objects.

```javascript
const group = new THREE.Group();
group.add(mesh1);
group.add(mesh2);
scene.add(group);

// Transform entire group
group.position.x = 5;
group.rotation.y = Math.PI / 4;
```

### Mesh

Combines geometry and material.

```javascript
const mesh = new THREE.Mesh(geometry, material);

// Multiple materials (one per geometry group)
const mesh = new THREE.Mesh(geometry, [material1, material2]);

// Useful properties
mesh.geometry;
mesh.material;
mesh.castShadow = true;
mesh.receiveShadow = true;

// Frustum culling
mesh.frustumCulled = true; // Default: skip if outside camera view

// Render order
mesh.renderOrder = 10; // Higher = rendered later
```

## Coordinate System

Three.js uses a **right-handed coordinate system**:

- **+X** points right
- **+Y** points up
- **+Z** points toward viewer (out of screen)

```javascript
// Axes helper
const axesHelper = new THREE.AxesHelper(5);
scene.add(axesHelper); // Red=X, Green=Y, Blue=Z
```

## Math Utilities

### Vector3

```javascript
const v = new THREE.Vector3(x, y, z);
v.set(x, y, z);
v.copy(otherVector);
v.clone();

// Operations (modify in place)
v.add(v2);
v.sub(v2);
v.multiply(v2);
v.multiplyScalar(2);
v.divideScalar(2);
v.normalize();
v.negate();
v.clamp(min, max);
v.lerp(target, alpha);

// Calculations (return new value)
v.length();
v.lengthSq(); // Faster than length()
v.distanceTo(v2);
v.dot(v2);
v.cross(v2); // Modifies v
v.angleTo(v2);

// Transform
v.applyMatrix4(matrix);
v.applyQuaternion(q);
v.project(camera); // World to NDC
v.unproject(camera); // NDC to world
```

### Matrix4

```javascript
const m = new THREE.Matrix4();
m.identity();
m.copy(other);
m.clone();

// Build transforms
m.makeTranslation(x, y, z);
m.makeRotationX(theta);
m.makeRotationY(theta);
m.makeRotationZ(theta);
m.makeRotationFromQuaternion(q);
m.makeScale(x, y, z);

// Compose/decompose
m.compose(position, quaternion, scale);
m.decompose(position, quaternion, scale);

// Operations
m.multiply(m2); // m = m * m2
m.premultiply(m2); // m = m2 * m
m.invert();
m.transpose();

// Camera matrices
m.makePerspective(left, right, top, bottom, near, far);
m.makeOrthographic(left, right, top, bottom, near, far);
m.lookAt(eye, target, up);
```

### Quaternion

```javascript
const q = new THREE.Quaternion();
q.setFromEuler(euler);
q.setFromAxisAngle(axis, angle);
q.setFromRotationMatrix(matrix);

q.multiply(q2);
q.slerp(target, t); // Spherical interpolation
q.normalize();
q.invert();
```

### Euler

```javascript
const euler = new THREE.Euler(x, y, z, "XYZ"); // Order matters!
euler.setFromQuaternion(q);
euler.setFromRotationMatrix(m);

// Rotation orders: 'XYZ', 'YXZ', 'ZXY', 'XZY', 'YZX', 'ZYX'
```

### Color

```javascript
const color = new THREE.Color(0xff0000);
const color = new THREE.Color("red");
const color = new THREE.Color("rgb(255, 0, 0)");
const color = new THREE.Color("#ff0000");

color.setHex(0x00ff00);
color.setRGB(r, g, b); // 0-1 range
color.setHSL(h, s, l); // 0-1 range

color.lerp(otherColor, alpha);
color.multiply(otherColor);
color.multiplyScalar(2);
```

### MathUtils

```javascript
THREE.MathUtils.clamp(value, min, max);
THREE.MathUtils.lerp(start, end, alpha);
THREE.MathUtils.mapLinear(value, inMin, inMax, outMin, outMax);
THREE.MathUtils.degToRad(degrees);
THREE.MathUtils.radToDeg(radians);
THREE.MathUtils.randFloat(min, max);
THREE.MathUtils.randInt(min, max);
THREE.MathUtils.smoothstep(x, min, max);
THREE.MathUtils.smootherstep(x, min, max);
```

## Common Patterns

### Proper Cleanup

```javascript
function dispose() {
  // Dispose geometries
  mesh.geometry.dispose();

  // Dispose materials
  if (Array.isArray(mesh.material)) {
    mesh.material.forEach((m) => m.dispose());
  } else {
    mesh.material.dispose();
  }

  // Dispose textures
  texture.dispose();

  // Remove from scene
  scene.remove(mesh);

  // Dispose renderer
  renderer.dispose();
}
```

### Clock for Animation

```javascript
const clock = new THREE.Clock();

function animate() {
  const delta = clock.getDelta(); // Time since last frame (seconds)
  const elapsed = clock.getElapsedTime(); // Total time (seconds)

  mesh.rotation.y += delta * 0.5; // Consistent speed regardless of framerate

  requestAnimationFrame(animate);
  renderer.render(scene, camera);
}
```

### Responsive Canvas

```javascript
function onWindowResize() {
  const width = window.innerWidth;
  const height = window.innerHeight;

  camera.aspect = width / height;
  camera.updateProjectionMatrix();

  renderer.setSize(width, height);
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
}
window.addEventListener("resize", onWindowResize);
```

### Loading Manager

```javascript
const manager = new THREE.LoadingManager();

manager.onStart = (url, loaded, total) => console.log("Started loading");
manager.onLoad = () => console.log("All loaded");
manager.onProgress = (url, loaded, total) => console.log(`${loaded}/${total}`);
manager.onError = (url) => console.error(`Error loading ${url}`);

const textureLoader = new THREE.TextureLoader(manager);
const gltfLoader = new GLTFLoader(manager);
```

## Performance Tips

1. **Limit draw calls**: Merge geometries, use instancing, atlas textures
2. **Frustum culling**: Enabled by default, ensure bounding boxes are correct
3. **LOD (Level of Detail)**: Use `THREE.LOD` for distance-based mesh switching
4. **Object pooling**: Reuse objects instead of creating/destroying
5. **Avoid `getWorldPosition` in loops**: Cache results

```javascript
// Merge static geometries
import { mergeGeometries } from "three/examples/jsm/utils/BufferGeometryUtils.js";
const merged = mergeGeometries([geo1, geo2, geo3]);

// LOD
const lod = new THREE.LOD();
lod.addLevel(highDetailMesh, 0);
lod.addLevel(medDetailMesh, 50);
lod.addLevel(lowDetailMesh, 100);
scene.add(lod);
```

## See Also

- `threejs-geometry` - Geometry creation and manipulation
- `threejs-materials` - Material types and properties
- `threejs-lighting` - Light types and shadows

---

## Merged Reference (legacy variant)

---
name: travel-health-analyzer
description: 分析旅行健康数据、评估目的地健康风险、提供疫苗接种建议、生成多语言紧急医疗信息卡片。支持WHO/CDC数据集成的专业级旅行健康风险评估。
allowed-tools: Read, Write, Grep, Glob
---

# 旅行健康分析技能

## 🚨 重要医学免责声明

**本技能提供的所有健康建议和信息仅供参考,不能替代专业医疗建议。**

- ⚠️ **所有建议必须由专业医生审核**
- ⚠️ **疫苗接种和用药方案必须由医生制定**
- ⚠️ **不提供具体的医疗处方或诊断**
- ⚠️ **健康风险数据来源于WHO/CDC,可能存在滞后性**
- ⚠️ **紧急情况下请立即就医**

---

## 技能功能

### 1. 旅行健康规划分析

分析用户的旅行计划,提供全面的健康准备建议。

**输入**: 旅行目的地、日期、旅行目的
**输出**:
- 目的地健康风险评估
- 必要和推荐的疫苗接种清单
- 旅行药箱建议清单
- 预防措施建议
- 旅行前准备时间表

**分析要点**:
- 识别目的地传染病风险
- 评估食物和饮水安全
- 确认环境风险(高温、高原等)
- 检查当前疫情爆发信息
- 提供WHO/CDC参考链接

---

### 2. 目的地健康风险评估

基于WHO/CDC数据,对旅行目的地进行专业级健康风险评估。

**数据源**:
- 世界卫生组织(WHO)国际旅行健康
- 美国疾控中心(CDC)旅行健康
- 当地卫生部门官方数据

**评估维度**:
- 传染病风险(登革热、疟疾、霍乱、甲肝等)
- 食物和饮水安全
- 环境风险(高温、高原、空气污染)
- 季节性风险
- 当前疫情爆发警报

**风险等级**:
- 🟢 **低风险** - 常规预防措施
- 🟡 **中等风险** - 需要特别注意
- 🔴 **高风险** - 需要采取严格预防措施
- ⚫ **极高风险** - 建议推迟旅行或采取特殊防护

**输出格式**:
```markdown
## 目的地健康风险评估: Thailand

### 传染病风险
#### 🔴 登革热 - 高风险
- **传播方式**: 蚊子叮咬
- **季节性**: 全年
- **症状**: 高热、头痛、肌肉关节痛、皮疹
- **预防**: 使用防蚊液、穿长袖衣物、住宿选择有空调房间
- **数据源**: [WHO](https://www.who.int/ith) | [CDC](https://www.cdc.gov/dengue)

### 食物饮水安全
#### 🟡 中等风险
- 饮用瓶装水或煮沸的水
- 避免冰块
- 避免生食
- 水果自己剥皮

### 当前疫情警报
暂无重大疫情爆发警报
```

---

### 3. 疫苗接种需求分析

根据目的地和旅行计划,分析疫苗接种需求。

**分析内容**:
- 必需疫苗接种(如黄热病)
- 推荐疫苗接种(如甲肝、伤寒)
- 疫苗接种时间规划
- 疫苗相互作用检查
- 接种禁忌症评估

**疫苗清单模板**:
```json
{
  "vaccine": "甲肝疫苗",
  "status": "completed|planned|not_required|contraindicated",
  "date": "2025-06-15",
  "booster_required": false,
  "notes": "已完成接种,提供长期保护"
}
```

**时间规划原则**:
- 出发前4-6周:完成必需疫苗接种
- 出发前2-4周:完成推荐疫苗接种
- 某些疫苗需要多次接种,需提前规划

---

### 4. 旅行药箱智能建议

根据目的地健康风险和个人健康状况,生成个性化旅行药箱清单。

**药箱分类**:

#### 处方药
- 个人慢性病用药(足量+额外)
- 疟疾预防用药(如需要)
- 其他医生开具的旅行用药

#### 非处方药
- 止泻药(洛哌丁胺)
- 口服补液盐
- 退烧止痛药(对乙酰氨基酚/布洛芬)
- 抗过敏药(氯雷他定)
- 晕车药
- 抗酸药

#### 防护用品
- 防蚊液(DEET 20-30%)
- 防晒霜(SPF 50+)
- 口罩(N95)

#### 急救用品
- 创可贴
- 消毒液
- 纱布和绷带
- 体温计
- 小剪刀和镊子

**个性化建议**:
- 根据个人疾病史调整用药
- 根据目的地风险增减物品
- 考虑旅行时长和活动类型

---

### 5. 用药相互作用检查

检查旅行用药与个人慢性病用药之间的潜在相互作用。

**检查内容**:
- 疟疾预防用药 vs 慢性病用药
- 旅行期间临时用药 vs 常规用药
- 疫苗 vs 药物相互作用
- 食物 vs 药物相互作用

**常见相互作用**:
- 多西环素 vs 抗酸药、钙铁补充剂
- 甲氟喹 vs 某些心脏病药物
- 某些抗生素 vs 口服避孕药

**输出**:
```markdown
## 用药相互作用检查结果

### ⚠️ 发现潜在相互作用

**多西环素 ↔ 抗酸药**
- **影响**: 抗酸药降低多西环素吸收
- **建议**: 间隔2小时服用
- **严重程度**: 中等

### ✅ 无相互作用
- 氨氯地平 vs 旅行用药无已知相互作用
```

---

### 6. 多语言紧急信息卡片生成

生成包含关键医疗信息的多语言紧急卡片。

**支持语言**:
- 英语 (en)
- 中文 (zh)
- 日语 (ja)
- 韩语 (ko)
- 法语 (fr)
- 西班牙语 (es)
- 泰语 (th)
- 越南语 (vi)

**卡片内容**:
```markdown
---
紧急医疗信息 | EMERGENCY MEDICAL INFORMATION
---

姓名: 张三 | Name: Zhang San
血型: A+ | Blood Type: A+
出生日期: 1990-01-01 | DOB: 1990-01-01

⚠️ 过敏史 | ALLERGIES
- 青霉素 (严重: 皮疹、呼吸困难) | Penicillin (Severe: Rash, Difficulty breathing)

当前用药 | CURRENT MEDICATIONS
- 氨氯地平 5mg 每日一次 (控制血压) | Amlodipine 5mg Once daily (Blood pressure)

疾病史 | MEDICAL CONDITIONS
- 高血压 (控制中) | Hypertension (Controlled)

紧急联系人 | EMERGENCY CONTACT
- 配偶: 李四 +86-138-1234-5678 | Spouse: Li Si +86-138-1234-5678
- 医生: 王医生 +86-10-8765-4321 | Doctor: Dr. Wang +86-10-8765-4321

---
[二维码: 扫描查看完整医疗记录]
[QR Code: Scan for complete medical records]
---
```

**二维码功能**:
- 编码关键医疗信息摘要
- 云端访问链接(模拟)
- 支持离线访问
- 可分享给医护人员

---

### 7. 旅行前后健康检查

#### 旅行前健康检查

**检查内容**:
- 个人健康状况评估
- 慢性病病情确认
- 用药充足性检查
- 疫苗接种确认
- 健康建议

**输出**:
```markdown
## 旅行前健康检查报告

### 整体评估: ✅ 适合旅行

### 健康状况
- 血压: 控制良好
- 慢性病: 稳定
- 用药: 充足

### 准备完成度
- ✅ 疫苗接种: 已完成
- ✅ 旅行药箱: 已准备
- ✅ 保险: 已购买
- ⚠️ 紧急卡片: 待生成

### 建议
1. 生成多语言紧急卡片
2. 携带足量慢性病用药
3. 旅行期间注意血压监测
```

#### 旅行后健康监测

**监测内容**:
- 发热监测(持续2-4周)
- 消化系统症状
- 皮肤异常
- 其他不适症状

**潜伏期疾病提醒**:
- 疟疾: 可在返回后数月内发病
- 登革热: 通常3-14天
- 伤寒: 1-3周
- 甲肝: 2-6周

---

## 数据文件操作

### 读取数据
```bash
# 读取旅行健康数据
Read: data/travel-health-tracker.json

# 读取示例数据
Read: data-example/travel-health-tracker.json
```

### 写入数据
```bash
# 更新旅行计划
Write: data/travel-health-tracker.json

# 保存健康检查日志
Write: data/travel-health-logs/pre-trip-assessment-YYYY-MM-DD.json
```

### 数据结构验证
- 验证必需字段存在
- 验证日期格式正确
- 验证枚举值有效
- 验证数据完整性

---

## WHO/CDC数据集成

### 静态数据库(当前实现)

内置常见旅行目的地健康风险数据:
- 东南亚: 登革热、甲肝、伤寒、疟疾
- 非洲: 疟疾、黄热病、霍乱、脑膜炎
- 南美: 登革热、黄热病、寨卡病毒
- 中东: 中东呼吸综合征(MERS)

**数据更新**: 手动更新,建议每季度更新一次

### 动态查询(未来扩展)

计划集成:
- WHO疫情新闻RSS订阅
- CDC Travel Health API
- 当地卫生部门疫情通报

---

## 输出格式

### 报告格式
- Markdown格式,便于阅读
- 结构化,便于程序处理
- 包含数据源引用
- 包含时间戳

### 日志格式
```json
{
  "log_id": "log_20250728_pretrip",
  "log_type": "pre_trip_assessment",
  "trip_id": "trip_20250801_seasia",
  "generated_at": "2025-07-28T10:00:00.000Z",
  "assessment_results": {
    "health_status": "suitable_for_travel",
    "vaccination_status": "completed",
    "risk_assessment": {...},
    "recommendations": [...]
  }
}
```

---

## 安全和隐私

### 数据保护
- 护照号码加密存储
- 二维码不包含完整敏感信息
- 支持数据导出和删除

### 医学安全
- 所有建议包含免责声明
- 强调医生咨询的必要性
- 不提供具体处方
- 引用权威数据源

---

## 使用示例

### 分析旅行计划
```
输入: "计划2025年8月去东南亚旅游14天"

输出:
1. 目的地健康风险评估
2. 疫苗接种建议
3. 旅行药箱清单
4. 预防措施
5. 时间表
```

### 生成紧急卡片
```
输入: "生成英中日泰四语紧急卡片"

输出:
1. 多语言卡片文本
2. 二维码(描述)
3. 保存建议
```

### 评估健康风险
```
输入: "评估泰国的健康风险"

输出:
1. 传染病风险清单
2. 食物饮水安全建议
3. 环境风险
4. 当前疫情警报
5. WHO/CDC参考链接
```

---

**版本**: v1.0.0
**最后更新**: 2025-01-08
**维护者**: WellAlly Tech

---

## Merged Reference (legacy variant)

---
name: weightloss-analyzer
description: 分析减肥数据、计算代谢率、追踪能量缺口、管理减肥阶段
---

# 减肥分析技能

分析减肥数据，计算代谢率，追踪能量缺口，管理减肥阶段。

## 功能

### 1. 身体成分分析

**BMI计算与分类**
- BMI = 体重(kg) / 身高(m)²
- 分类标准（WHO亚洲标准）：
  - 偏瘦：BMI < 18.5
  - 正常：18.5 ≤ BMI < 24
  - 超重：24 ≤ BMI < 28
  - 肥胖：BMI ≥ 28

**体脂率评估**
- 男性：15-20%（正常），20-25%（偏高），>25%（肥胖）
- 女性：20-25%（正常），25-30%（偏高），>30%（肥胖）

**围度分析**
- 腰围评估
  - 男性：< 90cm（正常），≥ 90cm（腹部肥胖）
  - 女性：< 85cm（正常），≥ 85cm（腹部肥胖）
- 腰臀比
  - 男性：< 0.9（正常），≥ 0.9（腹部肥胖）
  - 女性：< 0.85（正常），≥ 0.85（腹部肥胖）

**理想体重计算**
- BMI法：理想体重 = 身高(m)² × 22
- Broca法修正：理想体重 = (身高cm - 100) × 0.9

### 2. 代谢率计算

**Harris-Benedict公式（1919原始版）**
- 男性：BMR = 88.362 + (13.397 × 体重kg) + (4.799 × 身高cm) - (5.677 × 年龄)
- 女性：BMR = 447.593 + (9.247 × 体重kg) + (3.098 × 身高cm) - (4.330 × 年龄)

**Mifflin-St Jeor公式（推荐，更准确）**
- 男性：BMR = (10 × 体重kg) + (6.25 × 身高cm) - (5 × 年龄) + 5
- 女性：BMR = (10 × 体重kg) + (6.25 × 身高cm) - (5 × 年龄) - 161

**Katch-McArdle公式（基于瘦体重）**
- BMR = 370 + (21.6 × 瘦体重kg)
- 瘦体重 = 体重kg × (1 - 体脂率)

**TDEE计算**
- TDEE = BMR × 活动系数
- 活动系数：
  - 久坐：1.2
  - 轻度活动：1.375
  - 中度活动：1.55
  - 高度活动：1.725
  - 非常高度活动：1.9

### 3. 能量缺口管理

**每日能量缺口追踪**
- 缺口 = TDEE - 实际摄入 + 运动消耗
- 缺口达标分析：实际缺口 vs 目标缺口

**减重估算**
- 1kg脂肪 ≈ 7700大卡
- 预计周减重 = 每日缺口 × 7 / 7700
- 安全减重速度：0.5-1kg/周（缺口500-1000大卡/天）

**热量安全边界**
- 男性最低热量：1500大卡/天
- 女性最低热量：1200大卡/天
- 绝对最低：BMR × 1.2

### 4. 阶段管理

**减重期**
- 追踪体重变化
- 计算减重进度
- 监测减重速度

**平台期检测**
- 定义：2周以上体重无明显变化（波动<0.5kg）
- 原因分析：代谢适应、水分滞留、肌肉增加
- 突破方法：调整热量、改变运动、间歇性断食

**维持期**
- 目标体重±2kg范围内
- 定期监测体重
- 及时调整方案

## 数据源

### 主要数据源

1. **健身追踪器**
   - 路径：`data/fitness-tracker.json`
   - 内容：体重记录、身体成分、代谢率、阶段管理

2. **营养追踪器**
   - 路径：`data/nutrition-tracker.json`
   - 内容：热量摄入、能量缺口、膳食计划

3. **健康日志**
   - 路径：`data/health-logs/YYYY-MM/YYYY-MM-DD.json`
   - 内容：每日体重、饮食记录

## 输出格式

### 身体成分分析报告

```markdown
# 身体成分分析报告

## 基本信息
- 性别：男
- 年龄：52岁
- 身高：175cm
- 体重：75kg

## 身体指标

### BMI
- 当前BMI：24.5
- 分类：超重
- 理想体重：67kg（BMI=22）
- 需减重：8kg

### 体脂率
- 当前体脂率：25%
- 分类：偏高
- 目标体脂率：15-20%

### 围度分析
- 腰围：92cm（腹部肥胖风险）
- 臀围：98cm
- 腰臀比：0.94（腹部肥胖）

## 建议
1. 每周减重0.5-1kg
2. 目标减重时间：8-16周
3. 综合干预：饮食+运动
```

### 代谢率分析报告

```markdown
# 代谢率分析报告

## BMR计算

| 公式 | BMR | 说明 |
|------|-----|------|
| Harris-Benedict | 1650 | 1919原始公式 |
| Mifflin-St Jeor | 1620 | 推荐使用 ⭐ |
| Katch-McArdle | 1700 | 基于体脂率 |

**推荐BMR：1620 大卡/天**

## TDEE计算

- 活动水平：中度运动
- 活动系数：1.55
- TDEE：1620 × 1.55 = **2511 大卡/天**

### 热量分配
- BMR基础代谢：65% ≈ 1632 大卡
- 运动消耗：20% ≈ 502 大卡
- NEAT日常活动：15% ≈ 377 大卡

## 减肥热量目标

### 温和减重方案
- 每日缺口：500 大卡
- 目标摄入：2011 大卡/天
- 预计减重：0.5kg/周

### 积极减重方案
- 每日缺口：750 大卡
- 目标摄入：1761 大卡/天
- 预计减重：0.75kg/周

### 快速减重方案
- 每日缺口：1000 大卡
- 目标摄入：1511 大卡/天
- 预计减重：1kg/周
- ⚠️ 仅限短期使用

## 安全检查
- 最低热量要求：1500 大卡/天（男性）
- 快速方案热量：1511 大卡/天 ✅
- 建议选择：温和或积极方案
```

### 能量缺口追踪报告

```markdown
# 能量缺口追踪报告

## 本周汇总（2025-06-16 至 2025-06-22）

| 日期 | 摄入 | 运动消耗 | NEAT | 缺口 | 达标 |
|------|------|---------|------|------|------|
| 周一 | 1800 | 350 | 300 | 961 | ✅ |
| 周二 | 2100 | 200 | 250 | 461 | ❌ |
| 周三 | 1750 | 400 | 300 | 1061 | ✅ |
| 周四 | 1950 | 300 | 280 | 741 | ✅ |
| 周五 | 2200 | 150 | 200 | 261 | ❌ |
| 周六 | 2400 | 100 | 150 | -89 | ❌ |
| 周日 | 1850 | 350 | 300 | 911 | ✅ |

**目标缺口：500 大卡/天**

## 统计分析
- 平均缺口：642 大卡/天
- 达标天数：5/7天（71%）
- 总缺口：4494 大卡
- 预计减重：0.58kg

## 趋势分析
- 周末缺口偏小（社交活动增加）
- 建议提前规划周末饮食

## 下周目标
- 达标天数：7/7天
- 平均缺口：700 大卡/天
- 预计减重：0.64kg
```

### 阶段管理报告

```markdown
# 减肥阶段管理报告

## 当前阶段：减重期

### 进度追踪
- 开始日期：2025-01-01
- 初始体重：82kg
- 当前体重：75kg
- 目标体重：67kg
- 已减重：7kg
- 剩余：8kg
- 进度：47%

### 减重速度
- 总周数：24周
- 平均减重：0.29kg/周
- 最近4周：0.35kg/周 ⬆️ 加速中

## 状态分析

### 当前状态：✅ 良好
- 减重速度在健康范围（0.5-1kg/周）
- 代谢率稳定
- 肌肉量维持良好

### 平台期监测
- 最近2周变化：-0.8kg
- 状态：❌ 非平台期

## 下一步行动
1. 继续当前热量方案
2. 增加力量训练频率
3. 每周监测身体成分
```

## 使用方法

通过 `/fitness:weightloss-*` 和 `/nutrition:weightloss-*` 命令调用。

### 示例命令

```bash
# 设置减肥计划
/fitness:weightloss-setup --weight 75 --height 175 --age 52 --gender male

# 计算代谢率
/fitness:weightloss-bmr --formula mifflin

# 追踪能量缺口
/nutrition:weightloss-track --intake 1800 --exercise 350

# 生成阶段报告
/fitness:weightloss-report

# 检测平台期
/fitness:weightloss-plateau-check
```

## 安全原则

### 热量安全边界
- 不推荐 < 1200大卡/天（女性）
- 不推荐 < 1500大卡/天（男性）
- 绝对最低不低于 BMR × 1.2

### 减重速度控制
- 安全范围：0.5-1kg/周
- 最大不超过：1.5kg/周
- 长期平均：0.5-0.8kg/周

### 医学免责声明

本技能仅供健康参考，不构成医疗建议。

以下情况请咨询医生：
- BMI > 35
- 有心脏病、高血压、糖尿病等慢性病
- 服用处方药物
- 女性怀孕或哺乳期
- 任何健康状况不确定的情况

---

**技能版本**: v1.0
**最后更新**: 2026-01-14
**维护者**: WellAlly Tech

## Source: references/skills/healthcare-workflows/references/legacy/ai-analyzer/SKILL.md

---
name: ai-analyzer
description: AI驱动的综合健康分析系统，整合多维度健康数据、识别异常模式、预测健康风险、提供个性化建议。支持智能问答和AI健康报告生成。
allowed-tools: Read, Grep, Glob, Write
---

# AI健康分析器

基于AI技术的综合健康分析系统，提供智能健康洞察、风险预测和个性化建议。

## 核心功能

### 1. 智能健康分析
- **多维度数据整合**: 整合基础指标、生活方式、心理健康、医疗历史等4类数据源
- **异常模式识别**: 使用CUSUM、Z-score等算法检测异常值和变化点
- **相关性分析**: 计算不同健康指标之间的相关性（皮尔逊、斯皮尔曼）
- **趋势预测**: 基于历史数据进行趋势分析和预测

### 2. 健康风险预测
- **高血压风险**: 基于Framingham风险评分模型
- **糖尿病风险**: 基于ADA糖尿病风险评分标准
- **心血管疾病风险**: 基于ACC/AHA ASCVD指南
- **营养缺乏风险**: 基于RDA达成率和饮食模式分析
- **睡眠障碍风险**: 基于PSQI和睡眠模式分析

### 3. 个性化建议引擎
- **基础个性化**: 基于年龄、性别、BMI、活动水平等静态档案
- **建议分级**: Level 1（一般性）、Level 2（参考性）、Level 3（医疗建议）
- **循证依据**: 基于医学指南和循证医学证据
- **可操作性**: 提供具体、可行的改进建议

### 4. 自然语言交互
- **智能问答**: 支持健康数据查询、趋势分析、相关性查询等
- **上下文理解**: 维护对话历史，支持多轮对话
- **意图识别**: 识别用户查询意图，提供精准回复

### 5. AI健康报告生成
- **综合报告**: 包含所有维度健康数据、AI洞察、风险评估
- **快速摘要**: 关键指标概览、异常警示、主要建议
- **风险评估报告**: 各类疾病风险、风险因素分析、预防措施
- **趋势分析报告**: 多维度趋势、变化点识别、预测分析
- **HTML交互式报告**: ECharts图表、Tailwind CSS样式

## 使用说明

### 触发条件

当用户提到以下场景时，使用此技能：

**通用询问**:
- ✅ "AI分析我的健康状况"
- ✅ "我的健康有什么风险？"
- ✅ "生成AI健康报告"
- ✅ "AI分析所有数据"

**风险预测**:
- ✅ "预测我的高血压风险"
- ✅ "我有糖尿病风险吗？"
- ✅ "评估我的心血管风险"
- ✅ "AI预测健康风险"

**智能问答**:
- ✅ "我的睡眠怎么样？"
- ✅ "运动对我的健康有什么影响？"
- ✅ "我应该如何改善健康状况？"
- ✅ "AI健康助手问答"

**报告生成**:
- ✅ "生成AI健康报告"
- ✅ "创建综合分析报告"
- ✅ "AI风险评估报告"

### 执行步骤

#### 步骤 1: 读取AI配置

```javascript
const aiConfig = readFile('data/ai-config.json');
const aiHistory = readFile('data/ai-history.json');
```

检查AI功能是否启用，验证数据源配置。

#### 步骤 2: 读取用户档案

```javascript
const profile = readFile('data/profile.json');
```

获取基础信息：年龄、性别、身高、体重、BMI等。

#### 步骤 3: 读取健康数据

根据配置的数据源读取相关数据：

```javascript
// 基础健康指标
const indexData = readFile('data/index.json');

// 生活方式数据
const fitnessData = readFile('data-example/fitness-tracker.json');
const sleepData = readFile('data-example/sleep-tracker.json');
const nutritionData = readFile('data-example/nutrition-tracker.json');

// 心理健康数据
const mentalHealthData = readFile('data-example/mental-health-tracker.json');

// 医疗历史
const medications = exists('data/medications.json') ? readFile('data/medications.json') : null;
const allergies = exists('data/allergies.json') ? readFile('data/allergies.json') : null;
```

#### 步骤 4: 数据整合和预处理

整合所有数据源，进行数据清洗、时间对齐和缺失值处理。

#### 步骤 5: 多维度分析

**相关性分析**: 计算睡眠↔情绪、运动↔体重、营养↔生化指标等关联

**趋势分析**: 使用线性回归、移动平均等方法识别趋势方向

**异常检测**: 使用CUSUM、Z-score算法检测异常值和变化点

#### 步骤 6: 风险预测

基于Framingham、ADA、ACC/AHA等标准进行风险预测：

- 高血压风险（10年概率）
- 糖尿病风险（10年概率）
- 心血管疾病风险（10年概率）
- 营养缺乏风险
- 睡眠障碍风险

#### 步骤 7: 生成个性化建议

根据分析结果生成三级建议：

- **Level 1**: 一般性建议（基于标准指南）
- **Level 2**: 参考性建议（基于个人数据）
- **Level 3**: 医疗建议（需医生确认，包含免责声明）

#### 步骤 8: 生成分析报告

**文本报告**: 包含总体评估、风险预测、关键趋势、相关性发现、个性化建议

**HTML报告**: 调用 `scripts/generate_ai_report.py` 生成包含ECharts图表的交互式报告

#### 步骤 9: 更新AI历史记录

记录分析结果到 `data/ai-history.json`

## 数据源

| 数据源 | 文件路径 | 数据内容 |
|--------|---------|---------|
| 用户档案 | `data/profile.json` | 年龄、性别、身高、体重、BMI |
| 医疗记录 | `data/index.json` | 生化指标、影像检查 |
| 运动追踪 | `data-example/fitness-tracker.json` | 运动类型、时长、强度、MET值 |
| 睡眠追踪 | `data-example/sleep-tracker.json` | 睡眠时长、质量、PSQI评分 |
| 营养追踪 | `data-example/nutrition-tracker.json` | 饮食记录、营养素摄入、RDA达成率 |
| 心理健康 | `data-example/mental-health-tracker.json` | PHQ-9、GAD-7评分 |
| 用药记录 | `data/medications.json` | 药物名称、剂量、用法、依从性 |
| 过敏史 | `data/allergies.json` | 过敏原、严重程度 |

## 算法说明

### 相关性分析
- **皮尔逊相关系数**: 连续变量（如睡眠时长与情绪评分）
- **斯皮尔曼相关系数**: 有序变量（如症状严重程度）

### 异常检测
- **CUSUM算法**: 时间序列变化点检测
- **Z-score方法**: 统计异常值检测（|z| > 2）
- **IQR方法**: 四分位数异常值检测

### 风险预测
- **Framingham风险评分**: 高血压、心血管疾病风险
- **ADA风险评分**: 2型糖尿病风险
- **ASCVD计算器**: 动脉粥样硬化心血管病风险

## 安全与合规

### 必须遵循
- ❌ 不给出医疗诊断
- ❌ 不给出具体用药剂量建议
- ❌ 不判断生死预后
- ❌ 不替代医生建议
- ✅ 所有分析必须标注"仅供参考"
- ✅ Level 3建议必须包含免责声明
- ✅ 高风险预测必须建议咨询医生

### 隐私保护
- ✅ 所有数据保持本地
- ✅ 无外部API调用
- ✅ HTML报告独立运行

## 相关命令

- `/ai analyze` - AI综合分析
- `/ai predict [risk_type]` - 健康风险预测
- `/ai chat [query]` - 自然语言问答
- `/ai report generate [type]` - 生成AI健康报告
- `/ai status` - 查看AI功能状态

## 技术实现

### 工具限制
此Skill仅使用以下工具：
- **Read**: 读取JSON数据文件
- **Grep**: 搜索特定模式
- **Glob**: 按模式查找数据文件
- **Write**: 生成HTML报告和更新历史记录

### 性能优化
- 增量读取：仅读取指定时间范围的数据文件
- 数据缓存：避免重复读取同一文件
- 延迟计算：按需生成图表数据

## Source: references/skills/healthcare-workflows/references/legacy/bdi-mental-states/SKILL.md

---
name: bdi-mental-states
description: This skill should be used when the user asks to "model agent mental states", "implement BDI architecture", "create belief-desire-intention models", "transform RDF to beliefs", "build cognitive agent", or mentions BDI ontology, mental state modeling, rational agency, or neuro-symbolic AI integration.
---

# BDI Mental State Modeling

Transform external RDF context into agent mental states (beliefs, desires, intentions) using formal BDI ontology patterns. This skill enables agents to reason about context through cognitive architecture, supporting deliberative reasoning, explainability, and semantic interoperability within multi-agent systems.

## When to Activate

Activate this skill when:
- Processing external RDF context into agent beliefs about world states
- Modeling rational agency with perception, deliberation, and action cycles
- Enabling explainability through traceable reasoning chains
- Implementing BDI frameworks (SEMAS, JADE, JADEX)
- Augmenting LLMs with formal cognitive structures (Logic Augmented Generation)
- Coordinating mental states across multi-agent platforms
- Tracking temporal evolution of beliefs, desires, and intentions
- Linking motivational states to action plans

## Core Concepts

### Mental Reality Architecture

**Mental States (Endurants)**: Persistent cognitive attributes
- `Belief`: What the agent believes to be true about the world
- `Desire`: What the agent wishes to bring about
- `Intention`: What the agent commits to achieving

**Mental Processes (Perdurants)**: Events that modify mental states
- `BeliefProcess`: Forming/updating beliefs from perception
- `DesireProcess`: Generating desires from beliefs
- `IntentionProcess`: Committing to desires as actionable intentions

### Cognitive Chain Pattern

```turtle
:Belief_store_open a bdi:Belief ;
    rdfs:comment "Store is open" ;
    bdi:motivates :Desire_buy_groceries .

:Desire_buy_groceries a bdi:Desire ;
    rdfs:comment "I desire to buy groceries" ;
    bdi:isMotivatedBy :Belief_store_open .

:Intention_go_shopping a bdi:Intention ;
    rdfs:comment "I will buy groceries" ;
    bdi:fulfils :Desire_buy_groceries ;
    bdi:isSupportedBy :Belief_store_open ;
    bdi:specifies :Plan_shopping .
```

### World State Grounding

Mental states reference structured configurations of the environment:

```turtle
:Agent_A a bdi:Agent ;
    bdi:perceives :WorldState_WS1 ;
    bdi:hasMentalState :Belief_B1 .

:WorldState_WS1 a bdi:WorldState ;
    rdfs:comment "Meeting scheduled at 10am in Room 5" ;
    bdi:atTime :TimeInstant_10am .

:Belief_B1 a bdi:Belief ;
    bdi:refersTo :WorldState_WS1 .
```

### Goal-Directed Planning

Intentions specify plans that address goals through task sequences:

```turtle
:Intention_I1 bdi:specifies :Plan_P1 .

:Plan_P1 a bdi:Plan ;
    bdi:addresses :Goal_G1 ;
    bdi:beginsWith :Task_T1 ;
    bdi:endsWith :Task_T3 .

:Task_T1 bdi:precedes :Task_T2 .
:Task_T2 bdi:precedes :Task_T3 .
```

## T2B2T Paradigm

Triples-to-Beliefs-to-Triples implements bidirectional flow between RDF knowledge graphs and internal mental states:

**Phase 1: Triples-to-Beliefs**
```turtle
# External RDF context triggers belief formation
:WorldState_notification a bdi:WorldState ;
    rdfs:comment "Push notification: Payment request $250" ;
    bdi:triggers :BeliefProcess_BP1 .

:BeliefProcess_BP1 a bdi:BeliefProcess ;
    bdi:generates :Belief_payment_request .
```

**Phase 2: Beliefs-to-Triples**
```turtle
# Mental deliberation produces new RDF output
:Intention_pay a bdi:Intention ;
    bdi:specifies :Plan_payment .

:PlanExecution_PE1 a bdi:PlanExecution ;
    bdi:satisfies :Plan_payment ;
    bdi:bringsAbout :WorldState_payment_complete .
```

## Notation Selection by Level

| C4 Level | Notation | Mental State Representation |
|----------|----------|----------------------------|
| L1 Context | ArchiMate | Agent boundaries, external perception sources |
| L2 Container | ArchiMate | BDI reasoning engine, belief store, plan executor |
| L3 Component | UML | Mental state managers, process handlers |
| L4 Code | UML/RDF | Belief/Desire/Intention classes, ontology instances |

## Justification and Explainability

Mental entities link to supporting evidence for traceable reasoning:

```turtle
:Belief_B1 a bdi:Belief ;
    bdi:isJustifiedBy :Justification_J1 .

:Justification_J1 a bdi:Justification ;
    rdfs:comment "Official announcement received via email" .

:Intention_I1 a bdi:Intention ;
    bdi:isJustifiedBy :Justification_J2 .

:Justification_J2 a bdi:Justification ;
    rdfs:comment "Location precondition satisfied" .
```

## Temporal Dimensions

Mental states persist over bounded time periods:

```turtle
:Belief_B1 a bdi:Belief ;
    bdi:hasValidity :TimeInterval_TI1 .

:TimeInterval_TI1 a bdi:TimeInterval ;
    bdi:hasStartTime :TimeInstant_9am ;
    bdi:hasEndTime :TimeInstant_11am .
```

Query mental states active at specific moments:

```sparql
SELECT ?mentalState WHERE {
    ?mentalState bdi:hasValidity ?interval .
    ?interval bdi:hasStartTime ?start ;
              bdi:hasEndTime ?end .
    FILTER(?start <= "2025-01-04T10:00:00"^^xsd:dateTime && 
           ?end >= "2025-01-04T10:00:00"^^xsd:dateTime)
}
```

## Compositional Mental Entities

Complex mental entities decompose into constituent parts for selective updates:

```turtle
:Belief_meeting a bdi:Belief ;
    rdfs:comment "Meeting at 10am in Room 5" ;
    bdi:hasPart :Belief_meeting_time , :Belief_meeting_location .

# Update only location component
:BeliefProcess_update a bdi:BeliefProcess ;
    bdi:modifies :Belief_meeting_location .
```

## Integration Patterns

### Logic Augmented Generation (LAG)

Augment LLM outputs with ontological constraints:

```python
def augment_llm_with_bdi_ontology(prompt, ontology_graph):
    ontology_context = serialize_ontology(ontology_graph, format='turtle')
    augmented_prompt = f"{ontology_context}\n\n{prompt}"
    
    response = llm.generate(augmented_prompt)
    triples = extract_rdf_triples(response)
    
    is_consistent = validate_triples(triples, ontology_graph)
    return triples if is_consistent else retry_with_feedback()
```

### SEMAS Rule Translation

Map BDI ontology to executable production rules:

```prolog
% Belief triggers desire formation
[HEAD: belief(agent_a, store_open)] / 
[CONDITIONALS: time(weekday_afternoon)] » 
[TAIL: generate_desire(agent_a, buy_groceries)].

% Desire triggers intention commitment
[HEAD: desire(agent_a, buy_groceries)] / 
[CONDITIONALS: belief(agent_a, has_shopping_list)] » 
[TAIL: commit_intention(agent_a, buy_groceries)].
```

## Guidelines

1. Model world states as configurations independent of agent perspectives, providing referential substrate for mental states.

2. Distinguish endurants (persistent mental states) from perdurants (temporal mental processes), aligning with DOLCE ontology.

3. Treat goals as descriptions rather than mental states, maintaining separation between cognitive and planning layers.

4. Use `hasPart` relations for meronymic structures enabling selective belief updates.

5. Associate every mental entity with temporal constructs via `atTime` or `hasValidity`.

6. Use bidirectional property pairs (`motivates`/`isMotivatedBy`, `generates`/`isGeneratedBy`) for flexible querying.

7. Link mental entities to `Justification` instances for explainability and trust.

8. Implement T2B2T through: (1) translate RDF to beliefs, (2) execute BDI reasoning, (3) project mental states back to RDF.

9. Define existential restrictions on mental processes (e.g., `BeliefProcess ⊑ ∃generates.Belief`).

10. Reuse established ODPs (EventCore, Situation, TimeIndexedSituation, BasicPlan, Provenance) for interoperability.

## Competency Questions

Validate implementation against these SPARQL queries:

```sparql
# CQ1: What beliefs motivated formation of a given desire?
SELECT ?belief WHERE {
    :Desire_D1 bdi:isMotivatedBy ?belief .
}

# CQ2: Which desire does a particular intention fulfill?
SELECT ?desire WHERE {
    :Intention_I1 bdi:fulfils ?desire .
}

# CQ3: Which mental process generated a belief?
SELECT ?process WHERE {
    ?process bdi:generates :Belief_B1 .
}

# CQ4: What is the ordered sequence of tasks in a plan?
SELECT ?task ?nextTask WHERE {
    :Plan_P1 bdi:hasComponent ?task .
    OPTIONAL { ?task bdi:precedes ?nextTask }
} ORDER BY ?task
```

## Anti-Patterns

1. **Conflating mental states with world states**: Mental states reference world states, they are not world states themselves.

2. **Missing temporal bounds**: Every mental state should have validity intervals for diachronic reasoning.

3. **Flat belief structures**: Use compositional modeling with `hasPart` for complex beliefs.

4. **Implicit justifications**: Always link mental entities to explicit justification instances.

5. **Direct intention-to-action mapping**: Intentions specify plans which contain tasks; actions execute tasks.

## Integration

- **RDF Processing**: Apply after parsing external RDF context to construct cognitive representations
- **Semantic Reasoning**: Combine with ontology reasoning to infer implicit mental state relationships
- **Multi-Agent Communication**: Integrate with FIPA ACL for cross-platform belief sharing
- **Temporal Context**: Coordinate with temporal reasoning for mental state evolution
- **Explainable AI**: Feed into explanation systems tracing perception through deliberation to action
- **Neuro-Symbolic AI**: Apply in LAG pipelines to constrain LLM outputs with cognitive structures

## References

See `references/` folder for detailed documentation:
- `bdi-ontology-core.md` - Core ontology patterns and class definitions
- `rdf-examples.md` - Complete RDF/Turtle examples
- `sparql-competency.md` - Full competency question SPARQL queries
- `framework-integration.md` - SEMAS, JADE, LAG integration patterns

Primary sources:
- Zuppiroli et al. "The Belief-Desire-Intention Ontology" (2025)
- Rao & Georgeff "BDI agents: From theory to practice" (1995)
- Bratman "Intention, plans, and practical reason" (1987)


## Source: references/skills/healthcare-workflows/references/legacy/behavioral-modes/SKILL.md

---
name: behavioral-modes
description: "AI operational modes (brainstorm, implement, debug, review, teach, ship, orchestrate). Use to adapt behavior based on task type."
risk: unknown
source: community
date_added: "2026-02-27"
---

# Behavioral Modes - Adaptive AI Operating Modes

## Purpose
This skill defines distinct behavioral modes that optimize AI performance for specific tasks. Modes change how the AI approaches problems, communicates, and prioritizes.

---

## Available Modes

### 1. 🧠 BRAINSTORM Mode

**When to use:** Early project planning, feature ideation, architecture decisions

**Behavior:**
- Ask clarifying questions before assumptions
- Offer multiple alternatives (at least 3)
- Think divergently - explore unconventional solutions
- No code yet - focus on ideas and options
- Use visual diagrams (mermaid) to explain concepts

**Output style:**
```
"Let's explore this together. Here are some approaches:

Option A: [description]
  ✅ Pros: ...
  ❌ Cons: ...

Option B: [description]
  ✅ Pros: ...
  ❌ Cons: ...

What resonates with you? Or should we explore a different direction?"
```

---

### 2. ⚡ IMPLEMENT Mode

**When to use:** Writing code, building features, executing plans

**Behavior:**
- **CRITICAL: Use `clean-code` skill standards** - concise, direct, no verbose explanations
- Fast execution - minimize questions
- Use established patterns and best practices
- Write complete, production-ready code
- Include error handling and edge cases
- **NO tutorial-style explanations** - just code
- **NO unnecessary comments** - let code self-document
- **NO over-engineering** - solve the problem directly
- **NO RUSHING** - Quality > Speed. Read ALL references before coding.

**Output style:**
```
[Code block]

[Brief summary, max 1-2 sentences]
```

**NOT:**
```
"Building [feature]...

✓ Created [file1]
✓ Created [file2]
✓ Updated [file3]

[long explanation]

Run `npm run dev` to test."
```

---

### 3. 🔍 DEBUG Mode

**When to use:** Fixing bugs, troubleshooting errors, investigating issues

**Behavior:**
- Ask for error messages and reproduction steps
- Think systematically - check logs, trace data flow
- Form hypothesis → test → verify
- Explain the root cause, not just the fix
- Prevent future occurrences

**Output style:**
```
"Investigating...

🔍 Symptom: [what's happening]
🎯 Root cause: [why it's happening]
✅ Fix: [the solution]
🛡️ Prevention: [how to avoid in future]
```

---

### 4. 📋 REVIEW Mode

**When to use:** Code review, architecture review, security audit

**Behavior:**
- Be thorough but constructive
- Categorize by severity (Critical/High/Medium/Low)
- Explain the "why" behind suggestions
- Offer improved code examples
- Acknowledge what's done well

**Output style:**
```
## Code Review: [file/feature]

### 🔴 Critical
- [issue with explanation]

### 🟠 Improvements
- [suggestion with example]

### 🟢 Good
- [positive observation]
```

---

### 5. 📚 TEACH Mode

**When to use:** Explaining concepts, documentation, onboarding

**Behavior:**
- Explain from fundamentals
- Use analogies and examples
- Progress from simple to complex
- Include practical exercises
- Check understanding

**Output style:**
```
## Understanding [Concept]

### What is it?
[Simple explanation with analogy]

### How it works
[Technical explanation with diagram]

### Example
[Code example with comments]

### Try it yourself
[Exercise or task]
```

---

### 6. 🚀 SHIP Mode

**When to use:** Production deployment, final polish, release preparation

**Behavior:**
- Focus on stability over features
- Check for missing error handling
- Verify environment configs
- Run all tests
- Create deployment checklist

**Output style:**
```
## Pre-Ship Checklist

### ✅ Code Quality
- [ ] No TypeScript errors
- [ ] ESLint passing
- [ ] All tests passing

### ✅ Security
- [ ] No exposed secrets
- [ ] Input validation complete

### ✅ Performance
- [ ] Bundle size acceptable
- [ ] No console.logs

### 🚀 Ready to deploy
```

---

## Mode Detection

The AI should automatically detect the appropriate mode based on:

| Trigger | Mode |
|---------|------|
| "what if", "ideas", "options" | BRAINSTORM |
| "build", "create", "add" | IMPLEMENT |
| "not working", "error", "bug" | DEBUG |
| "review", "check", "audit" | REVIEW |
| "explain", "how does", "learn" | TEACH |
| "deploy", "release", "production" | SHIP |

---

## Multi-Agent Collaboration Patterns (2025)

Modern architectures optimized for agent-to-agent collaboration:

### 1. 🔭 EXPLORE Mode
**Role:** Discovery and Analysis (Explorer Agent)
**Behavior:** Socratic questioning, deep-dive code reading, dependency mapping.
**Output:** `discovery-report.json`, architectural visualization.

### 2. 🗺️ PLAN-EXECUTE-CRITIC (PEC)
Cyclic mode transitions for high-complexity tasks:
1. **Planner:** Decomposes the task into atomic steps (`task.md`).
2. **Executor:** Performs the actual coding (`IMPLEMENT`).
3. **Critic:** Reviews the code, performs security and performance checks (`REVIEW`).

### 3. 🧠 MENTAL MODEL SYNC
Behavior for creating and loading "Mental Model" summaries to preserve context between sessions.

---

## Combining Modes

---

## Manual Mode Switching

Users can explicitly request a mode:

```
/brainstorm new feature ideas
/implement the user profile page
/debug why login fails
/review this pull request
```

## When to Use
This skill is applicable to execute the workflow or actions described in the overview.

## Source: references/skills/healthcare-workflows/references/legacy/emergency-card/SKILL.md

---
name: emergency-card
description: 生成紧急情况下快速访问的医疗信息摘要卡片。当用户需要旅行、就诊准备、紧急情况或询问"紧急信息"、"医疗卡片"、"急救信息"时使用此技能。提取关键信息（过敏、用药、急症、植入物），支持多格式输出（JSON、文本、二维码），用于急救或快速就医。
risk: unknown
source: community
---

# 紧急医疗信息卡生成器

生成紧急情况下快速访问的医疗信息摘要，用于急救或就医。

## 核心功能

### 1. 紧急信息提取
从用户的健康数据中提取最关键的信息：
- **严重过敏**：优先提取4级（过敏性休克）和3级过敏
- **当前用药**：活跃药物的名称、剂量、频率
- **急症情况**：需要紧急处理的医疗状况
- **植入物**：心脏起搏器、支架等（影响检查和治疗）
- **紧急联系人**：快速联系的家属信息

### 2. 信息优先级排序
按照医疗紧急程度对信息排序：
1. **P0 - 危急信息**：过敏性休克、严重药物过敏、危及生命的疾病
2. **P1 - 重要信息**：当前用药、慢性病、植入物
3. **P2 - 一般信息**：血型、年龄、体重、最近检查

### 3. 多格式输出
支持多种输出格式以适应不同场景：
- **HTML格式**：可打印网页，使用Tailwind CSS和Lucide图标（推荐）
- **JSON格式**：结构化数据，便于系统集成
- **文本格式**：简洁可读，适合打印携带
- **PDF格式**：专业打印，适合长期保存

#### HTML格式（新增）
生成独立的HTML文件，包含：
- Tailwind CSS样式（通过CDN）
- Lucide图标（通过CDN）
- 响应式设计
- 打印优化
- 多种尺寸变体（A4、钱包卡、大字版）
- 自动卡片类型检测（标准、儿童、老年、严重过敏）

使用方式：
```bash
# 生成标准卡片
python scripts/generate_emergency_card.py

# 指定卡片类型
python scripts/generate_emergency_card.py standard
python scripts/generate_emergency_card.py child
python scripts/generate_emergency_card.py elderly
python scripts/generate_emergency_card.py severe

# 指定打印尺寸
python scripts/generate_emergency_card.py standard a4       # A4标准
python scripts/generate_emergency_card.py standard wallet   # 钱包卡
python scripts/generate_emergency_card.py standard large    # 大字版（老年）
```

输出文件：`emergency-cards/emergency-card-{variant}-{YYYY-MM-DD}.html`

### 4. 离线可用
- 支持手机保存（相册、文件）
- 支持打印携带（钱包、包）
- 支持云端备份（可选）

## 使用说明

### 触发条件
当用户提到以下场景时，使用此技能：
- ✅ "生成紧急医疗信息卡"
- ✅ "我需要旅行，如何快速提供医疗信息"
- ✅ "把我的过敏信息整理成卡片"
- ✅ "紧急情况急救信息"
- ✅ "就医准备资料"
- ✅ "医疗信息摘要"

### 执行步骤

#### 步骤 1: 读取用户基础数据
从以下数据源读取信息：

```javascript
// 1. 用户档案
const profile = readFile('data/profile.json');

// 2. 过敏史
const allergies = readFile('data/allergies.json');

// 3. 当前用药
const medications = readFile('data/medications/medications.json');

// 4. 辐射记录
const radiation = readFile('data/radiation-records.json');

// 5. 手术记录（查找植入物）
const surgeries = glob('data/手术记录/**/*.json');

// 6. 出院小结（查找急症）
const dischargeSummaries = glob('data/出院小结/**/*.json');
```

#### 步骤 2: 提取关键信息

##### 2.1 基础信息
```javascript
const basicInfo = {
  name: profile.basic_info?.name || "未设置",
  age: calculateAge(profile.basic_info?.birth_date),
  gender: profile.basic_info?.gender || "未设置",
  blood_type: profile.basic_info?.blood_type || "未知",
  weight: `${profile.basic_info?.weight} ${profile.basic_info?.weight_unit}`,
  height: `${profile.basic_info?.height} ${profile.basic_info?.height_unit}`,
  bmi: profile.calculated?.bmi,
  emergency_contacts: profile.emergency_contacts || []
};
```

#### 2.2 严重过敏
```javascript
// 过滤出3-4级严重过敏
const criticalAllergies = allergies.allergies
  .filter(a => a.severity_level >= 3 && a.current_status.status === 'active')
  .map(a => ({
    allergen: a.allergen.name,
    severity: `过敏${getSeverityLabel(a.severity_level)}（${a.severity_level}级）`,
    reaction: a.reaction_description,
    diagnosed_date: a.diagnosis_date
  }));
```

#### 2.3 慢性疾病诊断（新增）
```javascript
// 从慢性病管理数据中提取诊断信息
const chronicConditions = [];

// 高血压
try {
  const hypertensionData = readFile('data/hypertension-tracker.json');
  if (hypertensionData.hypertension_management?.diagnosis_date) {
    chronicConditions.push({
      condition: '高血压',
      diagnosis_date: hypertensionData.hypertension_management.diagnosis_date,
      classification: hypertensionData.hypertension_management.classification,
      current_bp: hypertensionData.hypertension_management.average_bp,
      risk_level: hypertensionData.hypertension_management.cardiovascular_risk?.risk_level
    });
  }
} catch (e) {
  // 文件不存在或读取失败，跳过
}

// 糖尿病
try {
  const diabetesData = readFile('data/diabetes-tracker.json');
  if (diabetesData.diabetes_management?.diagnosis_date) {
    chronicConditions.push({
      condition: diabetesData.diabetes_management.type === 'type_1' ? '1型糖尿病' : '2型糖尿病',
      diagnosis_date: diabetesData.diabetes_management.diagnosis_date,
      duration_years: diabetesData.diabetes_management.duration_years,
      hba1c: diabetesData.diabetes_management.hba1c?.history?.[0]?.value,
      control_status: diabetesData.diabetes_management.hba1c?.achievement ? '控制良好' : '需改善'
    });
  }
} catch (e) {
  // 文件不存在或读取失败，跳过
}

// COPD
try {
  const copdData = readFile('data/copd-tracker.json');
  if (copdData.copd_management?.diagnosis_date) {
    chronicConditions.push({
      condition: '慢阻肺（COPD）',
      diagnosis_date: copdData.copd_management.diagnosis_date,
      gold_grade: `GOLD ${copdData.copd_management.gold_grade}级`,
      cat_score: copdData.copd_management.symptom_assessment?.cat_score?.total_score,
      exacerbations_last_year: copdData.copd_management.exacerbations?.last_year
    });
  }
} catch (e) {
  // 文件不存在或读取失败，跳过
}
```

#### 2.4 当前用药
```javascript
// 只包含活跃的药物
const currentMedications = medications.medications
  .filter(m => m.active === true)
  .map(m => ({
    name: m.name,
    dosage: `${m.dosage.value}${m.dosage.unit}`,
    frequency: getFrequencyLabel(m.frequency),
    instructions: m.instructions,
    warnings: m.warnings || []
  }));
```

##### 2.4 医疗状况
从出院小结中提取诊断信息：
```javascript
const medicalConditions = dischargeSummaries
  .flatMap(ds => {
    const data = readFile(ds.file_path);
    return data.diagnoses || [];
  })
  .map(d => ({
    condition: d.condition,
    diagnosis_date: d.date,
    status: d.status || "随访中"
  }));
```

##### 2.5 植入物
从手术记录中提取植入物信息：
```javascript
const implants = surgeries
  .flatMap(s => {
    const data = readFile(s.file_path);
    return data.procedure?.implants || [];
  })
  .map(i => ({
    type: i.type,
    implant_date: i.date,
    hospital: i.hospital,
    notes: i.notes
  }));
```

##### 2.6 近期辐射暴露
```javascript
const recentRadiation = {
  total_dose_last_year: calculateTotalDose(radiation.records, 'last_year'),
  last_exam: radiation.records[radiation.records.length - 1]
};
```

#### 步骤 3: 生成信息卡片

按照优先级组织信息：
```javascript
const emergencyCard = {
  version: "1.0",
  generated_at: new Date().toISOString(),
  basic_info: basicInfo,
  critical_allergies: criticalAllergies.sort(bySeverityDesc),
  current_medications: currentMedications,
  medical_conditions: [...medicalConditions, ...chronicConditions], // 合并急症和慢性病
  implants: implants,
  recent_radiation_exposure: recentRadiation,
  disclaimer: "此信息卡仅供参考，不替代专业医疗诊断",
  data_source: "my-his个人健康信息系统",
  chronic_conditions: chronicConditions // 单独字段便于访问
};
```

#### 步骤 4: 格式化输出

##### JSON格式
直接输出结构化JSON数据。

##### 文本格式
生成易读的文本卡片：
```
╔═══════════════════════════════════════════════════════════╗
║                  紧急医疗信息卡                          ║
╠═══════════════════════════════════════════════════════════╣
║ 姓名：张三                      年龄：35岁               ║
║ 血型：A+                       体重：70kg                ║
╠═══════════════════════════════════════════════════════════╣
║ 🆘 严重过敏                                              ║
║ ─────────────────────────────────────────────────────── ║
║ • 青霉素 - 过敏性休克（4级）🆘                          ║
║   反应：呼吸困难、喉头水肿、意识丧失                     ║
╠═══════════════════════════════════════════════════════════╣
║ 💊 当前用药                                              ║
║ ─────────────────────────────────────────────────────── ║
║ • 氨氯地平 5mg - 每日1次（高血压）                      ║
║ • 二甲双胍 1000mg - 每日2次（糖尿病）                    ║
╠═══════════════════════════════════════════════════════════╣
║ 🏥 慢性疾病                                              ║
║ ─────────────────────────────────────────────────────── ║
║ • 高血压（2023-01-01诊断，1级，控制中）                 ║
║   平均血压：132/82 mmHg                                 ║
║ • 2型糖尿病（2022-05-10诊断，HbA1c 6.8%）              ║
║   控制状态：良好                                        ║
║ • 慢阻肺（2020-03-15诊断，GOLD 2级）                    ║
║   CAT评分：18分                                        ║
╠═══════════════════════════════════════════════════════════╣
║ 🏥 其他疾病                                              ║
║ ─────────────────────────────────────────────────────── ║
║ （其他急症或手术诊断，如有）                            ║
╠═══════════════════════════════════════════════════════════╣
║ 📿 植入物                                                ║
║ ─────────────────────────────────────────────────────── ║
║ • 心脏起搏器（2022-06-10植入）                           ║
║   医院：XX医院                                           ║
║   注意：定期复查，避免MRI检查                            ║
╠═══════════════════════════════════════════════════════════╣
║ 📞 紧急联系人                                            ║
║ ─────────────────────────────────────────────────────── ║
║ • 李四（配偶）- 138****1234                              ║
╠═══════════════════════════════════════════════════════════╣
║ ⚠️  免责声明                                            ║
║ 此信息卡仅供参考，不替代专业医疗诊断                     ║
║ 生成时间：2025-12-31 12:34:56                            ║
╚═══════════════════════════════════════════════════════════╝
```

##### 二维码格式
将JSON数据转换为二维码图片：
```javascript
const qrCode = generateQRCode(JSON.stringify(emergencyCard));
emergencyCard.qr_code = qrCode;
```

#### 步骤 5: 保存文件

根据用户选择的格式保存文件：
```javascript
// JSON格式
saveFile('emergency-card.json', JSON.stringify(emergencyCard, null, 2));

// 文本格式
saveFile('emergency-card.txt', generateTextCard(emergencyCard));

// 二维码格式
saveFile('emergency-card-qr.png', emergencyCard.qr_code);
```

#### 步骤 6: 输出确认信息

```
✅ 紧急医疗信息卡已生成

文件位置：data/emergency-cards/emergency-card-2025-12-31.json
生成时间：2025-12-31 12:34:56

包含信息：
━━━━━━━━━━━━━━━━━━━━━━━━━━
✓ 基础信息（姓名、年龄、血型）
✓ 严重过敏（1项4级过敏）
✓ 当前用药（2种药物）
✓ 医疗状况（2种疾病）
✓ 植入物（1项）
✓ 紧急联系人（1人）

💡 使用建议：
━━━━━━━━━━━━━━━━━━━━━━━━━━
• 将JSON文件保存到手机云盘
• 将二维码保存到手机相册
• 打印文本版随身携带
• 旅行前更新信息

⚠️  注意事项：
━━━━━━━━━━━━━━━━━━━━━━━━━━
• 此信息卡仅供参考，不替代专业医疗诊断
• 定期更新（建议每3个月或健康信息变化后）
• 如有严重过敏，请随身携带过敏急救卡
```

## 数据源

### 主要数据源
- **data/profile.json**：用户基础信息、血型、紧急联系人
- **data/allergies.json**：过敏史和严重程度分级
- **data/medications/medications.json**：当前用药计划和剂量

### 慢性病数据源（新增）
- **data/hypertension-tracker.json**：高血压管理数据（诊断日期、分级、血压控制、靶器官损害、心血管风险）
- **data/diabetes-tracker.json**：糖尿病管理数据（类型、HbA1c、血糖控制、并发症筛查）
- **data/copd-tracker.json**：COPD管理数据（GOLD分级、CAT评分、急性加重史、肺功能）

### 辅助数据源
- **data/radiation-records.json**：近期辐射暴露记录
- **data/手术记录/**/*.json**：手术植入物信息
- **data/出院小结/**/*.json**：医疗诊断信息

### 可选数据源
- **data/index.json**：全局数据索引

## 安全性原则

### 必须遵循
- ❌ 不添加用药建议（仅列出当前用药）
- ❌ 不提供诊断结论（仅列出已知诊断）
- ❌ 不给出治疗建议（不替代医生）
- ❌ 标注免责声明（仅供参考）

### 信息准确度
- ✅ 仅提取已记录的信息（不推测或推断）
- ✅ 标注信息来源和更新时间
- ✅ 建议定期更新信息

### 隐私保护
- ✅ 敏感信息可选隐藏
- ✅ 电话号码部分隐藏（如：138****1234）
- ✅ 所有数据仅保存在本地

## 错误处理

### 数据缺失
- **过敏数据缺失**：输出"未记录过敏史"
- **用药数据缺失**：输出"未记录当前用药"
- **植入物数据缺失**：输出"无植入物"

### 文件读取失败
- **无法读取profile.json**：使用默认值（姓名：未设置）
- **无法读取allergies.json**：跳过过敏信息
- **继续生成其他信息**：不因单个文件失败而中断

### 二维码生成失败
- 降级为文本格式输出
- 提示用户手动记录信息

## 示例输出

完整示例请参考相关文档。

## 测试数据

测试数据请参考相关文档。

## 格式说明

详细格式请参考相关文档。


## When to Use

Use this skill when tackling tasks related to its primary domain or functionality as described above.

## Source: references/skills/healthcare-workflows/references/legacy/family-health-analyzer/SKILL.md

---
name: family-health-analyzer
description: 分析家族病史、评估遗传风险、识别家庭健康模式、提供个性化预防建议
allowed-tools: Read, Write, Grep, Glob
---

# 家庭健康分析技能

## 技能概述

本技能提供家庭健康数据的深度分析,包括:
- 遗传风险评估
- 家族疾病模式识别
- 家庭共同问题分析
- 个性化预防建议
- 可视化报告生成

## 触发条件

当用户请求以下内容时,使用此技能:
- "家庭健康报告"
- "家族病史分析"
- "遗传风险评估"
- "家庭健康趋势"
- 执行 `/family report` 命令
- 执行 `/family risk` 命令

## 分析步骤

### 步骤1: 确定分析目标

识别用户请求类型:
- 家族病史分析
- 遗传风险评估
- 家庭健康趋势
- 家庭健康报告

### 步骤2: 读取家庭数据

**数据源:**
1. 主数据文件: `data/family-health-tracker.json`
2. 集成模块数据:
   - `data/hypertension-tracker.json`
   - `data/diabetes-tracker.json`
   - `data/profile.json`

### 步骤3: 数据验证与清洗

**验证项目:**
- 关系完整性
- 年龄合理性
- 数据一致性

### 步骤4: 遗传模式识别

**识别算法:**
1. 家族聚集性分析
2. 遗传模式识别
3. 早发病例识别(通常<50岁)

### 步骤5: 风险计算算法

**加权计算:**
```python
遗传风险评分 = (一级亲属患病数 × 0.4) +
              (早发病例数 × 0.3) +
              (家族聚集度 × 0.3)

风险等级:
- 高风险: ≥70%
- 中风险: 40%-69%
- 低风险: <40%
```

### 步骤6: 生成预防建议

**建议分类:**
- 筛查建议:定期检查项目
- 生活方式建议:饮食、运动、作息
- 就医建议:何时就医、咨询专科

**示例:**
```json
{
  "category": "screening",
  "action": "定期血压监测",
  "frequency": "每周3次",
  "start_age": 35,
  "priority": "high"
}
```

### 步骤7: 生成可视化报告

**HTML报告组件:**
1. 家谱树(ECharts树图)
2. 遗传风险热力图
3. 疾病分布饼图
4. 预防建议时间线

### 步骤8: 输出结果

**输出格式:**
1. 文本报告(简洁版):命令行输出
2. HTML报告(完整版):可视化图表

## 安全原则

### 医学安全边界
- ✅ 仅基于家族病史进行统计分析
- ✅ 提供预防建议和筛查提醒
- ✅ 明确标注不确定性
- ❌ 不进行遗传疾病诊断
- ❌ 不预测个体发病概率
- ❌ 不推荐具体治疗方案

### 免责声明
每次分析输出必须包含:
```
⚠️ 免责声明:
1. 本分析基于家族病史统计,仅供参考
2. 遗传风险评估不预测个体发病
3. 所有医疗决策请咨询专业医师
4. 遗传咨询建议咨询专业遗传咨询师
```

## 集成现有模块

- 读取高血压管理数据
- 读取糖尿病管理数据
- 关联用药记录

---

**技能版本**: v1.0
**最后更新**: 2025-01-08
**维护者**: WellAlly Tech

## Source: references/skills/healthcare-workflows/references/legacy/fitness-analyzer/SKILL.md

---
name: fitness-analyzer
description: 分析运动数据、识别运动模式、评估健身进展，并提供个性化训练建议。支持与慢性病数据的关联分析。
allowed-tools: Read, Grep, Glob, Write
---

# 运动分析器技能

分析运动数据，识别运动模式，评估健身进展，并提供个性化训练建议。

## 功能

### 1. 运动趋势分析
分析运动量、频率、强度的变化趋势，识别改善或需要调整的方面。

**分析维度**：
- 运动量趋势（时长、距离、卡路里）
- 运动频率趋势（每周运动天数）
- 强度分布变化（低/中/高强度占比）
- 运动类型偏好变化

**输出**：
- 趋势方向（改善/稳定/下降）
- 变化幅度和百分比
- 趋势显著性
- 改进建议

### 2. 运动进步追踪
追踪特定运动类型的进步情况，量化健身效果。

**支持的进步追踪**：
- **跑步进步**：配速提升、距离增加、心率改善
- **力量训练进步**：重量增加、容量提升、RPE变化
- **耐力进步**：运动时长增加、距离延长
- **柔韧性进步**：关节活动度改善

**输出**：
- 开始值 vs 当前值
- 改善百分比
- 进步可视化
- 达成的里程碑

### 3. 运动习惯分析
识别用户的运动习惯和模式。

**分析内容**：
- 常用运动时间（早晨/下午/晚上）
- 运动频率模式（每周几天）
- 运动类型偏好
- 休息日分布
- 运动一致性评分

**输出**：
- 习惯总结
- 一致性评分（0-100）
- 优化建议
- 习惯养成建议

### 4. 相关性分析
分析运动与其他健康指标的相关性。

**支持的相关性分析**：
- **运动 ↔ 体重**：运动消耗与体重变化的关系
- **运动 ↔ 血压**：运动对血压的长期影响
- **运动 ↔ 血糖**：运动对血糖控制的效果
- **运动 ↔ 情绪/睡眠**：运动对情绪和睡眠的影响

**输出**：
- 相关系数（-1到1）
- 相关性强度（弱/中/强）
- 统计显著性
- 因果关系推断
- 实践建议

### 5. 个性化建议生成
基于用户数据生成个性化运动建议。

**建议类型**：
- **运动频率建议**：是否需要增加/减少运动频率
- **运动强度建议**：强度调整建议
- **运动类型建议**：推荐尝试的运动类型
- **运动时间建议**：最佳运动时间
- **恢复建议**：休息和恢复建议

**建议依据**：
- WHO/ACSM/AHA运动指南
- 用户运动历史数据
- 用户健康状况
- 用户健身目标

## 输出格式

### 趋势分析报告

```markdown
# 运动趋势分析报告

## 分析周期
2025-03-20 至 2025-06-20（3个月）

## 运动量趋势

### 运动时长
- 趋势：⬆️ 上升
- 开始：平均120分钟/周
- 当前：平均180分钟/周
- 变化：+50%（+60分钟/周）
- 解读：运动量显著增加，表现优秀

### 卡路里消耗
- 趋势：⬆️ 上升
- 开始：平均960卡/周
- 当前：平均1440卡/周
- 变化：+50%
- 解读：运动消耗增加，有助于体重管理

### 运动距离
- 趋势：⬆️ 上升
- 开始：平均10公里/周
- 当前：平均20公里/周
- 变化：+100%
- 解读：耐力显著提升

## 运动频率

- 当前频率：4天/周
- 目标频率：4-5天/周
- 状态：✅ 达标
- 建议：保持当前频率

## 强度分布

| 强度 | 占比 | 变化 |
|------|------|------|
| 低强度 | 25% | +5% |
| 中等强度 | 55% | -10% |
| 高强度 | 20% | +5% |

**分析**：强度分布合理，中等强度占主导，符合有氧运动建议。

## 运动类型分布

| 运动类型 | 占比 |
|---------|------|
| 跑步 | 50% |
| 瑜伽 | 25% |
| 力量训练 | 25% |

**建议**：可以适当增加力量训练比例至30-40%。

## 洞察与建议

### 优势
1. ✅ 运动量稳定增长，(+50%)
2. ✅ 运动频率稳定，每周4天
3. ✅ 休息日充足，恢复良好

### 改进建议
1. 📈 每周增加2次力量训练
2. 📈 尝试不同运动类型避免单调
3. 📈 适当增加高强度间歇训练(HIIT)

### 警示
1. ⚠️ 注意运动强度不宜过高，控制在中等强度为主
```

### 相关性分析报告

```markdown
# 运动与血压相关性分析

## 数据来源
- 运动数据：fitness-logs (2025-03-20 至 2025-06-20)
- 血压数据：hypertension-tracker (同期)

## 分析结果

### 相关系数
- 变量：每周运动时长 ↔ 收缩压
- 相关系数：r = -0.68
- 相关性强度：**强负相关**
- 统计显著性：p < 0.01 **高度显著**

### 解读
运动时长与收缩压呈强负相关，意味着：
- 运动越多，血压越低
- 每增加30分钟运动，收缩压平均下降3-5 mmHg

### 实践建议
1. ✅ 继续保持规律运动，每周5-7天
2. ✅ 每次运动30-60分钟，中等强度
3. ✅ 优先选择有氧运动（快走、慢跑、骑行）
4. ⚠️ 避免憋气动作和突然爆发性运动

### 医学参考
- AHA声明：规律有氧运动可降低收缩压5-7 mmHg
- 您的运动效果：降低约10 mmHg，效果显著！
```

### 进步追踪报告

```markdown
# 跑步进步追踪

## 分析周期
2025-01-01 至 2025-06-20（6个月）

## 配速进步

| 指标 | 开始 | 当前 | 改善 |
|------|------|------|------|
| 平均配速 | 7:30 min/km | 6:00 min/km | +20% ⬆️ |
| 最快配速 | 7:00 min/km | 5:30 min/km | +22% ⬆️ |
| 5公里用时 | 37:30 | 30:00 | +20% ⬆️ |

**趋势**：配速持续稳定提升，进步显著！

## 距离进步

| 指标 | 开始 | 当前 | 改善 |
|------|------|------|------|
| 最长单次距离 | 3 km | 12 km | +300% ⬆️ |
| 月度总距离 | 40 km | 86 km | +115% ⬆️ |
| 平均距离 | 5 km | 6 km | +20% ⬆️ |

**趋势**：耐力大幅提升，可以完成更长距离。

## 心率改善

| 指标 | 开始 | 当前 | 改善 |
|------|------|------|------|
| 静息心率 | 78 bpm | 72 bpm | -6 bpm ⬇️ |
| 相同配速心率 | 155 bpm | 145 bpm | -10 bpm ⬇️ |

**分析**：心肺功能显著改善，相同配速下心率降低。

## 里程碑

- ✅ 2025-03-15：首次完成5公里跑
- ✅ 2025-05-20：首次完成10公里跑
- ✅ 2025-06-10：配速突破6:00 min/km

## 下一步目标

- 🎯 完成半程马拉松（21公里）
- 🎯 配速提升至5:30 min/km
- 🎯 尝试间歇训练提升速度
```

## 数据源

### 主要数据源

1. **运动日志**
   - 路径：`data/fitness-logs/YYYY-MM/YYYY-MM-DD.json`
   - 内容：运动记录（类型、时长、强度、心率、距离等）
   - 频率：每次运动后更新

2. **用户档案**
   - 路径：`data/fitness-tracker.json`
   - 内容：用户档案、健身目标、统计数据
   - 更新：定期更新

3. **健康数据关联**
   - `data/hypertension-tracker.json`（血压数据）
   - `data/diabetes-tracker.json`（血糖数据）
   - `data/profile.json`（体重、BMI等）

### 数据质量检查

- 数据完整性：检查必要字段是否存在
- 数据合理性：检查数值是否在合理范围内
- 时间一致性：检查时间戳是否合理
- 重复数据：检测并处理重复记录

## 算法说明

### 1. 线性回归趋势分析

使用线性回归分析运动数据的时间趋势。

**公式**：
y = a + bx

其中：
- y：运动指标（时长、卡路里、距离等）
- x：时间
- a：截距
- b：斜率（趋势方向和速度）

**解释**：
- b > 0：上升趋势
- b < 0：下降趋势
- b ≈ 0：稳定

### 2. Pearson相关系数

用于分析两个变量之间的线性相关性。

**公式**：
r = Σ[(xi - x̄)(yi - ȳ)] / √[Σ(xi - x̄)² × Σ(yi - ȳ)²]

**范围**：-1 ≤ r ≤ 1

**解释**：
- r = 1：完全正相关
- r = -1：完全负相关
- r = 0：无线性相关

**强度判断**：
- |r| < 0.3：弱相关
- 0.3 ≤ |r| < 0.7：中等相关
- |r| ≥ 0.7：强相关

### 3. 配速计算

**配速** = 运动时长 / 距离

单位：min/km 或 min/mile

**示例**：
- 30分钟跑5公里
- 配速 = 30 / 5 = 6 min/km

### 4. MET能量代谢计算

**卡路里消耗** = MET × 体重(kg) × 时间(小时)

**常见运动的MET值**：
- 走路（3-5 km/h）：3.5-5 MET
- 慢跑（8 km/h）：8 MET
- 快跑（10 km/h）：10 MET
- 游泳：6-10 MET
- 骑行（休闲）：4 MET
- 力量训练：5 MET
- 瑜伽：3 MET

## 医学安全边界

⚠️ **重要声明**
本分析仅供健康参考，不构成医疗建议。

### 分析能力范围

✅ **能做到**：
- 运动数据统计和分析
- 趋势识别和可视化
- 相关性计算和解释
- 一般性运动建议

❌ **不做到**：
- 疾病诊断
- 运动风险评估
- 具体运动处方设计
- 运动损伤诊断和治疗

### 危险信号检测

在分析过程中检测以下危险信号：

1. **心率异常**
   - 运动心率 > 95%最大心率
   - 静息心率 > 100 bpm

2. **血压异常**
   - 收缩压 ≥ 180 mmHg
   - 舒张压 ≥ 110 mmHg

3. **过度训练迹象**
   - 连续7天高强度运动
   - 运动感受持续下降（RPE > 17）

4. **体重快速下降**
   - 每周减重 > 1kg（可能不健康）

### 建议分级

**Level 1: 一般性建议**
- 基于WHO/ACSM指南
- 适用于一般人群

**Level 2: 参考性建议**
- 基于用户数据
- 需结合个人情况

**Level 3: 医疗建议**
- 涉及疾病管理
- 需医生确认

## 使用示例

### 示例1：生成运动趋势报告

```bash
/fitness trend 3months
```

输出：
- 3个月运动趋势分析
- 运动量、频率、强度变化
- 洞察和建议

### 示例2：追踪跑步进步

```bash
/fitness analysis progress running
```

输出：
- 配速进步
- 距离进步
- 心率改善
- 里程碑达成

### 示例3：分析运动与血压相关性

```bash
/fitness analysis correlation blood_pressure
```

输出：
- 相关系数
- 相关性强度
- 显著性检验
- 实践建议

---

**技能版本**: v1.0
**最后更新**: 2026-01-02
**维护者**: WellAlly Tech

## Source: references/skills/healthcare-workflows/references/legacy/geo-fundamentals/SKILL.md

---
name: geo-fundamentals
description: "Generative Engine Optimization for AI search engines (AI answer engines)."
risk: unknown
source: community
date_added: "2026-02-27"
---

# GEO Fundamentals

> Optimization for AI-powered search engines.

---

## 1. What is GEO?

**GEO** = Generative Engine Optimization

| Goal | Platform |
|------|----------|
| Be cited in AI responses | AI answer engines, Gemini |

### SEO vs GEO

| Aspect | SEO | GEO |
|--------|-----|-----|
| Goal | #1 ranking | AI citations |
| Platform | Google | AI engines |
| Metrics | Rankings, CTR | Citation rate |
| Focus | Keywords | Entities, data |

---

## 2. AI Engine Landscape

| Engine | Citation Style | Opportunity |
|--------|----------------|-------------|
| **Perplexity** | Numbered [1][2] | Highest citation rate |
| **ChatGPT** | Inline/footnotes | Custom GPTs |
| **AI assistant** | Contextual | Long-form content |
| **Gemini** | Sources section | SEO crossover |

---

## 3. RAG Retrieval Factors

How AI engines select content to cite:

| Factor | Weight |
|--------|--------|
| Semantic relevance | ~40% |
| Keyword match | ~20% |
| Authority signals | ~15% |
| Freshness | ~10% |
| Source diversity | ~15% |

---

## 4. Content That Gets Cited

| Element | Why It Works |
|---------|--------------|
| **Original statistics** | Unique, citable data |
| **Expert quotes** | Authority transfer |
| **Clear definitions** | Easy to extract |
| **Step-by-step guides** | Actionable value |
| **Comparison tables** | Structured info |
| **FAQ sections** | Direct answers |

---

## 5. GEO Content Checklist

### Content Elements

- [ ] Question-based titles
- [ ] Summary/TL;DR at top
- [ ] Original data with sources
- [ ] Expert quotes (name, title)
- [ ] FAQ section (3-5 Q&A)
- [ ] Clear definitions
- [ ] "Last updated" timestamp
- [ ] Author with credentials

### Technical Elements

- [ ] Article schema with dates
- [ ] Person schema for author
- [ ] FAQPage schema
- [ ] Fast loading (< 2.5s)
- [ ] Clean HTML structure

---

## 6. Entity Building

| Action | Purpose |
|--------|---------|
| Google Knowledge Panel | Entity recognition |
| Wikipedia (if notable) | Authority source |
| Consistent info across web | Entity consolidation |
| Industry mentions | Authority signals |

---

## 7. AI Crawler Access

### Key AI User-Agents

| Crawler | Engine |
|---------|--------|
| GPTBot | ChatGPT/OpenAI |
| AI-Assistant-Web | AI assistant |
| PerplexityBot | Perplexity |
| Googlebot | Gemini (shared) |

### Access Decision

| Strategy | When |
|----------|------|
| Allow all | Want AI citations |
| Block GPTBot | Don't want OpenAI training |
| Selective | Allow some, block others |

---

## 8. Measurement

| Metric | How to Track |
|--------|--------------|
| AI citations | Manual monitoring |
| "According to [Brand]" mentions | Search in AI |
| Competitor citations | Compare share |
| AI-referred traffic | UTM parameters |

---

## 9. Anti-Patterns

| ❌ Don't | ✅ Do |
|----------|-------|
| Publish without dates | Add timestamps |
| Vague attributions | Name sources |
| Skip author info | Show credentials |
| Thin content | Comprehensive coverage |

---

> **Remember:** AI cites content that's clear, authoritative, and easy to extract. Be the best answer.

---

## Script

| Script | Purpose | Command |
|--------|---------|---------|
| `scripts/geo_checker.py` | GEO audit (AI citation readiness) | `python scripts/geo_checker.py <project_path>` |


## When to Use
This skill is applicable to execute the workflow or actions described in the overview.

## Source: references/skills/healthcare-workflows/references/legacy/goal-analyzer/SKILL.md

---
name: goal-analyzer
description: 分析健康目标数据、识别目标模式、评估目标进度,并提供个性化目标管理建议。支持与营养、运动、睡眠等健康数据的关联分析。
allowed-tools: Read, Grep, Glob, Write
---

# 健康目标分析器技能

分析健康目标数据,识别目标模式和进度,评估目标达成情况,并提供个性化目标管理建议。

## 功能

### 1. SMART目标验证

验证设定的新目标是否符合SMART原则。

**验证维度**:
- **S**pecific(具体性)
  - 目标是否明确具体
  - 是否有清晰的定义
  - 是否避免模糊表述

- **M**easurable(可衡量性)
  - 是否有可量化的指标
  - 是否有明确的衡量标准
  - 是否可以追踪进度

- **A**chievable(可实现性)
  - 目标是否现实可行
  - 是否考虑了当前状况
  - 是否在合理时间范围内
  - 减重目标:建议每周0.5-1公斤
  - 运动目标:建议每周3-5次,每次30-60分钟

- **R**elevant(相关性)
  - 目标是否与健康相关
  - 是否符合用户整体健康计划
  - 是否与现有目标协调

- **T**ime-bound(有时限)
  - 是否有明确的截止日期
  - 时间框架是否合理
  - 是否有阶段性里程碑

**输出**:
- SMART评分(每个维度1-5分)
- 总体评分和等级(S级/A级/B级/C级)
- 改进建议
- 目标优化方案

**示例评估**:
```json
{
  "goal": "6个月内减重5公斤",
  "smart_scores": {
    "specific": 5,
    "measurable": 5,
    "achievable": 4,
    "relevant": 5,
    "time_bound": 5
  },
  "overall_score": 4.8,
  "grade": "A",
  "assessment": "优秀的SMART目标",
  "suggestions": [
    "建议设定阶段性里程碑(每2个月减重1.5-2公斤)",
    "建议配合运动计划和饮食调整"
  ]
}
```

---

### 2. 目标进度追踪

追踪和分析目标的完成进度。

**追踪内容**:
- **当前进度**
  - 完成百分比
  - 当前数值vs目标数值
  - 剩余差距

- **时间进度**
  - 已用时间占比
  - 剩余时间
  - 进度超前/落后判断

- **速度分析**
  - 平均进度速度(每周/每月)
  - 预计完成时间
  - 是否需要调整计划

- **趋势识别**
  - 进度趋势(加速/稳定/减速)
  - 周期性模式
  - 异常波动检测

**输出**:
- 进度可视化(进度条、百分比)
- 完成概率预测
- 时间预估(乐观/中性/悲观)
- 调整建议

**进度评级**:
- 🟢 **优秀** - 进度超前,预计提前完成
- 🟡 **正常** - 进度符合预期
- 🟠 **落后** - 进度略慢,需要加快
- 🔴 **严重落后** - 进度严重滞后,建议调整目标

---

### 3. 习惯养成分析

分析习惯的养成情况和连续性。

**分析内容**:
- **连续天数追踪**
  - 当前连续天数
  - 历史最长连续天数
  - 平均连续天数

- **完成率统计**
  - 总体完成率
  - 每周完成率
  - 每月完成率
  - 特定星期几完成率

- **习惯强度评估**
  - 习惯固化程度(1-10分)
  - 习惯稳定性评分
  - 自动化程度评估

- **习惯模式识别**
  - 最佳触发时间
  - 常见中断原因
  - 成功因素识别

**习惯养成阶段**:
- **第1-7天** - 启动期(最容易放弃)
- **第8-21天** - 形成期(逐渐稳定)
- **第22-30天** - 巩固期(接近自动化)
- **第31-66天** - 习惯期(基本养成)
- **第67天+** - 自动化期(完全自动化)

**输出**:
- 习惯热图(日历视图)
- 连续天数统计
- 完成率趋势图
- 习惯强度评分
- 习惯堆叠建议

**示例分析**:
```json
{
  "habit": "morning-stretch",
  "current_streak": 21,
  "longest_streak": 21,
  "completion_rate": 95.2,
  "strength_score": 7.5,
  "stage": "巩固期",
  "assessment": "习惯即将形成,继续保持!",
  "next_milestone": 30,
  "suggestions": [
    "继续保持,即将达到30天里程碑",
    "可以尝试添加新的相关习惯"
  ]
}
```

---

### 4. 动机评估与管理

评估和管理用户的动机水平。

**评估内容**:
- **动机评分追踪**
  - 当前动机水平(1-10分)
  - 动机变化趋势
  - 动机波动周期

- **动机因素分析**
  - 内在动机(健康、自我实现)
  - 外在动机(奖励、认可)
  - 社会支持(家人朋友鼓励)

- **动机低谷识别**
  - 动机下降信号
  - 常见低谷时间点
  - 风险时段预警

**动机提升策略**:
- **第2-3周** - 动机下降,需要强调已完成进度
- **第1-2个月** - 疲劳期,需要调整目标和奖励
- **3个月后** - 倦怠期,需要新鲜感和挑战

**输出**:
- 动机趋势图
- 动机低谷预警
- 个性化激励建议
- 奖励机制建议

**激励建议示例**:
- 当动机<5分:回顾初心,降低短期目标
- 当动机5-7分:强调进步,设置小奖励
- 当动机>7分:设定挑战,追求卓越

---

### 5. 成就系统管理

管理基础成就系统的解锁和进度。

**成就类型**:
- **目标相关成就**
  - 🏆 首次目标 - 完成第一个健康目标
  - 🎯 半程达成 - 任意目标完成50%
  - 🎉 目标达成 - 完成一个健康目标
  - ⚡ 提前完成 - 提前完成目标
  - 📈 超额完成 - 超额完成目标

- **习惯相关成就**
  - 🔥 连续7天 - 任意习惯连续7天打卡
  - 💪 连续21天 - 任意习惯连续21天打卡
  - ⭐ 连续30天 - 任意习惯连续30天打卡
  - 🌟 连续66天 - 任意习惯连续66天打卡(完全养成)

- **综合成就**
  - 🏅 多目标并行 - 同时完成3个目标
  - 💎 完美坚持 - 30天习惯完成率100%
  - 🚀 快速进步 - 单周进步最大
  - 👑 长期坚持 - 持续追踪180天

**成就追踪**:
- 已解锁成就列表
- 未解锁成就进度
- 成就解锁时间
- 成就相关建议

**输出**:
- 成就徽章展示
- 成就完成进度
- 下一个可解锁成就
- 成就达成建议

---

### 6. 障碍识别与建议

识别阻碍目标达成的因素,提供解决方案。

**障碍类型**:
- **时间障碍**
  - 忙碌、时间不足
  - 建议:缩短单次时长,增加频率;利用碎片时间

- **动机障碍**
  - 缺乏动力、拖延
  - 建议:设置提醒;寻找伙伴;调整目标

- **环境障碍**
  - 缺乏支持、诱惑过多
  - 建议:改变环境;寻找替代方案;建立支持系统

- **能力障碍**
  - 目标太难、缺乏知识
  - 建议:降低难度;学习知识;寻求专业帮助

- **身体障碍**
  - 疲劳、不适、受伤
  - 建议:休息恢复;调整计划;咨询医生

**输出**:
- 主要障碍识别
- 障碍频率统计
- 个性化解决方案
- 预防性建议

---

### 7. 数据关联分析

将健康目标与其他健康数据进行关联分析。

**关联维度**:
- **减重目标关联**
  - 营养摄入(卡路里、宏量营养素)
  - 运动消耗(频率、强度、时长)
  - 睡眠质量(时长、深度)
  - 体重变化趋势

- **运动目标关联**
  - 睡眠质量(恢复情况)
  - 营养摄入(蛋白质、碳水)
  - 身体指标(体重、体脂率)

- **饮食目标关联**
  - 营养素摄入(维生素、矿物质)
  - 身体指标(血压、血糖)
  - 运动表现

- **睡眠目标关联**
  - 运动时间(晚间运动影响)
  - 饮食时间(晚餐时间、咖啡因)
  - 屏幕时间(蓝光影响)

**分析方法**:
- 相关性分析(Pearson相关系数)
- 回归分析(预测模型)
- 趋势匹配(趋势同步性)
- 因果推断(潜在因果关系)

**输出**:
- 关联强度(强/中/弱)
- 正/负相关关系
- 因果关系推断
- 优化建议

**示例关联**:
```json
{
  "goal": "weight-loss",
  "correlations": [
    {
      "factor": "daily_calories",
      "correlation": -0.75,
      "strength": "强负相关",
      "insight": "每日卡路里摄入与减重进度呈强负相关,降低摄入加速进度"
    },
    {
      "factor": "exercise_frequency",
      "correlation": 0.68,
      "strength": "强正相关",
      "insight": "运动频率与减重进度呈强正相关,建议保持每周4次以上"
    },
    {
      "factor": "sleep_duration",
      "correlation": 0.45,
      "strength": "中等正相关",
      "insight": "睡眠时长影响减重,建议保证7-8小时睡眠"
    }
  ],
  "recommendations": [
    "重点控制卡路里摄入,保持当前运动频率",
    "优化睡眠时长,以提升减重效果"
  ]
}
```

---

### 8. 可视化报告生成

生成包含ECharts图表的HTML交互式报告。

**报告类型**:

#### A. 进度趋势报告
- 折线图展示目标进度随时间变化
- 里程碑标注
- 预测完成时间区间
- 进度速度分析

#### B. 习惯热图报告
- 日历热图展示习惯完成情况
- 颜色深浅表示完成频率
- 连续天数标注
- 完成率统计

#### C. 多目标对比报告
- 环形图展示多个目标完成率
- 优先级排序
- 资源分配建议
- 进度同步性分析

#### D. 动机趋势报告
- 折线图展示动机变化
- 动机与进度相关性
- 动机低谷预警
- 激励建议

#### E. 综合报告
- 包含以上所有图表
- 整体健康状况评估
- 综合改进建议
- 下阶段目标建议

**报告特点**:
- 响应式设计,支持移动端
- 深色/浅色主题切换
- 交互式图表(缩放、筛选)
- 数据表格展示
- 导出PDF功能
- 完全本地化,无需联网

**ECharts图表配置**:
```javascript
// 进度趋势折线图
{
  type: 'line',
  xAxis: { type: 'category', data: ['1月', '2月', '3月', ...] },
  yAxis: { type: 'value', name: '完成%' },
  series: [{
    name: '目标进度',
    type: 'line',
    data: [0, 15, 35, 50, 70, 85, 100],
    smooth: true,
    markLine: {
      data: [{ yAxis: 50, name: '50%里程碑' }]
    }
  }]
}

// 习惯热图
{
  type: 'heatmap',
  xAxis: { type: 'category', data: ['周一', '周二', ...] },
  yAxis: { type: 'category', data: ['第1周', '第2周', ...] },
  visualMap: {
    min: 0, max: 1,
    inRange: { color: ['#ebedf0', '#216e39'] }
  },
  series: [{
    type: 'heatmap',
    data: [[0, 0, 1], [1, 0, 1], [2, 0, 0], ...]
  }]
}

// 目标达成率环形图
{
  type: 'pie',
  radius: ['50%', '70%'],
  series: [{
    type: 'pie',
    radius: ['50%', '70%'],
    data: [
      { value: 70, name: '已完成' },
      { value: 30, name: '未完成' }
    ],
    label: { formatter: '{b}: {c}%' }
  }]
}
```

**输出**:
- HTML文件(包含完整的CSS、JS、ECharts)
- 图表交互功能
- 数据表格
- 分析文本
- 建议列表

---

## 医学安全边界

### 能力范围声明
- ✅ 辅助设定健康目标
- ✅ 追踪和分析目标进度
- ✅ 识别健康行为模式
- ✅ 提供一般性健康改善建议
- ✅ 生成可视化报告

- ❌ 不提供医疗诊断
- ❌ 不开具治疗处方
- ❌ 不替代专业医疗建议
- ❌ 不处理进食障碍或强迫行为

### 危险信号识别
**极端目标警告**:
- 减重目标>每周1公斤
- 增重目标>每周0.5公斤
- 极端卡路里限制(<1200卡/天)
- 过度运动(>2小时/天,7天/周)

**不健康行为迹象**:
- 完成率<30%持续3周
- 动机评分<3分持续2周
- 身体不适报告
- 强迫性行为模式

**转介建议**:
- 出现危险信号时,建议咨询医生
- 有慢性疾病时,建议咨询相关专科
- 设定饮食目标时,建议咨询营养师
- 设定运动目标时,建议咨询健身教练

---

## 输出格式

### 目标分析报告
```markdown
# 健康目标分析报告

## 目标概览
- 目标: 6个月内减重5公斤
- 开始日期: 2025-01-01
- 目标日期: 2025-06-30
- 当前日期: 2025-03-20

## SMART评估
- 具体性: ⭐⭐⭐⭐⭐ (5/5)
- 可衡量性: ⭐⭐⭐⭐⭐ (5/5)
- 可实现性: ⭐⭐⭐⭐ (4/5)
- 相关性: ⭐⭐⭐⭐⭐ (5/5)
- 有时限: ⭐⭐⭐⭐⭐ (5/5)

**总体评分: A (4.8/5)**

## 进度分析
- 当前进度: 70%
- 已完成: 3.5公斤 / 5.0公斤
- 时间进度: 27% (79天/180天)
- 进度评级: 🟢 优秀 (进度超前)

### 趋势分析
- 平均速度: 0.77公斤/月
- 预计完成: 2025-05-20 (提前40天)
- 进度趋势: 稳定上升

## 习惯追踪
### 早上拉伸习惯
- 当前连续: 21天 🔥
- 历史最长: 21天
- 完成率: 95.2%
- 习惯阶段: 巩固期
- 下一个里程碑: 30天 ⭐

## 动机评估
- 当前动机: 8/10
- 动机趋势: 稳定
- 动机状态: 良好

## 数据关联分析
### 强相关因素(影响度>60%)
1. 每日卡路里摄入 (负相关 -0.75)
2. 每周运动频次 (正相关 +0.68)
3. 睡眠时长 (正相关 +0.45)

### 建议
- 保持当前卡路里摄入水平
- 继续保持每周4次运动频率
- 优化睡眠时长至7-8小时

## 障碍识别
主要障碍: 社交活动饮食控制

解决方案:
- 社交活动前提前规划饮食
- 选择健康餐厅
- 适量控制份量

## 成就解锁
🔥 连续21天 - 早上拉伸习惯达成!
🎯 半程达成 - 减重目标完成50%!

## 下一步行动
1. 保持当前进度
2. 关注社交活动饮食控制
3. 继续养成早操习惯
4. 准备达成30天里程碑
```

---

## 技术实现要点

### 数据读取
- 读取主数据文件: `data-example/health-goals-tracker.json`
- 读取日志文件: `data-example/health-goals-logs/YYYY-MM/YYYY-MM-DD.json`
- 关联数据: `data-example/nutrition-tracker.json`, `fitness-tracker.json` 等

### 数据处理
- 计算完成百分比: `(current_value / target_value) * 100`
- 计算时间进度: `(days_elapsed / total_days) * 100`
- 计算连续天数: 遍历日志,统计连续完成天数
- 计算完成率: `(completed_days / total_days) * 100`
- 计算习惯强度: 基于完成率和连续天数的复合评分

### SMART验证算法
```python
def validate_smart_goal(goal):
    scores = {
        'specific': check_specificity(goal),
        'measurable': check_measurability(goal),
        'achievable': check_achievability(goal),
        'relevant': check_relevance(goal),
        'time_bound': check_time_bound(goal)
    }
    overall = sum(scores.values()) / len(scores)
    grade = get_grade(overall)
    return scores, overall, grade
```

### HTML报告生成
- 使用ECharts 5.x CDN
- 响应式CSS布局
- JavaScript处理图表交互
- 支持深色/浅色主题切换
- 数据从JSON文件动态加载

---

**使用此技能时,始终优先考虑用户的健康和安全!**

## Source: references/skills/healthcare-workflows/references/legacy/mental-health-analyzer/SKILL.md

---
name: mental-health-analyzer
description: 分析心理健康数据、识别心理模式、评估心理健康状况、提供个性化心理健康建议。支持与睡眠、运动、营养等其他健康数据的关联分析。
allowed-tools: Read, Grep, Glob, Write, Edit
---

# 心理健康分析技能

## 核心功能

心理健康分析技能提供全面的心理健康数据分析功能，帮助用户追踪心理状态、识别情绪模式、监测危机风险和优化应对策略。

**主要功能模块：**

1. **心理健康评估分析** - PHQ-9/GAD-7等量表评分趋势分析
2. **情绪模式识别** - 识别常见情绪、触发因素和应对方式效果
3. **心理治疗进展追踪** - 治疗目标达成和症状改善评估
4. **危机风险评估** - 多级危机风险检测（高/中/低）和预警
5. **睡眠-心理关联分析** - 睡眠质量与心理状态的关联性分析
6. **运动-情绪关联分析** - 运动与情绪改善的关系分析
7. **营养-心理关联分析** - 饮食对情绪和焦虑的影响分析
8. **慢性病-心理关联分析** - 慢性疾病与心理健康的关系分析

## 触发条件

技能在以下情况下自动触发：

1. 用户使用 `/mental trend` 查看心理状况趋势
2. 用户使用 `/mental pattern` 分析情绪模式
3. 用户使用 `/mental therapy progress` 查看治疗进展
4. 用户使用 `/crisis assessment` 进行危机风险评估
5. 用户使用 `/mental report` 生成心理健康报告

## 医学安全边界

**本技能不能做的事：**
- ❌ 不进行心理疾病诊断
- ❌ 不开具精神药物处方
- ❌ 不预测自杀风险或自伤行为
- ❌ 不替代专业心理治疗
- ❌ 不处理急性精神危机

**本技能能做的事：**
- ✅ 识别心理健康趋势和模式
- ✅ 评估危机风险等级并发出预警
- ✅ 提供应对策略建议（非治疗性）
- ✅ 追踪治疗进展和目标达成
- ✅ 提供就医建议和专业资源信息
- ✅ 分析心理健康与其他健康因素的关联

## 执行步骤

### 第1步：数据读取

读取心理健康数据文件：
- `data-example/mental-health-tracker.json` - 主心理健康档案
- `data-example/mental-health-logs/.index.json` - 日志索引
- `data-example/mental-health-logs/YYYY-MM/YYYY-MM-DD.json` - 每日情绪日记

**数据验证：**
- 检查文件是否存在
- 验证数据结构完整性
- 确认有足够的数据点进行分析（建议至少3次PHQ-9/GAD-7评估，或7天情绪日记）

### 第2步：心理健康评估趋势分析

**PHQ-9抑郁评分趋势分析：**
```
- 分析不同时间点的PHQ-9评分
- 计算评分变化速率（分/月）
- 识别严重程度变化（无/轻度/中度/重度）
- 检测PHQ-9第9项（自伤意念）的变化
- 预测未来趋势（改善/稳定/恶化）
- 与治疗进展关联分析
```

**GAD-7焦虑评分趋势分析：**
```
- 分析GAD-7评分时序变化
- 识别焦虑症状变化模式
- 关联触发因素与焦虑水平
- 评估应对方式效果
- 预测焦虑趋势
```

**PSQI睡眠质量与心理状态关联：**
```
- PSQI评分与PHQ-9/GAD-7评分的相关性
- 睡眠障碍对情绪的影响
- 睡眠改善与心理状态改善的关系
```

**严重程度变化检测：**
```
- 识别严重程度升级（需要关注）
- 识别严重程度降级（积极信号）
- 检测快速恶化（≥5分/月，危机预警）
- 检测快速改善（强化有效策略）
```

### 第3步：情绪模式识别

**常见情绪统计：**
```
- 统计最常见的主要情绪（top 5）
- 计算平均情绪强度
- 识别情绪分布模式
- 分析情绪多样性
```

**时间模式分析：**
```
- 一天中的情绪变化模式（早/中/晚）
- 一周中的情绪变化模式（周一至周日）
- 情绪波动程度（方差/标准差）
- 情绪稳定性评估
```

**触发因素分析：**
```
- 统计高频触发因素（top 10）
- 计算每个触发因素的平均影响
- 识别高危触发因素（高影响+高频）
- 触发因素与情绪类型的关联
```

**应对方式效果评估：**
```
- 计算每种应对方式的有效性（有帮助/没帮助的比例）
- 识别高效应对策略（>80%有效）
- 识别低效应对策略（<50%有效）
- 应对方式与情绪类型的匹配分析
```

### 第4步：心理治疗进展追踪

**治疗目标达成评估：**
```
- 计算每个目标的完成百分比
- 评估症状改善程度（基线→当前→目标）
- 预估目标达成时间
- 识别滞后目标（需要调整）
```

**治疗过程分析：**
```
- 治疗频率和依从性
- 作业完成率和质量
- 治疗联盟强度
- 咨询前后情绪变化
```

**症状改善评估：**
```
- PHQ-9/GAD-7评分变化（治疗前→治疗后）
- 症状缓解百分比
- 功能水平改善
- 生活质量变化
```

### 第5步：危机风险评估（优先级：最高）

**多级风险检测机制：**

```
风险等级计算（总分0-20+）：

1. PHQ-9第9项检测（最高优先级）
   - 得分=2（经常）：+10分，直接判定高风险
   - 得分=1（有时）：+5分
   - 得分=0（完全不会）：+0分

2. 症状快速恶化检测
   - 快速恶化（≥5分/月）：+5分
   - 恶化（2-4分/月）：+3分
   - 稳定（-1至1分/月）：+0分
   - 改善（≤-2分/月）：-2分

3. 高强度负面情绪占比检测
   - 占比>70%：+3分
   - 占比50-70%：+2分
   - 占比<50%：+0分

4. 情绪波动检测
   - 方差>6（波动大）：+2分
   - 方差4-6（波动中）：+1分
   - 方差<4（波动小）：+0分

5. 危机计划预警信号检测
   - 每出现一个预警信号：+2分

6. 社会退缩检测
   - 严重退缩（独处时间>80%）：+3分
   - 中度退缩（独处时间50-80%）：+2分
   - 轻度/无退缩：+0分

7. 功能受损检测
   - 严重受损（≥5天/周）：+4分
   - 中度受损（3-4天/周）：+2分
   - 轻度/无受损：+0分

风险等级判定：
- 高风险（≥10分）：立即就医，启动危机干预
- 中风险（5-9分）：密切关注，考虑就医（48小时内）
- 低风险（0-4分）：继续监测，定期评估
```

**危机预警信号检测：**
```
- 绝望感（hopelessness）
- 社会退缩（social_withdrawal）
- 极端情绪波动（extreme_mood_swings）
- 谈论死亡（talk_of_death）
- 送走财物（giving_away_possessions）
- 自伤意念（self_harm）
- 自杀想法（suicidal_thoughts）
- 物质滥用（substance_abuse）
```

**紧急行动触发条件：**
```
立即就医（24小时内）：
- PHQ-9第9项得分≥2
- 总风险评分≥10分
- 出现幻觉或妄想
- 有自伤或自杀计划

尽快就医（48小时内）：
- PHQ-9≥15分或GAD-7≥15分
- 总风险评分5-9分
- 症状快速恶化（≥5分/月）
- 严重影响功能

定期就医（1个月内）：
- PHQ-9 10-14分或GAD-7 10-14分
- 总风险评分<5分但症状持续
- 需要专业支持
```

### 第6步：睡眠-心理关联分析

**数据来源：**
- 读取 `data-example/sleep-tracker.json`
- 提取睡眠时长、睡眠质量（PSQI）、入睡时间等数据

**关联分析：**
```
- 睡眠时长与PHQ-9评分的相关性
- 睡眠质量与GAD-7评分的相关性
- 失眠症状与情绪稳定性的关系
- 睡眠改善与心理状态改善的时间关系
- 睡眠障碍类型与特定心理症状的关联
```

**分析输出：**
```
- 相关性系数和统计显著性
- 睡眠对心理状态的影响程度（高/中/低）
- 睡眠改善建议
- 睡眠与情绪的双向关系分析
```

### 第7步：运动-情绪关联分析

**数据来源：**
- 读取 `data-example/fitness-tracker.json`
- 提取运动频率、运动类型、运动强度、运动时长等数据

**关联分析：**
```
- 运动频率与平均情绪强度的关系
- 运动类型与情绪改善效果的关系
- 运动强度与焦虑水平的关系
- 运动时长与情绪持续时间的关系
- 运动后的情绪变化模式
- 运动习惯与抑郁症状的关系
```

**分析输出：**
```
- 运动对情绪的积极影响程度
- 最有效的运动类型推荐
- 最佳运动频率建议
- 运动与应对方式的关系
```

### 第8步：营养-心理关联分析

**数据来源：**
- 读取 `data-example/nutrition-tracker.json`
- 提取咖啡因摄入、糖分摄入、饮食习惯等数据

**关联分析：**
```
- 咖啡因摄入量与GAD-7焦虑评分的关系
- 糖分摄入与情绪波动的关联
- 饮食规律性与情绪稳定性的关系
- 特定营养素缺乏（维生素D、Omega-3）与抑郁症状
- 饮食模式与整体心理健康
```

**分析输出：**
```
- 饮食对心理状态的影响程度
- 营养建议（如减少咖啡因、均衡饮食）
- 可能的营养缺乏提示
- 饮食调整建议
```

### 第9步：慢性病-心理关联分析

**数据来源：**
- 读取相关慢性病数据文件（如 `diabetes-tracker.json`, `hypertension-tracker.json`）
- 提取疾病控制情况、症状负担、功能受限等数据

**关联分析：**
```
- 慢性疼痛与抑郁症状的关系
- 疾病控制情况与心理状态的关系
- 功能受限与心理健康的关系
- 疾病负担与焦虑水平的关系
- 共病模式识别
- 药物副作用对情绪的影响
- 药物依从性与症状改善的关系
```
```

**分析输出：**
```
- 慢性疾病对心理健康的影响程度
- 需要特别关注的心理问题
- 整体健康管理建议
- 心理支持对疾病管理的益处
```

### 第10步：生成报告

输出包括：
- 心理健康状况摘要
- 评估量表趋势分析
- 情绪模式和触发因素
- 治疗进展评估
- 危机风险等级和建议
- 与其他健康因素的关联分析
- 个性化建议和行动计划

## 输出格式

### 心理健康分析报告结构

```markdown
# 心理健康分析报告

**报告日期**: YYYY-MM-DD
**分析周期**: YYYY-MM-DD 至 YYYY-MM-DD
**数据完整性**: 良好

⚠️ **重要提示**：本报告仅供参考，不构成医学诊断。如有严重心理困扰，请寻求专业心理医生帮助。

---

## 危机风险预警

**当前风险等级**: 🟢 低风险 | 🟡 中风险 | 🔴 高风险

**风险评分**: X/20

**风险因素**:
- [列出检测到的风险因素]

**建议行动**:
- [根据风险等级提供具体建议]

---

## 1. 心理健康状况摘要

[整体评价：优秀/良好/一般/需改进/危机]
- PHQ-9评分：X分（严重程度）
- GAD-7评分：X分（严重程度）
- 睡眠质量：X分（PSQI）
- 整体趋势：改善/稳定/恶化

## 2. 心理评估趋势分析

### PHQ-9抑郁评分趋势
- 当前评分：X分
- 基线评分：X分
- 变化：±X分
- 变化速率：X分/月
- 趋势：改善/稳定/恶化
- 严重程度变化：[严重程度1] → [严重程度2]

**图表描述**：
- [折线图展示PHQ-9评分变化]
- [标记严重程度分界线：5, 10, 15]

**特别关注**：
- 第9项（自伤意念）得分：X
- 最高分项：[条目名称]
- 持续存在问题：[列出条目]

### GAD-7焦虑评分趋势
- 当前评分：X分
- 基线评分：X分
- 变化：±X分
- 变化速率：X分/月
- 趋势：改善/稳定/恶化

**图表描述**：
- [折线图展示GAD-7评分变化]
- [标记严重程度分界线：5, 10, 15]

**主要焦虑症状**：
- 最高分项：[条目名称]
- 主要触发因素：[列出]

### PSQI睡眠质量
- 总分：X分
- 睡眠质量：[评价]
- 主要问题：[列出问题成分]

## 3. 情绪模式分析

### 常见情绪
1. [情绪1] - 占比X%，平均强度X/10
2. [情绪2] - 占比X%，平均强度X/10
3. [情绪3] - 占比X%，平均强度X/10

**图表描述**：
- [饼图展示情绪分布]
- [雷达图展示多维度情绪]

### 时间模式
- 早晨：主要情绪[情绪]，平均强度X/10
- 下午：主要情绪[情绪]，平均强度X/10
- 晚上：主要情绪[情绪]，平均强度X/10

### 周模式
- 周一至周五：主要情绪[情绪]，平均强度X/10
- 周末：主要情绪[情绪]，平均强度X/10

### 情绪稳定性
- 波动程度：高/中/低
- 情绪方差：X

**图表描述**：
- [折线图展示情绪强度时序变化]
- [波动范围可视化]

## 4. 触发因素分析

### 高频触发因素（Top 10）
| 排名 | 触发因素 | 频次 | 平均影响 |
|------|----------|------|----------|
| 1 | [触发因素1] | X次 | 高/中/低 |
| 2 | [触发因素2] | X次 | 高/中/低 |
| ... |

### 高危触发因素（高影响+高频）
- [触发因素1] - 频次X，影响高，建议：[应对建议]
- [触发因素2] - 频次X，影响高，建议：[应对建议]

**图表描述**：
- [柱状图展示触发因素频次]
- [热图展示触发因素与情绪类型的关联]

## 5. 应对方式效果评估

### 应对方式排名（按效果）
| 应对方式 | 有效次数 | 无效次数 | 有效率 | 排名 |
|----------|----------|----------|--------|------|
| [应对方式1] | X次 | X次 | XX% | 1 |
| [应对方式2] | X次 | X次 | XX% | 2 |
| ... |

### 高效应对策略（>80%有效）
- [策略1] - 有效率XX%，推荐使用
- [策略2] - 有效率XX%，推荐使用

### 低效应对策略（<50%有效）
- [策略1] - 有效率XX%，建议调整或停止
- [策略2] - 有效率XX%，建议调整或停止

**图表描述**：
- [条形图展示应对方式效果排名]
- [饼图展示有效/无效比例]

## 6. 心理治疗进展

### 治疗概况
- 治疗类型：[CBT/心理动力学/人本主义等]
- 治疗频率：[每周/每两周等]
- 已进行咨询次数：X次
- 治疗时长：X个月

### 治疗目标进展
| 目标 | 基线 | 当前 | 目标 | 进展 | 预计达成时间 |
|------|------|------|------|------|--------------|
| [目标1] | X分 | X分 | X分 | XX% | YYYY-MM-DD |
| [目标2] | X分 | X分 | X分 | XX% | YYYY-MM-DD |

**整体进展评价**：[优秀/良好/一般/需改进]

### 症状改善
- PHQ-9评分变化：X分 → X分，改善XX%
- GAD-7评分变化：X分 → X分，改善XX%
- 整体功能水平：[改善/稳定/恶化]

### 作业完成情况
- 平均完成率：XX%
- 高质量完成：XX%
- 需要加强的方面：[列出]

## 7. 危机风险评估

### 风险等级
**当前风险等级**: 🟢 低风险 | 🟡 中风险 | 🔴 高风险

**风险评分**: X/20

### 风险因素分析
| 风险因素 | 得分 | 详情 |
|----------|------|------|
| PHQ-9第9项 | X分 | 得分X，[详情] |
| 症状变化 | X分 | [快速恶化/恶化/稳定/改善] |
| 情绪强度 | X分 | 高强度负面情绪占比XX% |
| 情绪波动 | X分 | 波动[大/中/小] |
| 预警信号 | X分 | 出现X个预警信号：[列出] |
| 社会退缩 | X分 | [严重/中度/轻度/无]退缩 |
| 功能受损 | X分 | [严重/中度/轻度/无]受损 |

### 检测到的预警信号
- [如有列出]

### 建议行动
- [根据风险等级提供具体行动建议]

### 紧急资源
- 心理危机热线：400-xxx-xxxx（24小时）
- 精神科急诊：就近三甲医院
- 急救电话：120

## 8. 与其他健康因素的关联分析

### 睡眠-心理关联
**关联强度**: 高/中/低

**主要发现**:
- 睡眠时长与PHQ-9评分的相关性：r=X.XX
- 睡眠质量与情绪稳定性的关系：[描述]
- 主要睡眠问题：[列出]
- 改善睡眠对心理状态的潜在益处：[描述]

**建议**:
- [具体的睡眠改善建议]

### 运动-情绪关联
**关联强度**: 高/中/低

**主要发现**:
- 运动频率与情绪改善的关系：[描述]
- 最有效的运动类型：[列出]
- 运动后的情绪变化：[描述]

**建议**:
- [具体的运动建议]

### 营养-心理关联
**关联强度**: 高/中/低

**主要发现**:
- 咖啡因摄入与焦虑的关系：[描述]
- 糖分摄入与情绪波动的关系：[描述]
- 可能的营养缺乏：[列出]

**建议**:
- [具体的营养建议]

### 慢性病-心理关联
**关联强度**: 高/中/低

**主要发现**:
- [慢性病]与心理状态的关系：[描述]
- 疾病负担对心理健康的影响：[描述]
- 功能受限与情绪的关系：[描述]

**建议**:
- [具体的整体健康管理建议]

## 9. 综合建议

### 立即行动（如适用）
- [如有紧急问题，列出立即需要采取的行动]

### 本周行动计划
1. [行动项1] - 优先级：高/中/低
2. [行动项2] - 优先级：高/中/低
3. ...

### 本月目标
1. [目标1]
2. [目标2]
3. ...

### 继续保持的方面
- [列出做得好的方面，鼓励继续保持]

### 需要改进的方面
- [列出需要改进的方面，提供具体建议]

### 推荐资源
- [书籍/APP/支持团体/在线资源等]

## 10. 数据质量说明

- 数据完整性：[优秀/良好/一般/需改进]
- PHQ-9评估次数：X次
- GAD-7评估次数：X次
- 情绪日记条目：X条
- 时间跨度：X天

---

**报告生成时间**: YYYY-MM-DD HH:MM:SS
**下次评估建议时间**: YYYY-MM-DD

⚠️ **免责声明**：本报告由心理健康分析技能自动生成，仅供参考，不构成医学诊断或治疗建议。如有任何心理健康问题，请寻求专业心理医生或精神科医生的帮助。
```

## 使用示例

### 示例1：趋势分析

**用户输入**：
```
/mental trend 3months
```

**技能执行**：
1. 读取最近3个月的PHQ-9和GAD-7评估数据
2. 计算评分变化速率和趋势
3. 分析严重程度变化
4. 检测PHQ-9第9项变化
5. 生成趋势报告

**输出**：
```markdown
# 心理健康趋势分析（近3个月）

## 整体趋势
- PHQ-9：14分 → 8分，改善6分，趋势：改善 ✓
- GAD-7：12分 → 6分，改善6分，趋势：改善 ✓
- 变化速率：约2分/月

## 严重程度变化
- PHQ-9：中度抑郁 → 轻度抑郁 ✓
- GAD-7：中度焦虑 → 轻度焦虑 ✓

## 积极信号
- 症状持续改善
- PHQ-9第9项得分：1 → 0 ✓
- 治疗效果良好

## 建议
- 继续当前治疗
- 保持运动和睡眠习惯
- 下次评估：1个月后
```

### 示例2：情绪模式分析

**用户输入**：
```
/mental pattern
```

**技能执行**：
1. 读取情绪日记数据
2. 统计常见情绪和时间模式
3. 分析触发因素和应对方式
4. 生成模式识别报告

**输出**：
```markdown
# 情绪模式分析

## 常见情绪（Top 3）
1. 焦虑 - 占比35%，平均强度7/10
2. 疲劳 - 占比25%，平均强度6/10
3. 平静 - 占比20%，平均强度7/10

## 时间模式
- 早晨：平静（强度7/10）😌
- 下午：焦虑（强度7/10）😰
- 晚上：疲劳（强度6/10）😴

## 主要触发因素（Top 5）
1. 工作压力 - 12次，影响高
2. 睡眠不足 - 8次，影响中
3. 运动 - 6次，影响积极
4. 社交 - 5次，影响积极
5. 交通拥堵 - 4次，影响中

## 高效应对策略
1. 运动 - 有效率90% ✓
2. 冥想 - 有效率85% ✓
3. 深呼吸 - 有效率75% ✓

## 建议
- 下午工作压力大时，可使用深呼吸或短暂散步
- 保持规律运动，对情绪改善效果显著
- 改善睡眠有助于减轻焦虑和疲劳
```

### 示例3：危机风险评估

**用户输入**：
```
/crisis assessment
```

**技能执行**：
1. 读取最近的PHQ-9/GAD-7评估
2. 读取最近的情绪日记
3. 执行危机风险检测算法
4. 计算风险评分和等级
5. 生成危机风险报告

**输出**：
```markdown
# 危机风险评估

## 当前风险等级：🟢 低风险

**风险评分**: 3/20

## 风险因素分析
| 风险因素 | 得分 | 详情 |
|----------|------|------|
| PHQ-9第9项 | 0分 | 得分0，无自伤意念 ✓ |
| 症状变化 | -2分 | 改善趋势 ✓ |
| 情绪强度 | 2分 | 高强度负面情绪占比45% |
| 情绪波动 | 1分 | 波动中等 |
| 预警信号 | 0分 | 未检测到 ✓ |
| 社会退缩 | 0分 | 社交活动良好 ✓ |
| 功能受损 | 0分 | 功能正常 ✓ |
| **总分** | **3分** | **低风险** ✓ |

## 建议行动
- 继续监测心理状态
- 保持健康的生活习惯
- 定期进行心理评估（每月1次）
- 继续心理治疗（如有）

## 紧急资源（备用）
- 心理危机热线：400-xxx-xxxx（24小时）
- 精神科急诊：就近三甲医院
- 急救电话：120

⚠️ 如出现以下情况，请立即寻求专业帮助：
- 有自伤或自杀想法或计划
- 幻觉、妄想
- 完全失去功能
- 无法控制的情绪爆发
```

### 示例4：治疗进展分析

**用户输入**：
```
/mental therapy progress
```

**技能执行**：
1. 读取治疗记录和目标
2. 计算目标完成百分比
3. 分析症状改善程度
4. 评估作业完成情况
5. 生成治疗进展报告

**输出**：
```markdown
# 心理治疗进展分析

## 治疗概况
- 治疗类型：CBT（认知行为治疗）
- 治疗频率：每周1次
- 已进行咨询：24次
- 治疗时长：5个月

## 治疗目标进展
| 目标 | 基线 | 当前 | 目标 | 进展 | 预计达成时间 |
|------|------|------|------|------|--------------|
| 降低焦虑水平 | 14分 | 8分 | 5分 | 57% | 2025-08-01 |
| 改善睡眠质量 | 10分 | 6分 | 4分 | 60% | 2025-07-15 |
| 增加愉快活动 | 2次/周 | 5次/周 | 7次/周 | 50% | 2025-07-01 |

**整体进展评价**: 良好 ✓

## 症状改善
- PHQ-9评分：14分 → 8分，改善43% ✓
- GAD-7评分：14分 → 6分，改善57% ✓
- 整体功能水平：显著改善 ✓

## 作业完成情况
- 平均完成率：85%
- 高质量完成：60%
- 需要加强：认知重构练习

## 治疗亮点
- 焦虑症状显著改善
- 睡眠质量明显提升
- 行为激活效果良好
- 认知扭曲识别能力提升

## 继续保持
- 每周心理咨询
- 每日放松练习
- 行为激活（运动、社交）
- 思维记录

## 需要加强
- 认知重构练习
- 应对技巧应用
- 睡眠卫生维持
```

### 示例5：关联分析

**用户输入**：
```
/mental analysis correlations
```

**技能执行**：
1. 读取心理健康、睡眠、运动、营养、慢性病数据
2. 计算相关性系数
3. 分析影响程度
4. 生成关联分析报告

**输出**：
```markdown
# 心理健康关联分析

## 睡眠-心理关联（关联强度：高）

### 主要发现
- 睡眠时长与PHQ-9评分呈负相关（r=-0.72, p<0.01）
- 睡眠质量与情绪稳定性呈正相关（r=0.68, p<0.01）
- PSQI评分每改善1分，PHQ-9评分平均降低1.2分

### 睡眠问题影响
- 入睡困难 → 次日焦虑增加40%
- 夜间易醒 → 次日情绪低落增加35%
- 睡眠不足 → 注意力不集中，情绪波动加大

### 建议
- 保持规律作息，每晚23:00前入睡
- 改善睡眠卫生：避免咖啡因下午摄入
- 继续放松练习，促进睡眠

## 运动-情绪关联（关联强度：高）

### 主要发现
- 运动频率与积极情绪占比呈正相关（r=0.75, p<0.01）
- 运动日情绪平均强度比非运动日高1.5分
- 运动后焦虑感平均降低50%

### 最有效的运动类型
1. 有氧运动（跑步、游泳）- 改善率85%
2. 瑜伽 - 改善率80%
3. 户外散步 - 改善率75%

### 建议
- 保持每周3-5次运动，每次30分钟以上
- 优先选择有氧运动
- 焦虑时可进行户外散步

## 营养-心理关联（关联强度：中）

### 主要发现
- 咖啡因摄入与GAD-7评分呈正相关（r=0.52, p<0.05）
- 高糖饮食与情绪波动呈正相关（r=0.48, p<0.05）
- Omega-3摄入不足可能与抑郁症状相关

### 建议
- 减少咖啡因摄入（每天≤2杯）
- 减少添加糖摄入
- 考虑补充Omega-3（咨询医生）

## 综合建议
基于关联分析，以下生活方式对改善心理健康最有效：
1. **规律运动**（每周3-5次，30分钟+）
2. **充足睡眠**（7-8小时，23:00前入睡）
3. **均衡饮食**（减少咖啡因和糖分）
4. **持续治疗**（CBT心理治疗）

这4个方面的综合干预对您的心理健康改善贡献率为**75%**。
```

### 示例6：完整报告生成

**用户输入**：
```
/mental report
```

**技能执行**：
1. 读取所有相关数据
2. 执行完整分析流程
3. 生成交互式HTML报告
4. 包含危机警告和建议

**输出**：
生成完整的心理健康分析报告HTML文件，包含：
- 所有图表（ECharts交互式图表）
- 危机风险警告（如适用）
- 详细分析和建议
- 可下载或打印

---

## 错误处理

### 数据文件不存在
```
错误：未找到心理健康数据文件
建议：请先使用 /mental assess 或 /mental mood 命令创建数据
```

### 数据不足
```
警告：数据不足以进行趋势分析
建议：至少需要3次PHQ-9/GAD-7评估或7天情绪日记
当前数据：PHQ-9评估X次，情绪日记X条
```

### 危机风险高
```
🔴 危机警告：检测到高风险因素

立即行动：
1. 联系心理危机热线：400-xxx-xxxx（24小时）
2. 前往最近的精神科急诊
3. 拨打急救电话：120
4. 联系家人或朋友陪伴

检测到的风险因素：
- [列出高风险因素]

不要犹豫，立即寻求专业帮助！
```

## 数据源说明

**主要数据源**：
- `data-example/mental-health-tracker.json` - 心理健康主数据
- `data-example/mental-health-logs/` - 情绪日记日志

**关联数据源**：
- `data-example/sleep-tracker.json` - 睡眠数据
- `data-example/fitness-tracker.json` - 运动数据
- `data-example/nutrition-tracker.json` - 营养数据
- `data-example/diabetes-tracker.json` - 糖尿病数据（如适用）
- `data-example/hypertension-tracker.json` - 高血压数据（如适用）
- `data-example/medication-tracker.json` - 用药数据

## 性能优化

对于大量数据（如>6个月的情绪日记），采用以下优化策略：
- 数据聚合：按周/月聚合情绪数据
- 抽样分析：随机抽样代表性数据点
- 增量分析：仅分析新增数据
- 缓存中间结果

---

**技能版本**: v1.0.0
**最后更新**: 2025-01-06
**维护者**: WellAlly Tech

## Source: references/skills/healthcare-workflows/references/legacy/nutrition-analyzer/SKILL.md

---
name: nutrition-analyzer
description: 分析营养数据、识别营养模式、评估营养状况，并提供个性化营养建议。支持与运动、睡眠、慢性病数据的关联分析。
allowed-tools: Read, Grep, Glob, Write
---

# 营养分析器技能

分析饮食和营养数据，识别营养模式，评估营养状况，并提供个性化营养改善建议。

## 功能

### 1. 营养趋势分析

分析营养素摄入的变化趋势，识别改善或需要关注的方面。

**分析维度**：
- 宏量营养素趋势（蛋白质、碳水、脂肪、纤维、卡路里）
- 微量营养素趋势（维生素、矿物质）
- 热量来源分布变化
- 餐食模式（饮食时间、频率）
- 食物类别偏好

**输出**：
- 趋势方向（改善/稳定/下降）
- 变化幅度和百分比
- 趋势显著性
- 改进建议

### 2. 营养素摄入评估

评估营养素摄入是否达到推荐标准（RDA/AI）。

**评估内容**：
- **宏量营养素评估**：
  - 蛋白质摄入量和质量
  - 碳水化合物类型分布（精制 vs 复杂碳水）
  - 脂肪类型分布（饱和/单不饱和/多不饱和/反式脂肪）
  - 膳食纤维摄入量

- **维生素评估**：
  - 维生素A、C、D、E、K
  - 维生素B族（B1、B2、B3、B6、B12、叶酸、泛酸、生物素）
  - 与RDA对比
  - 缺乏风险评估

- **矿物质评估**：
  - 常量矿物质：钙、磷、镁、钠、钾、氯、硫
  - 微量矿物质：铁、锌、铜、锰、碘、硒、铬、钼
  - 与RDA对比
  - 缺乏风险评估

- **特殊营养素评估**：
  - Omega-3脂肪酸（EPA、DHA、ALA）
  - 胆碱
  - 辅酶Q10
  - 植物化学物（类黄酮、类胡萝卜素等）

**输出**：
- 每种营养素的达成率
- 缺乏/不足/充足/过量分级
- 缺乏风险识别
- 优先改善建议

### 3. 营养状况评估

综合评估用户的营养状况。

**评估内容**：
- **整体营养质量评分**：
  - 营养密度评分
  - 食物多样性评分
  - 均衡饮食评分

- **营养模式识别**：
  - 饮食模式类型（地中海式、DASH、素食等）
  - 饮食时间模式（进食频率、进食窗口）
  - 零食和加餐模式

- **营养风险识别**：
  - 营养缺乏风险（如维生素D缺乏、铁缺乏）
  - 营养过量风险（如维生素A过量、钠过量）
  - 不健康饮食习惯（高糖、高脂、高钠）

**输出**：
- 营养状况等级（优秀/良好/一般/较差）
- 主要营养问题识别
- 风险因素列表
- 改善优先级

### 4. 相关性分析

分析营养与其他健康指标的相关性。

**支持的相关性分析**：
- **营养 ↔ 体重**：
  - 卡路里摄入与体重变化的关系
  - 宏量营养素比例与体重管理
  - 进食时间与代谢关系

- **营养 ↔ 运动**：
  - 营养摄入对运动表现的影响
  - 运动日vs休息日的营养需求
  - 蛋白质摄入与肌肉恢复

- **营养 ↔ 睡眠**：
  - 咖啡因摄入与睡眠质量
  - 晚餐时间与入睡时间
  - 特定营养素（如镁、色氨酸）与睡眠

- **营养 ↔ 血压**：
  - 钠摄入与血压
  - 钾/钠比值与血压
  - DASH饮食依从性与血压控制

- **营养 ↔ 血糖**：
  - 碳水化合物类型与血糖波动
  - 膳食纤维与血糖控制
  - 进食时间与血糖曲线

**输出**：
- 相关系数（-1到1）
- 相关性强度（弱/中/强）
- 统计显著性
- 因果关系推断
- 实践建议

### 5. 个性化建议生成

基于用户数据生成个性化营养改善建议。

**建议类型**：
- **营养素调整建议**：
  - 增加缺乏的营养素
  - 减少过量的营养素
  - 优化营养素比例

- **食物选择建议**：
  - 推荐特定食物类别
  - 食物替换建议（更健康的选择）
  - 食物搭配建议（促进吸收）

- **饮食习惯建议**：
  - 进食时间调整
  - 餐食频率调整
  - 烹饪方式建议

- **补充剂建议**（仅供参考）：
  - 基于缺乏风险的补充剂建议
  - 补充剂剂量和时机
  - 相互作用警示

**建议依据**：
- DRIs/RDA标准
- 用户营养历史数据
- 用户健康状况和目标
- 循证营养学证据

---

## 使用说明

### 触发条件

当用户请求以下内容时触发本技能：
- 营养趋势分析
- 营养素摄入评估
- 营养状况评估
- 营养改善建议
- 营养与其他健康指标的关联分析

### 执行步骤

#### 步骤 1: 确定分析范围

明确用户请求的分析类型和时间范围：
- 分析类型：趋势/评估/相关性/建议
- 时间范围：周/月/季度/自定义
- 分析深度：宏量营养素/微量营养素/全面分析

#### 步骤 2: 读取数据

**主要数据源**：
1. `data-example/nutrition-tracker.json` - 营养追踪主数据
2. `data-example/nutrition-logs/YYYY-MM/YYYY-MM-DD.json` - 每日饮食记录

**关联数据源**：
1. `data-example/profile.json` - 体重、BMI等基础数据
2. `data-example/fitness-tracker.json` - 运动数据
3. `data-example/sleep-tracker.json` - 睡眠数据
4. `data-example/hypertension-tracker.json` - 血压数据
5. `data-example/diabetes-tracker.json` - 血糖数据

#### 步骤 3: 数据分析

根据分析类型执行相应的分析算法：

**趋势分析算法**：
- 线性回归计算趋势斜率
- 移动平均平滑波动
- 统计显著性检验

**RDA达成率计算**：
```python
rda_achievement = (actual_intake / rda_value) * 100

status_classification:
- < 50%: 严重缺乏
- 50-75%: 不足
- 75-100%: 接近目标
- 100-150%: 充足（理想范围）
- > 150%: 过量（注意安全上限UL）
```

**营养密度评分**：
```python
nutrient_density_score = (
    (vitamins_achieved / total_vitamins) * 40 +
    (minerals_achieved / total_minerals) * 30 +
    (fiber_achieved / fiber_rda) * 30
)
```

**相关性分析算法**：
- Pearson相关系数计算
- 滞后相关性分析（考虑时间延迟效应）
- 多变量回归分析

#### 步骤 4: 生成报告

按照标准格式输出分析报告（见"输出格式"部分）

---

## 输出格式

### 营养趋势分析报告

```markdown
# 营养摄入趋势分析报告

## 分析周期
2025-03-20 至 2025-06-20（3个月，90天记录）

## 宏量营养素趋势

### 卡路里摄入
- **趋势**：⬇️ 下降
- **开始**：平均2100卡/天
- **当前**：平均1950卡/天
- **变化**：-150卡/天 (-7.1%)
- **解读**：卡路里摄入适度减少，与减重目标一致

**趋势线**：
```
2100 ┤ ╭╮
2050 ┤ ╭╯╰╮
2000 ┼─╯   ╰╮
1950 ┤      ╰
1900 └───────────
     3月  4月  5月  6月
```

### 蛋白质
- **趋势**：➡️ 稳定
- **平均**：82g/天（范围：70-95g）
- **目标**：80g/天
- **达标率**：93%（84/90天达标）
- **解读**：蛋白质摄入稳定，基本达标

### 膳食纤维
- **趋势**：⬆️ 改善
- **开始**：平均18g/天
- **当前**：平均22g/天
- **变化**：+4g/天 (+22%)
- **目标**：30g/天
- **解读**：纤维摄入显著增加，但仍需继续努力

### 脂肪
- **趋势**：⬇️ 下降
- **开始**：平均75g/天
- **当前**：平均68g/天
- **变化**：-7g/天 (-9.3%)
- **目标**：≤65g/天
- **解读**：脂肪摄入减少，接近目标

**脂肪类型分布变化**：
| 脂肪类型 | 开始 | 当前 | 目标 | 趋势 |
|---------|------|------|------|------|
| 饱和脂肪 | 25g | 20g | <20g | ⬇️ 改善 |
| 单不饱和 | 30g | 32g | >35g | ⬆️ 略增 |
| 多不饱和 | 15g | 12g | 15-20g | ⬇️ 需增加 |
| 反式脂肪 | 2g | 0.5g | 0g | ⬇️ 改善 |

## 维生素状况趋势

### 维生素D
- **摄入趋势**：⬆️ 增加（补充剂开始）
- **开始**：平均2μg/天（饮食来源）
- **当前**：平均52μg/天（含2000IU补充剂）
- **RDA**：15μg/天
- **血清水平变化**：
  - 基线（2025-05）：18 ng/mL
  - 当前（2025-06）：22 ng/mL
  - 目标：30-100 ng/mL
- **解读**：✅ 补充剂起效，但需继续监测

### 维生素C
- **趋势**：⬆️ 改善
- **开始**：平均65mg/天
- **当前**：平均85mg/天
- **RDA**：100mg/天
- **达标率**：从65% → 85%
- **建议**：增加柑橘类、奇异果、草莓等水果

### B族维生素
- **维生素B12**：✅ 充足（平均2.5μg，RDA 2.4μg）
- **叶酸**：⚠️ 不足（平均320μg，RDA 400μg）
- **B6**：✅ 充足（平均1.5mg，RDA 1.3mg）

## 矿物质趋势

### 钙
- **趋势**：➡️ 稳定
- **平均**：850mg/天
- **RDA**：1000mg/天
- **达标率**：85%
- **主要来源**：乳制品40%、豆腐25%、绿叶蔬菜20%

### 铁
- **趋势**：✅ 充足
- **平均**：12mg/天
- **RDA**：8mg/天（男性）
- **达标率**：150%
- **主要来源**：肉类、蛋类、豆类、绿叶蔬菜

### 钠
- **趋势**：⬇️ 改善
- **开始**：平均2800mg/天
- **当前**：平均2100mg/天
- **目标**：<2300mg/天（理想<1500mg）
- **解读**：✅ 达到一般目标，⚠️ 理想目标仍需努力

### 钾
- **趋势**：⬆️ 改善
- **开始**：平均2800mg/天
- **当前**：平均3200mg/天
- **目标**：3500-4700mg/天
- **钾/钠比值**：从1.0 → 1.5（目标>2）
- **建议**：继续增加水果和蔬菜

## 特殊营养素趋势

### Omega-3
- **趋势**：⬆️ 增加（鱼油补充剂）
- **开始**：平均150mg/天
- **当前**：平均850mg/天（含补充剂）
- **推荐量**：500-1000mg/天
- **状态**：✅ 达标

### 胆碱
- **趋势**：➡️ 稳定
- **平均**：350mg/天
- **AI（适宜摄入量）**：425mg/天
- **达标率**：82%
- **主要来源**：鸡蛋（60%）、肉类（25%）、豆类（15%）

## 饮食模式分析

### 食物类别分布
| 食物类别 | 占比 | 变化 | 评价 |
|---------|------|------|------|
| 蔬菜水果 | 35% | +8% | ✅ 增加 |
| 全谷物 | 20% | +5% | ✅ 改善 |
| 精制谷物 | 15% | -7% | ✅ 减少 |
| 蛋白质来源 | 20% | 稳定 | ✅ 充足 |
| 添加脂肪 | 8% | -3% | ✅ 减少 |
| 添加糖 | 2% | -2% | ✅ 减少 |

### 进食时间模式
- **平均进食窗口**：12.5小时（07:30 - 20:00）
- **进食频率**：平均4.2次/天
- **最常见餐食时间**：
  - 早餐：07:30（90%天数）
  - 午餐：12:15（95%天数）
  - 晚餐：18:45（98%天数）
  - 加餐：15:30（60%天数）

### 饮食质量评分
- **营养密度评分**：7.2/10（从6.5提升）
- **食物多样性评分**：6.8/10
- **均衡饮食评分**：7.5/10
- **综合评分**：7.2/10 → **良好**

## 洞察与建议

### 关键洞察

1. **膳食纤维持续改善但仍不足**
   - 从18g增至22g，但仍低于目标30g
   - 影响：饱腹感、肠道健康、血糖控制
   - 建议：每餐至少包含5g纤维

2. **脂肪质量改善**
   - 饱和脂肪减少，反式脂肪几乎消除
   - 多不饱和脂肪略低，需增加Omega-3食物
   - 建议：增加深海鱼类、坚果、亚麻籽

3. **钠摄入改善但钾/钠比仍低**
   - 钠减少33%，钾增加14%
   - 钾/钠比从1.0升至1.5，仍低于目标2.0
   - 建议：继续增加高钾食物（香蕉、橙子、土豆、菠菜）

4. **维生素D补充剂有效**
   - 血清水平从18升至22 ng/mL（4周+4ng）
   - 预计3-4个月可达目标范围
   - 建议：继续补充，定期监测

### 优先级行动计划

#### Priority 1：提升膳食纤维至30g/天（2周）

**具体行动**：
1. 早餐：全谷物（燕麦/全麦面包）+ 水果（9g）
2. 午餐：糙米/全麦面 + 2份蔬菜（8g）
3. 晚餐：红薯/杂粮 + 2份蔬菜（8g）
4. 加餐：水果 + 坚果（5g）
**总计**：30g ✅

#### Priority 2：优化钾/钠比值至2.0（4周）

**具体行动**：
1. 减少加工食品（主要钠源）
2. 每日2-3份高钾水果（香蕉、橙子、猕猴桃）
3. 蔬菜选择菠菜、土豆、蘑菇、番茄
4. 使用香料替代盐调味

#### Priority 3：维持维生素D补充（长期）

**监测计划**：
- 3个月后复查血清水平
- 目标：40-60 ng/mL
- 根据结果调整剂量

## 营养目标进度

| 目标 | 开始 | 当前 | 目标值 | 进度 | 状态 |
|------|------|------|--------|------|------|
| 卡路里 | 2100 | 1950 | 1800-2000 | 100% | ✅ 达标 |
| 蛋白质 | 75g | 82g | 80g | 100% | ✅ 达标 |
| 膳食纤维 | 18g | 22g | 30g | 73% | ⚠️ 进行中 |
| 维生素D | 18 ng/mL | 22 ng/mL | 30-100 | 20% | ⚠️ 改善中 |
| 钠摄入 | 2800mg | 2100mg | <2300 | 100% | ✅ 达标 |
| Omega-3 | 150mg | 850mg | 500-1000mg | 100% | ✅ 达标 |

---

**报告生成时间**：2025-06-20
**分析周期**：2025-03-20 至 2025-06-20（90天）
**数据记录数**：90天
**营养分析器版本**：v1.0
```

---

## 数据结构

### 饮食记录数据

```json
{
  "date": "2025-06-20",
  "meals": [
    {
      "type": "breakfast",
      "time": "07:30",
      "foods": ["鸡蛋", "牛奶", "全麦面包"],
      "calories": 450,
      "macronutrients": {
        "protein_g": 20,
        "carbs_g": 55,
        "fat_g": 15,
        "fiber_g": 5,
        "saturated_fat_g": 5,
        "monounsaturated_fat_g": 6,
        "polyunsaturated_fat_g": 3,
        "trans_fat_g": 0.1
      },
      "micronutrients": {
        "vitamin_a_mcg": 150,
        "vitamin_c_mg": 5,
        "vitamin_d_mcg": 1.5,
        "vitamin_e_mg": 1,
        "vitamin_k_mcg": 5,
        "thiamine_mg": 0.3,
        "riboflavin_mg": 0.4,
        "niacin_mg": 4,
        "vitamin_b6_mg": 0.1,
        "folate_mcg": 30,
        "vitamin_b12_mcg": 0.6,
        "calcium_mg": 250,
        "iron_mg": 2,
        "magnesium_mg": 40,
        "phosphorus_mg": 200,
        "zinc_mg": 2,
        "selenium_mcg": 10,
        "potassium_mg": 350,
        "sodium_mg": 300
      },
      "special_nutrients": {
        "omega_3_g": 0.1,
        "choline_mg": 150
      }
    }
  ],
  "daily_summary": {
    "total_calories": 2000,
    "total_macronutrients": {
      "protein_g": 80,
      "carbs_g": 250,
      "fat_g": 65,
      "fiber_g": 30
    },
    "rda_achievement": {
      "protein": 100,
      "vitamin_c": 85,
      "vitamin_d": 35,
      "calcium": 90,
      "iron": 75
    },
    "goal_achieved": true
  }
}
```

---

## 算法说明

### RDA达成率计算

```python
def calculate_rda_achievement(actual_intake, rda_value, ul_value=None):
    """
    计算RDA达成率和状态

    参数：
    - actual_intake: 实际摄入量
    - rda_value: 推荐膳食供给量
    - ul_value: 可耐受最高摄入量（可选）

    返回：
    - achievement_rate: 达成率百分比
    - status: 状态标签
    """
    achievement_rate = (actual_intake / rda_value) * 100

    if ul_value and actual_intake > ul_value:
        status = "exceeds_ul"
        category = "过量（危险）"
    elif achievement_rate < 50:
        status = "severe_deficiency"
        category = "严重缺乏"
    elif achievement_rate < 75:
        status = "insufficient"
        category = "不足"
    elif achievement_rate < 100:
        status = "approaching_target"
        category = "接近目标"
    elif achievement_rate <= 150:
        status = "adequate"
        category = "充足"
    else:
        status = "high_intake"
        category = "较高"

    return {
        'achievement_rate': round(achievement_rate, 1),
        'status': status,
        'category': category
    }
```

### 营养密度评分

```python
def calculate_nutrient_density_score(meal_data):
    """
    计算食物营养密度评分（0-10分）

    因素权重：
    - 维生素达成率：40%
    - 矿物质达成率：30%
    - 膳食纤维：20%
    - 限制性营养素（饱和脂肪、钠、添加糖）：10%
    """
    score = 0

    # 维生素评分
    vitamin_achievements = [
        meal_data['micronutrients'][v] / RDA[v]
        for v in ['vitamin_a', 'vitamin_c', 'vitamin_d', 'vitamin_e', 'vitamin_k']
    ]
    vitamin_score = min(sum(vitamin_achievements) / len(vitamin_achievements), 1.5) * 10
    score += min(vitamin_score, 10) * 0.40

    # 矿物质评分
    mineral_achievements = [
        meal_data['micronutrients'][m] / RDA[m]
        for m in ['calcium', 'iron', 'magnesium', 'zinc']
    ]
    mineral_score = min(sum(mineral_achievements) / len(mineral_achievements), 1.5) * 10
    score += min(mineral_score, 10) * 0.30

    # 膳食纤维评分
    fiber_score = min(meal_data['macronutrients']['fiber_g'] / 5, 2) * 10
    score += min(fiber_score, 10) * 0.20

    # 限制性营养素扣分
    penalty = 0
    if meal_data['macronutrients']['saturated_fat_g'] > 10:
        penalty += 2
    if meal_data['micronutrients']['sodium_mg'] > 600:
        penalty += 2
    if meal_data.get('added_sugars_g', 0) > 10:
        penalty += 2

    score = max(0, score - penalty * 0.10)

    return round(score, 1)
```

### 健康饮食指数评分

```python
def calculate_healthy_eating_index(daily_data):
    """
    计算健康饮食指数（HEI-2015改编）

    评分范围：0-100分
    """
    score = 0

    # 充足性成分（满分50分）
    # 1. 水果（5分）
    fruit_servings = daily_data['fruit_servings']
    score += min(fruit_servings, 2.5) * 2

    # 2. 蔬菜（5分）
    veg_servings = daily_data['vegetable_servings']
    score += min(veg_servings, 3) * 1.67

    # 3. 全谷物（10分）
    whole_grains_oz = daily_data['whole_grains_oz']
    score += min(whole_grains_oz, 3) * 3.33

    # 4. 乳制品（10分）
    dairy_servings = daily_data['dairy_servings']
    score += min(dairy_servings, 3) * 3.33

    # 5. 蛋白质（5分）
    protein_oz = daily_data['protein_oz']
    score += min(protein_oz, 5) * 1

    # 6. 海鲜/植物蛋白（5分）
    plant_protein_oz = daily_data['plant_protein_oz']
    score += min(plant_protein_oz, 2) * 2.5

    # 7. 脂肪酸比例（10分）
    fat_ratio = daily_data['unsaturated_fat_g'] / max(daily_data['saturated_fat_g'], 1)
    score += min(fat_ratio, 2.5) * 4

    # 适度性成分（满分40分，反向计分）
    # 8. 精制谷物（10分，越少越好）
    refined_grains_oz = daily_data['refined_grains_oz']
    score += max(10 - refined_grains_oz * 2, 0)

    # 9. 钠（10分，越少越好）
    sodium_g = daily_data['sodium_mg'] / 1000
    score += max(10 - sodium_g * 2, 0)

    # 10. 添加糖（10分，越少越好）
    added_sugars_pct = daily_data['added_sugars_g'] / (daily_data['total_calories'] / 100)
    score += max(10 - added_sugars_pct * 10, 0)

    # 11. 饱和脂肪（10分，越少越好）
    saturated_fat_pct = daily_data['saturated_fat_g'] / (daily_data['total_calories'] / 100)
    score += max(10 - saturated_fat_pct * 10, 0)

    return round(score, 1)
```

---

## 医学安全边界

⚠️ **重要声明**

本分析仅供健康参考，不构成医疗诊断或营养处方。

### 分析能力范围

✅ **能做到**：
- 营养数据统计和分析
- 趋势识别和可视化
- RDA达成率计算
- 营养缺乏风险评估
- 一般性营养建议
- 补充剂相互作用检查

❌ **不做到**：
- 诊断营养缺乏疾病
- 开具补充剂处方
- 替代注册营养师
- 处理严重营养不良
- 评估食物过敏

### 危险信号检测

在分析过程中检测以下危险信号：

1. **营养素过量**：
   - 维生素A > 3000μg（长期）
   - 维生素D > 100μg（长期）
   - 铁 > 45mg（长期）
   - 硒 > 400μg
   - 钠 > 2300mg（持续）

2. **营养素缺乏**：
   - 维生素D < 10μg/天（血清<12 ng/mL）
   - 维生素B12 < 1.5μg/天（素食者）
   - 铁 < 6mg/天（育龄女性）
   - 钙 < 500mg/天

3. **能量摄入异常**：
   - 持续<1200卡/天（可能营养不良）
   - 持续>3500卡/天（可能超重）

4. **饮食模式异常**：
   - 膳食纤维<10g/天
   - 添加糖>25%热量
   - 饱和脂肪>15%热量

### 建议分级

**Level 1: 一般性建议**
- 基于DRIs/RDA标准
- 适用于一般人群
- 无需医疗监督

**Level 2: 参考性建议**
- 基于用户数据和健康状况
- 需结合个人情况
- 建议咨询营养师

**Level 3: 医疗建议**
- 涉及疾病管理或补充剂
- 需医生确认
- 不得自行调整药物剂量

---

## 参考资源

- 中国居民膳食营养素参考摄入量 (DRIs)：http://www.cnsoc.org/
- 美国膳食指南：https://www.dietaryguidelines.gov/
- USDA FoodData Central：https://fooddatacentral.usda.gov/
- WHO营养建议：https://www.who.int/nutrition/
- 补充剂相互作用数据库：https://naturalmedicines.therapeuticresearch.com/

---

**技能版本**: v1.0
**创建日期**: 2026-01-06
**维护者**: WellAlly Tech

## Source: references/skills/healthcare-workflows/references/legacy/occupational-health-analyzer/SKILL.md

---
name: occupational-health-analyzer
description: 分析职业健康数据、识别工作相关健康风险、评估职业健康状况、提供个性化职业健康建议。支持与睡眠、运动、心理健康等其他健康数据的关联分析。
allowed-tools: Read, Grep, Glob, Write, Edit
---

# 职业健康分析技能

## 核心功能

职业健康分析技能提供全面的职业健康数据分析功能，帮助用户追踪工作相关健康问题、识别职业健康风险、评估工作环境人机工程水平和优化职业健康。

**主要功能模块：**

1. **职业健康风险评估** - 久坐、视屏终端、倒班工作、重复性劳损、工作压力等多维度风险评估
2. **工作相关问题追踪** - 颈肩腰腿痛、眼疲劳、腕管综合征等症状监测
3. **人机工程评估** - 工作站、椅子、显示器、键盘、环境等全方位评估
4. **职业病筛查** - 基于工作类型的职业病风险评估和筛查建议
5. **趋势分析** - 症状发展、改善效果、风险变化趋势
6. **关联分析** - 与睡眠、运动、心理健康、慢性病模块的关联分析
7. **个性化建议** - 工作姿势、休息提醒、设备建议、环境优化
8. **预警系统** - 高风险模式、症状恶化、职业病风险预警

## 触发条件

技能在以下情况下自动触发：

1. 用户使用 `/work trend` 查看职业健康趋势
2. 用户使用 `/work status` 查看综合健康状态
3. 用户使用 `/work recommend` 获取改进建议
4. 用户使用 `/work assess` 进行综合评估
5. 用户使用 `/work issue` 记录问题后的分析
6. 用户使用 `/work ergonomic` 进行人机工程评估后的分析

## 医学安全边界

**本技能不能做的事：**
- ❌ 不进行职业病诊断
- ❌ 不出具职业病诊断证明
- ❌ 不替代工作场所健康监护
- ❌ 不预测疾病发展
- ❌ 不处理急性健康危机

**本技能能做的事：**
- ✅ 职业健康风险评估和筛查
- ✅ 工作相关症状识别和追踪
- ✅ 人机工程评估和改进建议
- ✅ 职业病风险预警
- ✅ 工作环境改善建议
- ✅ 健康记录保存（就医时参考）
- ✅ 与其他健康数据的关联分析

## 执行步骤

### 第1步：数据读取

读取职业健康数据文件：
- `data-example/occupational-health-tracker.json` - 主职业健康档案

**数据验证：**
- 检查文件是否存在
- 验证数据结构完整性
- 确认有足够的数据点进行分析

### 第2步：职业健康风险评估

#### 久坐风险评估（Sedentary Risk Score）

**评分维度（每个维度0-10分）**：

1. **每天久坐时间** (sedentary_time_daily)
   - >8小时：10分
   - 6-8小时：7分
   - 4-6小时：4分
   - <4小时：1分

2. **休息频率** (break_frequency)
   - 无休息：10分
   - 每3小时+：8分
   - 每2小时：5分
   - 每小时：2分

3. **每周运动时间** (weekly_exercise_minutes)
   - 0分钟：10分
   - <60分钟：7分
   - 60-150分钟：4分
   - >150分钟：1分

4. **现有症状** (existing_symptoms_severity)
   - 严重症状：10分
   - 中度症状：7分
   - 轻度症状：4分
   - 无症状：1分

**总分计算**：
```
总分 = 久坐时间 + 休息频率 + 运动时间 + 现有症状
范围：4-40分
```

**风险等级判定**：
- 低风险：4-13分
- 中风险：14-26分
- 高风险：27-40分

#### 视屏终端风险评估（VDT Risk Score）

**评分维度（每个维度0-10分）**：

1. **每天屏幕时间** (screen_time_daily)
   - >8小时：10分
   - 6-8小时：7分
   - 4-6小时：4分
   - <4小时：1分

2. **20-20-20法则遵守** (rule_20_20_20_compliance)
   - 从不遵守：10分
   - 偶尔遵守：6分
   - 经常遵守：3分
   - 总是遵守：1分

3. **照明条件** (lighting_quality)
   - 很差：10分
   - 较差：7分
   - 一般：4分
   - 良好：1分

4. **眼部症状** (eye_symptoms_severity)
   - 严重症状：10分
   - 中度症状：7分
   - 轻度症状：4分
   - 无症状：1分

**总分计算和风险等级判定同久坐风险**

#### 综合风险评估

**综合风险等级计算**：
```
综合风险分数 = max(久坐风险, 视屏风险, 倒班风险, 劳损风险, 压力风险)

如果有多个高风险因素（≥27分），综合风险等级上调一级
如果有3个及以上中风险因素（14-26分），综合风险等级上调一级
```

### 第3步：人机工程评估

#### 评估维度和评分

**椅子评估**（0-20分）：
```
- 可调节性（0-5分）
- 腰椎支撑（0-5分）
- 座椅深度（0-5分）
- 扶手（0-5分）
```

**显示器评估**（0-20分）：
```
- 高度（0-7分）
- 距离（0-7分）
- 角度（0-6分）
```

**键盘和鼠标评估**（0-20分）：
```
- 键盘位置（0-5分）
- 鼠标位置（0-5分）
- 手腕支撑（0-10分）
```

**工作台评估**（0-20分）：
```
- 高度（0-10分）
- 空间（0-10分）
```

**环境评估**（0-20分）：
```
- 照明（0-7分）
- 噪音（0-7分）
- 温度（0-6分）
```

**总分计算**：
```
总分 = 椅子 + 显示器 + 键盘鼠标 + 工作台 + 环境
范围：0-100分

评分等级：
- 优秀：0-20分
- 良好：21-40分
- 一般：41-60分
- 较差：61-80分
- 差：81-100分
```

### 第4步：职业病筛查

#### 基于工作类型的筛查推荐

**办公室工作**：
```
必查项目：
- 视力测试（每年1次）
- 肌肉骨骼评估（每年1次）
```

**体力劳动**：
```
必查项目：
- 肌肉骨骼评估（每年1次）
- 肺功能检查（粉尘环境每年1次）
```

**倒班工作**：
```
必查项目：
- 睡眠质量评估（每6个月1次）
- 心理健康筛查（每年1次）
```

**噪音环境工作**：
```
必查项目：
- 听力测试（每年1次）
```

**粉尘/化学环境工作**：
```
必查项目：
- 肺功能检查（每年1次）
- 皮肤病筛查（每年1次）
```

### 第5步：关联分析

#### 睡眠-职业健康关联
- 倒班工作与睡眠质量的相关性
- 睡眠不足与工作相关症状的关系

#### 运动-职业健康关联
- 久坐工作与运动量的关系
- 运动与肌肉骨骼症状的关系

#### 心理健康-职业健康关联
- 工作压力与心理状态的关系
- 职业健康问题与心理症状的关联

### 第6步：生成报告

输出包括：
- 职业健康状况摘要
- 风险评估结果和趋势
- 工作相关问题分析
- 人机工程评估结果
- 职业病筛查建议
- 与其他健康因素的关联分析
- 预警信息（如适用）
- 个性化建议和行动计划

## 输出格式

### 职业健康分析报告结构

```markdown
# 职业健康分析报告

**报告日期**: YYYY-MM-DD
**分析周期**: YYYY-MM-DD 至 YYYY-MM-DD
**数据完整性**: 良好

⚠️ **重要提示**：本报告仅供参考，不构成职业病诊断。

---

## 1. 职业健康状况摘要

[整体评价：优秀/良好/一般/需改进/高风险]
- 综合风险等级：[低/中/高]
- 职业健康评分：X/100
- 人机工程评分：X/100
- 活跃问题数：X个
- 整体趋势：改善/稳定/恶化

## 2. 风险评估结果

### 久坐风险评估
**风险等级**: 🟢 低风险 | 🟡 中风险 | 🔴 高风险
**风险评分**: X/40

**建议**: [具体建议]

### 视屏终端风险评估
**风险等级**: 🟢 低风险 | 🟡 中风险 | 🔴 高风险
**风险评分**: X/40

**建议**: [具体建议]

## 3. 工作相关问题分析

### 当前活跃问题
- [问题1]: 严重程度、频率、持续时间
- [问题2]: 严重程度、频率、持续时间

### 症状趋势
- 改善的问题
- 稳定的问题
- 恶化的问题 ⚠️

## 4. 人机工程评估

**人机工程评分**: X/100
**评分等级**: 优秀/良好/一般/较差/差

### 改进建议
- 高优先级建议
- 中优先级建议
- 低优先级建议

## 5. 职业病筛查

### 推荐筛查
- [筛查项目1] - 建议时间
- [筛查项目2] - 建议时间

## 6. 综合建议

### 立即行动
- [行动项]

### 本周行动计划
- [行动项1]
- [行动项2]

### 预防措施
- [预防措施列表]

---

**报告生成时间**: YYYY-MM-DD HH:MM:SS
⚠️ **免责声明**：本报告仅供参考，不构成职业病诊断或治疗建议。
```

## 错误处理

### 数据文件不存在
```
错误：未找到职业健康数据文件
建议：请先使用 /work assess 命令创建数据
```

### 数据不足
```
警告：数据不足以进行趋势分析
建议：至少需要3次评估记录
```

### 高风险预警
```
🔴 职业病高风险警告

检测到以下高风险因素：
- [列出高风险因素]

建议行动：
1. 立即就医，进行职业病诊断
2. 咨询职业医学专科医生
3. 考虑工作调整
```

## 数据源说明

**主要数据源**：
- `data-example/occupational-health-tracker.json` - 职业健康主数据

**关联数据源**：
- `data-example/sleep-tracker.json` - 睡眠数据
- `data-example/fitness-tracker.json` - 运动数据
- `data-example/mental-health-tracker.json` - 心理健康数据

---

**技能版本**: v1.0.0
**最后更新**: 2025-01-08
**维护者**: WellAlly Tech

## Source: references/skills/healthcare-workflows/references/legacy/oral-health-analyzer/SKILL.md

---
name: oral-health-analyzer
description: 分析口腔健康数据、识别口腔问题模式、评估口腔健康状况、提供个性化口腔健康建议。支持与营养、慢性病、用药等其他健康数据的关联分析。
---
name: oral-health-analyzer

# 口腔健康分析技能

## 技能概述

本技能提供全面的口腔健康数据分析功能，包括趋势识别、风险评估、问题诊断和个性化建议生成。

## 医学免责声明

⚠️ **重要提示**：本技能提供的数据分析和建议仅供参考，不构成医学诊断或治疗建议。

- 所有口腔问题应由专业牙科医生诊断和治疗
- 分析结果不能替代专业口腔检查
- 紧急情况应立即就医
- 请遵循牙科医生的专业建议

## 核心功能

### 1. 趋势分析

#### 龋齿发展趋势
- 识别龋齿发生的模式和频率
- 分析龋齿在不同牙位的分布
- 评估龋齿发展速度
- 预测未来龋齿风险

**输出内容**：
- 龋齿数量变化曲线
- 高风险牙位识别
- 发展趋势预测
- 预防建议

#### 牙周健康变化
- 牙周出血频率统计
- 牙周袋深度变化
- 附着丧失监测
- 牙龈退缩进展

**输出内容**：
- 牙周健康评分趋势
- 疾病进展预警
- 治疗效果评估
- 维护建议

#### 卫生习惯改善
- 刷牙频率变化
- 牙线使用频率变化
- 洁牙记录追踪
- 卫生习惯评分

**输出内容**：
- 习惯改善曲线
- 评分变化趋势
- 目标达成情况
- 激励建议

### 2. 风险评估

#### 龋齿风险评估
基于以下因素进行综合评估：
- 饮食习惯（糖分摄入）
- 口腔卫生习惯
- 氟化物使用
- 唾液分泌情况
- 既往龋齿史
- 家族史

**风险等级**：
- **低风险**：良好的卫生习惯+低糖饮食+定期检查
- **中风险**：中等糖摄入+一般卫生习惯
- **高风险**：高糖饮食+差卫生习惯+不定期检查+龋齿史

**输出内容**：
- 风险等级（低/中/高）
- 主要风险因素
- 量化风险评分
- 降低风险建议

#### 牙周病风险评估
基于以下因素进行综合评估：
- 牙龈出血频率
- 牙周袋深度
- 附着丧失程度
- 吸烟状况
- 糖尿病控制情况
- 压力水平
- 家族史

**风险等级**：
- **健康**：无出血，探诊深度1-3mm
- **牙龈炎**：探诊出血，探诊深度3-4mm
- **轻度牙周炎**：探诊深度4-5mm，轻度附着丧失
- **中度牙周炎**：探诊深度5-6mm，中度附着丧失
- **重度牙周炎**：探诊深度>6mm，重度附着丧失

**输出内容**：
- 疾病分期
- 风险因素列表
- 进展风险预测
- 管理建议

#### 口腔癌风险评估
基于以下因素进行综合评估：
- 吸烟史
- 饮酒习惯
- 槟榔咀嚼
- HPV感染
- 日晒暴露（唇癌）
- 营养状况
- 口腔卫生

**风险等级**：
- **低风险**：无危险因素
- **中风险**：1-2个危险因素
- **高风险**：3个以上危险因素或既往病变

**输出内容**：
- 风险等级
- 主要危险因素
- 筛查建议
- 预防策略

### 3. 关联分析

#### 与营养模块的关联
**糖分摄入与龋齿风险**：
- 分析每日糖分摄入量
- 评估进食频率对龋齿的影响
- 识别高糖食物类型
- 推荐低糖替代食物

**钙和维生素D与牙齿健康**：
- 评估钙摄入量是否充足
- 分析维生素D水平
- 评估对牙齿强度的影响
- 推荐补充剂（如需要）

**营养缺乏的口腔表现**：
- 维生素C缺乏：牙龈出血
- 维生素B缺乏：口腔溃疡
- 铁缺乏：舌头炎症
- 蛋白质缺乏：黏膜萎缩

#### 与慢性病模块的关联
**糖尿病与牙周病**：
- 分析血糖控制与牙周健康的关系
- 评估糖尿病并发症风险
- 提供牙周病对血糖影响的说明
- 联合管理建议

**心血管疾病与牙周病**：
- 分析牙周炎对心血管疾病的影响
- 评估炎症指标关联
- 提供预防性治疗建议
- 联合监测建议

**妊娠期口腔健康**：
- 妊娠期牙龈炎风险评估
- 牙齿治疗时机建议
- 药物使用安全性评估
- 孕期口腔护理指导

**骨质疏松与牙齿健康**：
- 评估骨密度对牙齿的影响
- 分析抗骨吸收药物的副作用
- 提供牙齿保护建议

#### 与用药模块的关联
**药物引起的口干**：
- 识别导致口干的药物
- 评估口干严重程度
- 提供缓解建议
- 与医生沟通用药调整

**药物引起的牙龈增生**：
- 识别导致牙龈增生的药物
- 评估增生程度
- 提供管理建议
- 与医生沟通替代用药

**药物对牙齿颜色的影响**：
- 识别导致牙齿变色的药物
- 提供美容解决方案
- 预防措施建议

#### 与眼健康模块的关联
**干燥综合征**：
- 口干与眼干的联合分析
- 评估全身性自身免疫病
- 多系统症状追踪
- 专科转诊建议

**自身免疫病的口腔表现**：
- 狼疮的口腔病变
- 类风湿关节炎的颞下颌关节影响
- 其他免疫病的口腔表现

### 4. 个性化建议

#### 预防建议
**龋齿预防**：
- 刷牙技巧指导（巴氏刷牙法）
- 牙线使用方法
- 含氟产品推荐
- 饮食调整建议
- 定期检查提醒

**牙周病预防**：
- 改善口腔卫生习惯
- 戒烟支持
- 压力管理
- 血糖控制（糖尿病患者）
- 定期洁牙建议

**口腔癌预防**：
- 戒烟限酒
- 避免槟榔
- 防晒（唇部）
- 营养均衡
- 定期自查方法

#### 治疗建议
**根据问题类型提供**：
- 常规检查建议（每6个月）
- 紧急情况处理指导
- 专科转诊建议（如需要）
- 治疗时机建议
- 费用预估参考

#### 生活方式建议
**饮食调整**：
- 减少游离糖摄入
- 增加钙和维生素D摄入
- 多喝水（预防口干）
- 避免过硬食物（保护牙冠）

**习惯改善**：
- 制定个性化刷牙计划
- 逐步增加牙线使用频率
- 建立口腔卫生常规
- 设置提醒系统

**风险因素管理**：
- 戒烟策略
- 限酒建议
- 压力管理技巧
- 夜磨牙管理

### 5. 目标管理

#### 目标设定
- 与用户协商设定现实目标
- 分解为可实现的步骤
- 设定时间节点
- 建立评估标准

**常见目标类型**：
- 提高牙线使用频率
- 改善刷牙技巧
- 减少糖分摄入
- 定期口腔检查
- 戒烟

#### 进度追踪
- 定期评估目标达成情况
- 提供激励和反馈
- 调整目标（如需要）
- 庆祝里程碑达成

#### 障碍识别
- 识别阻碍目标达成的因素
- 提供克服障碍的策略
- 调整计划以适应实际情况
- 提供持续支持

### 6. 统计分析

#### 综合健康评分
基于以下因素计算：
- 口腔卫生习惯（40%）
- 检查频率（20%）
- 治疗完成情况（20%）
- 问题控制情况（10%）
- 目标达成情况（10%）

**评分范围**：0-100分
- **优秀**：90-100分
- **良好**：75-89分
- **一般**：60-74分
- **较差**：<60分

#### 口腔健康年龄
- 基于牙齿状态、牙周健康、卫生习惯计算
- 与实际年龄对比
- 提供改善建议

#### 治疗统计
- 治疗类型分布
- 治疗费用统计
- 治疗频率分析
- 牙医就诊记录

#### 问题统计
- 问题类型分布
- 问题发生频率
- 问题持续时间
- 解决率统计

### 7. 预警系统

#### 定期检查提醒
- 距离下次检查30天：温馨提醒
- 距离下次检查7天：紧急提醒
- 超过检查时间：逾期提醒

#### 问题预警
- 牙痛超过3天：建议就医
- 牙龈出血持续1周：建议检查
- 口腔溃疡超过2周：建议活检
- 新增肿块/白斑：立即就医

#### 趋势预警
- 龋齿数量快速增加：风险升级
- 牙周指标恶化：转诊牙周专科
- 卫生习惯下降：干预建议
- 治疗频率增加：深度评估

## 使用场景

### 场景1：定期健康评估
**用户请求**：分析最近6个月的口腔健康状况

**分析流程**：
1. 读取最近6个月的所有口腔健康记录
2. 分析检查记录、治疗记录、问题记录
3. 评估卫生习惯变化
4. 计算健康评分变化
5. 识别改善或恶化的趋势
6. 生成综合评估报告

**输出内容**：
- 健康评分变化趋势
- 主要改善点
- 需要关注的问题
- 下一步行动建议

### 场景2：问题诊断辅助
**用户请求**：我最近刷牙时牙龈出血，持续1周了

**分析流程**：
1. 检索最近的口腔检查记录
2. 分析牙周状况历史
3. 评估当前卫生习惯
4. 检查是否有相关用药记录
5. 分析营养数据（如维生素C摄入）
6. 生成诊断辅助报告

**输出内容**：
- 可能的原因分析
- 严重程度评估
- 就医建议
- 家庭护理方法
- 预防措施

### 场景3：治疗规划
**用户请求**：我想改善口腔卫生，降低龋齿风险

**分析流程**：
1. 评估当前龋齿风险
2. 分析主要风险因素
3. 评估当前卫生习惯
4. 识别需要改善的领域
5. 设定阶段性目标
6. 制定个性化计划

**输出内容**：
- 当前风险评估
- 改善目标
- 行动计划
- 时间表
- 进度追踪方法

### 场景4：多学科联合分析
**用户请求**：我有糖尿病，这对我的口腔健康有什么影响？

**分析流程**：
1. 读取糖尿病管理数据
2. 分析血糖控制情况
3. 评估牙周健康状况
4. 分析两者关联性
5. 评估并发症风险
6. 生成联合管理建议

**输出内容**：
- 糖尿病对口腔的影响
- 口腔健康对血糖的影响
- 并发症风险评估
- 联合管理策略
- 监测指标建议

### 场景5：预防性指导
**用户请求**：我准备怀孕，应该注意哪些口腔问题？

**分析流程**：
1. 评估当前口腔健康状况
2. 识别潜在风险
3. 分析当前用药安全性
4. 评估治疗紧迫性
5. 生成孕期口腔管理计划

**输出内容**：
- 孕前口腔检查建议
- 孕期常见口腔问题
- 药物使用安全性
- 治疗时机建议
- 孕期护理指导

## 数据分析方法

### 定量分析
- 统计描述（均值、中位数、标准差）
- 趋势分析（线性回归、移动平均）
- 相关性分析（Pearson/Spearman相关）
- 风险评分计算（多因素加权）

### 定性分析
- 文本描述分析
- 症状模式识别
- 主诉内容分类
- 满意度评估

### 可视化输出
- 时间序列图表
- 牙位分布图
- 风险评估雷达图
- 进度追踪仪表板
- 对比分析柱状图

## 质量保证

### 数据验证
- 检查数据完整性
- 验证数据一致性
- 识别异常值
- 处理缺失数据

### 结果验证
- 医学逻辑检查
- 与临床指南对照
- 专家审查（如有）
- 用户反馈收集

### 持续改进
- 定期更新分析算法
- 引入新的科学证据
- 优化用户体验
- 扩展功能范围

## 参考资源

### 临床指南
- 美国牙科协会（ADA）指南
- 世界卫生组织（WHO）口腔健康指南
- 中华口腔医学会临床指南
- Cochrane口腔健康组系统评价

### 评估工具
- DMFT指数（龋失补指数）
- CPI指数（社区牙周指数）
- 口腔健康影响.profile（OHIP-14）
- 龋齿风险评估工具（CAT）

### 数据源
- 用户记录数据
- 营养模块数据
- 慢性病模块数据
- 用药模块数据
- 眼健康模块数据

## 局限性

### 系统局限
- 不能替代专业口腔检查
- 不能进行影像学检查
- 不能进行实验室检测
- 分析结果受数据质量影响

### 数据局限
- 依赖用户记录准确性
- 可能存在遗漏记录
- 主观评估存在偏差
- 时间跨度可能不足

### 建议局限
- 不能考虑所有个体因素
- 不能预测所有并发症
- 需要结合临床判断
- 不能保证100%准确性

## 未来扩展

### 计划功能
- AI影像识别（牙片分析）
- 语音记录录入
- 智能提醒系统
- 社区支持功能
- 与牙医系统对接

### 研究方向
- 机器学习预测模型
- 个性化预防策略
- 基因风险分析
- 微生物组分析

---
name: oral-health-analyzer

**版本**: v1.0.0
**最后更新**: 2025-01-06
**维护者**: WellAlly Tech

## Source: references/skills/healthcare-workflows/references/legacy/rehabilitation-analyzer/SKILL.md

---
name: rehabilitation-analyzer
description: 分析康复训练数据、识别康复模式、评估康复进展，并提供个性化康复建议
allowed-tools: Read, Grep, Glob, Write, Edit
---

# 康复训练分析技能

## 核心功能

康复训练分析技能提供全面的康复数据分析功能，帮助用户追踪康复进展、识别改善模式和优化训练计划。

**主要功能模块：**

1. **康复进展分析** - 评估功能改善趋势和康复效果
2. **功能改善曲线** - 可视化ROM、肌力、平衡等功能指标变化
3. **疼痛模式识别** - 分析疼痛评分变化趋势和触发因素
4. **目标达成率评估** - 追踪康复目标完成情况
5. **康复阶段分析** - 评估当前阶段进展和阶段转换准备度
6. **训练依从性评估** - 分析训练计划执行情况

## 触发条件

技能在以下情况下自动触发：

1. 用户使用 `/rehab progress` 查看康复进展
2. 用户使用 `/rehab analysis` 进行康复分析
3. 用户使用 `/rehab trends` 查看趋势分析
4. 用户使用 `/rehab report` 生成康复报告

## 执行步骤

### 第1步：数据读取
读取康复数据文件：
- `data/rehabilitation-tracker.json` - 主康复档案
- `data/rehabilitation-logs/YYYY-MM/YYYY-MM-DD.json` - 每日训练日志

**数据验证：**
- 检查文件是否存在
- 验证数据结构完整性
- 确认有足够的数据点进行分析（建议至少3次评估或10天训练记录）

### 第2步：功能评估趋势分析

**关节活动度（ROM）分析：**
```
- 分析不同时间点的ROM测量值
- 计算ROM改善速率（度/周）
- 识别ROM平台期或倒退
- 预测达到目标ROM的时间
- 与目标范围对比
```

**肌力改善分析：**
```
- 追踪肌力等级变化（MMT评分）
- 识别肌力提升模式
- 比较不同肌群恢复速度
- 评估肌力不平衡情况
```

**平衡功能分析：**
```
- 平衡测试分数趋势
- 单腿站立时间改善
- 平衡稳定性评估
- 跌倒风险变化
```

### 第3步：疼痛模式分析

**疼痛时序分析：**
```
- 分析晨起疼痛趋势
- 分析活动后疼痛趋势
- 识别疼痛加重/缓解模式
- 关联疼痛与训练强度
```

**疼痛触发因素识别：**
```
- 特定训练项目与疼痛关系
- 训练强度与疼痛相关性
- 活动类型与疼痛关系
- 时间因素对疼痛影响
```

### 第4步：训练依从性计算

**依从性指标：**
```
依从性 = (实际训练次数 / 计划训练次数) × 100%
```

**分析维度：**
- 周依从性
- 月依从性
- 整体依从性
- 不同训练类型的依从性

### 第5步：目标达成评估

**目标进度追踪：**
- 计算每个目标的完成百分比
- 预估目标达成时间
- 识别滞后目标
- 提供目标调整建议

### 第6步：康复阶段评估

**当前阶段分析：**
- 阶段目标完成情况
- 是否准备好进入下一阶段
- 阶段转换建议

### 第7步：生成报告

输出包括：
- 康复进展摘要
- 功能改善趋势
- 疼痛控制情况
- 训练依从性评价
- 目标达成评估
- 阶段进展建议
- 个性化建议

## 输出格式

### 康复进展报告结构

```markdown
# 康复进展报告
**报告日期**: YYYY-MM-DD
**康复时长**: X天
**当前阶段**: 第X阶段 - 阶段名称

## 1. 康复进展摘要

[整体进展评价：优秀/良好/一般/需改进]
- 康复时长：X天（第X周）
- 完成训练：X次
- 训练依从性：X%
- 当前阶段进展：X%

## 2. 功能改善趋势

### 关节活动度（ROM）
- [关节名] [活动类型]: 基线X° → 当前X° → 改善X°
- 改善速率：X°/周
- 达到目标时间预估：X周
- 趋势分析：[改善趋势描述]

### 肌力评估
- [肌群名]: 基线X/5 → 当前X/5 → 改善X级
- 肌力提升模式：[描述]
- 肌力平衡：[评估]

### 平衡功能
- [测试类型]: 基线X → 当前X → 改善X
- 平衡稳定性：[评估]
- 跌倒风险：[评估]

## 3. 疼痛控制情况

- 平均疼痛水平：X/10
- 疼痛趋势：[改善/稳定/加重]
- 疼痛模式：[描述]
- 触发因素：[识别出的触发因素]
- 疼痛控制建议：[建议]

## 4. 训练依从性

- 整体依从性：X%
- 计划训练：X次
- 实际训练：X次
- 依从性评价：[优秀/良好/一般/需改进]
- 缺训原因分析：[如有]

## 5. 目标达成情况

### 已达成目标（X个）
- 目标1：[描述] - 达成日期：YYYY-MM-DD
- ...

### 进行中目标（X个）
- 目标1：[描述] - 当前进度：X% - 预计达成：YYYY-MM-DD
- ...

### 滞后目标（X个）
- 目标1：[描述] - 当前进度：X% - 需要关注

## 6. 康复阶段进展

**当前阶段**: 第X阶段 - [阶段名称]
- 阶段目标完成：X/X
- 阶段进度：X%
- 阶段持续时间：X周
- **阶段评价**: [评价]

**是否准备好进入下一阶段**: [是/否]
- [准备好的理由] / [需要继续努力的项目]

## 7. 个性化建议

### 训练建议
- [具体训练建议]

### 目标调整建议
- [目标调整建议]

### 阶段转换建议
- [阶段转换建议]

### 注意事项
- [需要注意的事项]

## 8. 下次评估

**下次评估日期**: YYYY-MM-DD
**评估重点**: [重点评估项目]
```

### 简要进展报告

```markdown
## 康复进展简报

📊 **整体进展**: 良好
⏱️ **康复时长**: 第X周（X天）
🎯 **阶段**: 第X阶段 - [阶段名称]

**功能改善**:
- ROM: +X°（改善速率X°/周）✅
- 肌力: 提升X级 ✅
- 平衡: 改善X% ✅

**疼痛控制**: 平均X/10（[趋势]）
**训练依从性**: X%（[评价]）
**目标达成**: X/X（X%）

**当前阶段**: X/X目标完成
**下一阶段准备**: [是/否]

💡 **建议**: [1-2条核心建议]
```

## 数据源

### 主数据文件
- **文件路径**: `data/rehabilitation-tracker.json`
- **读取字段**:
  - `user_profile` - 用户档案和康复基本信息
  - `rehabilitation_goals` - 康复目标列表
  - `exercise_log` - 训练日志
  - `functional_assessments` - 功能评估记录
  - `phase_progression` - 阶段进展记录
  - `pain_diary` - 疼痛日记
  - `statistics` - 统计数据

### 日志数据文件
- **文件路径**: `data/rehabilitation-logs/YYYY-MM/YYYY-MM-DD.json`
- **读取字段**:
  - `daily_summary` - 日训练摘要
  - `exercise_sessions` - 训练详情
  - `pain_entries` - 疼痛记录
  - `assessments` - 评估记录
  - `notes` - 每日备注

## 分析算法

### 1. 改善趋势分析

**线性回归分析：**
```
使用最小二乘法拟合功能改善趋势
改善速率 = (当前值 - 基线值) / 时间间隔
```

**改善模式识别：**
- 线性改善：稳定持续改善
- 阶梯式改善：平台期后快速改善
- 平台期：改善停滞
- 倒退：功能下降（需要关注）

### 2. 疼痛时序分析

**移动平均计算：**
```
7日移动平均疼痛 = sum(近7天疼痛) / 7
```

**疼痛趋势判断：**
- 改善：疼痛评分下降≥20%
- 稳定：疼痛评分变化<20%
- 加重：疼痛评分上升≥20%

### 3. 依从性计算

```
总体依从性 = (实际训练天数 / 计划训练天数) × 100%

训练类型依从性 = (某类型实际完成 / 某类型计划完成) × 100%
```

**依从性评价：**
- 优秀：≥90%
- 良好：75-89%
- 一般：60-74%
- 需改进：<60%

### 4. 目标达成预测

**线性外推：**
```
预测时间 = 当前日期 + ((目标值 - 当前值) / 改善速率)
```

**考虑因素：**
- 近期改善速率
- 平台期历史
- 训练依从性

### 5. 阶段转换准备度评估

**准备度评分：**
```
准备度 = (已达成阶段目标数 / 阶段目标总数) × 100%

准备度 ≥ 80%: 建议进入下一阶段
准备度 60-79%: 可考虑进入下一阶段，需谨慎
准备度 < 60%: 建议继续当前阶段
```

## 安全与隐私

### 数据安全原则

1. **本地存储**
   - 所有康复数据仅存储在用户本地设备
   - 不上传至任何云端服务器
   - 不与第三方共享数据

2. **隐私保护**
   - 个人健康信息严格保密
   - 数据文件不包含个人身份信息
   - 用户完全控制数据访问权限

3. **数据完整性**
   - 原始数据不被修改
   - 分析结果基于真实数据
   - 支持数据导出和备份

### 医学安全边界

**系统不能做的事：**
- ❌ 不提供具体康复训练处方
- ❌ 不替代康复师专业指导
- ❌ 不诊断损伤或并发症
- ❌ 不调整康复阶段计划
- ❌ 不预测康复预后时间
- ❌ 不处理急性疼痛或损伤

**系统能做的事：**
- ✅ 提供数据分析和趋势识别
- ✅ 提供进展追踪和目标管理
- ✅ 提供一般性康复建议
- ✅ 提供专业康复就医提醒
- ✅ 记录训练和评估数据
- ✅ 生成康复进展报告

**重要提示：**
- 所有康复训练计划应遵循康复师指导
- 任何疼痛加重或功能倒退应及时就医
- 定期专业评估是康复成功的关键
- 系统建议仅供参考，不替代专业判断

## 错误处理

### 数据读取错误

**错误类型1：文件不存在**
```
错误信息: "未找到康复数据文件，请先使用 /rehab start 开始康复追踪"
处理建议: 引导用户开始康复记录
```

**错误类型2：数据不足**
```
错误信息: "数据不足，至少需要3次功能评估或10天训练记录才能生成分析报告"
当前数据: X次评估，X天训练记录
处理建议: 建议用户继续记录更多数据
```

**错误类型3：数据结构错误**
```
错误信息: "数据文件结构异常，请检查数据完整性"
处理建议: 建议用户重新初始化康复档案
```

### 分析过程错误

**错误类型：计算异常**
```
错误信息: "数据分析过程中出现异常，请稍后重试"
处理建议: 记录错误日志，提供基础数据展示
```

### 输出生成错误

**错误类型：报告生成失败**
```
错误信息: "报告生成失败，请尝试简化查询条件或联系技术支持"
处理建议: 提供简化版报告或原始数据导出
```

## 使用示例

### 示例1：查看康复进展

**用户输入：**
```
/rehab progress
```

**技能执行：**
1. 读取 rehabilitation-tracker.json
2. 读取近30天的康复日志
3. 分析功能改善趋势
4. 计算训练依从性
5. 评估目标达成情况
6. 生成进展报告

**输出：**
```
# 康复进展报告

## 康复进展摘要
📊 整体进展: 良好
⏱️ 康复时长: 第6周（36天）
🎯 当前阶段: 第3阶段 - 强化期

## 功能改善
- 膝关节屈曲: 30° → 120° (+90°) ✅
- 膝关节伸直: -10° → 0° (+10°) ✅
- 股四头肌肌力: 3/5 → 4/5 (提升1级) ✅
- 单腿站立: 5秒 → 30秒 (+25秒) ✅

## 疼痛控制
- 平均疼痛: 1.5/10（良好控制）
- 疼痛趋势: 稳定 ✅

## 训练依从性: 92%（优秀）

## 目标达成: 8/14（57%）
- ✅ 已达成: 8个
- 🔄 进行中: 5个
- ⚠️ 滞后: 1个

## 阶段进展
第3阶段进度: 2/5目标完成（40%）
下一阶段准备: 需要继续努力

💡 建议: 继续当前训练强度，重点关注股四头肌强化训练
```

### 示例2：分析功能改善趋势

**用户输入：**
```
/rehab trends rom
```

**技能执行：**
1. 提取所有ROM评估记录
2. 绘制ROM改善曲线（文字描述）
3. 计算改善速率
4. 预测达到目标时间
5. 识别改善模式

**输出：**
```
# 关节活动度（ROM）趋势分析

## 膝关节屈曲
📈 改善趋势: 良好

时间线:
- 5/15: 30° (基线)
- 5/30: 70° (+40°)
- 6/15: 100° (+30°)
- 6/20: 120° (+20°)

改善速率: 8.6°/周
目标: 135°
预计达成: 2025-08-01（还需2周）
趋势: 持续改善 ✅

## 膝关节伸直
✅ 已达成目标

时间线:
- 5/15: -10° (基线)
- 6/10: 0° (达成目标) ✅
- 6/20: 0° (维持)

改善速率: 2.5°/周
目标: 0°
达成日期: 2025-06-10
趋势: 维持目标 ✅

## 建议
- 膝关节屈曲进展良好，继续保持
- 注意伸直维持训练，避免屈曲挛缩
- 预计2周内可达到屈曲目标
```

### 示例3：评估疼痛模式

**用户输入：**
```
/rehab analysis pain
```

**技能执行：**
1. 提取所有疼痛记录
2. 分析疼痛时序变化
3. 识别疼痛触发因素
4. 评估疼痛控制效果

**输出：**
```
# 疼痛模式分析

## 疼痛趋势
📉 总体趋势: 改善中

- 基线疼痛: 5/10
- 当前疼痛: 2/10
- 改善: 3分（60%改善）✅

## 时序模式
- 晨起疼痛: 1/10（轻度）
- 活动后疼痛: 2/10（轻度）
- 休息时疼痛: 0/10（无痛）

## 触发因素识别
- 主要触发因素: 延长坐姿、上下楼梯
- 疼痛加剧活动: 下楼梯、深蹲
- 缓解因素: 休息、冰敷、抬高

## 训练相关疼痛
- 训练时平均疼痛: 1.2/10（安全范围）
- 训练后疼痛: 2/10（快速缓解）
- 训练依从性不受疼痛影响 ✅

## 建议
- 疼痛控制良好，继续当前训练强度
- 注意训练后休息和冰敷
- 避免疼痛加剧活动（深蹲、下楼梯）
- 如疼痛>4/10，及时就医评估
```

## 相关性分析

### 与运动模块关联

**关联分析：**
- 康复训练与运动能力恢复的关联
- 康复训练强度与心率变化的关系
- 功能改善与日常活动量的关联

**示例：**
```
用户使用 /rehab analysis correlation fitness
技能读取:
- rehabilitation-tracker.json
- fitness-tracker.json
- 分析康复训练与运动指标的相关性
```

### 与睡眠模块关联

**关联分析：**
- 训练强度与睡眠质量的关系
- 疼痛水平与睡眠时长的关系
- 恢复期睡眠需求分析

### 与用药模块关联

**关联分析：**
- 止痛药使用趋势
- 用药与训练强度的关系
- 疼痛控制与用药依从性

## 使用示例

### 场景1：新用户开始康复
```
用户: /rehab start acl-surgery 2025-05-01
系统: 初始化康复档案，设置基础目标，提供初始建议
技能: rehabilitation-analyzer（可选，用于初步评估）
```

### 场景2：记录每日训练
```
用户: /rehab exercise slr 3x15 pain2
系统: 记录训练数据，更新训练日志
技能: 不触发（仅记录）
```

### 场景3：查看进展报告
```
用户: /rehab progress
系统: 调用 rehabilitation-analyzer 技能
技能: 完整分析，生成进展报告
```

### 场景4：分析特定功能
```
用户: /rehab trends rom
系统: 调用 rehabilitation-analyzer 技能
技能: ROM专项分析，生成趋势报告
```

### 场景5：评估疼痛模式
```
用户: /rehab analysis pain
系统: 调用 rehabilitation-analyzer 技能
技能: 疼痛专项分析，识别模式和触发因素
```

---

**技能版本**: v1.0
**最后更新**: 2026-01-06
**维护者**: WellAlly Tech

## Source: references/skills/healthcare-workflows/references/legacy/sexual-health-analyzer/SKILL.md

---
name: sexual-health-analyzer
description: Sexual Health Analyzer
---

# 性健康分析技能

## 技能概述

本技能提供全面的性健康数据分析功能,包括IIEF-5评分分析、STD筛查管理、避孕效果评估、性活动统计以及与用药、慢性病、心理、营养、运动等模块的深度关联分析。

## 医学免责声明

⚠️ **重要提示**:本技能提供的数据分析和建议仅供参考,不构成医学诊断或治疗建议。

- 所有性健康问题应由专业医生诊断和治疗
- 分析结果不能替代专业医疗检查
- 紧急情况应立即就医
- 请遵循医生的专业建议

## 核心功能

### 1. IIEF-5 评分分析

#### 1.1 交互式问卷

**问卷结构**:
- 5个问题,每个问题0-5分
- 总分范围:0-25分
- 评估时间范围:过去6个月

**问题详解**:

**问题1**:勃起信心
- 评估用户对获得和维持勃起的信心程度
- 反映心理因素对性功能的影响
- 低分可能提示表现焦虑

**问题2**:勃起获得
- 评估受到性刺激时获得勃起的能力
- 反映血管和神经功能
- 低分可能提示器质性ED

**问题3**:插入能力
- 评估勃起硬度是否足够插入
- 临床相关的勃起质量指标
- 低分通常需要医疗干预

**问题4**:勃起维持
- 评估完成性交过程中维持勃起的能力
- 反映静脉闭塞功能
- 与问题3联合分析可确定ED类型

**问题5**:性交满意度
- 评估性交过程的主观满意度
- 受硬度、持续时间、伴侣满意度等多因素影响
- 综合性功能的最终指标

#### 1.2 ED严重程度评估

| 总分 | ED严重程度 | 临床意义 | 推荐措施 |
|------|-----------|----------|----------|
| 22-25 | 正常 | 勃起功能良好 | 继续健康生活方式 |
| 17-21 | 轻度ED | 轻度功能障碍 | 生活方式调整,定期评估 |
| 12-16 | 轻中度ED | 中度功能障碍 | 建议就医评估 |
| 8-11 | 中度ED | 明显功能障碍 | 需要医疗干预 |
| 5-7 | 重度ED | 严重功能障碍 | 全面医疗评估和治疗 |

#### 1.3 趋势分析

**分析维度**:
- 总分变化趋势(改善/稳定/恶化)
- 各问题得分变化模式
- ED严重程度变化轨迹
- 治疗干预效果评估

**输出内容**:
- IIEF-5评分时间序列图表
- 改善/恶化趋势标识
- 变化速率计算
- 与其他健康指标的相关性分析

#### 1.4 风险因素分析

**生理因素**:
- 年龄:每增加10年,ED风险增加约20%
- 糖尿病:ED风险增加3倍
- 心血管疾病:ED风险增加2-3倍
- 高血压:ED风险增加1.5-2倍
- 肥胖:BMI>30增加ED风险
- 荷尔蒙异常:低睾酮水平

**心理因素**:
- 表现焦虑
- 抑郁症状
- 压力水平
- 伴侣关系问题

**生活方式因素**:
- 吸烟:增加ED风险1.5倍
- 酗酒:长期影响性功能
- 缺乏运动:心血管健康下降
- 睡眠质量:影响荷尔蒙分泌

**药物因素**:
- 抗抑郁药(SSRIs等)
- 抗高血压药(β受体阻滞剂、噻嗪类)
- 抗精神病药
- 激素类药物

#### 1.5 改善建议

**生活方式干预**:
- **戒烟**:显著改善血管健康
- **限酒**:男性每日<2杯
- **减重**:BMI控制在18.5-24.9
- **规律运动**:
  - 每周150分钟中等强度有氧运动
  - 每周2-3次力量训练
  - 每日盆底肌训练(凯格尔运动)
- **健康饮食**:
  - 地中海饮食模式
  - 增加水果蔬菜摄入
  - 减少饱和脂肪和加工食品
  - 适量坚果和全谷物

**心理干预**:
- 性治疗师咨询
- 认知行为疗法
- 伴侣治疗
- 压力管理技术(冥想、瑜伽)

**医疗干预**:
- PDE5抑制剂(需医生处方)
- 睾酮补充疗法(如睾酮低)
- 真空勃起装置
- 阴茎注射疗法
- 手术治疗(血管手术、假体)

### 2. STD 筛查管理

#### 2.1 筛查项目详解

**HIV (艾滋病病毒)**:
- **检测方法**:血液检测(抗体+抗原组合)
- **窗口期**:1-3个月
- **高危人群**:MSM、性工作者、多性伴侣者
- **筛查频率**:高风险每3-6个月,一般风险每年

**梅毒 (Syphilis)**:
- **检测方法**:血液检测(RPR/VDRL+TPPA确认)
- **窗口期**:10-90天
- **分期**:一期、二期、潜伏期、三期
- **治疗**:青霉素有效,早期治愈率高

**衣原体 (Chlamydia)**:
- **检测方法**:尿液检测或拭子
- **窗口期**:1-3周
- **特点**:常无症状,但可导致不孕
- **治疗**:阿奇霉素或多西环素

**淋病 (Gonorrhea)**:
- **检测方法**:尿液检测或拭子
- **窗口期**:1-14天
- **特点**:男性症状明显,女性常无症状
- **治疗**:头孢曲松+阿奇霉素(考虑耐药性)

**HPV (人乳头瘤病毒)**:
- **检测方法**:拭子DNA检测
- **窗口期**:1个月-数年
- **特点**:非常常见,大多数自愈
- **高危型**:HPV 16/18与宫颈癌相关
- **预防**:HPV疫苗有效

**乙肝 (Hepatitis B)**:
- **检测方法**:血液检测(HBsAg+抗HBs)
- **窗口期**:1-6个月
- **预防**:乙肝疫苗有效
- **治疗**:抗病毒药物

**生殖器疱疹 (Herpes)**:
- **检测方法**:拭子PCR或血液抗体
- **窗口期**:2-12天
- **特点**:无治愈方法,可控制症状
- **治疗**:抗病毒药物(阿昔洛韦等)

#### 2.2 风险评估

**行为风险因素**:
- 性伴侣数量(>3个/年 = 高风险)
- 保护措施使用频率
- 性伴侣的STD状况
- 性工作或性工作者接触史
- MSM人群
- 注射吸毒史

**动态风险评分**:
- **低风险**(<10分):单一稳定伴侣,坚持保护
- **中风险**(10-30分):2-3个性伴侣,偶尔保护
- **高风险**(30-50分):多性伴侣,保护不一致
- **极高风险**(>50分):性工作者,MSM,无保护

#### 2.3 筛查频率建议

基于风险等级的个性化筛查计划:

| 风险等级 | HIV/梅毒 | 衣原体/淋病 | HPV | 乙肝 |
|----------|---------|------------|-----|------|
| 低风险 | 每1-2年 | 每1-2年 | 每3年 | 已免疫无需检测 |
| 中风险 | 每年 | 每年 | 每3年 | 每1-2年 |
| 高风险 | 每3-6月 | 每3-6月 | 每年 | 每年 |
| 极高风险 | 每3月 | 每3月 | 每6月 | 每6月 |

#### 2.4 阳性结果管理

**立即行动**:
- 开始治疗(遵医嘱)
- 通知性伴侣并进行检测
- 暂停性生活或严格保护
- 避免传播风险

**治疗追踪**:
- 治疗后检测以确认治愈
- 监测药物副作用
- 评估治疗依从性
- 记录治疗过程和结果

**预防再感染**:
- 性伴侣同时治疗
- 治愈后重新开始保护措施
- 定期复查
- 风险教育

#### 2.5 统计分析

- 筛查频率趋势
- 阳性率变化
- 感染类型分布
- 治愈率统计
- 再感染率分析

### 3. 避孕管理

#### 3.1 避孕方法详细分析

**避孕套 (男/女)**:
- **典型使用有效率**:85%
- **完美使用有效率**:98%
- **优点**:
  - 唯一防孕又防病的方法
  - 无激素副作用
  - 易于获取
  - 即刻起效
- **缺点**:
  - 需要每次使用
  - 可能影响性快感
  - 可能破裂或滑落
- **满意度影响因素**:
  - 尺寸是否合适
  - 润滑剂使用
  - 佩戴技巧
  - 品牌偏好

**口服避孕药**:
- **典型使用有效率**:91%
- **完美使用有效率**:99.7%
- **类型**:
  - 复方避孕药(雌激素+孕激素)
  - 单纯孕激素药(适合哺乳期)
  - 24/4方案 vs 21/7方案
- **优点**:
  - 高效避孕
  - 可调节月经周期
  - 改善痤疮和经前综合症
  - 降低卵巢癌和子宫内膜癌风险
- **缺点**:
  - 需要每日服用
  - 激素副作用
  - 不适合吸烟女性>35岁
  - 不能预防STD
- **副作用追踪**:
  - 恶心、乳房胀痛
  - 情绪变化
  - 性欲改变
  - 体重变化
  - 月经间期出血

**宫内节育器 (IUD)**:
- **有效率**:99%+
- **类型**:
  - 铜IUD(10-12年)
  - 左炔诺孕酮IUD(3-8年)
- **优点**:
  - 长效可逆
  - 即刻起效
  - 可随时取出
  - 激素IUD可减轻月经
- **缺点**:
  - 需要医生放置
  - 放置时不适
  - 可能增加月经量和痛经(铜IUD)
  - 不能预防STD
- **副作用追踪**:
  - 放置后疼痛
  - 月经变化
  - 点滴出血
  - 穿孔风险(罕见)

**皮下埋植**:
- **有效率**:99%+
- **持续时间**:3-5年
- **优点**:
  - 长效可逆
  - 放置简单
  - 可随时取出
  - 隐蔽性好
- **缺点**:
  - 激素副作用
  - 可能导致月经紊乱
  - 放置部位可能瘢痕
  - 不能预防STD

**避孕针**:
- **典型使用有效率**:94%
- **完美使用有效率**:99%+
- **频率**:每3个月一次
- **优点**:
  - 不需要每日服用
  - 隐蔽性好
- **缺点**:
  - 需要定期注射
  - 体重增加常见
  - 生育力恢复可能延迟
  - 不能预防STD

**体外射精**:
- **典型使用有效率**:78%
- **完美使用有效率**:96%
- **风险**:
  - 需要高度自控
  - 射精前可能有精子溢出
  - 增加性焦虑
  - 不能预防STD
- **不推荐**:失败率较高

**安全期法**:
- **典型使用有效率**:76-88%
- **完美使用有效率**:95-99%
- **方法**:
  - 日历法
  - 基础体温法
  - 宫颈黏液法
  - 症状体温法
- **风险**:
  - 月经不规律时不可靠
  - 需要严格记录
  - 排卵期可能不规律
  - 不能预防STD
- **不推荐**:失败率较高

**结扎手术**:
- **有效率**:99%+
- **类型**:
  - 输精管结扎(男性)
  - 输卵管结扎(女性)
- **优点**:
  - 永久性避孕
  - 高效
  - 无激素影响
- **缺点**:
  - 通常不可逆
  - 需要手术
  - 术后恢复期
  - 不能预防STD

#### 3.2 效果评估

**避孕失败率分析**:
- Pearl指数(每100女性年失败数)
- 典型使用 vs 完美使用差异
- 使用错误分析
- 失败原因追踪

**满意度评分**:
- 易用性(1-10分)
- 舒适度(1-10分)
- 对性生活影响(1-10分)
- 副作用可接受度(1-10分)
- 整体满意度(1-10分)

#### 3.3 副作用追踪

**荷尔蒙相关副作用**:
- 月经模式改变
- 情绪波动
- 性欲变化
- 体重变化
- 乳房胀痛

**非荷尔蒙副作用**:
- 疼痛或不适(IUD)
- 过敏反应(避孕套)
- 疤痕形成(埋植、结扎)

**严重副作用**:
- 血栓栓塞风险(激素类)
- 异位妊娠风险(IUD失败时)
- 感染风险(IUD放置)

#### 3.4 切换历史

**切换原因分析**:
- 副作用不耐受
- 效果不满意
- 生活方式改变
- 健康状况变化
- 经济原因
- 伴侣偏好

**切换建议**:
- 基于副作用史选择
- 考虑年龄和生育计划
- 评估健康风险因素
- 伴侣讨论

### 4. 性活动日志

#### 4.1 记录内容

**基础信息**:
- 日期和时间
- 活动类型(性交、口交、手交等)
- 持续时间
- 伴侣类型(固定、新伴侣等)

**保护措施**:
- 避孕方法(避孕套、口服避孕药等)
- 是否正确使用
- 是否破损或失败

**主观体验**:
- 满意度评分(1-10分)
- 性欲水平(1-10分)
- 疼痛或不适(有/无,程度)
- 是否达到高潮

**特殊情况**:
- 异常症状
- 避孕失败
- 意外情况
- 备注

#### 4.2 隐私保护

**数据标记**:
- 敏感数据标记
- 加密建议
- 访问权限设置
- 数据匿名化选项

**用户控制**:
- 可选功能,完全自主决定
- 可随时删除记录
- 可选择性导出数据
- 就医时可选择性展示

#### 4.3 统计分析

**频率统计**:
- 每周/每月/每年性活动次数
- 频率变化趋势
- 与年龄/关系阶段对比

**满意度分析**:
- 平均满意度评分
- 满意度趋势变化
- 影响满意度的因素分析
- 与IIEF-5/FSFI评分相关性

**保护措施统计**:
- 保护措施使用率
- 各避孕方法使用频率
- 避孕失败次数和原因
- 保护措施与满意度关系

**模式识别**:
- 性活动时间模式
- 与生理周期关系(女性)
- 与情绪/压力相关性
- 与药物使用相关性

### 5. 关联分析

#### 5.1 与用药模块的关联

**PDE5抑制剂效果追踪**:
- 药物名称和剂量
- 服用频率和时机
- 效果评分(1-10分)
- 副作用记录
- 效果随时间变化
- 与IIEF-5评分相关性
- 成本效益分析

**抗抑郁药对性功能的影响**:
- 药物类别(SSRIs, SNRIs, TCAs等)
- 性功能副作用类型
- 严重程度评估
- 发生时间(用药初期/长期)
- 与性欲、勃起、高潮的关系
- 换药或加药建议

**降压药对性功能的影响**:
- 药物类别(β受体阻滞剂、噻嗪类等)
- ED发生率
- 性欲影响
- 替代药物选择建议

**激素类药物**:
- 睾酮补充治疗
- 雌激素/孕激素
- 性功能影响
- 剂量调整建议

**其他药物**:
- 抗精神病药
- 抗组胺药
- 化疗药物
- 对性功能的影响

#### 5.2 与慢性病模块的关联

**糖尿病与ED**:
- **病理机制**:
  - 血管内皮损伤
  - 神经病变
  - 荷尔蒙异常
- **血糖控制与ED关系**:
  - HbA1c <7%:ED风险较低
  - HbA1c 7-9%:中度风险
  - HbA1c >9%:高度风险
- **糖尿病病程与ED**:
  - <5年:ED风险增加2倍
  - 5-10年:ED风险增加3倍
  - >10年:ED风险增加4-5倍
- **管理建议**:
  - 严格控制血糖
  - 定期ED筛查
  - 早期干预
  - 综合管理(血压、血脂)

**高血压与性功能**:
- **病理机制**:
  - 血管损伤
  - 内皮功能障碍
- **降压药的影响**:
  - β受体阻滞剂:增加ED风险
  - 噻嗪类利尿剂:可能引起ED
  - ACEI/ARB:中性或有益
  - 钙通道阻滞剂:中性
- **管理建议**:
  - 控制血压至目标值
  - 选择对性功能影响小的药物
  - 定期评估性功能

**心血管疾病与性功能**:
- **ED作为预警信号**:
  - ED可能早于心绞痛症状2-3年
  - ED是心血管疾病的独立预测因子
  - 建议ED患者进行心血管评估
- **性生活安全评估**:
  - 心功能分级评估
  - 运动耐量评估
  - 药物使用(硝酸酯类药物禁用PDE5抑制剂)
- **心肌梗死后性生活指导**:
  - 通常2-4周后可恢复
  - 逐步增加强度
  - 监测症状

**肥胖与性功能**:
- **影响机制**:
  - 荷尔蒙变化(睾酮降低,雌激素升高)
  - 血管内皮功能障碍
  - 心理因素(身体意象)
- **减重效果**:
  - 减重5-10%可显著改善
  - 减重后IIEF-5评分平均提高3-5分
  - 运动结合饮食效果最佳

#### 5.3 与心理健康模块的关联

**焦虑与性功能**:
- **表现焦虑**:
  - 担心性表现
  - 害怕不能满足伴侣
  - 导致勃起困难或早泄
- **广泛性焦虑**:
  - 性欲下降
  - 难以放松享受
  - 分心难以集中
- **干预**:
  - 认知行为疗法
  - 放松训练
  - 感觉集中训练

**抑郁与性功能**:
- **抑郁症状与性欲**:
  - 性欲丧失常见症状
  - 性兴趣显著下降
  - 可能是最早出现的症状之一
- **抗抑郁药的双重影响**:
  - 改善抑郁可能恢复性欲
  - 但药物本身可能引起性功能障碍
- **管理策略**:
  - 选择对性功能影响小的抗抑郁药(安非他酮)
  - 加用药物(如丁螺环酮)
  - 剂量调整
  - 心理治疗

**创伤后应激障碍(PTSD)**:
- 性回避
- 性唤起困难
- 闪回影响
- 需要专业创伤治疗

**身体意象**:
- 对自己身体的不满
- 影响性自信
- 导致回避亲密关系
- 身体积极性训练

**伴侣关系**:
- 关系质量与性生活满意度高度相关
- 沟通问题影响性满足
- 冲突未解决影响性欲
- 伴侣治疗可能有益

#### 5.4 与营养模块的关联

**关键营养素**:

**锌**:
- **功能**:睾酮合成必需元素
- **缺乏表现**:性欲下降,ED
- **推荐摄入**:男性11mg/天
- **食物来源**:牡蛎、牛肉、南瓜子、腰果
- **补充建议**:如缺乏可补充15-30mg/天

**精氨酸**:
- **功能**:促进一氧化氮生成,改善血流
- **对ED的潜在益处**:可能轻度改善勃起功能
- **推荐剂量**:3-5g/天
- **食物来源**:坚果、种子、肉类、鱼类
- **注意事项**:可能与某些药物相互作用

**维生素D**:
- **功能**:支持睾酮合成
- **缺乏表现**:低维生素D水平与ED相关
- **目标水平**:血清25(OH)D >30 ng/mL
- **补充建议**:如缺乏可补充1000-2000 IU/天

**镁**:
- **功能**:支持睾酮合成,改善血流
- **推荐摄入**:男性400-420mg/天
- **食物来源**:绿叶蔬菜、坚果、全谷物
- **补充建议**:如缺乏可补充200-400mg/天

**Omega-3脂肪酸**:
- **功能**:改善心血管健康,间接改善性功能
- **推荐摄入**:1-2g EPA+DHA/天
- **食物来源**:深海鱼类、亚麻籽、核桃

**抗氧化物质**:
- **功能**:保护血管内皮
- **重要抗氧化剂**:维生素C、维生素E、硒、番茄红素
- **食物来源**:水果、蔬菜、坚果

**膳食模式**:

**地中海饮食**:
- **特点**:高水果蔬菜、全谷物、橄榄油、鱼类
- **研究证据**:改善ED,降低心血管风险
- **机制**:改善血管健康,降低炎症

**限制**:
- **饱和脂肪**:减少红肉和全脂乳制品
- **反式脂肪**:避免加工食品
- **添加糖**:控制糖分摄入,特别是糖尿病患者
- **酒精**:男性每日<2杯

**营养状况评估**:
- 评估营养素缺乏
- 提供个性化营养建议
- 推荐补充剂(如需要)
- 监测营养改善效果

#### 5.5 与运动模块的关联

**有氧运动**:
- **类型**:快走、跑步、游泳、骑行
- **推荐量**:每周150分钟中等强度
- **对ED的益处**:
  - 改善心血管健康
  - 增强血流
  - 降低ED风险约40%
  - IIEF-5评分平均提高2-4分
- **机制**:
  - 改善内皮功能
  - 增加一氧化氮生物利用度
  - 降低血压和血糖

**力量训练**:
- **类型**:重量训练、抗阻训练
- **推荐量**:每周2-3次
- **对性功能的益处**:
  - 提高睾酮水平
  - 增强肌肉力量和耐力
  - 改善身体意象和自信
- **注意事项**:
  - 避免过度训练
  - 充分恢复

**盆底肌训练(凯格尔运动)**:
- **功能**:
  - 增强勃起硬度和维持能力
  - 改善射精控制
  - 对ED和早泄均有益
- **方法**:
  - 收缩盆底肌肉(如中断排尿)
  - 保持5秒,放松5秒
  - 每日3组,每组10-15次
- **效果**:
  - 6-12周后显著改善
  - IIEF-5评分平均提高3-5分

**瑜伽**:
- **益处**:
  - 改善身体意象和性自信
  - 增强柔韧性和身体意识
  - 降低压力和焦虑
  - 某些体式增强盆底肌
- **推荐**:
  - 每周2-3次
  - 结合冥想和呼吸练习

**运动与性欲**:
- 适度运动提高性欲
- 过度运动可能降低性欲(女运动员三联征)
- 找到平衡点

**运动处方**:
- 基于年龄、健康状况、兴趣
- 渐进式增加
- 结合有氧、力量、柔韧性训练
- 盆底肌训练作为补充

### 6. 风险评估

#### 6.1 ED风险评分

**风险因素加权**:

| 风险因素 | 权重 | 评分 |
|----------|------|------|
| 年龄 | 15% | <40:0, 40-49:1, 50-59:2, 60+:3 |
| 糖尿病 | 20% | 无:0, 控制:1, 未控制:3 |
| 心血管疾病 | 15% | 无:0, 稳定:1, 不稳定:3 |
| 高血压 | 10% | 无:0, 控制:1, 未控制:2 |
| 吸烟 | 10% | 从不:0, 已戒烟:1, 吸烟:2 |
| 酗酒 | 5% | 无:0, 偶尔:1, 经常:2 |
| 肥胖 | 10% | BMI<25:0, 25-30:1, >30:2 |
| 缺乏运动 | 5% | 规律:0, 偶尔:1, 缺乏:2 |
| 压力/焦虑 | 5% | 无:0, 轻度:1, 中重度:2 |
| 药物副作用 | 5% | 无:0, 轻度:1, 明显:2 |

**风险等级**:
- **低风险**(0-20分):ED可能性低
- **中风险**(21-40分):ED风险增加
- **高风险**(41-60分):ED高度可能
- **极高风险**(>60分):几乎肯定有ED

#### 6.2 STD风险评分

**行为因素**:

| 风险因素 | 评分 |
|----------|------|
| 性伴侣数量 | 单一:0, 2-3:5, 4-10:15, >10:30 |
| 保护措施使用 | 总是:0, 通常:5, 有时:15, 从不:30 |
| 性伴侣类型 | 固定:0, 新伴侣/偶尔:10, 性工作者:30 |
| MSM | 否:0, 是:20 |
| 已知伴侣感染 | 无:0, 有:50 |
| 注射吸毒 | 否:0, 是:30 |
| 既往STD史 | 无:0, 1次:10, >1次:20 |

**风险等级**:
- **低风险**(0-10分):STD可能性低
- **中风险**(11-30分):STD风险增加
- **高风险**(31-50分):STD高度可能
- **极高风险**(>50分):需要立即筛查

### 7. 个性化建议

#### 7.1 基于IIEF-5评分的建议

**正常(22-25分)**:
- 继续健康生活方式
- 定期评估(每年)
- 预防性措施

**轻度ED(17-21分)**:
- 生活方式干预优先
- 压力管理
- 限制酒精和戒烟
- 3-6个月后重新评估

**轻中度ED(12-16分)**:
- 生活方式干预
- 考虑PDE5抑制剂
- 心理因素评估
- 建议就医

**中度ED(8-11分)**:
- 积极医疗干预
- PDE5抑制剂
- 考虑其他治疗选项
- 心理咨询

**重度ED(5-7分)**:
- 全面医疗评估
- 多学科治疗
- 可能需要专科转诊
- 伴侣参与

#### 7.2 基于风险评估的建议

**高风险ED**:
- 定期筛查(每3-6个月)
- 积极控制危险因素
- 预防性干预
- 早期治疗

**高风险STD**:
- 频繁筛查(每3个月)
- PrEP(暴露前预防)考虑
- 疫苗接种(HPV、乙肝)
- 风险降低咨询

#### 7.3 生活方式处方

**运动处方**:
- 有氧运动:每周150分钟
- 力量训练:每周2-3次
- 盆底肌训练:每日
- 灵活性训练:每周2-3次

**饮食处方**:
- 地中海饮食模式
- 增加水果蔬菜至5-9份/天
- 全谷物替代精制谷物
- 每周2次深海鱼类
- 限制加工食品和添加糖

**行为处方**:
- 戒烟计划
- 限酒:男性<2杯/天
- 睡眠改善:7-9小时/天
- 压力管理:每日放松练习
- 体重管理:BMI 18.5-24.9

### 8. 预警系统

#### 8.1 定期检查提醒

**IIEF-5评估**:
- 正常:每年
- 轻度ED:每6个月
- 中度以上:每3-6个月

**STD筛查**:
- 基于风险等级个性化设置
- 高风险:每3个月
- 一般风险:每年
- 低风险:每1-2年

**性健康检查**:
- 40岁以下:每1-2年
- 40岁以上:每年
- 慢性病患者:每年

#### 8.2 问题预警

**IIEF-5评分下降**:
- 连续2次评估下降>3分
- 一个月内下降>5分
- ED严重程度升级

**STD高风险行为**:
- 无保护性行为增加
- 性伴侣数量增加
- 已知暴露后未筛查

**避孕失效**:
- 避孕套破裂>2次/月
- 漏服避孕药>2次/月
- IUD位置异常

#### 8.3 趋势预警

**性欲显著下降**:
- 持续>3个月
- 影响生活质量
- 伴侣关系受影响

**满意度持续降低**:
- 平均满意度<5分
- 持续下降趋势
- 需要专业评估

## 使用场景

### 场景1:定期性健康评估

**用户请求**:分析最近6个月的性健康状况

**分析流程**:
1. 读取最近6个月的所有性健康记录
2. 分析IIEF-5评分变化趋势
3. 评估STD筛查历史
4. 检查避孕方法有效性
5. 分析用药效果
6. 评估生活方式因素

**输出内容**:
- IIEF-5评分变化曲线
- ED严重程度变化
- 主要风险因素
- 改善建议
- 下次检查时间

### 场景2:ED诊断辅助

**用户请求**:我最近勃起困难,IIEF-5评分15分,什么原因?

**分析流程**:
1. 检索最近IIEF-5评分历史
2. 分析用药记录
3. 评估慢性病控制情况
4. 检查心理状态记录
5. 分析生活方式因素
6. 识别主要原因

**输出内容**:
- ED严重程度:轻中度
- 主要风险因素(如糖尿病控制不佳)
- 可修改因素(如吸烟、缺乏运动)
- 药物影响分析
- 个性化改善计划

### 场景3:避孕方法选择

**用户请求**:我想换一种避孕方法,当前口服避孕药有副作用

**分析流程**:
1. 评估当前避孕方法满意度和副作用
2. 分析健康史和风险因素
3. 考虑年龄和生育计划
4. 对比各种避孕方法的优缺点
5. 识别适合的替代方案

**输出内容**:
- 当前方法问题分析
- 适合的替代方案
- 各方案优缺点对比
- 推荐方案及理由
- 切换时间建议

### 场景4:STD风险评估

**用户请求**:我最近有新伴侣,需要STD筛查吗?

**分析流程**:
1. 评估性行为模式
2. 识别风险因素
3. 计算风险评分
4. 确定需要筛查的项目
5. 设置筛查时间表

**输出内容**:
- 当前风险等级
- 推荐筛查项目
- 筛查时间建议
- 风险降低措施
- 随访计划

### 场景5:多学科联合分析

**用户请求**:我有糖尿病,这对性功能有什么影响?

**分析流程**:
1. 读取糖尿病管理数据
2. 分析血糖控制情况
3. 评估性功能状态
4. 分析两者关联性
5. 评估并发症风险
6. 生成联合管理建议

**输出内容**:
- 糖尿病对性功能的影响机制
- 当前血糖控制与ED风险
- 综合管理策略
- 监测指标建议
- 生活方式干预重点

## 数据分析方法

### 定量分析
- 统计描述(均值、中位数、标准差)
- 趋势分析(线性回归、移动平均)
- 相关性分析(Pearson/Spearman相关)
- 风险评分计算(多因素加权)

### 定性分析
- 文本描述分析
- 症状模式识别
- 主诉内容分类
- 满意度评估

### 可视化输出
- IIEF-5评分时间序列图表
- ED严重程度变化图
- STD筛查历史时间线
- 避孕方法效果对比
- 性活动频率统计图
- 风险因素雷达图

## 质量保证

### 数据验证
- 检查数据完整性
- 验证数据一致性
- 识别异常值
- 处理缺失数据

### 结果验证
- 医学逻辑检查
- 与临床指南对照
- 专家审查(如有)
- 用户反馈收集

### 持续改进
- 定期更新分析算法
- 引入新的科学证据
- 优化用户体验
- 扩展功能范围

## 参考资源

### 临床指南
- WHO性健康指南
- EAU(欧洲泌尿协会)ED指南
- AUA(美国泌尿协会)性功能障碍指南
- CDCSTD筛查和治疗指南
- 中华医学会男科学指南

### 评估工具
- IIEF-5(国际勃起功能指数-5)
- FSFI(女性性功能指数)
- SHEF(性健康评估框架)

### 数据源
- 用户记录数据
- 用药模块数据
- 慢性病模块数据
- 心理模块数据
- 营养模块数据
- 运动模块数据

## 局限性

### 系统局限
- 不能替代专业医疗检查
- 不能进行实验室检测
- 不能进行体格检查
- 分析结果受数据质量影响

### 数据局限
- 依赖用户记录准确性
- 可能存在遗漏记录
- 主观评估存在偏差
- 时间跨度可能不足

### 建议局限
- 不能考虑所有个体因素
- 不能预测所有并发症
- 需要结合临床判断
- 不能保证100%准确性

## 未来扩展

### 计划功能
- AI辅助诊断
- 个性化治疗方案生成
- 伴侣健康关联分析
- 生殖健康追踪(生育规划)
- 性教育模块

### 研究方向
- 机器学习预测模型
- 基因风险分析
- 个性化预防策略
- 远程医疗集成

---

**版本**: v1.0.0
**最后更新**: 2025-01-06
**维护者**: WellAlly Tech

## Source: references/skills/healthcare-workflows/references/legacy/skin-health-analyzer/SKILL.md

---
name: skin-health-analyzer
description: Analyze skin health data, identify skin problem patterns, assess skin health status. Supports correlation analysis with nutrition, chronic diseases, and medication data.
risk: unknown
source: community
---

# 皮肤健康分析技能

## 技能概述

本技能提供全面的皮肤健康数据分析功能，包括趋势识别、风险评估、问题诊断和个性化建议生成。特别强调痣的监测和皮肤癌预防。

## 医学免责声明

⚠️ **重要提示**：本技能提供的数据分析和建议仅供参考，不构成医学诊断或治疗建议。

- 所有皮肤问题应由专业皮肤科医生诊断和治疗
- 痣的异常变化必须立即就医检查
- 皮肤癌需要专业诊断，不能仅依靠自我评估
- 分析结果不能替代专业皮肤科检查
- 紧急情况应立即就医
- 请遵循皮肤科医生的专业建议

## 核心功能

### 1. 趋势分析

#### 皮肤问题发展趋势
- 识别痤疮、湿疹等问题的发生模式
- 分析问题的季节性和周期性
- 评估问题严重程度的变化
- 预测未来发作风险

**输出内容**：
- 问题发生频率曲线
- 严重程度变化趋势
- 诱发因素分析
- 预防建议

#### 痣的变化监测
- 新增痣的位置和数量追踪
- 已有痣的大小变化监测
- ABCDE特征变化记录
- 高风险痣识别

**输出内容**：
- 痣的分布图
- 变化预警报告
- 需要关注的美容痣列表
- 就医建议

#### 护肤效果评估
- 护肤程序使用频率分析
- 产品效果评估
- 皮肤状态改善情况
- 不良反应监测

**输出内容**：
- 护肤效果评分
- 产品推荐
- 程序优化建议
- 成本效益分析

#### 日晒防护效果分析
- 防晒霜使用情况统计
- 日晒伤发生频率
- 光老化迹象评估
- 防护习惯改进建议

**输出内容**：
- 防护评分趋势
- 风险评估
- 改进建议
- 产品推荐

### 2. 风险评估

#### 皮肤癌风险评估
基于以下因素进行综合评估：
- 皮肤类型（Fitzpatrick分型）
- 日晒暴露史
- 痣的数量和特征
- 日晒伤历史
- 家族史
- 使用日光浴床历史

**风险等级**：
- **低风险**：深色皮肤、少日晒、无痣异常
- **中风险**：浅色皮肤、中度日晒、有痣异常
- **高风险**：浅色皮肤、大量日晒、多个异常痣、家族史

**输出内容**：
- 风险等级（低/中/高）
- 主要风险因素
- 量化风险评分
- 降低风险策略
- 筛查建议

#### 痤疮严重程度评估
基于以下因素进行综合评估：
- 痤疮类型（黑头、白头、炎性丘疹、结节、囊肿）
- 病灶数量和分布
- 炎症程度
- 瘢痕形成风险

**严重程度分级**：
- **轻度**：主要是黑头和白头，少量炎性病灶
- **中度**：较多炎性病灶，可能形成轻微瘢痕
- **重度**：结节和囊肿，高瘢痕风险

**输出内容**：
- 严重程度分级
- 主要诱因分析
- 治疗建议参考
- 护肤建议
- 就医建议

#### 过敏风险识别
基于以下因素进行综合评估：
- 已知过敏原
- 皮肤敏感史
- 产品使用历史
- 季节性过敏模式
- 家族过敏史

**输出内容**：
- 过敏原列表
- 风险评估
- 避免建议
- 替代产品推荐

#### 光老化风险预测
基于以下因素进行综合评估：
- 日晒暴露总量
- 防护习惯
- 皮肤类型
- 年龄
- 生活方式

**输出内容**：
- 光老化风险等级
- 当前光老化迹象
- 预防建议
- 治疗选择参考

### 3. 关联分析

#### 与营养模块的关联
**营养素对皮肤健康的影响**：
- 维生素A：皮肤细胞更新、视力
- 维生素C：胶原蛋白合成、抗氧化
- 维生素E：抗氧化、保护细胞膜
- Omega-3脂肪酸：抗炎作用
- 锌：伤口愈合、油脂控制
- 水：皮肤水合作用

**食物对皮肤问题的影响**：
- 高糖食物：痤疮加重
- 乳制品：部分人群痤疮诱发因素
- 辛辣食物：玫瑰痤疮加重
- 酒精：皮肤脱水、潮红

**营养缺乏的皮肤表现**：
- 维生素A缺乏：皮肤干燥、角化
- 维生素C缺乏：伤口愈合慢、易淤青
- 维生素B缺乏：皮炎、口角炎
- 铁缺乏：苍白、脆弱
- 蛋白质缺乏：皮肤松弛、水肿

**输出内容**：
- 营养状况评估
- 缺乏风险识别
- 饮食调整建议
- 补充剂建议（如需要）

#### 与慢性病模块的关联
**糖尿病与皮肤**：
- 糖尿病皮肤病（糖尿病性皮肤病）
- 伤口愈合延迟
- 真菌感染风险增加
- 黑棘皮病
- 脂质性渐进性坏死

**自身免疫病与皮肤**：
- 狼疮：蝶形红斑、光敏感
- 类风湿关节炎：类风湿结节、血管炎
- 银屑病关节炎：银屑病皮损
- 皮肌炎：Gottron征、向阳性皮疹

**甲状腺疾病与皮肤**：
- 甲亢：皮肤湿润、头发变细、指甲松动
- 甲减：皮肤干燥、毛发粗燥、水肿

**肝脏疾病与皮肤**：
- 黄疸：皮肤和巩膜黄染
- 蜘蛛痣：血管性蜘蛛状病变
- 掌红斑：手掌红斑
- 皮肤瘙痒：胆汁淤积

**输出内容**：
- 皮肤症状与疾病关联分析
- 并发症风险评估
- 综合管理建议
- 专科转诊建议

#### 与用药模块的关联
**药物疹（药物过敏）**：
- 常见致敏药物：抗生素、抗癫痫药、NSAIDs
- 皮疹类型：麻疹样、荨麻疹、固定药疹
- 严重反应：Stevens-Johnson综合征

**光敏性药物**：
- 四环素类抗生素
- 噻嗪类利尿剂
- NSAIDs
- 某些抗精神病药

**药物引起的色素沉着**：
- 米诺环素：蓝色灰色色素沉着
- 胺碘酮：蓝灰色色素沉着
- 某些化疗药物

**药物引起的皮肤干燥**：
- 维A酸类
- 苯二氮卓类
- 抗组胺药（长期使用）

**输出内容**：
- 药物风险识别
- 相互作用分析
- 替代药物建议（需与医生讨论）
- 监测建议

#### 与内分泌模块的关联
**激素变化对皮肤的影响**：
- 青春期：雄激素增加，痤疮
- 妊娠期：色素沉着、妊娠纹、皮肤血管变化
- 更年期：雌激素下降，皮肤干燥、皱纹
- 月经周期：周期性痤疮加重

**多囊卵巢综合征（PCOS）**：
- 痤疮
- 多毛症
- 雄激素性脱发
- 黑棘皮病

**库欣综合征**：
- 月亮脸、水牛背
- 皮肤变薄、紫纹
- 痤疮、多毛

**输出内容**：
- 激素对皮肤的影响分析
- 周期性症状识别
- 管理建议
- 治疗时机建议

### 4. 个性化建议

#### 护肤程序优化
**根据皮肤类型定制**：
- 干性皮肤：加强保湿，避免过度清洁
- 油性皮肤：控油，保持清洁，水油平衡
- 混合性皮肤：分区护理，T区控油，U区保湿
- 中性皮肤：维持现状，基础护理
- 敏感性皮肤：温和产品，避免刺激

**根据主要问题定制**：
- 痤疮：清洁、控油、抗炎、避免致痘成分
- 色斑：防晒、美白成分、抗氧化
- 抗衰老：抗氧化、修复、防晒
- 敏感：舒缓、修复、屏障保护

**输出内容**：
- 早晨护肤程序建议
- 晚间护肤程序建议
- 每周护理建议
- 产品选择指导
- 预算范围建议

#### 生活方式调整
**饮食调整**：
- 低升糖指数饮食（痤疮）
- 抗炎饮食（湿疹、银屑病）
- 抗氧化食物（抗衰老）
- 充足水分摄入

**睡眠管理**：
- 保证7-9小时睡眠
- 规律作息时间
- 睡前护肤程序
- 枕头清洁（痤疮）

**压力管理**：
- 识别压力诱发的皮肤问题
- 学习放松技巧
- 规律运动
- 兴爱好

**环境调整**：
- 室内湿度控制（干燥皮肤）
- 避免过敏原（过敏肌肤）
- 工作环境防护（职业性皮肤问题）

**输出内容**：
- 个性化生活方式建议
- 目标设定
- 进度追踪方法
- 激励机制

#### 预防措施建议
**皮肤癌预防**：
- 每日防晒（SPF 30+）
- 避免日光浴床
- 定期皮肤检查
- 保护儿童免受日晒
- 早期发现异常痣

**痤疮预防**：
- 正确清洁皮肤
- 避免触摸面部
- 清洁手机和眼镜
- 更换枕套频率
- 非致痘性化妆品

**湿疹预防**：
- 保持皮肤保湿
- 避免已知诱因
- 使用温和洗涤剂
- 穿着棉质衣物
- 控制室内温度和湿度

**光老化预防**：
- 全年防晒
- 抗氧化护肤品
- 不吸烟
- 充足睡眠
- 健康饮食

**输出内容**：
- 针对性预防策略
- 优先级排序
- 实施步骤
- 效果评估方法

#### 产品选择建议
**成分知识**：
- 痤疮治疗：水杨酸、过氧化苯甲酰、维A酸
- 美白：维生素C、烟酰胺、熊果苷
- 抗衰老：视黄醇、肽类、透明质酸
- 保湿：透明质酸、甘油、神经酰胺
- 舒缓：芦荟、积雪草、燕麦

**产品选择原则**：
- 根据皮肤类型选择
- 避免已知过敏原
- 成分简单优于复杂
- 无香料配方更安全
- 先试用小包装

**阅读产品标签**：
- 识别致痘成分
- 识别过敏原
- 理解活性成分浓度
- 理解产品功效宣称

**输出内容**：
- 成分教育
- 产品推荐框架（非具体品牌）
- 避免成分列表
- 产品试用建议

### 5. 目标管理

#### 目标设定
- 与用户协商设定现实目标
- 分解为可实现的步骤
- 设定时间节点
- 建立评估标准

**常见目标类型**：
- 改善痤疮状况
- 建立规律护肤习惯
- 增加防晒使用频率
- 减少色斑
- 改善皮肤干燥
- 建立定期自查习惯

#### 进度追踪
- 定期评估目标达成情况
- 提供激励和反馈
- 调整目标（如需要）
- 庆祝里程碑达成
- 记录改进过程

#### 障碍识别
- 识别阻碍目标达成的因素
- 提供克服障碍的策略
- 调整计划以适应实际情况
- 提供持续支持
- 连接资源和支持网络

### 6. 统计分析

#### 综合健康评分
基于以下因素计算：
- 皮肤问题控制情况（30%）
- 护肤习惯（25%）
- 日晒防护（20%）
- 定期检查（15%）
- 目标达成（10%）

**评分范围**：0-100分
- **优秀**：90-100分
- **良好**：75-89分
- **一般**：60-74分
- **较差**：<60分

#### 皮肤健康年龄
- 基于皮肤状态、问题情况、防护习惯计算
- 与实际年龄对比
- 提供改善建议

#### 问题统计
- 问题类型分布
- 问题发生频率
- 问题持续时间
- 解决率统计
- 复发率分析

#### 护肤统计
- 护肤程序执行率
- 产品使用频率
- 护肤花费统计
- 产品更换频率
- 不良反应统计

### 7. 预警系统

#### 痣的变化预警
- 新增痣数量异常增加
- 已有痣快速增大
- ABCDE特征出现异常
- 颜色或形态改变
- 出现症状（瘙痒、出血）

**预警级别**：
- **黄色预警**：需要观察，下次检查时咨询医生
- **橙色预警**：需要尽快就医（1周内）
- **红色预警**：需要立即就医

#### 皮肤问题预警
- 痤疮突然恶化
- 新出现严重皮疹
- 药物反应迹象
- 感染征象（红肿热痛）
- 慢性病皮肤表现

#### 护肤预警
- 产品不良反应
- 护肤程序不当
- 过度护肤征象
- 过期产品使用
- 产品相互作用

#### 检查提醒
- 定期皮肤自查提醒（每月）
- 皮肤科检查提醒（每年）
- 痣监测提醒（每月）
- 防晒补涂提醒

## 使用场景

### 场景1：定期健康评估
**用户请求**：分析最近6个月的皮肤健康状况

**分析流程**：
1. 读取最近6个月的所有皮肤健康记录
2. 分析问题记录、痣监测、护肤记录
3. 评估防护习惯变化
4. 计算健康评分变化
5. 识别改善或恶化的趋势
6. 生成综合评估报告

**输出内容**：
- 健康评分变化趋势
- 主要改善点
- 需要关注的问题
- 下一步行动建议

### 场景2：痣的监测评估
**用户请求**：我发现背部有个痣有些变化，帮我评估一下

**分析流程**：
1. 检索该痣的历史记录
2. 对比ABCDE特征变化
3. 评估风险等级
4. 检查是否有其他异常痣
5. 分析个人风险因素
6. 生成评估报告

**输出内容**：
- ABCDE评估结果
- 变化程度分析
- 风险等级
- 就医建议（强烈建议/建议/观察）
- 监测频率建议

### 场景3：痤疮管理规划
**用户请求**：我想改善痤疮问题，制定一个管理计划

**分析流程**：
1. 评估当前痤疮严重程度
2. 分析主要诱发因素
3. 评估当前护肤和饮食习惯
4. 识别需要改善的领域
5. 设定阶段性目标
6. 制定个性化计划

**输出内容**：
- 当前严重程度评估
- 主要诱因分析
- 护肤程序建议
- 饮食和生活方式建议
- 目标和时间表
- 何时就医建议

### 场景4：防晒改进计划
**用户请求**：我的防晒习惯不好，帮我制定改进计划

**分析流程**：
1. 评估当前防晒习惯
2. 分析日晒暴露模式
3. 评估皮肤类型和风险
4. 识别主要障碍
5. 设定可达成的目标
6. 制定渐进式改进计划

**输出内容**：
- 当前防晒评分
- 风险评估
- 改进目标
- 产品选择建议
- 使用习惯建立策略
- 进度追踪方法

### 场景5：多学科联合分析
**用户请求**：我有糖尿病，这对我的皮肤有什么影响？

**分析流程**：
1. 读取糖尿病管理数据
2. 分析血糖控制情况
3. 评估皮肤并发症风险
4. 识别潜在的糖尿病皮肤问题
5. 分析两者关联性
6. 生成联合管理建议

**输出内容**：
- 糖尿病对皮肤的影响
- 常见糖尿病皮肤问题
- 并发症风险评估
- 联合管理策略
- 监测指标建议
- 何时就医

### 场景6：抗衰老规划
**用户请求**：我想预防皮肤老化，从现在开始应该注意什么？

**分析流程**：
1. 评估当前皮肤状态
2. 分析生活方式和习惯
3. 评估光老化风险
4. 识别可改变的风险因素
5. 制定预防策略
6. 建立监测指标

**输出内容**：
- 当前皮肤年龄评估
- 主要老化风险因素
- 预防策略（防晒、护肤、生活方式）
- 护肤程序建议
- 定期评估建议
- 投资回报分析

## 数据分析方法

### 定量分析
- 统计描述（均值、中位数、标准差）
- 趋势分析（线性回归、移动平均）
- 相关性分析（Pearson/Spearman相关）
- 风险评分计算（多因素加权）
- 时间序列分析

### 定性分析
- 文本描述分析
- 症状模式识别
- 主诉内容分类
- 满意度评估
- 图片分析（如可用）

### ABCDE评估算法
- 不对称性评分（0-2分）
- 边缘规则性评分（0-2分）
- 颜色均匀性评分（0-2分）
- 直径评分（0-2分）
- 变化评分（0-2分）
- 总分≥4分：建议就医

### 可视化输出
- 时间序列图表
- 身体部位分布图
- 痣的位置地图
- 风险评估雷达图
- 进度追踪仪表板
- 对比分析柱状图

## 质量保证

### 数据验证
- 检查数据完整性
- 验证数据一致性
- 识别异常值
- 处理缺失数据
- 交叉验证不同来源数据

### 结果验证
- 医学逻辑检查
- 与临床指南对照
- 专家审查（如有）
- 用户反馈收集
- 定期更新算法

### 持续改进
- 定期更新分析算法
- 引入新的科学证据
- 优化用户体验
- 扩展功能范围
- 提高准确性

## 参考资源

### 临床指南
- 美国皮肤病学会（AAD）指南
- 欧洲皮肤病学会（EADV）指南
- 中华皮肤科分会临床指南
- 皮肤癌基金会（SCF）指南

### 评估工具
- ABCDE法则（黑色素瘤筛查）
- Glasgow七点清单（黑色素瘤评估）
- 痤疮严重程度评分系统
- 湿疹面积和严重程度指数（EASI）
- 皮肤病生活质量指数（DLQI）

### 数据源
- 用户记录数据
- 营养模块数据
- 慢性病模块数据
- 用药模块数据
- 内分泌模块数据
- 环境数据（紫外线指数）

## 局限性

### 系统局限
- 不能替代专业皮肤科检查
- 不能进行皮肤镜检查
- 不能进行病理检查
- 分析结果受数据质量影响
- 不能进行生物活检

### 数据局限
- 依赖用户记录准确性
- 可能存在遗漏记录
- 主观评估存在偏差
- 时间跨度可能不足
- 照片质量影响评估

### 建议局限
- 不能考虑所有个体因素
- 不能预测所有并发症
- 需要结合临床判断
- 不能保证100%准确性
- 产品建议可能存在个体差异

## 未来扩展

### 计划功能
- AI图像识别（痣和皮肤病变分析）
- 语音记录录入
- 智能提醒系统
- 与皮肤科医生系统对接
- 远程皮肤病学支持

### 研究方向
- 机器学习预测模型
- 个性化预防策略
- 基因风险分析
- 皮肤微生物组分析
- 环境因素影响分析

---

**版本**: v1.0.0
**最后更新**: 2025-01-06
**维护者**: WellAlly Tech


## When to Use

Use this skill when tackling tasks related to its primary domain or functionality as described above.

## Source: references/skills/healthcare-workflows/references/legacy/sleep-analyzer/SKILL.md

---
name: sleep-analyzer
description: 分析睡眠数据、识别睡眠模式、评估睡眠质量，并提供个性化睡眠改善建议。支持与其他健康数据的关联分析。
allowed-tools: Read, Grep, Glob, Write
---

# 睡眠分析器技能

分析睡眠数据，识别睡眠模式，评估睡眠质量，并提供个性化睡眠改善建议。

## 功能

### 1. 睡眠趋势分析

分析睡眠时长、质量、效率的变化趋势，识别改善或需要关注的方面。

**分析维度**：
- 睡眠时长趋势（平均睡眠时长变化）
- 睡眠效率趋势（睡眠效率百分比变化）
- 入睡时间模式（上床时间、入睡时间、起床时间）
- 作息规律性评分（sleep consistency score）
- 周末vs工作日对比（social jetlag）

**输出**：
- 趋势方向（改善/稳定/下降）
- 变化幅度和百分比
- 趋势显著性评估
- 最佳睡眠时间窗口识别
- 改进建议

### 2. 睡眠质量评估

综合评估睡眠质量，识别影响睡眠质量的关键因素。

**评估内容**：
- PSQI分数追踪和趋势
- 主观睡眠质量分布（好/中/差）
- 夜间觉醒分析（次数、时长、原因）
- 睡眠阶段分析（深睡、浅睡、REM比例）
- 睡后恢复感评估

**输出**：
- 睡眠质量等级（优秀/良好/一般/较差）
- 质量变化趋势
- 主要影响因素识别
- 质量改善优先级建议

### 3. 睡眠问题识别

识别常见的睡眠问题和风险因素。

**识别内容**：
- **失眠模式**：
  - 入睡困难（sleep latency >30分钟）
  - 睡眠维持困难（夜间觉醒>2次或总觉醒时间>30分钟）
  - 早醒（比预期提前醒来>30分钟）
  - 混合型失眠

- **呼吸暂停风险**：
  - STOP-BANG问卷评分
  - 症状分析（打鼾、憋醒、白天嗜睡）
  - 风险等级（低/中/高）

- **其他问题**：
  - 作息不规律检测
  - 睡眠债计算（理想时长vs实际时长）
  - 社交时差评估

**输出**：
- 问题存在与否
- 问题类型和严重程度
- 风险因素列表
- 是否需要就医建议

### 4. 相关性分析

分析睡眠与其他健康指标的相关性。

**支持的相关性分析**：
- **睡眠 ↔ 运动**：
  - 运动日vs休息日的睡眠差异
  - 运动时间对睡眠的影响（早晨/下午/晚间运动）
  - 运动强度与睡眠质量的相关性

- **睡眠 ↔ 饮食**：
  - 咖啡因摄入与睡眠时长、入睡时间的关系
  - 酒精摄入对睡眠结构的影响
  - 晚餐时间与睡眠质量的关系

- **睡眠 ↔ 情绪**：
  - 睡眠与情绪的双向关系分析
  - 压力水平对睡眠质量的影响
  - 睡眠剥夺对日间情绪的影响

- **睡眠 ↔ 慢性病**：
  - 睡眠与高血压的关系
  - 睡眠与血糖控制的关联
  - 睡眠与体重变化的关系

**输出**：
- 相关系数（-1到1）
- 相关性强度（弱/中/强）
- 统计显著性
- 因果关系推断
- 实践建议

### 5. 个性化建议生成

基于用户数据生成个性化睡眠改善建议。

**建议类型**：
- **作息调整建议**：
  - 最佳上床/起床时间
  - 作息一致性改善方案
  - 午睡管理建议

- **睡前准备建议**：
  - 睡前例行程序设计
  - 放松技巧推荐
  - 屏幕时间管理

- **睡眠环境优化**：
  - 温度、湿度、光线、噪音优化
  - 床品舒适度建议

- **生活方式调整**：
  - 运动、饮食、咖啡因、酒精管理
  - 压力管理建议

- **CBT-I元素**：
  - 刺激控制建议
  - 睡眠限制建议
  - 认知重构建议

**输出**：
- 优先级排序的建议列表
- 具体实施步骤
- 预期效果说明
- 实施时间线

---

## 使用说明

### 触发条件

当用户请求以下内容时触发本技能：
- 睡眠趋势分析
- 睡眠质量评估
- 睡眠问题识别
- 睡眠改善建议
- 睡眠与其他健康指标的关联分析

### 执行步骤

#### 步骤 1: 确定分析范围

明确用户请求的分析类型和时间范围：
- 分析类型：趋势/质量/问题/相关性/建议
- 时间范围：周/月/季度/自定义

#### 步骤 2: 读取数据

**主要数据源**：
1. `data-example/sleep-tracker.json` - 睡眠追踪主数据
2. `data-example/sleep-logs/YYYY-MM/YYYY-MM-DD.json` - 每日睡眠记录

**关联数据源**：
1. `data-example/fitness-tracker.json` - 运动数据
2. `data-example/hypertension-tracker.json` - 血压数据
3. `data-example/diabetes-tracker.json` - 血糖数据
4. `data-example/diet-records/` - 饮食记录
5. `data-example/mood-tracker.json` - 情绪数据

#### 步骤 3: 数据分析

根据分析类型执行相应的分析算法：

**趋势分析算法**：
- 线性回归计算趋势斜率
- 移动平均平滑波动
- 统计显著性检验

**相关性分析算法**：
- Pearson相关系数计算
- 滞后相关性分析（考虑时间延迟效应）
- 多变量回归分析

**模式识别算法**：
- 时间序列模式识别
- 异常值检测
- 周期性分析

#### 步骤 4: 生成报告

按照标准格式输出分析报告（见"输出格式"部分）

---

## 输出格式

### 睡眠质量分析报告

```markdown
# 睡眠质量分析报告

## 分析周期
2025-03-20 至 2025-06-20（3个月）

---

## 睡眠时长趋势

- **趋势**：⬆️ 改善
- **开始**：平均6.2小时/晚
- **当前**：平均7.1小时/晚
- **变化**：+0.9小时 (+14.5%)
- **解读**：睡眠时长显著增加，接近理想目标（7.5小时）

**趋势线**：
```
6.5h ┤     ╭╮
6.0h ┤   ╭─╯╰╮
5.5h ┤ ╭─╯   ╰─╮
5.0h ┼─┘       ╰─
     └───────────
     3月  4月  5月  6月
```

---

## 睡眠效率

- **平均睡眠效率**：85.3%
- **效率范围**：78%-92%
- **达标率**：63%（>85%为达标）
- **解读**：睡眠效率正常，仍有提升空间

**效率分布**：
- 优秀（>90%）：15晚
- 良好（85-90%）：28晚
- 需改善（<85%）：47晚

---

## 作息规律性

- **平均上床时间**：23:15（范围：22:30-01:00）
- **平均起床时间**：07:05（范围：06:30-08:30）
- **作息一致性评分**：72/100
- **社交时差**：45分钟（周末比工作日晚睡晚起）
- **解读**：作息基本规律，但周末波动较大

**建议**：
- 🎯 保持一致的起床时间，包括周末
- 🎯 逐步调整上床时间，避免周末过度延迟

---

## 睡眠质量分布

| 质量等级 | 天数 | 占比 | 趋势 |
|---------|------|------|------|
| 优秀 | 8 | 9% | ⬆️ |
| 很好 | 12 | 13% | ➡️ |
| 好 | 15 | 17% | ⬆️ |
| 一般 | 42 | 47% | ⬇️ |
| 差 | 10 | 11% | ⬇️ |
| 很差 | 3 | 3% | ➡️ |

**解读**：睡眠质量以"一般"为主，但"好"及以上质量的天数在增加

---

## 夜间觉醒分析

- **平均觉醒次数**：1.8次/晚
- **平均觉醒时长**：18分钟
- **主要原因**：
  1. 尿意（45%）
  2. 噪音（25%）
  3. 温度过热（15%）
  4. 其他（15%）

**建议**：
- 🎯 睡前2小时限制液体摄入
- 🎯 优化卧室温度（18-22℃）
- 🎯 使用白噪音机器遮蔽背景噪音

---

## PSQI 评估趋势

- **最新分数**：8分（睡眠质量一般）
- **上次分数**：10分（2025-03-20）
- **变化**：-2分（改善）
- **趋势**：⬆️ 持续改善

**历史趋势**：
```
12 ┤ ●
10 ┤  ●
 8 ┤    ●
 6 ┤
   └──────
   12月 3月 6月
```

**各成分变化**：
- 主观睡眠质量：2→2（稳定）
- 入睡时间：2→2（稳定）
- 睡眠时长：2→1（改善）
- 睡眠效率：2→1（改善）
- 睡眠障碍：2→1（改善）

---

## 睡眠问题识别

### 失眠评估

- **类型**：混合型失眠
- **频率**：4-5晚/周
- **持续时间**：18个月
- **主要症状**：
  - ✗ 入睡困难（潜伏期>30分钟）
  - ✗ 睡眠维持困难（夜间觉醒>2次）
  - ✓ 无早醒问题

- **影响**：
  - 白天疲劳：中度
  - 情绪烦躁：是
  - 注意力困难：是
  - 工作表现：轻度影响

- **建议**：🏥 持续>3个月，建议就医咨询睡眠专科

### 呼吸暂停筛查（STOP-BANG）

- **评分**：3/8
- **风险等级**：中等风险
- **阳性项目**：
  - ✗ Snoring（打鼾）
  - ✗ Tired（白天疲劳）
  - ✓ Observed apnea（未观察到呼吸暂停）
  - ✗ Pressure（高血压）
  - ✓ BMI > 28
  - ✓ Age > 50
  - ✗ Neck size > 40cm
  - ✓ Gender = male

- **建议**：⚠️ 建议进行睡眠检查（PSG）

---

## 相关性分析

### 睡眠 ↔ 运动

**运动日 vs 休息日**：
- 运动日平均睡眠：7.3小时
- 休息日平均睡眠：6.8小时
- 差异：+0.5小时（+7.4%）

**运动时间对睡眠的影响**：
- 早晨运动：睡眠时长7.5小时，质量评分7.8/10
- 下午运动：睡眠时长7.2小时，质量评分7.5/10
- 晚间运动：睡眠时长6.8小时，质量评分6.8/10

**相关性**：中等正相关（r = 0.42）
**结论**：规律运动有助于改善睡眠，但应避免睡前2-3小时剧烈运动

**建议**：
- 🎯 保持规律运动习惯
- 🎯 将运动时间移至早晨或下午
- 🎯 睡前2-3小时避免剧烈运动

---

### 睡眠 ↔ 咖啡因

**咖啡因摄入时间分析**：
- 下午2点前摄入：平均睡眠7.2小时，入睡潜伏期25分钟
- 下午2点后摄入：平均睡眠6.7小时，入睡潜伏期40分钟
- 差异：-0.5小时时长，+15分钟潜伏期

**相关性**：中等负相关（r = -0.38）
**结论**：下午2点后摄入咖啡因显著影响睡眠

**建议**：
- 🎯 避免下午2点后摄入咖啡因
- 🎯 睡前6小时完全避免咖啡因

---

### 睡眠 ↔ 情绪

**睡眠质量对次日情绪的影响**：
- 睡眠好：次日情绪积极概率82%
- 睡眠一般：次日情绪积极概率45%
- 睡眠差：次日情绪积极概率18%

**睡前情绪对入睡的影响**：
- 睡前压力高：入睡潜伏期45分钟
- 睡前压力低：入睡潜伏期20分钟
- 差异：+25分钟

**相关性**：强双向相关（r = 0.65）
**结论**：睡眠与情绪存在显著的相互影响

**建议**：
- 🎯 睡前进行压力管理（冥想、深呼吸）
- 🎯 建立放松的睡前例行程序
- 🎯 记录情绪日记，识别压力模式

---

## 洞察与建议

### 关键洞察

1. **作息不一致是主要问题**
   - 社交时差45分钟
   - 周末作息显著偏离工作日
   - 影响：生物钟紊乱，周一"时差反应"

2. **晚间运动影响入睡**
   - 晚间运动日入睡潜伏期延长15分钟
   - 建议：调整运动时间

3. **睡眠环境可优化**
   - 噪音觉醒占25%
   - 温度过热占15%
   - 建议针对性改善

---

### 优先级行动计划

#### Priority 1：建立一致作息（2周）

**目标**：提高作息一致性评分至85分

**具体行动**：
1. 固定起床时间07:00（包括周末）
2. 固定上床时间23:00
3. 限制午睡<30分钟，且下午3点前
4. 逐步调整周末作息（每次提前15分钟）

**预期效果**：
- 作息一致性评分：72 → 85
- 睡眠效率提升：+3-5%
- 周一疲劳感减轻

---

#### Priority 2：创建睡前例行程序（3周）

**目标**：建立稳定的睡前例行程序

**具体行动**：
1. 提前1小时开始例行程序（22:00）
2. 关闭电子设备（22:30）
3. 调暗卧室灯光
4. 进行放松活动（阅读、冥想、温水澡）
5. 保持卧室安静、黑暗、凉爽（18-22℃）

**预期效果**：
- 入睡潜伏期缩短：30 → 20分钟
- 睡眠质量提升：一般 → 好
- 睡前压力降低

---

#### Priority 3：优化睡眠环境（1周）

**目标**：消除环境对睡眠的干扰

**具体行动**：
1. 安装遮光窗帘
2. 使用白噪音机器遮蔽背景噪音
3. 优化温度至18-22℃
4. 移除卧室时钟
5. 更换舒适的枕头和床垫

**预期效果**：
- 夜间觉醒减少：1.8 → 1.2次/晚
- 睡眠连续性提升
- 晨起状态改善

---

#### Priority 4：生活方式调整（4周）

**目标**：消除影响睡眠的生活习惯

**具体行动**：
1. 将运动移至早晨或下午
2. 下午2点后停止咖啡因摄入
3. 睡前3小时避免酒精
4. 睡前2小时避免大餐
5. 睡前1小时避免工作相关讨论

**预期效果**：
- 睡眠时长增加：+0.3小时
- 睡眠质量评分提升：+1分
- PSQI分数改善：8 → 6

---

## 长期目标

- **睡眠时长**：达到7.5小时/晚（当前7.1小时）
- **睡眠效率**：提升至>90%（当前85%）
- **PSQI分数**：降至≤5分（当前8分）
- **作息一致性**：提升至≥85分（当前72分）
- **入睡潜伏期**：缩短至<20分钟（当前28分钟）

---

## 医学安全提醒

⚠️ **就医建议**：
- 🏥 失眠持续>3个月，建议咨询睡眠专科
- 🏥 STOP-BANG≥3分，建议进行睡眠检查（PSG）
- 🏥 严重嗜睡影响驾驶安全，需立即就医

---

**报告生成时间**：2025-06-20
**分析周期**：2025-03-20 至 2025-06-20（90天）
**数据记录数**：90晚
**睡眠分析器版本**：v1.0
```

---

## 数据结构

### 睡眠记录数据

```json
{
  "sleep_records": [
    {
      "id": "sleep_20250620001",
      "date": "2025-06-20",
      "sleep_times": {
        "bedtime": "23:00",
        "sleep_onset_time": "23:30",
        "wake_time": "07:00",
        "out_of_bed_time": "07:15"
      },
      "sleep_metrics": {
        "sleep_duration_hours": 7.0,
        "time_in_bed_hours": 8.25,
        "sleep_latency_minutes": 30,
        "sleep_efficiency": 84.8
      },
      "sleep_quality": {
        "subjective_quality": "fair",
        "quality_score": 5,
        "rested_feeling": "somewhat"
      },
      "factors": {
        "exercise": true,
        "exercise_time": "evening",
        "caffeine_after_2pm": false,
        "screen_time_before_bed_minutes": 60
      }
    }
  ]
}
```

---

## 算法说明

### 睡眠质量评分算法

```python
def calculate_sleep_quality_score(record):
    """
    计算睡眠质量评分（0-10分）

    因素权重：
    - 睡眠时长：30%
    - 睡眠效率：25%
    - 入睡潜伏期：20%
    - 夜间觉醒：15%
    - 主观质量：10%
    """
    score = 0

    # 睡眠时长评分（理想7-9小时）
    duration = record['sleep_duration_hours']
    if 7 <= duration <= 9:
        duration_score = 10
    elif 6 <= duration < 7 or 9 < duration <= 10:
        duration_score = 7
    else:
        duration_score = 4
    score += duration_score * 0.30

    # 睡眠效率评分（>90%优秀）
    efficiency = record['sleep_efficiency']
    efficiency_score = min(efficiency / 90 * 10, 10)
    score += efficiency_score * 0.25

    # 入睡潜伏期评分（<15分钟优秀）
    latency = record['sleep_latency_minutes']
    if latency <= 15:
        latency_score = 10
    elif latency <= 30:
        latency_score = 7
    elif latency <= 45:
        latency_score = 4
    else:
        latency_score = 1
    score += latency_score * 0.20

    # 夜间觉醒评分（0次优秀）
    awakenings = record['awakenings']['count']
    awakening_score = max(10 - awakenings * 2, 0)
    score += awakening_score * 0.15

    # 主观质量评分
    quality_map = {
        'excellent': 10,
        'very_good': 8,
        'good': 7,
        'fair': 5,
        'poor': 3,
        'very_poor': 1
    }
    subjective_score = quality_map.get(
        record['sleep_quality']['subjective_quality'],
        5
    )
    score += subjective_score * 0.10

    return round(score, 1)
```

### 作息规律性评分算法

```python
def calculate_sleep_consistency_score(records):
    """
    计算作息规律性评分（0-100分）

    因素：
    - 上床时间标准差
    - 起床时间标准差
    - 睡眠时长标准差
    - 工作日vs周末差异
    """
    # 提取时间数据
    bedtimes = [r['bedtime'] for r in records]
    wake_times = [r['wake_time'] for r in records]
    durations = [r['sleep_duration_hours'] for r in records]

    # 计算标准差（分钟）
    bedtime_std = time_to_minutes_std(bedtimes)
    wake_std = time_to_minutes_std(wake_times)
    duration_std = statistics.stdev(durations)

    # 计算工作日vs周末差异
    weekday_avg = avg([r['sleep_duration_hours']
                       for r in records if is_weekday(r)])
    weekend_avg = avg([r['sleep_duration_hours']
                       for r in records if is_weekend(r)])
    diff = abs(weekday_avg - weekend_avg)

    # 综合评分
    score = 100
    score -= bedtime_std * 0.5  # 上床时间标准差影响
    score -= wake_std * 0.5     # 起床时间标准差影响
    score -= duration_std * 2   # 睡眠时长标准差影响
    score -= diff * 10          # 工作日周末差异影响

    return max(0, min(100, round(score)))
```

### 相关性分析算法

```python
def calculate_correlation(sleep_data, other_data, lag_days=0):
    """
    计算睡眠与其他指标的相关性

    参数：
    - sleep_data: 睡眠数据列表
    - other_data: 其他指标数据列表
    - lag_days: 滞后天数（考虑延迟效应）

    返回：
    - correlation_coefficient: 相关系数
    - p_value: 统计显著性
    - interpretation: 相关性解释
    """
    # 对齐数据（考虑滞后）
    aligned = align_data_with_lag(sleep_data, other_data, lag_days)

    # 计算Pearson相关系数
    from scipy import stats
    corr, p_value = stats.pearsonr(
        aligned['sleep_values'],
        aligned['other_values']
    )

    # 解释相关性
    if abs(corr) < 0.3:
        strength = "弱"
    elif abs(corr) < 0.7:
        strength = "中等"
    else:
        strength = "强"

    direction = "正相关" if corr > 0 else "负相关"
    significant = p_value < 0.05

    interpretation = f"{strength}{direction}"
    if significant:
        interpretation += "（统计学显著）"

    return {
        'correlation_coefficient': round(corr, 3),
        'p_value': round(p_value, 4),
        'interpretation': interpretation,
        'significant': significant
    }
```

---

## 医学安全声明

本技能提供的分析和建议仅供参考，不构成医疗诊断或治疗方案。

**本技能能够做到的**：
- ✅ 分析睡眠数据和模式
- ✅ 识别睡眠问题风险
- ✅ 提供睡眠卫生建议
- ✅ 评估与其他健康指标的相关性

**本技能不能做的**：
- ❌ 诊断失眠、睡眠呼吸暂停等疾病
- ❌ 开具助眠药物或治疗
- ❌ 替代专业睡眠医学治疗
- ❌ 处理严重睡眠障碍

**何时需要就医**：
- 🏥 失眠持续>3个月
- 🏥 疑似睡眠呼吸暂停（STOP-BANG≥3）
- 🏥 严重嗜睡影响安全
- 🏥 突发严重睡眠问题

---

## 参考资源

- AASM 睡眠评分标准：https://aasm.org/
- PSQI 量表：https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3455216/
- STOP-BANG 问卷：https://www.stopbang.ca/
- CBT-I 治疗：https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3455216/

---

**技能版本**: v1.0
**创建日期**: 2026-01-02
**维护者**: WellAlly Tech

## Source: references/skills/healthcare-workflows/references/legacy/tcm-constitution-analyzer/SKILL.md

---
name: tcm-constitution-analyzer
description: 分析中医体质数据、识别体质类型、评估体质特征,并提供个性化养生建议。支持与营养、运动、睡眠等健康数据的关联分析。
allowed-tools: Read, Grep, Glob, Write
---

# 中医体质辨识分析器技能

分析中医体质数据,识别体质类型,评估体质特征,并提供个性化养生改善建议。

## 功能

### 1. 体质辨识评估

基于《中医体质分类与判定》标准进行体质辨识。

**评估维度**:
- 9种体质类型评分(平和质、气虚质、阳虚质、阴虚质、痰湿质、湿热质、血瘀质、气郁质、特禀质)
- 主体质判定
- 兼夹体质识别
- 体质特征分析

**评估方法**:
- 60题标准化问卷
- 5分制评分(没有/很少/有时/经常/总是)
- 转化分数计算(0-100分)

**输出**:
- 体质类型判定结果
- 各体质评分
- 体质特征描述
- 个体化养生建议

### 2. 体质特征分析

综合评估用户的体质特征。

**分析内容**:
- **形体特征**:
  - 体型特点
  - 面色表现
  - 舌象脉象

- **心理特征**:
  - 性格特点
  - 情绪倾向

- **发病倾向**:
  - 易感疾病
  - 健康风险

- **适应能力**:
  - 环境适应
  - 季节适应

**输出**:
- 体质类型分类
- 特征描述
- 风险评估
- 调理优先级

### 3. 体质变化趋势分析

追踪体质变化,评估调理效果。

**分析内容**:
- 多次评估对比
- 评分变化趋势
- 体质稳定性分析
- 调理效果评估

**输出**:
- 趋势图表
- 改善幅度
- 稳定性评估
- 继续调理建议

### 4. 相关性分析

分析体质与其他健康指标的相关性。

**支持的相关性分析**:
- **体质 ↔ 营养**:
  - 体质类型与饮食偏好的关系
  - 营养状况对体质的影响
  - 个性化饮食建议

- **体质 ↔ 运动**:
  - 不同体质适合的运动类型
  - 运动对体质改善的作用

- **体质 ↔ 睡眠**:
  - 体质与睡眠质量的关系
  - 睡眠对体质的影响

- **体质 ↔ 慢性病**:
  - 不同体质易患疾病
  - 体质与疾病的关系

**输出**:
- 相关系数
- 相关性强度
- 统计显著性
- 实践建议

### 5. 个性化建议生成

基于体质类型生成个性化养生建议。

**建议类型**:
- **饮食调养**:
  - 宜食食物清单
  - 忌食食物清单
  - 推荐食谱
  - 饮食原则

- **起居调摄**:
  - 作息建议
  - 环境要求
  - 生活习惯

- **运动锻炼**:
  - 推荐运动类型
  - 运动频次和强度
  - 注意事项

- **情志调摄**:
  - 情绪管理
  - 心理调节

- **穴位保健**:
  - 推荐穴位
  - 按摩方法
  - 艾灸建议

- **中药调理**:
  - 推荐方剂
  - 方剂组成
  - 用法用量
  - 注意事项

**建议依据**:
- 中医体质理论
- 用户体质类型
- 季节因素
- 用户健康状况

---

## 使用说明

### 触发条件

当用户请求以下内容时触发本技能:
- 中医体质辨识评估
- 体质类型查询
- 体质特征分析
- 中医养生建议
- 体质趋势分析
- 体质与其他健康指标的关联分析

### 执行步骤

#### 步骤 1: 确定分析范围

明确用户请求的分析类型:
- 体质辨识评估
- 体质特征查询
- 养生建议获取
- 趋势分析
- 相关性分析

#### 步骤 2: 读取数据

**主要数据源**:
1. `data/constitutions.json` - 体质知识库
2. `data/constitution-recommendations.json` - 养生建议库
3. `data-example/tcm-constitution-tracker.json` - 体质追踪主数据
4. `data-example/tcm-constitution-logs/YYYY-MM/YYYY-MM-DD.json` - 每日评估记录

**关联数据源**:
1. `data-example/profile.json` - 基础信息
2. `data-example/nutrition-tracker.json` - 营养数据
3. `data-example/fitness-tracker.json` - 运动数据
4. `data-example/sleep-tracker.json` - 睡眠数据

#### 步骤 3: 数据分析

根据分析类型执行相应的分析算法:

**体质评分算法**:
```python
def calculate_constitution_scores(answers):
    """
    基于《中医体质分类与判定》标准

    计算公式:
    转化分数 = [(原始分数 - 题目数) / (题目数 × 4)] × 100

    其中:
    - 原始分数 = 各题目得分之和
    - 题目数 = 该体质的问题数量
    """
    scores = {}
    for constitution, questions in CONSTITUTION_QUESTIONS.items():
        original_score = sum(answers[q] for q in questions)
        question_count = len(questions)
        converted_score = ((original_score - question_count) / (question_count * 4)) * 100
        scores[constitution] = round(converted_score, 1)
    return scores
```

**体质判定算法**:
```python
def determine_constitution_type(scores):
    """
    判定逻辑:
    1. 平和质判定:
       - 得分 ≥ 60分
       - 其他8种体质得分均 < 40分

    2. 偏颇体质判定:
       - 得分最高的体质为判定结果

    3. 兼夹体质判定:
       - 次高分的体质得分 ≥ 40分
       - 则为兼夹体质
    """
    peaceful_score = scores['平和质']
    other_scores = {k: v for k, v in scores.items() if k != '平和质'}

    # 判定是否为平和质
    if peaceful_score >= 60 and all(s < 40 for s in other_scores.values()):
        return {
            'primary': '平和质',
            'secondary': [],
            'type': 'balanced'
        }

    # 偏颇体质判定
    sorted_scores = sorted(other_scores.items(), key=lambda x: x[1], reverse=True)
    primary = sorted_scores[0][0]

    # 判断兼夹体质
    secondary = [k for k, v in sorted_scores[1:3] if v >= 40]

    return {
        'primary': primary,
        'secondary': secondary,
        'type': 'compound' if secondary else 'single'
    }
```

**趋势分析算法**:
- 线性回归计算趋势
- 移动平均平滑波动
- 统计显著性检验

#### 步骤 4: 生成报告

按照标准格式输出分析报告(见"输出格式"部分)

---

## 输出格式

### 体质辨识评估报告

```markdown
# 中医体质辨识评估报告

## 评估日期
2025-06-20

## 评估结果

### 体质类型判定
- **主体质**: 气虚质
- **兼夹体质**: 阳虚质
- **体质类型**: 兼夹体质

### 各体质评分

| 体质类型 | 评分 | 判定 |
|---------|------|------|
| 气虚质 | 78.5 | ⚠️ 偏颇 |
| 阳虚质 | 62.3 | ⚠️ 偏颇 |
| 平和质 | 42.1 | 正常 |
| 痰湿质 | 38.7 | 正常 |
| 气郁质 | 35.2 | 正常 |
| 阴虚质 | 32.1 | 正常 |
| 湿热质 | 28.4 | 正常 |
| 血瘀质 | 25.6 | 正常 |
| 特禀质 | 18.3 | 正常 |

---

## 体质特征分析

### 气虚质特征

**形体特征**:
- 肌肉松软
- 容易疲乏
- 声音低弱
- 喜静懒言
- 容易出汗

**心理特征**:
- 性格内向
- 不喜冒险
- 情绪不稳定

**发病倾向**:
- 易感冒
- 易内脏下垂
- 易疲劳

**适应能力**:
- 不耐受风、寒、暑、湿邪
- 秋季易发病

### 阳虚质特征

**形体特征**:
- 畏寒怕冷
- 手足不温
- 喜热饮食

**心理特征**:
- 性格多沉静
- 内向

**发病倾向**:
- 易患痰饮、肿胀、腹泻
- 易感寒邪

**适应能力**:
- 不耐寒邪,耐受夏热
- 冬季易发病

---

## 养生建议

### 饮食调养

**原则**: 补气健脾,温补肾阳

**宜食食物**:
- 补气类: 山药、大枣、黄芪、人参、白术
- 温阳类: 羊肉、韭菜、花椒、生姜、桂圆
- 健脾类: 薏苡仁、茯苓、扁豆

**忌食食物**:
- 生冷寒凉: 冰淇淋、冰镇饮料、生鱼片
- 油腻厚味: 油炸食品、肥肉
- 辛辣燥热: 辣椒、花椒

**推荐食谱**:
1. 黄芪炖鸡
2. 山药粥
3. 红枣茯苓粥
4. 当归生姜羊肉汤

**饮食建议**:
- 少食多餐,细嚼慢咽
- 饮食宜温热,忌生冷
- 饭后适当休息

### 起居调摄

**作息建议**:
- 保证充足睡眠(8小时以上)
- 早睡晚起
- 避免熬夜

**环境要求**:
- 保持环境温暖干燥
- 避免受风寒
- 注意保暖,特别是腰腹部和脚部

**生活习惯**:
- 避免过度劳累
- 劳逸结合
- 可适当晒太阳
- 温水泡脚

### 运动锻炼

**原则**: 温和运动,避免剧烈

**推荐运动**:
- 太极拳
- 八段锦
- 散步
- 气功
- 瑜伽

**运动建议**:
- 频率: 每日1-2次
- 时长: 每次20-30分钟
- 强度: 低至中等强度
- 注意: 以不感到过度疲劳为宜

**注意事项**:
- 避免剧烈运动
- 运动后及时休息
- 循序渐进
- 避免在寒冷环境中运动

### 情志调摄

**原则**: 保持心情舒畅,避免过度思虑

**调摄方法**:
- 保持积极乐观
- 避免过度思虑
- 适当参加社交活动
- 学会放松

**情绪管理**:
- 培养兴趣爱好
- 保持社交活动
- 学会调节情绪

### 穴位保健

**推荐穴位**:

#### 1. 足三里
- **位置**: 小腿外侧,膝眼下3寸
- **功效**: 健脾益气,强壮身体
- **方法**: 每日按揉3-5分钟,可艾灸

#### 2. 气海
- **位置**: 肚脐下1.5寸
- **功效**: 培补元气
- **方法**: 每日按揉3-5分钟,可艾灸

#### 3. 关元
- **位置**: 肚脐下3寸
- **功效**: 培元固本,温补肾阳
- **方法**: 每日按揉3-5分钟,可艾灸10-15分钟

### 中药调理

⚠️ **重要提醒**: 以下内容仅供中医师参考,不可自行抓药服用

**推荐方剂**: 四君子汤加减

**方源**: 《太平惠民和剂局方》

**方剂组成**:
- 人参: 9-15g, 大补元气
- 白术: 9-12g, 健脾益气
- 茯苓: 9-15g, 健脾渗湿
- 甘草: 6-9g, 调和诸药

**随症加减**:
- 气虚重者: 加黄芪 15-30g
- 脾虚湿盛者: 加薏苡仁 15-30g, 扁豆 10-15g
- 食少腹胀者: 加陈皮 6-9g, 砂仁 3-6g

**用法**: 水煎服,日一剂,分早晚两次温服

**注意事项**:
- ⚠️ 需经专业中医师辨证后使用
- ⚠️ 孕妇、儿童、体弱者需医师指导
- ⚠️ 服药期间忌食生冷、油腻、辛辣食物
- ⚠️ 感冒发烧时暂停服用
- ⚠️ 服用期间出现不良反应立即停用并就医

---

## 季节调养建议

### 春季调养
- 养阳为主,顺应生发之气
- 多食韭菜、菠菜、山药
- 保持心情舒畅,适当运动
- 注意防风保暖

### 夏季调养
- 清暑热,养心神
- 多食绿豆、冬瓜、苦瓜
- 注意防暑降温
- 保持心情平和

### 秋季调养
- 养收润燥,养肺
- 多食银耳、百合、梨
- 注意保暖,避免受凉
- 保持情绪稳定

### 冬季调养
- 养藏为主,温补肾阳
- 多食羊肉、核桃、栗子
- 注意保暖,特别是腰腹部
- 早睡晚起,避免过度劳累

---

## 与其他健康指标的关联

### 体质与营养
- 气虚质、阳虚质: 宜温补饮食
- 阴虚质、湿热质: 宜清淡饮食
- 痰湿质: 宜低脂低糖,控制体重

### 体质与运动
- 气虚质、阳虚质: 温和运动为主
- 湿热质、痰湿质: 适度加强运动强度
- 阴虚质: 避免剧烈运动

### 体质与睡眠
- 气虚质、阳虚质: 保证充足睡眠
- 阴虚质: 避免熬夜
- 气郁质: 疏肝解郁,改善睡眠质量

### 体质与慢性病
- 痰湿质: 易患高血压、糖尿病、高脂血症
- 湿热质: 易患代谢综合征
- 血瘀质: 易患心血管疾病
- 气郁质: 易患抑郁症、焦虑症

---

## 医学安全边界

⚠️ **重要声明**

本分析仅供健康参考,不构成医疗诊断或治疗建议。

### 分析能力范围

✅ **能做到**:
- 中医体质辨识评估
- 体质特征分析
- 一般性养生建议
- 中医知识普及
- 体质趋势追踪

❌ **不做到**:
- 中医疾病诊断
- 中药处方开具
- 替代中医师诊疗
- 针灸等治疗操作
- 处理严重健康问题

### 危险信号检测

在分析过程中检测以下危险信号:

1. **严重体质偏颇**:
   - 单一偏颇体质得分 > 80分
   - 多种偏颇体质兼夹

2. **健康风险提示**:
   - 痰湿质 → 高血压、糖尿病风险
   - 湿热质 → 代谢综合征风险
   - 血瘀质 → 心血管疾病风险
   - 气郁质 → 抑郁症风险

3. **就医引导**:
   - 疑似疾病症状 → 建议就医
   - 需要中药治疗 → 咨询中医师
   - 体质调理无效 → 寻求专业帮助

### 建议分级

**Level 1: 一般性建议**
- 基于中医体质理论
- 适用于一般人群
- 无需医疗监督

**Level 2: 参考性建议**
- 基于用户体质和健康状况
- 需结合个人情况
- 建议咨询中医师

**Level 3: 医疗建议**
- 涉及中药调理
- 需中医师确认
- 不得自行服用中药

---

## 数据结构

### 体质评估记录

```json
{
  "date": "2025-06-20",
  "questionnaire": {
    "questions": [
      {
        "id": 1,
        "constitution": "气虚质",
        "question": "您容易疲乏吗?",
        "answer": 4,
        "weight": 1.0
      }
    ],
    "total_questions": 60
  },
  "results": {
    "primary_constitution": "气虚质",
    "secondary_constitutions": ["阳虚质"],
    "constitution_scores": {
      "平和质": 42.1,
      "气虚质": 78.5,
      "阳虚质": 62.3,
      "阴虚质": 32.1,
      "痰湿质": 38.7,
      "湿热质": 28.4,
      "血瘀质": 25.6,
      "气郁质": 35.2,
      "特禀质": 18.3
    },
    "constitution_type": "compound"
  },
  "characteristics": {
    "physical": ["容易疲劳", "气短", "自汗"],
    "psychological": ["性格内向", "不喜欢说话"]
  },
  "recommendations": {
    "diet": {
      "principles": ["补气健脾", "温补肾阳"],
      "beneficial": ["山药", "大枣", "黄芪"],
      "avoid": ["生冷寒凉", "油腻厚味"]
    },
    "exercise": "温和运动,如太极拳、散步",
    "lifestyle": "规律作息,避免过度劳累",
    "acupoints": ["足三里", "气海", "关元"]
  }
}
```

---

## 参考资源

### 中医体质理论
- 《中医体质分类与判定》标准
- 王琦九种体质学说
- 《中医体质学》教材

### 养生原则
- 中医基础理论
- 四季养生原则
- 辨证施治原则

### 中药方剂
- 《方剂学》教材
- 《太平惠民和剂局方》
- 《金匮要略》

---

**技能版本**: v1.0
**创建日期**: 2026-01-08
**维护者**: WellAlly Tech

## Source: references/skills/healthcare-workflows/references/legacy/threejs-fundamentals/SKILL.md

---
name: threejs-fundamentals
description: Three.js scene setup, cameras, renderer, Object3D hierarchy, coordinate systems. Use when setting up 3D scenes, creating cameras, configuring renderers, managing object hierarchies, or working with transforms.
---

# Three.js Fundamentals

## Quick Start

```javascript
import * as THREE from "three";

// Create scene, camera, renderer
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(
  75,
  window.innerWidth / window.innerHeight,
  0.1,
  1000,
);
const renderer = new THREE.WebGLRenderer({ antialias: true });

renderer.setSize(window.innerWidth, window.innerHeight);
renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
document.body.appendChild(renderer.domElement);

// Add a mesh
const geometry = new THREE.BoxGeometry(1, 1, 1);
const material = new THREE.MeshStandardMaterial({ color: 0x00ff00 });
const cube = new THREE.Mesh(geometry, material);
scene.add(cube);

// Add light
scene.add(new THREE.AmbientLight(0xffffff, 0.5));
const dirLight = new THREE.DirectionalLight(0xffffff, 1);
dirLight.position.set(5, 5, 5);
scene.add(dirLight);

camera.position.z = 5;

// Animation loop
function animate() {
  requestAnimationFrame(animate);
  cube.rotation.x += 0.01;
  cube.rotation.y += 0.01;
  renderer.render(scene, camera);
}
animate();

// Handle resize
window.addEventListener("resize", () => {
  camera.aspect = window.innerWidth / window.innerHeight;
  camera.updateProjectionMatrix();
  renderer.setSize(window.innerWidth, window.innerHeight);
});
```

## Core Classes

### Scene

Container for all 3D objects, lights, and cameras.

```javascript
const scene = new THREE.Scene();
scene.background = new THREE.Color(0x000000); // Solid color
scene.background = texture; // Skybox texture
scene.background = cubeTexture; // Cubemap
scene.environment = envMap; // Environment map for PBR
scene.fog = new THREE.Fog(0xffffff, 1, 100); // Linear fog
scene.fog = new THREE.FogExp2(0xffffff, 0.02); // Exponential fog
```

### Cameras

**PerspectiveCamera** - Most common, simulates human eye.

```javascript
// PerspectiveCamera(fov, aspect, near, far)
const camera = new THREE.PerspectiveCamera(
  75, // Field of view (degrees)
  window.innerWidth / window.innerHeight, // Aspect ratio
  0.1, // Near clipping plane
  1000, // Far clipping plane
);

camera.position.set(0, 5, 10);
camera.lookAt(0, 0, 0);
camera.updateProjectionMatrix(); // Call after changing fov, aspect, near, far
```

**OrthographicCamera** - No perspective distortion, good for 2D/isometric.

```javascript
// OrthographicCamera(left, right, top, bottom, near, far)
const aspect = window.innerWidth / window.innerHeight;
const frustumSize = 10;
const camera = new THREE.OrthographicCamera(
  (frustumSize * aspect) / -2,
  (frustumSize * aspect) / 2,
  frustumSize / 2,
  frustumSize / -2,
  0.1,
  1000,
);
```

**ArrayCamera** - Multiple viewports with sub-cameras.

```javascript
const cameras = [];
for (let i = 0; i < 4; i++) {
  const subcamera = new THREE.PerspectiveCamera(40, 1, 0.1, 100);
  subcamera.viewport = new THREE.Vector4(
    Math.floor(i % 2) * 0.5,
    Math.floor(i / 2) * 0.5,
    0.5,
    0.5,
  );
  cameras.push(subcamera);
}
const arrayCamera = new THREE.ArrayCamera(cameras);
```

**CubeCamera** - Renders environment maps for reflections.

```javascript
const cubeRenderTarget = new THREE.WebGLCubeRenderTarget(256);
const cubeCamera = new THREE.CubeCamera(0.1, 1000, cubeRenderTarget);
scene.add(cubeCamera);

// Use for reflections
material.envMap = cubeRenderTarget.texture;

// Update each frame (expensive!)
cubeCamera.position.copy(reflectiveMesh.position);
cubeCamera.update(renderer, scene);
```

### WebGLRenderer

```javascript
const renderer = new THREE.WebGLRenderer({
  canvas: document.querySelector("#canvas"), // Optional existing canvas
  antialias: true, // Smooth edges
  alpha: true, // Transparent background
  powerPreference: "high-performance", // GPU hint
  preserveDrawingBuffer: true, // For screenshots
});

renderer.setSize(width, height);
renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));

// Tone mapping
renderer.toneMapping = THREE.ACESFilmicToneMapping;
renderer.toneMappingExposure = 1.0;

// Color space (Three.js r152+)
renderer.outputColorSpace = THREE.SRGBColorSpace;

// Shadows
renderer.shadowMap.enabled = true;
renderer.shadowMap.type = THREE.PCFSoftShadowMap;

// Clear color
renderer.setClearColor(0x000000, 1);

// Render
renderer.render(scene, camera);
```

### Object3D

Base class for all 3D objects. Mesh, Group, Light, Camera all extend Object3D.

```javascript
const obj = new THREE.Object3D();

// Transform
obj.position.set(x, y, z);
obj.rotation.set(x, y, z); // Euler angles (radians)
obj.quaternion.set(x, y, z, w); // Quaternion rotation
obj.scale.set(x, y, z);

// Local vs World transforms
obj.getWorldPosition(targetVector);
obj.getWorldQuaternion(targetQuaternion);
obj.getWorldDirection(targetVector);

// Hierarchy
obj.add(child);
obj.remove(child);
obj.parent;
obj.children;

// Visibility
obj.visible = false;

// Layers (for selective rendering/raycasting)
obj.layers.set(1);
obj.layers.enable(2);
obj.layers.disable(0);

// Traverse hierarchy
obj.traverse((child) => {
  if (child.isMesh) child.material.color.set(0xff0000);
});

// Matrix updates
obj.matrixAutoUpdate = true; // Default: auto-update matrices
obj.updateMatrix(); // Manual matrix update
obj.updateMatrixWorld(true); // Update world matrix recursively
```

### Group

Empty container for organizing objects.

```javascript
const group = new THREE.Group();
group.add(mesh1);
group.add(mesh2);
scene.add(group);

// Transform entire group
group.position.x = 5;
group.rotation.y = Math.PI / 4;
```

### Mesh

Combines geometry and material.

```javascript
const mesh = new THREE.Mesh(geometry, material);

// Multiple materials (one per geometry group)
const mesh = new THREE.Mesh(geometry, [material1, material2]);

// Useful properties
mesh.geometry;
mesh.material;
mesh.castShadow = true;
mesh.receiveShadow = true;

// Frustum culling
mesh.frustumCulled = true; // Default: skip if outside camera view

// Render order
mesh.renderOrder = 10; // Higher = rendered later
```

## Coordinate System

Three.js uses a **right-handed coordinate system**:

- **+X** points right
- **+Y** points up
- **+Z** points toward viewer (out of screen)

```javascript
// Axes helper
const axesHelper = new THREE.AxesHelper(5);
scene.add(axesHelper); // Red=X, Green=Y, Blue=Z
```

## Math Utilities

### Vector3

```javascript
const v = new THREE.Vector3(x, y, z);
v.set(x, y, z);
v.copy(otherVector);
v.clone();

// Operations (modify in place)
v.add(v2);
v.sub(v2);
v.multiply(v2);
v.multiplyScalar(2);
v.divideScalar(2);
v.normalize();
v.negate();
v.clamp(min, max);
v.lerp(target, alpha);

// Calculations (return new value)
v.length();
v.lengthSq(); // Faster than length()
v.distanceTo(v2);
v.dot(v2);
v.cross(v2); // Modifies v
v.angleTo(v2);

// Transform
v.applyMatrix4(matrix);
v.applyQuaternion(q);
v.project(camera); // World to NDC
v.unproject(camera); // NDC to world
```

### Matrix4

```javascript
const m = new THREE.Matrix4();
m.identity();
m.copy(other);
m.clone();

// Build transforms
m.makeTranslation(x, y, z);
m.makeRotationX(theta);
m.makeRotationY(theta);
m.makeRotationZ(theta);
m.makeRotationFromQuaternion(q);
m.makeScale(x, y, z);

// Compose/decompose
m.compose(position, quaternion, scale);
m.decompose(position, quaternion, scale);

// Operations
m.multiply(m2); // m = m * m2
m.premultiply(m2); // m = m2 * m
m.invert();
m.transpose();

// Camera matrices
m.makePerspective(left, right, top, bottom, near, far);
m.makeOrthographic(left, right, top, bottom, near, far);
m.lookAt(eye, target, up);
```

### Quaternion

```javascript
const q = new THREE.Quaternion();
q.setFromEuler(euler);
q.setFromAxisAngle(axis, angle);
q.setFromRotationMatrix(matrix);

q.multiply(q2);
q.slerp(target, t); // Spherical interpolation
q.normalize();
q.invert();
```

### Euler

```javascript
const euler = new THREE.Euler(x, y, z, "XYZ"); // Order matters!
euler.setFromQuaternion(q);
euler.setFromRotationMatrix(m);

// Rotation orders: 'XYZ', 'YXZ', 'ZXY', 'XZY', 'YZX', 'ZYX'
```

### Color

```javascript
const color = new THREE.Color(0xff0000);
const color = new THREE.Color("red");
const color = new THREE.Color("rgb(255, 0, 0)");
const color = new THREE.Color("#ff0000");

color.setHex(0x00ff00);
color.setRGB(r, g, b); // 0-1 range
color.setHSL(h, s, l); // 0-1 range

color.lerp(otherColor, alpha);
color.multiply(otherColor);
color.multiplyScalar(2);
```

### MathUtils

```javascript
THREE.MathUtils.clamp(value, min, max);
THREE.MathUtils.lerp(start, end, alpha);
THREE.MathUtils.mapLinear(value, inMin, inMax, outMin, outMax);
THREE.MathUtils.degToRad(degrees);
THREE.MathUtils.radToDeg(radians);
THREE.MathUtils.randFloat(min, max);
THREE.MathUtils.randInt(min, max);
THREE.MathUtils.smoothstep(x, min, max);
THREE.MathUtils.smootherstep(x, min, max);
```

## Common Patterns

### Proper Cleanup

```javascript
function dispose() {
  // Dispose geometries
  mesh.geometry.dispose();

  // Dispose materials
  if (Array.isArray(mesh.material)) {
    mesh.material.forEach((m) => m.dispose());
  } else {
    mesh.material.dispose();
  }

  // Dispose textures
  texture.dispose();

  // Remove from scene
  scene.remove(mesh);

  // Dispose renderer
  renderer.dispose();
}
```

### Clock for Animation

```javascript
const clock = new THREE.Clock();

function animate() {
  const delta = clock.getDelta(); // Time since last frame (seconds)
  const elapsed = clock.getElapsedTime(); // Total time (seconds)

  mesh.rotation.y += delta * 0.5; // Consistent speed regardless of framerate

  requestAnimationFrame(animate);
  renderer.render(scene, camera);
}
```

### Responsive Canvas

```javascript
function onWindowResize() {
  const width = window.innerWidth;
  const height = window.innerHeight;

  camera.aspect = width / height;
  camera.updateProjectionMatrix();

  renderer.setSize(width, height);
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
}
window.addEventListener("resize", onWindowResize);
```

### Loading Manager

```javascript
const manager = new THREE.LoadingManager();

manager.onStart = (url, loaded, total) => console.log("Started loading");
manager.onLoad = () => console.log("All loaded");
manager.onProgress = (url, loaded, total) => console.log(`${loaded}/${total}`);
manager.onError = (url) => console.error(`Error loading ${url}`);

const textureLoader = new THREE.TextureLoader(manager);
const gltfLoader = new GLTFLoader(manager);
```

## Performance Tips

1. **Limit draw calls**: Merge geometries, use instancing, atlas textures
2. **Frustum culling**: Enabled by default, ensure bounding boxes are correct
3. **LOD (Level of Detail)**: Use `THREE.LOD` for distance-based mesh switching
4. **Object pooling**: Reuse objects instead of creating/destroying
5. **Avoid `getWorldPosition` in loops**: Cache results

```javascript
// Merge static geometries
import { mergeGeometries } from "three/examples/jsm/utils/BufferGeometryUtils.js";
const merged = mergeGeometries([geo1, geo2, geo3]);

// LOD
const lod = new THREE.LOD();
lod.addLevel(highDetailMesh, 0);
lod.addLevel(medDetailMesh, 50);
lod.addLevel(lowDetailMesh, 100);
scene.add(lod);
```

## See Also

- `threejs-geometry` - Geometry creation and manipulation
- `threejs-materials` - Material types and properties
- `threejs-lighting` - Light types and shadows

## Source: references/skills/healthcare-workflows/references/legacy/travel-health-analyzer/SKILL.md

---
name: travel-health-analyzer
description: 分析旅行健康数据、评估目的地健康风险、提供疫苗接种建议、生成多语言紧急医疗信息卡片。支持WHO/CDC数据集成的专业级旅行健康风险评估。
allowed-tools: Read, Write, Grep, Glob
---

# 旅行健康分析技能

## 🚨 重要医学免责声明

**本技能提供的所有健康建议和信息仅供参考,不能替代专业医疗建议。**

- ⚠️ **所有建议必须由专业医生审核**
- ⚠️ **疫苗接种和用药方案必须由医生制定**
- ⚠️ **不提供具体的医疗处方或诊断**
- ⚠️ **健康风险数据来源于WHO/CDC,可能存在滞后性**
- ⚠️ **紧急情况下请立即就医**

---

## 技能功能

### 1. 旅行健康规划分析

分析用户的旅行计划,提供全面的健康准备建议。

**输入**: 旅行目的地、日期、旅行目的
**输出**:
- 目的地健康风险评估
- 必要和推荐的疫苗接种清单
- 旅行药箱建议清单
- 预防措施建议
- 旅行前准备时间表

**分析要点**:
- 识别目的地传染病风险
- 评估食物和饮水安全
- 确认环境风险(高温、高原等)
- 检查当前疫情爆发信息
- 提供WHO/CDC参考链接

---

### 2. 目的地健康风险评估

基于WHO/CDC数据,对旅行目的地进行专业级健康风险评估。

**数据源**:
- 世界卫生组织(WHO)国际旅行健康
- 美国疾控中心(CDC)旅行健康
- 当地卫生部门官方数据

**评估维度**:
- 传染病风险(登革热、疟疾、霍乱、甲肝等)
- 食物和饮水安全
- 环境风险(高温、高原、空气污染)
- 季节性风险
- 当前疫情爆发警报

**风险等级**:
- 🟢 **低风险** - 常规预防措施
- 🟡 **中等风险** - 需要特别注意
- 🔴 **高风险** - 需要采取严格预防措施
- ⚫ **极高风险** - 建议推迟旅行或采取特殊防护

**输出格式**:
```markdown
## 目的地健康风险评估: Thailand

### 传染病风险
#### 🔴 登革热 - 高风险
- **传播方式**: 蚊子叮咬
- **季节性**: 全年
- **症状**: 高热、头痛、肌肉关节痛、皮疹
- **预防**: 使用防蚊液、穿长袖衣物、住宿选择有空调房间
- **数据源**: [WHO](https://www.who.int/ith) | [CDC](https://www.cdc.gov/dengue)

### 食物饮水安全
#### 🟡 中等风险
- 饮用瓶装水或煮沸的水
- 避免冰块
- 避免生食
- 水果自己剥皮

### 当前疫情警报
暂无重大疫情爆发警报
```

---

### 3. 疫苗接种需求分析

根据目的地和旅行计划,分析疫苗接种需求。

**分析内容**:
- 必需疫苗接种(如黄热病)
- 推荐疫苗接种(如甲肝、伤寒)
- 疫苗接种时间规划
- 疫苗相互作用检查
- 接种禁忌症评估

**疫苗清单模板**:
```json
{
  "vaccine": "甲肝疫苗",
  "status": "completed|planned|not_required|contraindicated",
  "date": "2025-06-15",
  "booster_required": false,
  "notes": "已完成接种,提供长期保护"
}
```

**时间规划原则**:
- 出发前4-6周:完成必需疫苗接种
- 出发前2-4周:完成推荐疫苗接种
- 某些疫苗需要多次接种,需提前规划

---

### 4. 旅行药箱智能建议

根据目的地健康风险和个人健康状况,生成个性化旅行药箱清单。

**药箱分类**:

#### 处方药
- 个人慢性病用药(足量+额外)
- 疟疾预防用药(如需要)
- 其他医生开具的旅行用药

#### 非处方药
- 止泻药(洛哌丁胺)
- 口服补液盐
- 退烧止痛药(对乙酰氨基酚/布洛芬)
- 抗过敏药(氯雷他定)
- 晕车药
- 抗酸药

#### 防护用品
- 防蚊液(DEET 20-30%)
- 防晒霜(SPF 50+)
- 口罩(N95)

#### 急救用品
- 创可贴
- 消毒液
- 纱布和绷带
- 体温计
- 小剪刀和镊子

**个性化建议**:
- 根据个人疾病史调整用药
- 根据目的地风险增减物品
- 考虑旅行时长和活动类型

---

### 5. 用药相互作用检查

检查旅行用药与个人慢性病用药之间的潜在相互作用。

**检查内容**:
- 疟疾预防用药 vs 慢性病用药
- 旅行期间临时用药 vs 常规用药
- 疫苗 vs 药物相互作用
- 食物 vs 药物相互作用

**常见相互作用**:
- 多西环素 vs 抗酸药、钙铁补充剂
- 甲氟喹 vs 某些心脏病药物
- 某些抗生素 vs 口服避孕药

**输出**:
```markdown
## 用药相互作用检查结果

### ⚠️ 发现潜在相互作用

**多西环素 ↔ 抗酸药**
- **影响**: 抗酸药降低多西环素吸收
- **建议**: 间隔2小时服用
- **严重程度**: 中等

### ✅ 无相互作用
- 氨氯地平 vs 旅行用药无已知相互作用
```

---

### 6. 多语言紧急信息卡片生成

生成包含关键医疗信息的多语言紧急卡片。

**支持语言**:
- 英语 (en)
- 中文 (zh)
- 日语 (ja)
- 韩语 (ko)
- 法语 (fr)
- 西班牙语 (es)
- 泰语 (th)
- 越南语 (vi)

**卡片内容**:
```markdown
---
紧急医疗信息 | EMERGENCY MEDICAL INFORMATION
---

姓名: 张三 | Name: Zhang San
血型: A+ | Blood Type: A+
出生日期: 1990-01-01 | DOB: 1990-01-01

⚠️ 过敏史 | ALLERGIES
- 青霉素 (严重: 皮疹、呼吸困难) | Penicillin (Severe: Rash, Difficulty breathing)

当前用药 | CURRENT MEDICATIONS
- 氨氯地平 5mg 每日一次 (控制血压) | Amlodipine 5mg Once daily (Blood pressure)

疾病史 | MEDICAL CONDITIONS
- 高血压 (控制中) | Hypertension (Controlled)

紧急联系人 | EMERGENCY CONTACT
- 配偶: 李四 +86-138-1234-5678 | Spouse: Li Si +86-138-1234-5678
- 医生: 王医生 +86-10-8765-4321 | Doctor: Dr. Wang +86-10-8765-4321

---
[二维码: 扫描查看完整医疗记录]
[QR Code: Scan for complete medical records]
---
```

**二维码功能**:
- 编码关键医疗信息摘要
- 云端访问链接(模拟)
- 支持离线访问
- 可分享给医护人员

---

### 7. 旅行前后健康检查

#### 旅行前健康检查

**检查内容**:
- 个人健康状况评估
- 慢性病病情确认
- 用药充足性检查
- 疫苗接种确认
- 健康建议

**输出**:
```markdown
## 旅行前健康检查报告

### 整体评估: ✅ 适合旅行

### 健康状况
- 血压: 控制良好
- 慢性病: 稳定
- 用药: 充足

### 准备完成度
- ✅ 疫苗接种: 已完成
- ✅ 旅行药箱: 已准备
- ✅ 保险: 已购买
- ⚠️ 紧急卡片: 待生成

### 建议
1. 生成多语言紧急卡片
2. 携带足量慢性病用药
3. 旅行期间注意血压监测
```

#### 旅行后健康监测

**监测内容**:
- 发热监测(持续2-4周)
- 消化系统症状
- 皮肤异常
- 其他不适症状

**潜伏期疾病提醒**:
- 疟疾: 可在返回后数月内发病
- 登革热: 通常3-14天
- 伤寒: 1-3周
- 甲肝: 2-6周

---

## 数据文件操作

### 读取数据
```bash
# 读取旅行健康数据
Read: data/travel-health-tracker.json

# 读取示例数据
Read: data-example/travel-health-tracker.json
```

### 写入数据
```bash
# 更新旅行计划
Write: data/travel-health-tracker.json

# 保存健康检查日志
Write: data/travel-health-logs/pre-trip-assessment-YYYY-MM-DD.json
```

### 数据结构验证
- 验证必需字段存在
- 验证日期格式正确
- 验证枚举值有效
- 验证数据完整性

---

## WHO/CDC数据集成

### 静态数据库(当前实现)

内置常见旅行目的地健康风险数据:
- 东南亚: 登革热、甲肝、伤寒、疟疾
- 非洲: 疟疾、黄热病、霍乱、脑膜炎
- 南美: 登革热、黄热病、寨卡病毒
- 中东: 中东呼吸综合征(MERS)

**数据更新**: 手动更新,建议每季度更新一次

### 动态查询(未来扩展)

计划集成:
- WHO疫情新闻RSS订阅
- CDC Travel Health API
- 当地卫生部门疫情通报

---

## 输出格式

### 报告格式
- Markdown格式,便于阅读
- 结构化,便于程序处理
- 包含数据源引用
- 包含时间戳

### 日志格式
```json
{
  "log_id": "log_20250728_pretrip",
  "log_type": "pre_trip_assessment",
  "trip_id": "trip_20250801_seasia",
  "generated_at": "2025-07-28T10:00:00.000Z",
  "assessment_results": {
    "health_status": "suitable_for_travel",
    "vaccination_status": "completed",
    "risk_assessment": {...},
    "recommendations": [...]
  }
}
```

---

## 安全和隐私

### 数据保护
- 护照号码加密存储
- 二维码不包含完整敏感信息
- 支持数据导出和删除

### 医学安全
- 所有建议包含免责声明
- 强调医生咨询的必要性
- 不提供具体处方
- 引用权威数据源

---

## 使用示例

### 分析旅行计划
```
输入: "计划2025年8月去东南亚旅游14天"

输出:
1. 目的地健康风险评估
2. 疫苗接种建议
3. 旅行药箱清单
4. 预防措施
5. 时间表
```

### 生成紧急卡片
```
输入: "生成英中日泰四语紧急卡片"

输出:
1. 多语言卡片文本
2. 二维码(描述)
3. 保存建议
```

### 评估健康风险
```
输入: "评估泰国的健康风险"

输出:
1. 传染病风险清单
2. 食物饮水安全建议
3. 环境风险
4. 当前疫情警报
5. WHO/CDC参考链接
```

---

**版本**: v1.0.0
**最后更新**: 2025-01-08
**维护者**: WellAlly Tech

## Source: references/skills/healthcare-workflows/references/legacy/weightloss-analyzer/SKILL.md

---
name: weightloss-analyzer
description: 分析减肥数据、计算代谢率、追踪能量缺口、管理减肥阶段
---

# 减肥分析技能

分析减肥数据，计算代谢率，追踪能量缺口，管理减肥阶段。

## 功能

### 1. 身体成分分析

**BMI计算与分类**
- BMI = 体重(kg) / 身高(m)²
- 分类标准（WHO亚洲标准）：
  - 偏瘦：BMI < 18.5
  - 正常：18.5 ≤ BMI < 24
  - 超重：24 ≤ BMI < 28
  - 肥胖：BMI ≥ 28

**体脂率评估**
- 男性：15-20%（正常），20-25%（偏高），>25%（肥胖）
- 女性：20-25%（正常），25-30%（偏高），>30%（肥胖）

**围度分析**
- 腰围评估
  - 男性：< 90cm（正常），≥ 90cm（腹部肥胖）
  - 女性：< 85cm（正常），≥ 85cm（腹部肥胖）
- 腰臀比
  - 男性：< 0.9（正常），≥ 0.9（腹部肥胖）
  - 女性：< 0.85（正常），≥ 0.85（腹部肥胖）

**理想体重计算**
- BMI法：理想体重 = 身高(m)² × 22
- Broca法修正：理想体重 = (身高cm - 100) × 0.9

### 2. 代谢率计算

**Harris-Benedict公式（1919原始版）**
- 男性：BMR = 88.362 + (13.397 × 体重kg) + (4.799 × 身高cm) - (5.677 × 年龄)
- 女性：BMR = 447.593 + (9.247 × 体重kg) + (3.098 × 身高cm) - (4.330 × 年龄)

**Mifflin-St Jeor公式（推荐，更准确）**
- 男性：BMR = (10 × 体重kg) + (6.25 × 身高cm) - (5 × 年龄) + 5
- 女性：BMR = (10 × 体重kg) + (6.25 × 身高cm) - (5 × 年龄) - 161

**Katch-McArdle公式（基于瘦体重）**
- BMR = 370 + (21.6 × 瘦体重kg)
- 瘦体重 = 体重kg × (1 - 体脂率)

**TDEE计算**
- TDEE = BMR × 活动系数
- 活动系数：
  - 久坐：1.2
  - 轻度活动：1.375
  - 中度活动：1.55
  - 高度活动：1.725
  - 非常高度活动：1.9

### 3. 能量缺口管理

**每日能量缺口追踪**
- 缺口 = TDEE - 实际摄入 + 运动消耗
- 缺口达标分析：实际缺口 vs 目标缺口

**减重估算**
- 1kg脂肪 ≈ 7700大卡
- 预计周减重 = 每日缺口 × 7 / 7700
- 安全减重速度：0.5-1kg/周（缺口500-1000大卡/天）

**热量安全边界**
- 男性最低热量：1500大卡/天
- 女性最低热量：1200大卡/天
- 绝对最低：BMR × 1.2

### 4. 阶段管理

**减重期**
- 追踪体重变化
- 计算减重进度
- 监测减重速度

**平台期检测**
- 定义：2周以上体重无明显变化（波动<0.5kg）
- 原因分析：代谢适应、水分滞留、肌肉增加
- 突破方法：调整热量、改变运动、间歇性断食

**维持期**
- 目标体重±2kg范围内
- 定期监测体重
- 及时调整方案

## 数据源

### 主要数据源

1. **健身追踪器**
   - 路径：`data/fitness-tracker.json`
   - 内容：体重记录、身体成分、代谢率、阶段管理

2. **营养追踪器**
   - 路径：`data/nutrition-tracker.json`
   - 内容：热量摄入、能量缺口、膳食计划

3. **健康日志**
   - 路径：`data/health-logs/YYYY-MM/YYYY-MM-DD.json`
   - 内容：每日体重、饮食记录

## 输出格式

### 身体成分分析报告

```markdown
# 身体成分分析报告

## 基本信息
- 性别：男
- 年龄：52岁
- 身高：175cm
- 体重：75kg

## 身体指标

### BMI
- 当前BMI：24.5
- 分类：超重
- 理想体重：67kg（BMI=22）
- 需减重：8kg

### 体脂率
- 当前体脂率：25%
- 分类：偏高
- 目标体脂率：15-20%

### 围度分析
- 腰围：92cm（腹部肥胖风险）
- 臀围：98cm
- 腰臀比：0.94（腹部肥胖）

## 建议
1. 每周减重0.5-1kg
2. 目标减重时间：8-16周
3. 综合干预：饮食+运动
```

### 代谢率分析报告

```markdown
# 代谢率分析报告

## BMR计算

| 公式 | BMR | 说明 |
|------|-----|------|
| Harris-Benedict | 1650 | 1919原始公式 |
| Mifflin-St Jeor | 1620 | 推荐使用 ⭐ |
| Katch-McArdle | 1700 | 基于体脂率 |

**推荐BMR：1620 大卡/天**

## TDEE计算

- 活动水平：中度运动
- 活动系数：1.55
- TDEE：1620 × 1.55 = **2511 大卡/天**

### 热量分配
- BMR基础代谢：65% ≈ 1632 大卡
- 运动消耗：20% ≈ 502 大卡
- NEAT日常活动：15% ≈ 377 大卡

## 减肥热量目标

### 温和减重方案
- 每日缺口：500 大卡
- 目标摄入：2011 大卡/天
- 预计减重：0.5kg/周

### 积极减重方案
- 每日缺口：750 大卡
- 目标摄入：1761 大卡/天
- 预计减重：0.75kg/周

### 快速减重方案
- 每日缺口：1000 大卡
- 目标摄入：1511 大卡/天
- 预计减重：1kg/周
- ⚠️ 仅限短期使用

## 安全检查
- 最低热量要求：1500 大卡/天（男性）
- 快速方案热量：1511 大卡/天 ✅
- 建议选择：温和或积极方案
```

### 能量缺口追踪报告

```markdown
# 能量缺口追踪报告

## 本周汇总（2025-06-16 至 2025-06-22）

| 日期 | 摄入 | 运动消耗 | NEAT | 缺口 | 达标 |
|------|------|---------|------|------|------|
| 周一 | 1800 | 350 | 300 | 961 | ✅ |
| 周二 | 2100 | 200 | 250 | 461 | ❌ |
| 周三 | 1750 | 400 | 300 | 1061 | ✅ |
| 周四 | 1950 | 300 | 280 | 741 | ✅ |
| 周五 | 2200 | 150 | 200 | 261 | ❌ |
| 周六 | 2400 | 100 | 150 | -89 | ❌ |
| 周日 | 1850 | 350 | 300 | 911 | ✅ |

**目标缺口：500 大卡/天**

## 统计分析
- 平均缺口：642 大卡/天
- 达标天数：5/7天（71%）
- 总缺口：4494 大卡
- 预计减重：0.58kg

## 趋势分析
- 周末缺口偏小（社交活动增加）
- 建议提前规划周末饮食

## 下周目标
- 达标天数：7/7天
- 平均缺口：700 大卡/天
- 预计减重：0.64kg
```

### 阶段管理报告

```markdown
# 减肥阶段管理报告

## 当前阶段：减重期

### 进度追踪
- 开始日期：2025-01-01
- 初始体重：82kg
- 当前体重：75kg
- 目标体重：67kg
- 已减重：7kg
- 剩余：8kg
- 进度：47%

### 减重速度
- 总周数：24周
- 平均减重：0.29kg/周
- 最近4周：0.35kg/周 ⬆️ 加速中

## 状态分析

### 当前状态：✅ 良好
- 减重速度在健康范围（0.5-1kg/周）
- 代谢率稳定
- 肌肉量维持良好

### 平台期监测
- 最近2周变化：-0.8kg
- 状态：❌ 非平台期

## 下一步行动
1. 继续当前热量方案
2. 增加力量训练频率
3. 每周监测身体成分
```

## 使用方法

通过 `/fitness:weightloss-*` 和 `/nutrition:weightloss-*` 命令调用。

### 示例命令

```bash
# 设置减肥计划
/fitness:weightloss-setup --weight 75 --height 175 --age 52 --gender male

# 计算代谢率
/fitness:weightloss-bmr --formula mifflin

# 追踪能量缺口
/nutrition:weightloss-track --intake 1800 --exercise 350

# 生成阶段报告
/fitness:weightloss-report

# 检测平台期
/fitness:weightloss-plateau-check
```

## 安全原则

### 热量安全边界
- 不推荐 < 1200大卡/天（女性）
- 不推荐 < 1500大卡/天（男性）
- 绝对最低不低于 BMR × 1.2

### 减重速度控制
- 安全范围：0.5-1kg/周
- 最大不超过：1.5kg/周
- 长期平均：0.5-0.8kg/周

### 医学免责声明

本技能仅供健康参考，不构成医疗建议。

以下情况请咨询医生：
- BMI > 35
- 有心脏病、高血压、糖尿病等慢性病
- 服用处方药物
- 女性怀孕或哺乳期
- 任何健康状况不确定的情况

---

**技能版本**: v1.0
**最后更新**: 2026-01-14
**维护者**: WellAlly Tech

