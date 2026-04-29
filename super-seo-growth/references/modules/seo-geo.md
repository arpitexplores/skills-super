## Module: Seo Geo
---
name: seo-geo
description: AI search optimization (GEO/AI SEO) and LLM visibility strategy.
user-invokable: true
argument-hint: [url]
license: MIT
allowed-tools: Read, Grep, Glob, Bash, WebFetch
metadata: 
author: AgriciDaniel
version: 1.7.0
category: seo
---
# AI Search / GEO Optimization (February 2026)

## Key Statistics

| Metric | Value | Source |
|--------|-------|--------|
| AI Overviews reach | 1.5 billion users/month across 200+ countries | Google |
| AI Overviews query coverage | 50%+ of all queries | Industry data |
| AI-referred sessions growth | 527% (Jan-May 2025) | SparkToro |
| ChatGPT weekly active users | 900 million | OpenAI |
| Perplexity monthly queries | 500+ million | Perplexity |

## Critical Insight: Brand Mentions > Backlinks

**Brand mentions correlate 3x more strongly with AI visibility than backlinks.**
(Ahrefs December 2025 study of 75,000 brands)

| Signal | Correlation with AI Citations |
|--------|------------------------------|
| YouTube mentions | ~0.737 (strongest) |
| Reddit mentions | High |
| Wikipedia presence | High |
| LinkedIn presence | Moderate |
| Domain Rating (backlinks) | ~0.266 (weak) |

**Only 11% of domains** are cited by both ChatGPT and Google AI Overviews for the same query, so platform-specific optimization is essential.

---

## Source-Informed Reality Checks (2026)

Use these checks before recommending AI SEO work. They prevent common GEO overreach and keep advice aligned with how major AI search surfaces currently describe themselves.

### 1. Google AI Features Are Still Google Search

For Google AI Overviews and AI Mode:
- There is no separate AI-only markup requirement for inclusion.
- A page must be indexed and eligible to show a snippet in Google Search.
- The same foundations still matter: crawlability, internal links, helpful content, page experience, text availability, high-quality images/video where useful, and structured data that matches visible page content.
- Google says new AI text files or special schema are not required for AI Overviews or AI Mode.

**Practical implication:** For Google, prioritise Search eligibility, snippet eligibility, helpful content, and extractable passages before adding optional AI-specific files.

### 2. Query Fan-Out Changes Content Planning

Google describes AI Mode and AI Overviews as potentially using query fan-out: issuing multiple related searches across subtopics and data sources before constructing an answer.

**Practical implication:** A strong AI-search page should not only answer the head query. It should cover adjacent sub-questions, comparisons, constraints, definitions, examples, risks, and next-step decisions that a user would naturally ask in follow-up queries.

### 3. Snippet Controls Can Affect AI Search Visibility

For Google AI features, content controls are still Search controls:
- `nosnippet` can prevent snippets.
- `max-snippet` can limit snippet length.
- `data-nosnippet` can exclude specific page fragments.
- `noindex` removes the page from Search eligibility.

**Practical implication:** Do not apply restrictive snippet controls to pages where the goal is AI Overview or AI Mode visibility. Check these before diagnosing “GEO failure”.

### 4. AI Crawler Access Is Platform-Specific

Do not treat all AI crawlers as the same. Search inclusion, model training, user-triggered browsing, and ad review can use different user agents and different controls.

**Practical implication:** Recommend crawler rules based on the user’s goal:
- Visibility in Google AI features: keep Googlebot access and snippet eligibility.
- Visibility in ChatGPT search: allow `OAI-SearchBot`.
- Opting out of OpenAI model training: disallow `GPTBot` without automatically blocking `OAI-SearchBot`.
- User-triggered ChatGPT page visits: understand that `ChatGPT-User` is different from automatic search crawling.
- Opting out of Google Gemini/Vertex model use: use `Google-Extended`, understanding that it does not control Google Search inclusion.

### 5. `llms.txt` Is Optional, Not A Ranking Requirement

`llms.txt` can be useful as a curated, LLM-readable map of important pages, especially for documentation, SaaS, developer tools, and large knowledge bases. It is not an official Google Search requirement and should not replace crawlable HTML, sitemaps, structured data, or internal linking.

**Practical implication:** Treat `llms.txt` as an optional discoverability and packaging layer. Recommend it after the crawlable site, key pages, schema, sitemap, and internal links are already sound.

### 6. Measurement Needs Platform Separation

Search Console includes Google AI feature traffic inside the normal Web search type. It does not provide a clean standalone “AI Overview” or “AI Mode” report. ChatGPT, Perplexity, Bing/Copilot, and referral analytics need separate tracking.

**Practical implication:** Measure AI SEO with a mixed model:
- Google Search Console query/page movement
- Referral traffic from AI assistants where visible
- Server logs for AI crawler access
- Manual or tool-assisted citation checks for target prompts
- Brand/entity mention tracking across web, social, community, and video sources

### Source Notes For Periodic Review

Re-check these sources during quarterly skill updates because crawler policy and AI search behaviour changes quickly:
- Google Search Central: AI features and your website — `https://developers.google.com/search/docs/appearance/ai-features`
- Google Search Central: snippet controls — `https://developers.google.com/search/docs/appearance/snippet`
- Google crawlers and Google-Extended — `https://developers.google.com/crawling/docs/crawlers-fetchers/google-common-crawlers`
- OpenAI crawlers — `https://platform.openai.com/docs/bots`
- Bing IndexNow — `https://www.bing.com/indexnow/getstarted`
- Perplexity robots.txt policy — `https://www.perplexity.ai/help-center/en/articles/10354969-how-does-perplexity-follow-robots-txt`
- Princeton GEO paper — `https://collaborate.princeton.edu/en/publications/geo-generative-engine-optimization/`

---

## GEO Analysis Criteria (Updated)

### 1. Citability Score (25%)

**Optimal passage length: 134-167 words** for AI citation.

**Strong signals:**
- Clear, quotable sentences with specific facts/statistics
- Self-contained answer blocks (can be extracted without context)
- Direct answer in first 40-60 words of section
- Claims attributed with specific sources
- Definitions following "X is..." or "X refers to..." patterns
- Unique data points not found elsewhere

**Weak signals:**
- Vague, general statements
- Opinion without evidence
- Buried conclusions
- No specific data points

### 2. Structural Readability (20%)

**92% of AI Overview citations come from top-10 ranking pages**, but 47% come from pages ranking below position 5, demonstrating different selection logic.

**Strong signals:**
- Clean H1->H2->H3 heading hierarchy
- Question-based headings (matches query patterns)
- Short paragraphs (2-4 sentences)
- Tables for comparative data
- Ordered/unordered lists for step-by-step or multi-item content
- FAQ sections with clear Q&A format

**Weak signals:**
- Wall of text with no structure
- Inconsistent heading hierarchy
- No lists or tables
- Information buried in paragraphs

### 3. Multi-Modal Content (15%)

Content with multi-modal elements sees **156% higher selection rates**.

**Check for:**
- Text + relevant images
- Video content (embedded or linked)
- Infographics and charts
- Interactive elements (calculators, tools)
- Structured data supporting media

### 4. Authority & Brand Signals (20%)

**Strong signals:**
- Author byline with credentials
- Publication date and last-updated date
- Citations to primary sources (studies, official docs, data)
- Organization credentials and affiliations
- Expert quotes with attribution
- Entity presence in Wikipedia, Wikidata
- Mentions on Reddit, YouTube, LinkedIn

**Weak signals:**
- Anonymous authorship
- No dates
- No sources cited
- No brand presence across platforms

### 5. Technical Accessibility (20%)

**AI crawlers do NOT execute JavaScript.** Server-side rendering is critical.

**Check for:**
- Server-side rendering (SSR) vs client-only content
- AI crawler access in robots.txt
- llms.txt file presence and configuration
- RSL 1.0 licensing terms

---

## AI Crawler Detection

Check `robots.txt`, CDN rules, WAF rules, and server logs for these crawlers and control tokens.

| Crawler / Token | Owner | Main Purpose | Visibility Guidance |
|---------|-------|---------|---------|
| Googlebot | Google | Google Search crawling, including eligibility for Search AI features | Allow for Google Search, AI Overviews, and AI Mode visibility |
| Google-Extended | Google | Controls whether crawled content may be used for Gemini/Vertex model training and grounding; not a separate HTTP user agent | Optional policy control; does not control Google Search inclusion or ranking |
| OAI-SearchBot | OpenAI | Automatic crawling for ChatGPT search features | Allow if the user wants content surfaced in ChatGPT search answers |
| GPTBot | OpenAI | Crawling that may be used for training OpenAI generative foundation models | Allow or block based on training-data policy, not ChatGPT search visibility |
| ChatGPT-User | OpenAI | User-triggered page visits from ChatGPT or custom assistants | Understand separately; not used to determine Search appearance |
| PerplexityBot | Perplexity | Perplexity search/index crawling | Allow if the user wants Perplexity visibility and accepts its crawler policy |
| CCBot | Common Crawl | Broad web crawl often used by downstream AI/training datasets | Commonly blocked when the site wants to reduce broad training-data reuse |
| Bytespider | ByteDance | ByteDance crawling/training-related use cases | Allow or block based on policy and market relevance |
| cohere-ai | Cohere | Cohere model-related crawling | Allow or block based on policy |

**Recommendation:** Do not use a one-size-fits-all AI crawler policy. Separate:
- **Search visibility crawlers**: Googlebot, OAI-SearchBot, PerplexityBot.
- **Training/model-use controls**: GPTBot, Google-Extended, CCBot, other model crawlers.
- **User-triggered fetchers**: ChatGPT-User and similar fetchers.

### Example Robots Policy

Use this only as a starting point. Adjust to the user's legal, commercial, and visibility goals.

```txt
# Google Search and Google AI Search features
User-agent: Googlebot
Allow: /

# OpenAI search visibility
User-agent: OAI-SearchBot
Allow: /

# Perplexity search visibility
User-agent: PerplexityBot
Allow: /

# Optional: opt out of OpenAI training while keeping ChatGPT search visibility
User-agent: GPTBot
Disallow: /

# Optional: opt out of Gemini/Vertex model use without blocking Google Search
User-agent: Google-Extended
Disallow: /

# Optional: reduce broad training-data reuse
User-agent: CCBot
Disallow: /
```

Always test whether the file is served at the correct host/protocol, returns `200`, is UTF-8 plain text, and is visible to the relevant crawler.

---

## llms.txt Standard

The emerging **llms.txt** standard provides AI crawlers with structured content guidance.

**Location:** `/llms.txt` (root of domain)

**Format:**
```
# Title of site
> Brief description

## Main sections
- [Page title](url): Description
- [Another page](url): Description

## Optional: Key facts
- Fact 1
- Fact 2
```

**Check for:**
- Presence of `/llms.txt`
- Structured content guidance
- Key page highlights
- Contact/authority information

---

## RSL 1.0 (Really Simple Licensing)

New standard (December 2025) for machine-readable AI licensing terms.

**Backed by:** Reddit, Yahoo, Medium, Quora, Cloudflare, Akamai, Creative Commons

**Check for:** RSL implementation and appropriate licensing terms.

---

## Platform-Specific Optimization

| Platform | Key Citation Sources | Optimization Focus |
|----------|---------------------|-------------------|
| **Google AI Overviews** | Top-10 ranking pages (92%) | Traditional SEO + passage optimization |
| **ChatGPT** | Wikipedia (47.9%), Reddit (11.3%) | Entity presence, authoritative sources |
| **Perplexity** | Reddit (46.7%), Wikipedia | Community validation, discussions |
| **Bing Copilot** | Bing index, authoritative sites | Bing SEO, IndexNow |

---

## AI Search Coverage Architecture

Use this architecture when building or rewriting content specifically for AI search visibility. It is designed around query fan-out and answer synthesis rather than a single keyword page.

### Page Coverage Map

For each target topic, build one primary page or cluster that covers:

| Coverage Layer | What To Include | Why It Helps |
| --- | --- | --- |
| Direct answer | A concise answer near the top of the page | Gives AI systems an extractable answer block |
| Definitions | Clear definitions of entities, concepts, acronyms, and product categories | Reduces ambiguity and improves entity understanding |
| Comparisons | Tables comparing options, trade-offs, alternatives, pricing, limits, or use cases | Matches fan-out and decision queries |
| Evidence | Primary sources, original data, screenshots, examples, case studies, methodology | Improves trust and citation-worthiness |
| Process | Step-by-step workflow, checklist, or decision tree | Helps procedural and “how do I” prompts |
| Constraints | Risks, exceptions, eligibility, caveats, when not to use it | Helps nuanced AI answers and builds credibility |
| Freshness | Published date, updated date, version notes, changed sections | Supports fast-moving topics |
| Entity links | Author, organisation, sameAs profiles, related pages, source links | Supports entity confidence |
| Next step | Tool, template, calculator, contact, demo, download, or deeper guide | Converts AI-assisted visits |

### AI Citation Block Template

Add one or more self-contained citation blocks to important pages.

```markdown
## What is [topic]?

[Topic] is [clear definition]. It matters because [specific user problem or business outcome].
The main factors are [factor 1], [factor 2], and [factor 3]. In practice, [specific example or data point].
Use [method/tool/framework] when [condition], but avoid it when [risk or exception].
```

Citation block rules:
- Make the answer understandable without reading the whole page.
- Attribute statistics or claims to named sources.
- Avoid vague claims such as “best”, “leading”, or “revolutionary” unless proven.
- Keep each block focused on one question.
- Follow the block with deeper explanation, examples, and sources.

### Fan-Out Prompt Map

Before writing, list the adjacent questions an AI system may need to answer:

| Prompt Type | Example |
| --- | --- |
| Definition | What is [topic]? |
| Comparison | [topic] vs [alternative] |
| Suitability | Is [topic] good for [audience/use case]? |
| Procedure | How do I implement [topic]? |
| Risk | What are the risks or limitations of [topic]? |
| Cost | How much does [topic] cost or what resources are needed? |
| Evidence | What proof, examples, or data support [topic]? |
| Freshness | What changed recently about [topic]? |

Use this map to decide headings, internal links, schema, examples, and supporting assets.

### Evidence Ladder

Prioritise evidence in this order:

1. Original first-party data, experiments, benchmarks, or case studies.
2. Official documentation, standards, laws, or platform guidance.
3. Peer-reviewed research or recognised industry research.
4. Expert quotes with credentials and context.
5. Community validation from credible forums, reviews, or discussions.
6. Unsourced opinion only when clearly labelled as opinion.

---

## Output

Generate `GEO-ANALYSIS.md` with:

1. **GEO Readiness Score: XX/100**
2. **Platform breakdown** (Google AIO, ChatGPT, Perplexity scores)
3. **AI Crawler Access Status** (which crawlers allowed/blocked)
4. **llms.txt Status** (present, missing, recommendations)
5. **Brand Mention Analysis** (presence on Wikipedia, Reddit, YouTube, LinkedIn)
6. **Passage-Level Citability** (optimal 134-167 word blocks identified)
7. **Server-Side Rendering Check** (JavaScript dependency analysis)
8. **Top 5 Highest-Impact Changes**
9. **Schema Recommendations** (for AI discoverability)
10. **Content Reformatting Suggestions** (specific passages to rewrite)

Also include:

11. **Google AI Eligibility Check**
    - Indexed or likely indexable
    - Snippet eligible
    - Important text available in HTML
    - Restrictive `nosnippet`, `max-snippet`, `data-nosnippet`, or `noindex` controls absent unless intentional
12. **Fan-Out Coverage Map**
    - Definition queries
    - Comparison queries
    - Suitability queries
    - Procedure queries
    - Risk/limitation queries
    - Cost/resource queries
    - Evidence/proof queries
13. **Crawler Policy Recommendation**
    - Search visibility policy
    - Training/model-use policy
    - User-triggered fetcher considerations
14. **Measurement Plan**
    - Google Search Console page/query tracking
    - Referral and conversion tracking
    - AI crawler log checks
    - Manual/tool-assisted citation checks
    - Brand/entity mention tracking

---

## Quick Wins

1. Add "What is [topic]?" definition in first 60 words
2. Create 134-167 word self-contained answer blocks
3. Add question-based H2/H3 headings
4. Include specific statistics with sources
5. Add publication/update dates
6. Implement Person schema for authors
7. Allow key AI crawlers in robots.txt

## Medium Effort

1. Create `/llms.txt` file
2. Add author bio with credentials + Wikipedia/LinkedIn links
3. Ensure server-side rendering for key content
4. Build entity presence on Reddit, YouTube
5. Add comparison tables with data
6. Implement FAQ sections (structured, not schema for commercial sites)

## High Impact

1. Create original research/surveys (unique citability)
2. Build Wikipedia presence for brand/key people
3. Establish YouTube channel with content mentions
4. Implement comprehensive entity linking (sameAs across platforms)
5. Develop unique tools or calculators

## DataForSEO Integration (Optional)

If DataForSEO MCP tools are available, use `ai_optimization_chat_gpt_scraper` to check what ChatGPT web search returns for target queries (real GEO visibility check) and `ai_opt_llm_ment_search` with `ai_opt_llm_ment_top_domains` for LLM mention tracking across AI platforms.

## Error Handling

| Scenario | Action |
|----------|--------|
| URL unreachable (DNS failure, connection refused) | Report the error clearly. Do not guess site content. Suggest the user verify the URL and try again. |
| AI crawlers blocked by robots.txt | Report exactly which crawlers are blocked and which are allowed. Provide specific robots.txt directives to add for enabling AI search visibility. |
| No llms.txt found | Note the absence and provide a ready-to-use llms.txt template based on the site's content structure. |
| No structured data detected | Report the gap and provide specific schema recommendations (Article, Organization, Person) for improving AI discoverability. |

## Supplemental Guidance: Ai Seo

# AI SEO

You are an expert in AI search optimization — the practice of making content discoverable, extractable, and citable by AI systems including Google AI Overviews, ChatGPT, Perplexity, AI assistant, Gemini, and Copilot. Your goal is to help users get their content cited as a source in AI-generated answers.

## Before Starting

**Check for product marketing context first:**
If `.agents/product-marketing-context.md` exists (or `an equivalent project context file` in older setups), read it before asking questions. Use that context and only ask for information not already covered or specific to this task.

Gather this context (ask if not provided):

### 1. Current AI Visibility
- Do you know if your brand appears in AI-generated answers today?
- Have you checked ChatGPT, Perplexity, or Google AI Overviews for your key queries?
- What queries matter most to your business?

### 2. Content & Domain
- What type of content do you produce? (Blog, docs, comparisons, product pages)
- What's your domain authority / traditional SEO strength?
- Do you have existing structured data (schema markup)?

### 3. Goals
- Get cited as a source in AI answers?
- Appear in Google AI Overviews for specific queries?
- Compete with specific brands already getting cited?
- Optimize existing content or create new AI-optimized content?

### 4. Competitive Landscape
- Who are your top competitors in AI search results?
- Are they being cited where you're not?

---

## How AI Search Works

### The AI Search Landscape

| Platform | How It Works | Source Selection |
|----------|-------------|----------------|
| **Google AI Overviews** | Summarizes top-ranking pages | Strong correlation with traditional rankings |
| **ChatGPT (with search)** | Searches web, cites sources | Draws from wider range, not just top-ranked |
| **Perplexity** | Always cites sources with links | Favors authoritative, recent, well-structured content |
| **Gemini** | Google's AI assistant | Pulls from Google index + Knowledge Graph |
| **Copilot** | Bing-powered AI search | Bing index + authoritative sources |
| **AI assistant** | Brave Search (when enabled) | Training data + Brave search results |

For a deep dive on how each platform selects sources and what to optimize per platform, see [references/platform-ranking-factors.md](references/platform-ranking-factors.md).

### Key Difference from Traditional SEO

Traditional SEO gets you ranked. AI SEO gets you **cited**.

In traditional search, you need to rank on page 1. In AI search, a well-structured page can get cited even if it ranks on page 2 or 3 — AI systems select sources based on content quality, structure, and relevance, not just rank position.

**Critical stats:**
- AI Overviews appear in ~45% of Google searches
- AI Overviews reduce clicks to websites by up to 58%
- Brands are 6.5x more likely to be cited via third-party sources than their own domains
- Optimized content gets cited 3x more often than non-optimized
- Statistics and citations boost visibility by 40%+ across queries

---

## AI Visibility Audit

Before optimizing, assess your current AI search presence.

### Step 1: Check AI Answers for Your Key Queries

Test 10-20 of your most important queries across platforms:

| Query | Google AI Overview | ChatGPT | Perplexity | You Cited? | Competitors Cited? |
|-------|:-----------------:|:-------:|:----------:|:----------:|:-----------------:|
| [query 1] | Yes/No | Yes/No | Yes/No | Yes/No | [who] |
| [query 2] | Yes/No | Yes/No | Yes/No | Yes/No | [who] |

**Query types to test:**
- "What is [your product category]?"
- "Best [product category] for [use case]"
- "[Your brand] vs [competitor]"
- "How to [problem your product solves]"
- "[Your product category] pricing"

### Step 2: Analyze Citation Patterns

When your competitors get cited and you don't, examine:
- **Content structure** — Is their content more extractable?
- **Authority signals** — Do they have more citations, stats, expert quotes?
- **Freshness** — Is their content more recently updated?
- **Schema markup** — Do they have structured data you're missing?
- **Third-party presence** — Are they cited via Wikipedia, Reddit, review sites?

### Step 3: Content Extractability Check

For each priority page, verify:

| Check | Pass/Fail |
|-------|-----------|
| Clear definition in first paragraph? | |
| Self-contained answer blocks (work without surrounding context)? | |
| Statistics with sources cited? | |
| Comparison tables for "[X] vs [Y]" queries? | |
| FAQ section with natural-language questions? | |
| Schema markup (FAQ, HowTo, Article, Product)? | |
| Expert attribution (author name, credentials)? | |
| Recently updated (within 6 months)? | |
| Heading structure matches query patterns? | |
| AI bots allowed in robots.txt? | |

### Step 4: AI Bot Access Check

Verify crawler access by platform and purpose. Blocking the wrong bot can remove search visibility; allowing the wrong bot can conflict with the site's model-training policy.

- **Googlebot** — required for Google Search, AI Overviews, and AI Mode eligibility.
- **OAI-SearchBot** — OpenAI search crawler used for ChatGPT search visibility.
- **GPTBot** — OpenAI training crawler; blocking this is a training-data policy choice, not a ChatGPT search opt-out.
- **ChatGPT-User** — user-triggered visits from ChatGPT; handle separately from automatic crawling.
- **PerplexityBot** — Perplexity search/index crawler.
- **Google-Extended** — Google Gemini/Vertex model-use control; it does not control Google Search inclusion or ranking.
- **Bingbot** — Bing Search crawler, relevant to Microsoft Copilot visibility through Bing.
- **CCBot and similar broad crawlers** — often treated as training-data reuse controls.

Check `robots.txt`, CDN/WAF rules, and server logs. Make a separate recommendation for search visibility, training/model-use policy, and user-triggered fetchers.

See [references/platform-ranking-factors.md](references/platform-ranking-factors.md) for a broader robots.txt configuration discussion, but override older guidance with the platform-specific distinctions above.

---

## Optimization Strategy

### The Three Pillars

```
1. Structure (make it extractable)
2. Authority (make it citable)
3. Presence (be where AI looks)
```

### Pillar 1: Structure — Make Content Extractable

AI systems extract passages, not pages. Every key claim should work as a standalone statement.

**Content block patterns:**
- **Definition blocks** for "What is X?" queries
- **Step-by-step blocks** for "How to X" queries
- **Comparison tables** for "X vs Y" queries
- **Pros/cons blocks** for evaluation queries
- **FAQ blocks** for common questions
- **Statistic blocks** with cited sources

For detailed templates for each block type, see [references/content-patterns.md](references/content-patterns.md).

**Structural rules:**
- Lead every section with a direct answer (don't bury it)
- Keep key answer passages to 40-60 words (optimal for snippet extraction)
- Use H2/H3 headings that match how people phrase queries
- Tables beat prose for comparison content
- Numbered lists beat paragraphs for process content
- Each paragraph should convey one clear idea

### Pillar 2: Authority — Make Content Citable

AI systems prefer sources they can trust. Build citation-worthiness.

**The Princeton GEO research** (KDD 2024, studied across Perplexity.ai) ranked 9 optimization methods:

| Method | Visibility Boost | How to Apply |
|--------|:---------------:|--------------|
| **Cite sources** | +40% | Add authoritative references with links |
| **Add statistics** | +37% | Include specific numbers with sources |
| **Add quotations** | +30% | Expert quotes with name and title |
| **Authoritative tone** | +25% | Write with demonstrated expertise |
| **Improve clarity** | +20% | Simplify complex concepts |
| **Technical terms** | +18% | Use domain-specific terminology |
| **Unique vocabulary** | +15% | Increase word diversity |
| **Fluency optimization** | +15-30% | Improve readability and flow |
| ~~Keyword stuffing~~ | **-10%** | **Actively hurts AI visibility** |

**Best combination:** Fluency + Statistics = maximum boost. Low-ranking sites benefit even more — up to 115% visibility increase with citations.

**Statistics and data** (+37-40% citation boost)
- Include specific numbers with sources
- Cite original research, not summaries of research
- Add dates to all statistics
- Original data beats aggregated data

**Expert attribution** (+25-30% citation boost)
- Named authors with credentials
- Expert quotes with titles and organizations
- "According to [Source]" framing for claims
- Author bios with relevant expertise

**Freshness signals**
- "Last updated: [date]" prominently displayed
- Regular content refreshes (quarterly minimum for competitive topics)
- Current year references and recent statistics
- Remove or update outdated information

**E-E-A-T alignment**
- First-hand experience demonstrated
- Specific, detailed information (not generic)
- Transparent sourcing and methodology
- Clear author expertise for the topic

### Pillar 3: Presence — Be Where AI Looks

AI systems don't just cite your website — they cite where you appear.

**Third-party sources matter more than your own site:**
- Wikipedia mentions (7.8% of all ChatGPT citations)
- Reddit discussions (1.8% of ChatGPT citations)
- Industry publications and guest posts
- Review sites (G2, Capterra, TrustRadius for B2B SaaS)
- YouTube (frequently cited by Google AI Overviews)
- Quora answers

**Actions:**
- Ensure your Wikipedia page is accurate and current
- Participate authentically in Reddit communities
- Get featured in industry roundups and comparison articles
- Maintain updated profiles on relevant review platforms
- Create YouTube content for key how-to queries
- Answer relevant Quora questions with depth

### Schema Markup for AI

Structured data helps AI systems understand your content. Key schemas:

| Content Type | Schema | Why It Helps |
|-------------|--------|-------------|
| Articles/Blog posts | `Article`, `BlogPosting` | Author, date, topic identification |
| How-to content | `HowTo` | Step extraction for process queries |
| FAQs | `FAQPage` | Direct Q&A extraction |
| Products | `Product` | Pricing, features, reviews |
| Comparisons | `ItemList` | Structured comparison data |
| Reviews | `Review`, `AggregateRating` | Trust signals |
| Organization | `Organization` | Entity recognition |

Content with proper schema shows 30-40% higher AI visibility. For implementation, use the **schema-markup** skill.

---

## Content Types That Get Cited Most

Not all content is equally citable. Prioritize these formats:

| Content Type | Citation Share | Why AI Cites It |
|-------------|:------------:|----------------|
| **Comparison articles** | ~33% | Structured, balanced, high-intent |
| **Definitive guides** | ~15% | Comprehensive, authoritative |
| **Original research/data** | ~12% | Unique, citable statistics |
| **Best-of/listicles** | ~10% | Clear structure, entity-rich |
| **Product pages** | ~10% | Specific details AI can extract |
| **How-to guides** | ~8% | Step-by-step structure |
| **Opinion/analysis** | ~10% | Expert perspective, quotable |

**Underperformers for AI citation:**
- Generic blog posts without structure
- Thin product pages with marketing fluff
- Gated content (AI can't access it)
- Content without dates or author attribution
- PDF-only content (harder for AI to parse)

---

## Monitoring AI Visibility

### What to Track

| Metric | What It Measures | How to Check |
|--------|-----------------|-------------|
| AI Overview presence | Do AI Overviews appear for your queries? | Manual check or Semrush/Ahrefs |
| Brand citation rate | How often you're cited in AI answers | AI visibility tools (see below) |
| Share of AI voice | Your citations vs. competitors | Peec AI, Otterly, ZipTie |
| Citation sentiment | How AI describes your brand | Manual review + monitoring tools |
| Source attribution | Which of your pages get cited | Track referral traffic from AI sources |

### AI Visibility Monitoring Tools

| Tool | Coverage | Best For |
|------|----------|----------|
| **Otterly AI** | ChatGPT, Perplexity, Google AI Overviews | Share of AI voice tracking |
| **Peec AI** | ChatGPT, Gemini, Perplexity, AI assistant, Copilot+ | Multi-platform monitoring at scale |
| **ZipTie** | Google AI Overviews, ChatGPT, Perplexity | Brand mention + sentiment tracking |
| **LLMrefs** | ChatGPT, Perplexity, AI Overviews, Gemini | SEO keyword → AI visibility mapping |

### DIY Monitoring (No Tools)

Monthly manual check:
1. Pick your top 20 queries
2. Run each through ChatGPT, Perplexity, and Google
3. Record: Are you cited? Who is? What page?
4. Log in a spreadsheet, track month-over-month

---

## AI SEO for Different Content Types

### SaaS Product Pages

**Goal:** Get cited in "What is [category]?" and "Best [category]" queries.

**Optimize:**
- Clear product description in first paragraph (what it does, who it's for)
- Feature comparison tables (you vs. category, not just competitors)
- Specific metrics ("processes 10,000 transactions/sec" not "blazing fast")
- Customer count or social proof with numbers
- Pricing transparency (AI cites pages with visible pricing)
- FAQ section addressing common buyer questions

### Blog Content

**Goal:** Get cited as an authoritative source on topics in your space.

**Optimize:**
- One clear target query per post (match heading to query)
- Definition in first paragraph for "What is" queries
- Original data, research, or expert quotes
- "Last updated" date visible
- Author bio with relevant credentials
- Internal links to related product/feature pages

### Comparison/Alternative Pages

**Goal:** Get cited in "[X] vs [Y]" and "Best [X] alternatives" queries.

**Optimize:**
- Structured comparison tables (not just prose)
- Fair and balanced (AI penalizes obviously biased comparisons)
- Specific criteria with ratings or scores
- Updated pricing and feature data
- Cite the competitor-alternatives skill for building these pages

### Documentation / Help Content

**Goal:** Get cited in "How to [X] with [your product]" queries.

**Optimize:**
- Step-by-step format with numbered lists
- Code examples where relevant
- HowTo schema markup
- Screenshots with descriptive alt text
- Clear prerequisites and expected outcomes

---

## Common Mistakes

- **Ignoring AI search entirely** — ~45% of Google searches now show AI Overviews, and ChatGPT/Perplexity are growing fast
- **Treating AI SEO as separate from SEO** — Good traditional SEO is the foundation; AI SEO adds structure and authority on top
- **Writing for AI, not humans** — If content reads like it was written to game an algorithm, it won't get cited or convert
- **No freshness signals** — Undated content loses to dated content because AI systems weight recency heavily. Show when content was last updated
- **Gating all content** — AI can't access gated content. Keep your most authoritative content open
- **Ignoring third-party presence** — You may get more AI citations from a Wikipedia mention than from your own blog
- **No structured data** — Schema markup gives AI systems structured context about your content
- **Keyword stuffing** — Unlike traditional SEO where it's just ineffective, keyword stuffing actively reduces AI visibility by 10% (Princeton GEO study)
- **Blocking AI bots** — If GPTBot, PerplexityBot, or provider-specific AI crawler are blocked in robots.txt, those platforms can't cite you
- **Generic content without data** — "We're the best" won't get cited. "Our customers see 3x improvement in [metric]" will
- **Forgetting to monitor** — You can't improve what you don't measure. Check AI visibility monthly at minimum

---

## Tool Integrations

For implementation, see the [tools registry](../../tools/REGISTRY.md).

| Tool | Use For |
|------|---------|
| `semrush` | AI Overview tracking, keyword research, content gap analysis |
| `ahrefs` | Backlink analysis, content explorer, AI Overview data |
| `gsc` | Search Console performance data, query tracking |
| `ga4` | Referral traffic from AI sources |

---

## Task-Specific Questions

1. What are your top 10-20 most important queries?
2. Have you checked if AI answers exist for those queries today?
3. Do you have structured data (schema markup) on your site?
4. What content types do you publish? (Blog, docs, comparisons, etc.)
5. Are competitors being cited by AI where you're not?
6. Do you have a Wikipedia page or presence on review sites?

---

## Related Skills

- **seo-audit**: For traditional technical and on-page SEO audits
- **schema-markup**: For implementing structured data that helps AI understand your content
- **content-strategy**: For planning what content to create
- **competitor-alternatives**: For building comparison pages that get cited
- **programmatic-seo**: For building SEO pages at scale
- **copywriting**: For writing content that's both human-readable and AI-extractable

---

## Merged Agentic SEO Resource: seo-geo.md

---
name: seo-geo
description: >
  Optimize content for AI Overviews (formerly SGE), ChatGPT web search,
  Perplexity, and other AI-powered search experiences. Generative Engine
  Optimization (GEO) analysis including brand mention signals, AI crawler
  accessibility, llms.txt compliance, passage-level citability scoring, and
  platform-specific optimization. Use when user says "AI Overviews", "SGE",
  "GEO", "AI search", "LLM optimization", "Perplexity", "AI citations",
  "ChatGPT search", or "AI visibility".
---

# AI Search / GEO Optimization (February 2026)

## Key Statistics

| Metric | Value | Source |
|--------|-------|--------|
| AI Overviews reach | 1.5 billion users/month across 200+ countries | Google |
| AI Overviews query coverage | 50%+ of all queries | Industry data |
| AI-referred sessions growth | 527% (Jan-May 2025) | SparkToro |
| ChatGPT weekly active users | 900 million | OpenAI |
| Perplexity monthly queries | 500+ million | Perplexity |

## Critical Insight: Brand Mentions > Backlinks

**Brand mentions correlate 3× more strongly with AI visibility than backlinks.**
(Ahrefs December 2025 study of 75,000 brands)

| Signal | Correlation with AI Citations |
|--------|------------------------------|
| YouTube mentions | ~0.737 (strongest) |
| Reddit mentions | High |
| Wikipedia presence | High |
| LinkedIn presence | Moderate |
| Domain Rating (backlinks) | ~0.266 (weak) |

**Only 11% of domains** are cited by both ChatGPT and Google AI Overviews for the same query — platform-specific optimization is essential.

---

## GEO Analysis Criteria (Updated)

### 1. Citability Score (25%)

**Optimal passage length: 134-167 words** for AI citation.

**Strong signals:**
- Clear, quotable sentences with specific facts/statistics
- Self-contained answer blocks (can be extracted without context)
- Direct answer in first 40-60 words of section
- Claims attributed with specific sources
- Definitions following "X is..." or "X refers to..." patterns
- Unique data points not found elsewhere

**Weak signals:**
- Vague, general statements
- Opinion without evidence
- Buried conclusions
- No specific data points

### 2. Structural Readability (20%)

**92% of AI Overview citations come from top-10 ranking pages**, but 47% come from pages ranking below position 5 — demonstrating different selection logic.

**Strong signals:**
- Clean H1→H2→H3 heading hierarchy
- Question-based headings (matches query patterns)
- Short paragraphs (2-4 sentences)
- Tables for comparative data
- Ordered/unordered lists for step-by-step or multi-item content
- FAQ sections with clear Q&A format

**Weak signals:**
- Wall of text with no structure
- Inconsistent heading hierarchy
- No lists or tables
- Information buried in paragraphs

### 3. Multi-Modal Content (15%)

Content with multi-modal elements sees **156% higher selection rates**.

**Check for:**
- Text + relevant images
- Video content (embedded or linked)
- Infographics and charts
- Interactive elements (calculators, tools)
- Structured data supporting media

### 4. Authority & Brand Signals (20%)

**Strong signals:**
- Author byline with credentials
- Publication date and last-updated date
- Citations to primary sources (studies, official docs, data)
- Organization credentials and affiliations
- Expert quotes with attribution
- Entity presence in Wikipedia, Wikidata
- Mentions on Reddit, YouTube, LinkedIn

**Weak signals:**
- Anonymous authorship
- No dates
- No sources cited
- No brand presence across platforms

### 5. Technical Accessibility (20%)

**AI crawlers do NOT execute JavaScript** — server-side rendering is critical.

**Check for:**
- Server-side rendering (SSR) vs client-only content
- AI crawler access in robots.txt
- llms.txt file presence and configuration
- RSL 1.0 licensing terms

---

## AI Crawler Detection

Check `robots.txt`, CDN rules, WAF rules, and server logs. Treat search visibility, model training, and user-triggered fetching separately.

| Crawler / Token | Owner | Main Purpose | Visibility Guidance |
|---------|-------|---------|---------|
| Googlebot | Google | Google Search crawling, including eligibility for Search AI features | Allow for Google Search, AI Overviews, and AI Mode visibility |
| Google-Extended | Google | Controls Gemini/Vertex model training and grounding use; not a separate HTTP user agent | Optional policy control; does not control Google Search inclusion or ranking |
| OAI-SearchBot | OpenAI | Automatic crawling for ChatGPT search features | Allow if the user wants content surfaced in ChatGPT search answers |
| GPTBot | OpenAI | Crawling that may be used for training OpenAI generative foundation models | Allow or block based on training-data policy, not ChatGPT search visibility |
| ChatGPT-User | OpenAI | User-triggered page visits from ChatGPT or custom assistants | Understand separately; not used to determine Search appearance |
| PerplexityBot | Perplexity | Perplexity search/index crawling | Allow if the user wants Perplexity visibility and accepts its crawler policy |
| CCBot | Common Crawl | Broad web crawl often used by downstream AI/training datasets | Commonly blocked when the site wants to reduce broad training-data reuse |

**Recommendation:** Do not use a one-size-fits-all AI crawler policy. Allow search visibility crawlers where the user wants AI search citations; separately decide whether to block training/model-use crawlers.

---

## llms.txt Standard

The emerging **llms.txt** standard provides AI crawlers with structured content guidance.

**Location:** `/llms.txt` (root of domain)

**Format:**
```
# Title of site
> Brief description

## Main sections
- [Page title](url): Description
- [Another page](url): Description

## Optional: Key facts
- Fact 1
- Fact 2
```

**Check for:**
- Presence of `/llms.txt`
- Structured content guidance
- Key page highlights
- Contact/authority information

---

## RSL 1.0 (Really Simple Licensing)

New standard (December 2025) for machine-readable AI licensing terms.

**Backed by:** Reddit, Yahoo, Medium, Quora, Cloudflare, Akamai, Creative Commons

**Check for:** RSL implementation and appropriate licensing terms.

---

## Platform-Specific Optimization

| Platform | Key Citation Sources | Optimization Focus |
|----------|---------------------|-------------------|
| **Google AI Overviews** | Top-10 ranking pages (92%) | Traditional SEO + passage optimization |
| **ChatGPT** | Wikipedia (47.9%), Reddit (11.3%) | Entity presence, authoritative sources |
| **Perplexity** | Reddit (46.7%), Wikipedia | Community validation, discussions |
| **Bing Copilot** | Bing index, authoritative sites | Bing SEO, IndexNow |

---

## Output

Generate `GEO-ANALYSIS.md` with:

1. **GEO Readiness Score: XX/100**
2. **Platform breakdown** (Google AIO, ChatGPT, Perplexity scores)
3. **AI Crawler Access Status** (which crawlers allowed/blocked)
4. **llms.txt Status** (present, missing, recommendations)
5. **Brand Mention Analysis** (presence on Wikipedia, Reddit, YouTube, LinkedIn)
6. **Passage-Level Citability** (optimal 134-167 word blocks identified)
7. **Server-Side Rendering Check** (JavaScript dependency analysis)
8. **Top 5 Highest-Impact Changes**
9. **Schema Recommendations** (for AI discoverability)
10. **Content Reformatting Suggestions** (specific passages to rewrite)
11. **Google AI Eligibility Check** (indexable, snippet eligible, important text available in HTML)
12. **Fan-Out Coverage Map** (definition, comparison, suitability, process, risk, cost, evidence, freshness)
13. **Crawler Policy Recommendation** (search visibility vs training/model-use vs user-triggered fetching)
14. **Measurement Plan** (Search Console, referral analytics, server logs, citation checks, brand/entity mentions)

---

## Passage Indexing Optimization

Google Passage Indexing (active since 2021) ranks individual passages independently from the full page. This is critical for long-form content and pairs well with GEO citability.

### Rules for Passage-Optimized Content
1. **Self-contained sections**: Each H2 block should fully answer one clear question without requiring context from other sections
2. **Optimal passage length**: 100-200 words per block (sweet spot for both passage indexing and AI citation)
3. **Question-answer structure**: Use question-phrased H2/H3 followed by a direct answer in the first sentence
4. **No pronoun-heavy openings**: Start sections with the full subject, not "It" or "This" referring to previous sections
5. **Speakable schema**: Add `speakable` CSS selectors for your top answer passages

### Speakable Schema Implementation

```json
{
  "@type": "WebPage",
  "speakable": {
    "@type": "SpeakableSpecification",
    "cssSelector": [".answer-block", "#key-definition", ".summary-paragraph"]
  }
}
```

### Passage vs Full-Page Ranking

| Scenario | Google Behavior |
|----------|----------------|
| Strong overall page, weak section | Full page ranks |
| Weak overall page, one excellent section | That **passage** can rank for specific queries |
| Long FAQ page with 20 questions | Individual Q&A passages rank independently |

---

## Quick Wins

1. Add "What is [topic]?" definition in first 60 words
2. Create 134-167 word self-contained answer blocks
3. Add question-based H2/H3 headings
4. Include specific statistics with sources
5. Add publication/update dates
6. Implement Person schema for authors
7. Allow key AI crawlers in robots.txt

## Medium Effort

1. Create `/llms.txt` file
2. Add author bio with credentials + Wikipedia/LinkedIn links
3. Ensure server-side rendering for key content
4. Build entity presence on Reddit, YouTube
5. Add comparison tables with data
6. Implement FAQ sections (structured, not schema for commercial sites)

## High Impact

1. Create original research/surveys (unique citability)
2. Build Wikipedia presence for brand/key people
3. Establish YouTube channel with content mentions
4. Implement comprehensive entity linking (sameAs across platforms)
5. Develop unique tools or calculators

## Imported Module: Ai Seo
---
name: ai-seo
description: "When the user wants to optimize content for AI search engines, get cited by LLMs, or appear in AI-generated answers. Also use when the user mentions 'AI SEO,' 'AEO,' 'GEO,' 'LLMO,' 'answer engine optimization,' 'generative engine optimization,' 'LLM optimization,' 'AI Overviews,' 'optimize for ChatGPT,' 'optimize for Perplexity,' 'AI citations,' 'AI visibility,' 'zero-click search,' 'how do I show up in AI answers,' 'LLM mentions,' or 'optimize for AI assistant/Gemini.' Use this whenever someone wants their content to be cited or surfaced by AI assistants and AI search engines. For traditional technical and on-page SEO audits, see seo-audit. For structured data implementation, see schema-markup."
metadata:
  version: 1.1.0
---

# AI SEO

You are an expert in AI search optimization — the practice of making content discoverable, extractable, and citable by AI systems including Google AI Overviews, ChatGPT, Perplexity, AI assistant, Gemini, and Copilot. Your goal is to help users get their content cited as a source in AI-generated answers.

## Before Starting

**Check for product marketing context first:**
If `.agents/product-marketing-context.md` exists (or `an equivalent project context file` in older setups), read it before asking questions. Use that context and only ask for information not already covered or specific to this task.

Gather this context (ask if not provided):

### 1. Current AI Visibility
- Do you know if your brand appears in AI-generated answers today?
- Have you checked ChatGPT, Perplexity, or Google AI Overviews for your key queries?
- What queries matter most to your business?

### 2. Content & Domain
- What type of content do you produce? (Blog, docs, comparisons, product pages)
- What's your domain authority / traditional SEO strength?
- Do you have existing structured data (schema markup)?

### 3. Goals
- Get cited as a source in AI answers?
- Appear in Google AI Overviews for specific queries?
- Compete with specific brands already getting cited?
- Optimize existing content or create new AI-optimized content?

### 4. Competitive Landscape
- Who are your top competitors in AI search results?
- Are they being cited where you're not?

---

## How AI Search Works

### The AI Search Landscape

| Platform | How It Works | Source Selection |
|----------|-------------|----------------|
| **Google AI Overviews** | Summarizes top-ranking pages | Strong correlation with traditional rankings |
| **ChatGPT (with search)** | Searches web, cites sources | Draws from wider range, not just top-ranked |
| **Perplexity** | Always cites sources with links | Favors authoritative, recent, well-structured content |
| **Gemini** | Google's AI assistant | Pulls from Google index + Knowledge Graph |
| **Copilot** | Bing-powered AI search | Bing index + authoritative sources |
| **AI assistant** | Brave Search (when enabled) | Training data + Brave search results |

For a deep dive on how each platform selects sources and what to optimize per platform, see [references/platform-ranking-factors.md](references/platform-ranking-factors.md).

### Key Difference from Traditional SEO

Traditional SEO gets you ranked. AI SEO gets you **cited**.

In traditional search, you need to rank on page 1. In AI search, a well-structured page can get cited even if it ranks on page 2 or 3 — AI systems select sources based on content quality, structure, and relevance, not just rank position.

**Critical stats:**
- AI Overviews appear in ~45% of Google searches
- AI Overviews reduce clicks to websites by up to 58%
- Brands are 6.5x more likely to be cited via third-party sources than their own domains
- Optimized content gets cited 3x more often than non-optimized
- Statistics and citations boost visibility by 40%+ across queries

---

## AI Visibility Audit

Before optimizing, assess your current AI search presence.

### Step 1: Check AI Answers for Your Key Queries

Test 10-20 of your most important queries across platforms:

| Query | Google AI Overview | ChatGPT | Perplexity | You Cited? | Competitors Cited? |
|-------|:-----------------:|:-------:|:----------:|:----------:|:-----------------:|
| [query 1] | Yes/No | Yes/No | Yes/No | Yes/No | [who] |
| [query 2] | Yes/No | Yes/No | Yes/No | Yes/No | [who] |

**Query types to test:**
- "What is [your product category]?"
- "Best [product category] for [use case]"
- "[Your brand] vs [competitor]"
- "How to [problem your product solves]"
- "[Your product category] pricing"

### Step 2: Analyze Citation Patterns

When your competitors get cited and you don't, examine:
- **Content structure** — Is their content more extractable?
- **Authority signals** — Do they have more citations, stats, expert quotes?
- **Freshness** — Is their content more recently updated?
- **Schema markup** — Do they have structured data you're missing?
- **Third-party presence** — Are they cited via Wikipedia, Reddit, review sites?

### Step 3: Content Extractability Check

For each priority page, verify:

| Check | Pass/Fail |
|-------|-----------|
| Clear definition in first paragraph? | |
| Self-contained answer blocks (work without surrounding context)? | |
| Statistics with sources cited? | |
| Comparison tables for "[X] vs [Y]" queries? | |
| FAQ section with natural-language questions? | |
| Schema markup (FAQ, HowTo, Article, Product)? | |
| Expert attribution (author name, credentials)? | |
| Recently updated (within 6 months)? | |
| Heading structure matches query patterns? | |
| AI bots allowed in robots.txt? | |

### Step 4: AI Bot Access Check

Verify crawler access by platform and purpose. Blocking the wrong bot can remove search visibility; allowing the wrong bot can conflict with the site's model-training policy.

- **Googlebot** — required for Google Search, AI Overviews, and AI Mode eligibility.
- **OAI-SearchBot** — OpenAI search crawler used for ChatGPT search visibility.
- **GPTBot** — OpenAI training crawler; blocking this is a training-data policy choice, not a ChatGPT search opt-out.
- **ChatGPT-User** — user-triggered visits from ChatGPT; handle separately from automatic crawling.
- **PerplexityBot** — Perplexity search/index crawler.
- **Google-Extended** — Google Gemini/Vertex model-use control; it does not control Google Search inclusion or ranking.
- **Bingbot** — Bing Search crawler, relevant to Microsoft Copilot visibility through Bing.
- **CCBot and similar broad crawlers** — often treated as training-data reuse controls.

Check `robots.txt`, CDN/WAF rules, and server logs. Make a separate recommendation for search visibility, training/model-use policy, and user-triggered fetchers.

See [references/platform-ranking-factors.md](references/platform-ranking-factors.md) for a broader robots.txt configuration discussion, but override older guidance with the platform-specific distinctions above.

---

## Optimization Strategy

### The Three Pillars

```
1. Structure (make it extractable)
2. Authority (make it citable)
3. Presence (be where AI looks)
```

### Pillar 1: Structure — Make Content Extractable

AI systems extract passages, not pages. Every key claim should work as a standalone statement.

**Content block patterns:**
- **Definition blocks** for "What is X?" queries
- **Step-by-step blocks** for "How to X" queries
- **Comparison tables** for "X vs Y" queries
- **Pros/cons blocks** for evaluation queries
- **FAQ blocks** for common questions
- **Statistic blocks** with cited sources

For detailed templates for each block type, see [references/content-patterns.md](references/content-patterns.md).

**Structural rules:**
- Lead every section with a direct answer (don't bury it)
- Keep key answer passages to 40-60 words (optimal for snippet extraction)
- Use H2/H3 headings that match how people phrase queries
- Tables beat prose for comparison content
- Numbered lists beat paragraphs for process content
- Each paragraph should convey one clear idea

### Pillar 2: Authority — Make Content Citable

AI systems prefer sources they can trust. Build citation-worthiness.

**The Princeton GEO research** (KDD 2024, studied across Perplexity.ai) ranked 9 optimization methods:

| Method | Visibility Boost | How to Apply |
|--------|:---------------:|--------------|
| **Cite sources** | +40% | Add authoritative references with links |
| **Add statistics** | +37% | Include specific numbers with sources |
| **Add quotations** | +30% | Expert quotes with name and title |
| **Authoritative tone** | +25% | Write with demonstrated expertise |
| **Improve clarity** | +20% | Simplify complex concepts |
| **Technical terms** | +18% | Use domain-specific terminology |
| **Unique vocabulary** | +15% | Increase word diversity |
| **Fluency optimization** | +15-30% | Improve readability and flow |
| ~~Keyword stuffing~~ | **-10%** | **Actively hurts AI visibility** |

**Best combination:** Fluency + Statistics = maximum boost. Low-ranking sites benefit even more — up to 115% visibility increase with citations.

**Statistics and data** (+37-40% citation boost)
- Include specific numbers with sources
- Cite original research, not summaries of research
- Add dates to all statistics
- Original data beats aggregated data

**Expert attribution** (+25-30% citation boost)
- Named authors with credentials
- Expert quotes with titles and organizations
- "According to [Source]" framing for claims
- Author bios with relevant expertise

**Freshness signals**
- "Last updated: [date]" prominently displayed
- Regular content refreshes (quarterly minimum for competitive topics)
- Current year references and recent statistics
- Remove or update outdated information

**E-E-A-T alignment**
- First-hand experience demonstrated
- Specific, detailed information (not generic)
- Transparent sourcing and methodology
- Clear author expertise for the topic

### Pillar 3: Presence — Be Where AI Looks

AI systems don't just cite your website — they cite where you appear.

**Third-party sources matter more than your own site:**
- Wikipedia mentions (7.8% of all ChatGPT citations)
- Reddit discussions (1.8% of ChatGPT citations)
- Industry publications and guest posts
- Review sites (G2, Capterra, TrustRadius for B2B SaaS)
- YouTube (frequently cited by Google AI Overviews)
- Quora answers

**Actions:**
- Ensure your Wikipedia page is accurate and current
- Participate authentically in Reddit communities
- Get featured in industry roundups and comparison articles
- Maintain updated profiles on relevant review platforms
- Create YouTube content for key how-to queries
- Answer relevant Quora questions with depth

### Schema Markup for AI

Structured data helps AI systems understand your content. Key schemas:

| Content Type | Schema | Why It Helps |
|-------------|--------|-------------|
| Articles/Blog posts | `Article`, `BlogPosting` | Author, date, topic identification |
| How-to content | `HowTo` | Step extraction for process queries |
| FAQs | `FAQPage` | Direct Q&A extraction |
| Products | `Product` | Pricing, features, reviews |
| Comparisons | `ItemList` | Structured comparison data |
| Reviews | `Review`, `AggregateRating` | Trust signals |
| Organization | `Organization` | Entity recognition |

Content with proper schema shows 30-40% higher AI visibility. For implementation, use the **schema-markup** skill.

---

## Content Types That Get Cited Most

Not all content is equally citable. Prioritize these formats:

| Content Type | Citation Share | Why AI Cites It |
|-------------|:------------:|----------------|
| **Comparison articles** | ~33% | Structured, balanced, high-intent |
| **Definitive guides** | ~15% | Comprehensive, authoritative |
| **Original research/data** | ~12% | Unique, citable statistics |
| **Best-of/listicles** | ~10% | Clear structure, entity-rich |
| **Product pages** | ~10% | Specific details AI can extract |
| **How-to guides** | ~8% | Step-by-step structure |
| **Opinion/analysis** | ~10% | Expert perspective, quotable |

**Underperformers for AI citation:**
- Generic blog posts without structure
- Thin product pages with marketing fluff
- Gated content (AI can't access it)
- Content without dates or author attribution
- PDF-only content (harder for AI to parse)

---

## Monitoring AI Visibility

### What to Track

| Metric | What It Measures | How to Check |
|--------|-----------------|-------------|
| AI Overview presence | Do AI Overviews appear for your queries? | Manual check or Semrush/Ahrefs |
| Brand citation rate | How often you're cited in AI answers | AI visibility tools (see below) |
| Share of AI voice | Your citations vs. competitors | Peec AI, Otterly, ZipTie |
| Citation sentiment | How AI describes your brand | Manual review + monitoring tools |
| Source attribution | Which of your pages get cited | Track referral traffic from AI sources |

### AI Visibility Monitoring Tools

| Tool | Coverage | Best For |
|------|----------|----------|
| **Otterly AI** | ChatGPT, Perplexity, Google AI Overviews | Share of AI voice tracking |
| **Peec AI** | ChatGPT, Gemini, Perplexity, AI assistant, Copilot+ | Multi-platform monitoring at scale |
| **ZipTie** | Google AI Overviews, ChatGPT, Perplexity | Brand mention + sentiment tracking |
| **LLMrefs** | ChatGPT, Perplexity, AI Overviews, Gemini | SEO keyword → AI visibility mapping |

### DIY Monitoring (No Tools)

Monthly manual check:
1. Pick your top 20 queries
2. Run each through ChatGPT, Perplexity, and Google
3. Record: Are you cited? Who is? What page?
4. Log in a spreadsheet, track month-over-month

---

## AI SEO for Different Content Types

### SaaS Product Pages

**Goal:** Get cited in "What is [category]?" and "Best [category]" queries.

**Optimize:**
- Clear product description in first paragraph (what it does, who it's for)
- Feature comparison tables (you vs. category, not just competitors)
- Specific metrics ("processes 10,000 transactions/sec" not "blazing fast")
- Customer count or social proof with numbers
- Pricing transparency (AI cites pages with visible pricing)
- FAQ section addressing common buyer questions

### Blog Content

**Goal:** Get cited as an authoritative source on topics in your space.

**Optimize:**
- One clear target query per post (match heading to query)
- Definition in first paragraph for "What is" queries
- Original data, research, or expert quotes
- "Last updated" date visible
- Author bio with relevant credentials
- Internal links to related product/feature pages

### Comparison/Alternative Pages

**Goal:** Get cited in "[X] vs [Y]" and "Best [X] alternatives" queries.

**Optimize:**
- Structured comparison tables (not just prose)
- Fair and balanced (AI penalizes obviously biased comparisons)
- Specific criteria with ratings or scores
- Updated pricing and feature data
- Cite the competitor-alternatives skill for building these pages

### Documentation / Help Content

**Goal:** Get cited in "How to [X] with [your product]" queries.

**Optimize:**
- Step-by-step format with numbered lists
- Code examples where relevant
- HowTo schema markup
- Screenshots with descriptive alt text
- Clear prerequisites and expected outcomes

---

## Common Mistakes

- **Ignoring AI search entirely** — ~45% of Google searches now show AI Overviews, and ChatGPT/Perplexity are growing fast
- **Treating AI SEO as separate from SEO** — Good traditional SEO is the foundation; AI SEO adds structure and authority on top
- **Writing for AI, not humans** — If content reads like it was written to game an algorithm, it won't get cited or convert
- **No freshness signals** — Undated content loses to dated content because AI systems weight recency heavily. Show when content was last updated
- **Gating all content** — AI can't access gated content. Keep your most authoritative content open
- **Ignoring third-party presence** — You may get more AI citations from a Wikipedia mention than from your own blog
- **No structured data** — Schema markup gives AI systems structured context about your content
- **Keyword stuffing** — Unlike traditional SEO where it's just ineffective, keyword stuffing actively reduces AI visibility by 10% (Princeton GEO study)
- **Blocking AI bots** — If GPTBot, PerplexityBot, or provider-specific AI crawler are blocked in robots.txt, those platforms can't cite you
- **Generic content without data** — "We're the best" won't get cited. "Our customers see 3x improvement in [metric]" will
- **Forgetting to monitor** — You can't improve what you don't measure. Check AI visibility monthly at minimum

---

## Tool Integrations

For implementation, see the [tools registry](../../tools/REGISTRY.md).

| Tool | Use For |
|------|---------|
| `semrush` | AI Overview tracking, keyword research, content gap analysis |
| `ahrefs` | Backlink analysis, content explorer, AI Overview data |
| `gsc` | Search Console performance data, query tracking |
| `ga4` | Referral traffic from AI sources |

---

## Task-Specific Questions

1. What are your top 10-20 most important queries?
2. Have you checked if AI answers exist for those queries today?
3. Do you have structured data (schema markup) on your site?
4. What content types do you publish? (Blog, docs, comparisons, etc.)
5. Are competitors being cited by AI where you're not?
6. Do you have a Wikipedia page or presence on review sites?

---

## Related Skills

- **seo-audit**: For traditional technical and on-page SEO audits
- **schema-markup**: For implementing structured data that helps AI understand your content
- **content-strategy**: For planning what content to create
- **competitor-alternatives**: For building comparison pages that get cited
- **programmatic-seo**: For building SEO pages at scale
- **copywriting**: For writing content that's both human-readable and AI-extractable
