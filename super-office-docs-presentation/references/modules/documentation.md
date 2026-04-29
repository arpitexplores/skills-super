## Source: references/skills/documentation/SKILL.md

---
name: documentation
description: "Documentation generation workflow covering API docs, architecture docs, README files, code comments, and technical writing."
category: workflow-bundle
risk: safe
source: personal
date_added: "2026-02-27"
---

# Documentation Workflow Bundle

## Overview

Comprehensive documentation workflow for generating API documentation, architecture documentation, README files, code comments, and technical content from codebases.

## When to Use This Workflow

Use this workflow when:
- Creating project documentation
- Generating API documentation
- Writing architecture docs
- Documenting code
- Creating user guides
- Maintaining wikis

## Workflow Phases

### Phase 1: Documentation Planning

#### Skills to Invoke
- `docs-architect` - Documentation architecture
- `documentation-templates` - Documentation templates

#### Actions
1. Identify documentation needs
2. Choose documentation tools
3. Plan documentation structure
4. Define style guidelines
5. Set up documentation site

#### Copy-Paste Prompts
```
Use @docs-architect to plan documentation structure
```

```
Use @documentation-templates to set up documentation
```

### Phase 2: API Documentation

#### Skills to Invoke
- `api-documenter` - API documentation
- `api-documentation-generator` - Auto-generation
- `openapi-spec-generation` - OpenAPI specs

#### Actions
1. Extract API endpoints
2. Generate OpenAPI specs
3. Create API reference
4. Add usage examples
5. Set up auto-generation

#### Copy-Paste Prompts
```
Use @api-documenter to generate API documentation
```

```
Use @openapi-spec-generation to create OpenAPI specs
```

### Phase 3: Architecture Documentation

#### Skills to Invoke
- `c4-architecture-c4-architecture` - C4 architecture
- `c4-context` - Context diagrams
- `c4-container` - Container diagrams
- `c4-component` - Component diagrams
- `c4-code` - Code diagrams
- `mermaid-expert` - Mermaid diagrams

#### Actions
1. Create C4 diagrams
2. Document architecture
3. Generate sequence diagrams
4. Document data flows
5. Create deployment docs

#### Copy-Paste Prompts
```
Use @c4-architecture-c4-architecture to create C4 diagrams
```

```
Use @mermaid-expert to create architecture diagrams
```

### Phase 4: Code Documentation

#### Skills to Invoke
- `code-documentation-code-explain` - Code explanation
- `code-documentation-doc-generate` - Doc generation
- `documentation-generation-doc-generate` - Auto-generation

#### Actions
1. Extract code comments
2. Generate JSDoc/TSDoc
3. Create type documentation
4. Document functions
5. Add usage examples

#### Copy-Paste Prompts
```
Use @code-documentation-code-explain to explain code
```

```
Use @code-documentation-doc-generate to generate docs
```

### Phase 5: README and Getting Started

#### Skills to Invoke
- `readme` - README generation
- `environment-setup-guide` - Setup guides
- `tutorial-engineer` - Tutorial creation

#### Actions
1. Create README
2. Write getting started guide
3. Document installation
4. Add usage examples
5. Create troubleshooting guide

#### Copy-Paste Prompts
```
Use @readme to create project README
```

```
Use @tutorial-engineer to create tutorials
```

### Phase 6: Wiki and Knowledge Base

#### Skills to Invoke
- `wiki-architect` - Wiki architecture
- `wiki-page-writer` - Wiki pages
- `wiki-onboarding` - Onboarding docs
- `wiki-qa` - Wiki Q&A
- `wiki-researcher` - Wiki research
- `wiki-vitepress` - VitePress wiki

#### Actions
1. Design wiki structure
2. Create wiki pages
3. Write onboarding guides
4. Document processes
5. Set up wiki site

#### Copy-Paste Prompts
```
Use @wiki-architect to design wiki structure
```

```
Use @wiki-page-writer to create wiki pages
```

```
Use @wiki-onboarding to create onboarding docs
```

### Phase 7: Changelog and Release Notes

#### Skills to Invoke
- `changelog-automation` - Changelog generation
- `wiki-changelog` - Changelog from git

#### Actions
1. Extract commit history
2. Categorize changes
3. Generate changelog
4. Create release notes
5. Publish updates

#### Copy-Paste Prompts
```
Use @changelog-automation to generate changelog
```

```
Use @wiki-changelog to create release notes
```

### Phase 8: Documentation Maintenance

#### Skills to Invoke
- `doc-coauthoring` - Collaborative writing
- `reference-builder` - Reference docs

#### Actions
1. Review documentation
2. Update outdated content
3. Fix broken links
4. Add new features
5. Gather feedback

#### Copy-Paste Prompts
```
Use @doc-coauthoring to collaborate on docs
```

## Documentation Types

### Code-Level
- JSDoc/TSDoc comments
- Function documentation
- Type definitions
- Example code

### API Documentation
- Endpoint reference
- Request/response schemas
- Authentication guides
- SDK documentation

### Architecture Documentation
- System overview
- Component diagrams
- Data flow diagrams
- Deployment architecture

### User Documentation
- Getting started guides
- User manuals
- Tutorials
- FAQs

### Process Documentation
- Runbooks
- Onboarding guides
- SOPs
- Decision records

## Quality Gates

- [ ] All APIs documented
- [ ] Architecture diagrams current
- [ ] README up to date
- [ ] Code comments helpful
- [ ] Examples working
- [ ] Links valid

## Related Workflow Bundles

- `development` - Development workflow
- `testing-qa` - Documentation testing
- `ai-ml` - AI documentation

---

## Merged Reference (legacy variant)

---
name: code-documentation-code-explain
description: "You are a code education expert specializing in explaining complex code through clear narratives, visual diagrams, and step-by-step breakdowns. Transform difficult concepts into understandable expl..."
risk: unknown
source: community
date_added: "2026-02-27"
---

# Code Explanation and Analysis

You are a code education expert specializing in explaining complex code through clear narratives, visual diagrams, and step-by-step breakdowns. Transform difficult concepts into understandable explanations for developers at all levels.

## Use this skill when

- Explaining complex code, algorithms, or system behavior
- Creating onboarding walkthroughs or learning materials
- Producing step-by-step breakdowns with diagrams
- Teaching patterns or debugging reasoning

## Do not use this skill when

- The request is to implement new features or refactors
- You only need API docs or user documentation
- There is no code or design to analyze

## Context
The user needs help understanding complex code sections, algorithms, design patterns, or system architectures. Focus on clarity, visual aids, and progressive disclosure of complexity to facilitate learning and onboarding.

## Requirements
$ARGUMENTS

## Instructions

- Assess structure, dependencies, and complexity hotspots.
- Explain the high-level flow, then drill into key components.
- Use diagrams, pseudocode, or examples when useful.
- Call out pitfalls, edge cases, and key terminology.
- If detailed examples are required, open `resources/implementation-playbook.md`.

## Output Format

- High-level summary of purpose and flow
- Step-by-step walkthrough of key parts
- Diagram or annotated snippet when helpful
- Pitfalls, edge cases, and suggested next steps

## Resources

- `resources/implementation-playbook.md` for detailed examples and templates.

---

## Merged Reference (legacy variant)

---
name: code-documentation-doc-generate
description: "You are a documentation expert specializing in creating comprehensive, maintainable documentation from code. Generate API docs, architecture diagrams, user guides, and technical references using AI..."
risk: unknown
source: community
date_added: "2026-02-27"
---

# Automated Documentation Generation

You are a documentation expert specializing in creating comprehensive, maintainable documentation from code. Generate API docs, architecture diagrams, user guides, and technical references using AI-powered analysis and industry best practices.

## Use this skill when

- Generating API, architecture, or user documentation from code
- Building documentation pipelines or automation
- Standardizing docs across a repository

## Do not use this skill when

- The project has no codebase or source of truth
- You only need ad-hoc explanations
- You cannot access code or requirements

## Context
The user needs automated documentation generation that extracts information from code, creates clear explanations, and maintains consistency across documentation types. Focus on creating living documentation that stays synchronized with code.

## Requirements
$ARGUMENTS

## Instructions

- Identify required doc types and target audiences.
- Extract information from code, configs, and comments.
- Generate docs with consistent terminology and structure.
- Add automation (linting, CI) and validate accuracy.
- If detailed examples are required, open `resources/implementation-playbook.md`.

## Safety

- Avoid exposing secrets, internal URLs, or sensitive data in docs.

## Output Format

- Documentation plan and artifacts to generate
- File paths and tooling configuration
- Assumptions, gaps, and follow-up tasks

## Resources

- `resources/implementation-playbook.md` for detailed examples and templates.

---

## Merged Reference (legacy variant)

---
name: documentation-generation-doc-generate
description: "You are a documentation expert specializing in creating comprehensive, maintainable documentation from code. Generate API docs, architecture diagrams, user guides, and technical references using AI..."
risk: unknown
source: community
date_added: "2026-02-27"
---

# Automated Documentation Generation

You are a documentation expert specializing in creating comprehensive, maintainable documentation from code. Generate API docs, architecture diagrams, user guides, and technical references using AI-powered analysis and industry best practices.

## Use this skill when

- Generating API, architecture, or user documentation from code
- Building documentation pipelines or automation
- Standardizing docs across a repository

## Do not use this skill when

- The project has no codebase or source of truth
- You only need ad-hoc explanations
- You cannot access code or requirements

## Context
The user needs automated documentation generation that extracts information from code, creates clear explanations, and maintains consistency across documentation types. Focus on creating living documentation that stays synchronized with code.

## Requirements
$ARGUMENTS

## Instructions

- Identify required doc types and target audiences.
- Extract information from code, configs, and comments.
- Generate docs with consistent terminology and structure.
- Add automation (linting, CI) and validate accuracy.
- If detailed examples are required, open `resources/implementation-playbook.md`.

## Safety

- Avoid exposing secrets, internal URLs, or sensitive data in docs.

## Output Format

- Documentation plan and artifacts to generate
- File paths and tooling configuration
- Assumptions, gaps, and follow-up tasks

## Resources

- `resources/implementation-playbook.md` for detailed examples and templates.

---

## Merged Reference (legacy variant)

---
name: documentation-templates
description: "Documentation templates and structure guidelines. README, API docs, code comments, and AI-friendly documentation."
risk: unknown
source: community
date_added: "2026-02-27"
---

# Documentation Templates

> Templates and structure guidelines for common documentation types.

---

## 1. README Structure

### Essential Sections (Priority Order)

| Section | Purpose |
|---------|---------|
| **Title + One-liner** | What is this? |
| **Quick Start** | Running in <5 min |
| **Features** | What can I do? |
| **Configuration** | How to customize |
| **API Reference** | Link to detailed docs |
| **Contributing** | How to help |
| **License** | Legal |

### README Template

```markdown
# Project Name

Brief one-line description.

## Quick Start

[Minimum steps to run]

## Features

- Feature 1
- Feature 2

## Configuration

| Variable | Description | Default |
|----------|-------------|---------|
| PORT | Server port | 3000 |

## Documentation

- API Reference
- Architecture

## License

MIT
```

---

## 2. API Documentation Structure

### Per-Endpoint Template

```markdown
## GET /users/:id

Get a user by ID.

**Parameters:**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| id | string | Yes | User ID |

**Response:**
- 200: User object
- 404: User not found

**Example:**
[Request and response example]
```

---

## 3. Code Comment Guidelines

### JSDoc/TSDoc Template

```typescript
/**
 * Brief description of what the function does.
 * 
 * @param paramName - Description of parameter
 * @returns Description of return value
 * @throws ErrorType - When this error occurs
 * 
 * @example
 * const result = functionName(input);
 */
```

### When to Comment

| ✅ Comment | ❌ Don't Comment |
|-----------|-----------------|
| Why (business logic) | What (obvious) |
| Complex algorithms | Every line |
| Non-obvious behavior | Self-explanatory code |
| API contracts | Implementation details |

---

## 4. Changelog Template (Keep a Changelog)

```markdown
# Changelog

## [Unreleased]
### Added
- New feature

## [1.0.0] - 2025-01-01
### Added
- Initial release
### Changed
- Updated dependency
### Fixed
- Bug fix
```

---

## 5. Architecture Decision Record (ADR)

```markdown
# ADR-001: [Title]

## Status
Accepted / Deprecated / Superseded

## Context
Why are we making this decision?

## Decision
What did we decide?

## Consequences
What are the trade-offs?
```

---

## 6. AI-Friendly Documentation (2025)

### llms.txt Template

For AI crawlers and agents:

```markdown
# Project Name
> One-line objective.

## Core Files
- [src/index.ts]: Main entry
- [src/api/]: API routes
- [docs/]: Documentation

## Key Concepts
- Concept 1: Brief explanation
- Concept 2: Brief explanation
```

### MCP-Ready Documentation

For RAG indexing:
- Clear H1-H3 hierarchy
- JSON/YAML examples for data structures
- Mermaid diagrams for flows
- Self-contained sections

---

## 7. Structure Principles

| Principle | Why |
|-----------|-----|
| **Scannable** | Headers, lists, tables |
| **Examples first** | Show, don't just tell |
| **Progressive detail** | Simple → Complex |
| **Up to date** | Outdated = misleading |

---

> **Remember:** Templates are starting points. Adapt to your project's needs.

## When to Use
This skill is applicable to execute the workflow or actions described in the overview.

---

## Merged Reference (legacy variant)

---
name: readme
description: "When the user wants to create or update a README.md file for a project. Also use when the user says 'write readme,' 'create readme,' 'document this project,' 'project documentation,' or asks for he..."
risk: safe
source: "https://github.com/Shpigford/skills/tree/main/readme"
date_added: "2026-02-27"
---

# README Generator

You are an expert technical writer creating comprehensive project documentation. Your goal is to write a README.md that is absurdly thorough—the kind of documentation you wish every project had.

## When to Use This Skill

Use this skill when:

- User wants to create or update a README.md file
- User says "write readme" or "create readme"
- User asks to "document this project"
- User requests "project documentation"
- User asks for help with README.md

## The Three Purposes of a README

1. **Local Development** - Help any developer get the app running locally in minutes
2. **Understanding the System** - Explain in great detail how the app works
3. **Production Deployment** - Cover everything needed to deploy and maintain in production

---

## Before Writing

### Step 1: Deep Codebase Exploration

Before writing a single line of documentation, thoroughly explore the codebase. You MUST understand:

**Project Structure**

- Read the root directory structure
- Identify the framework/language (Gemfile for Rails, package.json, go.mod, requirements.txt, etc.)
- Find the main entry point(s)
- Map out the directory organization

**Configuration Files**

- .env.example, .env.sample, or documented environment variables
- Rails config files (config/database.yml, config/application.rb, config/environments/)
- Credentials setup (config/credentials.yml.enc, config/master.key)
- Docker files (Dockerfile, docker-compose.yml)
- CI/CD configs (.github/workflows/, .gitlab-ci.yml, etc.)
- Deployment configs (config/deploy.yml for Kamal, fly.toml, render.yaml, Procfile, etc.)

**Database**

- db/schema.rb or db/structure.sql
- Migrations in db/migrate/
- Seeds in db/seeds.rb
- Database type from config/database.yml

**Key Dependencies**

- Gemfile and Gemfile.lock for Ruby gems
- package.json for JavaScript dependencies
- Note any native gem dependencies (pg, nokogiri, etc.)

**Scripts and Commands**

- bin/ scripts (bin/dev, bin/setup, bin/ci)
- Procfile or Procfile.dev
- Rake tasks (lib/tasks/)

### Step 2: Identify Deployment Target

Look for these files to determine deployment platform and tailor instructions:

- `Dockerfile` / `docker-compose.yml` → Docker-based deployment
- `vercel.json` / `.vercel/` → Vercel
- `netlify.toml` → Netlify
- `fly.toml` → Fly.io
- `railway.json` / `railway.toml` → Railway
- `render.yaml` → Render
- `app.yaml` → Google App Engine
- `Procfile` → Heroku or Heroku-like platforms
- `.ebextensions/` → AWS Elastic Beanstalk
- `serverless.yml` → Serverless Framework
- `terraform/` / `*.tf` → Terraform/Infrastructure as Code
- `k8s/` / `kubernetes/` → Kubernetes

If no deployment config exists, provide general guidance with Docker as the recommended approach.

### Step 3: Ask Only If Critical

Only ask the user questions if you cannot determine:

- What the project does (if not obvious from code)
- Specific deployment credentials or URLs needed
- Business context that affects documentation

Otherwise, proceed with exploration and writing.

---

## README Structure

Write the README with these sections in order:

### 1. Project Title and Overview

```markdown
# Project Name

Brief description of what the project does and who it's for. 2-3 sentences max.

## Key Features

- Feature 1
- Feature 2
- Feature 3
```

### 2. Tech Stack

List all major technologies:

```markdown
## Tech Stack

- **Language**: Ruby 3.3+
- **Framework**: Rails 7.2+
- **Frontend**: Inertia.js with React
- **Database**: PostgreSQL 16
- **Background Jobs**: Solid Queue
- **Caching**: Solid Cache
- **Styling**: Tailwind CSS
- **Deployment**: [Detected platform]
```

### 3. Prerequisites

What must be installed before starting:

```markdown
## Prerequisites

- Node.js 20 or higher
- PostgreSQL 15 or higher (or Docker)
- pnpm (recommended) or npm
- A Google Cloud project for OAuth (optional for development)
```

### 4. Getting Started

The complete local development guide:

```markdown
## Getting Started

### 1. Clone the Repository

\`\`\`bash
git clone https://github.com/user/repo.git
cd repo
\`\`\`

### 2. Install Ruby Dependencies

Ensure you have Ruby 3.3+ installed (via rbenv, asdf, or mise):

\`\`\`bash
bundle install
\`\`\`

### 3. Install JavaScript Dependencies

\`\`\`bash
yarn install
\`\`\`

### 4. Environment Setup

Copy the example environment file:

\`\`\`bash
cp .env.example .env
\`\`\`

Configure the following variables:

| Variable           | Description                  | Example                                    |
| ------------------ | ---------------------------- | ------------------------------------------ |
| `DATABASE_URL`     | PostgreSQL connection string | `postgresql://localhost/myapp_development` |
| `REDIS_URL`        | Redis connection (if used)   | `redis://localhost:6379/0`                 |
| `SECRET_KEY_BASE`  | Rails secret key             | `bin/rails secret`                         |
| `RAILS_MASTER_KEY` | For credentials encryption   | Check `config/master.key`                  |

### 5. Database Setup

Start PostgreSQL (if using Docker):

\`\`\`bash
docker run --name postgres -e POSTGRES_PASSWORD=postgres -p 5432:5432 -d postgres:16
\`\`\`

Create and set up the database:

\`\`\`bash
bin/rails db:setup
\`\`\`

This runs `db:create`, `db:schema:load`, and `db:seed`.

For existing databases, run migrations:

\`\`\`bash
bin/rails db:migrate
\`\`\`

### 6. Start Development Server

Using Foreman/Overmind (recommended, runs Rails + Vite):

\`\`\`bash
bin/dev
\`\`\`

Or manually:

\`\`\`bash

# Terminal 1: Rails server

bin/rails server

# Terminal 2: Vite dev server (for Inertia/React)

bin/vite dev
\`\`\`

Open [http://localhost:3000](http://localhost:3000) in your browser.
```

Include every step. Assume the reader is setting up on a fresh machine.

### 5. Architecture Overview

This is where you go absurdly deep:

```markdown
## Architecture

### Directory Structure

\`\`\`
├── app/
│ ├── controllers/ # Rails controllers
│ │ ├── concerns/ # Shared controller modules
│ │ └── api/ # API-specific controllers
│ ├── models/ # ActiveRecord models
│ │ └── concerns/ # Shared model modules
│ ├── jobs/ # Background jobs (Solid Queue)
│ ├── mailers/ # Email templates
│ ├── views/ # Rails views (minimal with Inertia)
│ └── frontend/ # Inertia.js React components
│ ├── components/ # Reusable UI components
│ ├── layouts/ # Page layouts
│ ├── pages/ # Inertia page components
│ └── lib/ # Frontend utilities
├── config/
│ ├── routes.rb # Route definitions
│ ├── database.yml # Database configuration
│ └── initializers/ # App initializers
├── db/
│ ├── migrate/ # Database migrations
│ ├── schema.rb # Current schema
│ └── seeds.rb # Seed data
├── lib/
│ └── tasks/ # Custom Rake tasks
└── public/ # Static assets
\`\`\`

### Request Lifecycle

1. Request hits Rails router (`config/routes.rb`)
2. Middleware stack processes request (authentication, sessions, etc.)
3. Controller action executes
4. Models interact with PostgreSQL via ActiveRecord
5. Inertia renders React component with props
6. Response sent to browser

### Data Flow

\`\`\`
User Action → React Component → Inertia Visit → Rails Controller → ActiveRecord → PostgreSQL
↓
React Props ← Inertia Response ←
\`\`\`

### Key Components

**Authentication**

- Devise/Rodauth for user authentication
- Session-based auth with encrypted cookies
- `authenticate_user!` before_action for protected routes

**Inertia.js Integration (`app/frontend/`)**

- React components receive props from Rails controllers
- `inertia_render` in controllers passes data to frontend
- Shared data via `inertia_share` for layout props

**Background Jobs (`app/jobs/`)**

- Solid Queue for job processing
- Jobs stored in PostgreSQL (no Redis required)
- Dashboard at `/jobs` for monitoring

**Database (`app/models/`)**

- ActiveRecord models with associations
- Query objects for complex queries
- Concerns for shared model behavior

### Database Schema

\`\`\`
users
├── id (bigint, PK)
├── email (string, unique, not null)
├── encrypted_password (string)
├── name (string)
├── created_at (datetime)
└── updated_at (datetime)

posts
├── id (bigint, PK)
├── title (string, not null)
├── content (text)
├── published (boolean, default: false)
├── user_id (bigint, FK → users)
├── created_at (datetime)
└── updated_at (datetime)

solid_queue_jobs (background jobs)
├── id (bigint, PK)
├── queue_name (string)
├── class_name (string)
├── arguments (json)
├── scheduled_at (datetime)
└── ...
\`\`\`
```

### 6. Environment Variables

Complete reference for all env vars:

```markdown
## Environment Variables

### Required

| Variable           | Description                       | How to Get                             |
| ------------------ | --------------------------------- | -------------------------------------- |
| `DATABASE_URL`     | PostgreSQL connection string      | Your database provider                 |
| `SECRET_KEY_BASE`  | Rails secret for sessions/cookies | Run `bin/rails secret`                 |
| `RAILS_MASTER_KEY` | Decrypts credentials file         | Check `config/master.key` (not in git) |

### Optional

| Variable            | Description                                       | Default                      |
| ------------------- | ------------------------------------------------- | ---------------------------- |
| `REDIS_URL`         | Redis connection string (for caching/ActionCable) | -                            |
| `RAILS_LOG_LEVEL`   | Logging verbosity                                 | `debug` (dev), `info` (prod) |
| `RAILS_MAX_THREADS` | Puma thread count                                 | `5`                          |
| `WEB_CONCURRENCY`   | Puma worker count                                 | `2`                          |
| `SMTP_ADDRESS`      | Mail server hostname                              | -                            |
| `SMTP_PORT`         | Mail server port                                  | `587`                        |

### Rails Credentials

Sensitive values should be stored in Rails encrypted credentials:

\`\`\`bash

# Edit credentials (opens in $EDITOR)

bin/rails credentials:edit

# Or for environment-specific credentials

RAILS_ENV=production bin/rails credentials:edit
\`\`\`

Credentials file structure:
\`\`\`yaml
secret_key_base: xxx
stripe:
public_key: pk_xxx
secret_key: sk_xxx
google:
client_id: xxx
client_secret: xxx
\`\`\`

Access in code: `Rails.application.credentials.stripe[:secret_key]`

### Environment-Specific

**Development**
\`\`\`
DATABASE_URL=postgresql://localhost/myapp_development
REDIS_URL=redis://localhost:6379/0
\`\`\`

**Production**
\`\`\`
DATABASE_URL=<production-connection-string>
RAILS_ENV=production
RAILS_SERVE_STATIC_FILES=true
\`\`\`
```

### 7. Available Scripts

```markdown
## Available Scripts

| Command                       | Description                                         |
| ----------------------------- | --------------------------------------------------- |
| `bin/dev`                     | Start development server (Rails + Vite via Foreman) |
| `bin/rails server`            | Start Rails server only                             |
| `bin/vite dev`                | Start Vite dev server only                          |
| `bin/rails console`           | Open Rails console (IRB with app loaded)            |
| `bin/rails db:migrate`        | Run pending database migrations                     |
| `bin/rails db:rollback`       | Rollback last migration                             |
| `bin/rails db:seed`           | Run database seeds                                  |
| `bin/rails db:reset`          | Drop, create, migrate, and seed database            |
| `bin/rails routes`            | List all routes                                     |
| `bin/rails test`              | Run test suite (Minitest)                           |
| `bundle exec rspec`           | Run test suite (RSpec, if used)                     |
| `bin/rails assets:precompile` | Compile assets for production                       |
| `bin/rubocop`                 | Run Ruby linter                                     |
| `yarn lint`                   | Run JavaScript/TypeScript linter                    |
```

### 8. Testing

```markdown
## Testing

### Running Tests

\`\`\`bash

# Run all tests (Minitest)

bin/rails test

# Run all tests (RSpec, if used)

bundle exec rspec

# Run specific test file

bin/rails test test/models/user_test.rb
bundle exec rspec spec/models/user_spec.rb

# Run tests matching a pattern

bin/rails test -n /creates_user/
bundle exec rspec -e "creates user"

# Run system tests (browser tests)

bin/rails test:system

# Run with coverage (SimpleCov)

COVERAGE=true bin/rails test
\`\`\`

### Test Structure

\`\`\`
test/ # Minitest structure
├── controllers/ # Controller tests
├── models/ # Model unit tests
├── integration/ # Integration tests
├── system/ # System/browser tests
├── fixtures/ # Test data
└── test_helper.rb # Test configuration

spec/ # RSpec structure (if used)
├── models/
├── requests/
├── system/
├── factories/ # FactoryBot factories
├── support/
└── rails_helper.rb
\`\`\`

### Writing Tests

**Minitest example:**
\`\`\`ruby
require "test_helper"

class UserTest < ActiveSupport::TestCase
test "creates user with valid attributes" do
user = User.new(email: "test@example.com", name: "Test User")
assert user.valid?
end

test "requires email" do
user = User.new(name: "Test User")
assert_not user.valid?
assert_includes user.errors[:email], "can't be blank"
end
end
\`\`\`

**RSpec example:**
\`\`\`ruby
require "rails_helper"

RSpec.describe User, type: :model do
describe "validations" do
it "is valid with valid attributes" do
user = build(:user)
expect(user).to be_valid
end

    it "requires an email" do
      user = build(:user, email: nil)
      expect(user).not_to be_valid
      expect(user.errors[:email]).to include("can't be blank")
    end

end
end
\`\`\`

### Frontend Testing

For Inertia/React components:

\`\`\`bash
yarn test
\`\`\`

\`\`\`typescript
import { render, screen } from '@testing-library/react'
import { Dashboard } from './Dashboard'

describe('Dashboard', () => {
it('renders user name', () => {
render(<Dashboard user={{ name: 'Josh' }} />)
expect(screen.getByText('Josh')).toBeInTheDocument()
})
})
\`\`\`
```

### 9. Deployment

Tailor this to detected platform (look for Dockerfile, fly.toml, render.yaml, kamal/, etc.):

```markdown
## Deployment

### Kamal (Recommended for Rails)

If using Kamal for deployment:

\`\`\`bash

# Setup Kamal (first time)

kamal setup

# Deploy

kamal deploy

# Rollback to previous version

kamal rollback

# View logs

kamal app logs

# Run console on production

kamal app exec --interactive 'bin/rails console'
\`\`\`

Configuration lives in `config/deploy.yml`.

### Docker

Build and run:

\`\`\`bash

# Build image

docker build -t myapp .

# Run with environment variables

docker run -p 3000:3000 \
 -e DATABASE_URL=postgresql://... \
 -e SECRET_KEY_BASE=... \
 -e RAILS_ENV=production \
 myapp
\`\`\`

### Heroku

\`\`\`bash

# Create app

heroku create myapp

# Add PostgreSQL

heroku addons:create heroku-postgresql:mini

# Set environment variables

heroku config:set SECRET_KEY_BASE=$(bin/rails secret)
heroku config:set RAILS_MASTER_KEY=$(cat config/master.key)

# Deploy

git push heroku main

# Run migrations

heroku run bin/rails db:migrate
\`\`\`

### Fly.io

\`\`\`bash

# Launch (first time)

fly launch

# Deploy

fly deploy

# Run migrations

fly ssh console -C "bin/rails db:migrate"

# Open console

fly ssh console -C "bin/rails console"
\`\`\`

### Render

If `render.yaml` exists, connect your repo to Render and it will auto-deploy.

Manual setup:

1. Create new Web Service
2. Connect GitHub repository
3. Set build command: `bundle install && bin/rails assets:precompile`
4. Set start command: `bin/rails server`
5. Add environment variables in dashboard

### Manual/VPS Deployment

\`\`\`bash

# On the server:

# Pull latest code

git pull origin main

# Install dependencies

bundle install --deployment

# Compile assets

RAILS_ENV=production bin/rails assets:precompile

# Run migrations

RAILS_ENV=production bin/rails db:migrate

# Restart application server (e.g., Puma via systemd)

sudo systemctl restart myapp
\`\`\`
```

### 10. Troubleshooting

```markdown
## Troubleshooting

### Database Connection Issues

**Error:** `could not connect to server: Connection refused`

**Solution:**

1. Verify PostgreSQL is running: `pg_isready` or `docker ps`
2. Check `DATABASE_URL` format: `postgresql://USER:PASSWORD@HOST:PORT/DATABASE`
3. Ensure database exists: `bin/rails db:create`

### Pending Migrations

**Error:** `Migrations are pending`

**Solution:**
\`\`\`bash
bin/rails db:migrate
\`\`\`

### Asset Compilation Issues

**Error:** `The asset "application.css" is not present in the asset pipeline`

**Solution:**
\`\`\`bash

# Clear and recompile assets

bin/rails assets:clobber
bin/rails assets:precompile
\`\`\`

### Bundle Install Failures

**Error:** Native extension build failures

**Solution:**

1. Ensure system dependencies are installed:
   \`\`\`bash

   # macOS

   brew install postgresql libpq

   # Ubuntu

   sudo apt-get install libpq-dev
   \`\`\`

2. Try again: `bundle install`

### Credentials Issues

**Error:** `ActiveSupport::MessageEncryptor::InvalidMessage`

**Solution:**
The master key doesn't match the credentials file. Either:

1. Get the correct `config/master.key` from another team member
2. Or regenerate credentials: `rm config/credentials.yml.enc && bin/rails credentials:edit`

### Vite/Inertia Issues

**Error:** `Vite Ruby - Build failed`

**Solution:**
\`\`\`bash

# Clear Vite cache

rm -rf node_modules/.vite

# Reinstall JS dependencies

rm -rf node_modules && yarn install
\`\`\`

### Solid Queue Issues

**Error:** Jobs not processing

**Solution:**
Ensure the queue worker is running:
\`\`\`bash
bin/jobs

# or

bin/rails solid_queue:start
\`\`\`
```

### 11. Contributing (Optional)

Include if open source or team project.

### 12. License (Optional)

---

## Writing Principles

1. **Be Absurdly Thorough** - When in doubt, include it. More detail is always better.

2. **Use Code Blocks Liberally** - Every command should be copy-pasteable.

3. **Show Example Output** - When helpful, show what the user should expect to see.

4. **Explain the Why** - Don't just say "run this command," explain what it does.

5. **Assume Fresh Machine** - Write as if the reader has never seen this codebase.

6. **Use Tables for Reference** - Environment variables, scripts, and options work great as tables.

7. **Keep Commands Current** - Use `pnpm` if the project uses it, `npm` if it uses npm, etc.

8. **Include a Table of Contents** - For READMEs over ~200 lines, add a TOC at the top.

---

## Output Format

Generate a complete README.md file with:

- Proper markdown formatting
- Code blocks with language hints (`bash, `typescript, etc.)
- Tables where appropriate
- Clear section hierarchy
- Linked table of contents for long documents

Write the README directly to `README.md` in the project root.

---

## Merged Reference (legacy variant)

---
name: wiki-changelog
description: "Analyzes git commit history and generates structured changelogs categorized by change type. Use when the user asks about recent changes, wants a changelog, or needs to understand what changed in th..."
risk: unknown
source: community
date_added: "2026-02-27"
---

# Wiki Changelog

Generate structured changelogs from git history.

## When to Activate

- User asks "what changed recently", "generate a changelog", "summarize commits"
- User wants to understand recent development activity

## Procedure

1. Examine git log (commits, dates, authors, messages)
2. Group by time period: daily (last 7 days), weekly (older)
3. Classify each commit: Features (🆕), Fixes (🐛), Refactoring (🔄), Docs (📝), Config (🔧), Dependencies (📦), Breaking (⚠️)
4. Generate concise user-facing descriptions using project terminology

## Constraints

- Focus on user-facing changes
- Merge related commits into coherent descriptions
- Use project terminology from README
- Highlight breaking changes prominently with migration notes

## When to Use
This skill is applicable to execute the workflow or actions described in the overview.

---

## Merged Reference (legacy variant)

---
name: wiki-page-writer
description: "Generates rich technical documentation pages with dark-mode Mermaid diagrams, source code citations, and first-principles depth. Use when writing documentation, generating wiki pages, creating tech..."
risk: unknown
source: community
date_added: "2026-02-27"
---

# Wiki Page Writer

You are a senior documentation engineer that generates comprehensive technical documentation pages with evidence-based depth.

## When to Activate

- User asks to document a specific component, system, or feature
- User wants a technical deep-dive with diagrams
- A wiki catalogue section needs its content generated

## Depth Requirements (NON-NEGOTIABLE)

1. **TRACE ACTUAL CODE PATHS** — Do not guess from file names. Read the implementation.
2. **EVERY CLAIM NEEDS A SOURCE** — File path + function/class name.
3. **DISTINGUISH FACT FROM INFERENCE** — If you read the code, say so. If inferring, mark it.
4. **FIRST PRINCIPLES** — Explain WHY something exists before WHAT it does.
5. **NO HAND-WAVING** — Don't say "this likely handles..." — read the code.

## Procedure

1. **Plan**: Determine scope, audience, and documentation budget based on file count
2. **Analyze**: Read all relevant files; identify patterns, algorithms, dependencies, data flow
3. **Write**: Generate structured Markdown with diagrams and citations
4. **Validate**: Verify file paths exist, class names are accurate, Mermaid renders correctly

## Mandatory Requirements

### VitePress Frontmatter
Every page must have:
```
---
title: "Page Title"
description: "One-line description"
---
```

### Mermaid Diagrams
- **Minimum 2 per page**
- Use `autonumber` in all `sequenceDiagram` blocks
- Choose appropriate types: `graph`, `sequenceDiagram`, `classDiagram`, `stateDiagram-v2`, `erDiagram`, `flowchart`
- **Dark-mode colors (MANDATORY)**: node fills `#2d333b`, borders `#6d5dfc`, text `#e6edf3`
- Subgraph backgrounds: `#161b22`, borders `#30363d`, lines `#8b949e`
- If using inline `style`, use dark fills with `,color:#e6edf3`
- Do NOT use `<br/>` (use `<br>` or line breaks)

### Citations
- Every non-trivial claim needs `(file_path:line_number)`
- Minimum 5 different source files cited per page
- If evidence is missing: `(Unknown – verify in path/to/check)`

### Structure
- Overview (explain WHY) → Architecture → Components → Data Flow → Implementation → References
- Use Markdown tables for APIs, configs, and component summaries
- Use comparison tables when introducing technologies
- Include pseudocode in a familiar language when explaining complex code paths

### VitePress Compatibility
- Escape bare generics outside code fences: `` `List<T>` `` not bare `List<T>`
- No `<br/>` in Mermaid blocks
- All hex colors must be 3 or 6 digits

## When to Use
This skill is applicable to execute the workflow or actions described in the overview.

---

## Merged Reference (legacy variant)

---
name: wiki-qa
description: "Answers questions about a code repository using source file analysis. Use when the user asks a question about how something works, wants to understand a component, or needs help navigating the code..."
risk: unknown
source: community
date_added: "2026-02-27"
---

# Wiki Q&A

Answer repository questions grounded entirely in source code evidence.

## When to Activate

- User asks a question about the codebase
- User wants to understand a specific file, function, or component
- User asks "how does X work" or "where is Y defined"

## Procedure

1. Detect the language of the question; respond in the same language
2. Search the codebase for relevant files
3. Read those files to gather evidence
4. Synthesize an answer with inline citations

## Response Format

- Use `##` headings, code blocks with language tags, tables, bullet lists
- Cite sources inline: `(src/path/file.ts:42)`
- Include a "Key Files" table mapping files to their roles
- If information is insufficient, say so and suggest files to examine

## Rules

- ONLY use information from actual source files
- NEVER invent, guess, or use external knowledge
- Think step by step before answering

## When to Use
This skill is applicable to execute the workflow or actions described in the overview.

---

## Merged Reference (legacy variant)

---
name: wiki-vitepress
description: "Packages generated wiki Markdown into a VitePress static site with dark theme, dark-mode Mermaid diagrams with click-to-zoom, and production build output. Use when the user wants to create a browsa..."
risk: unknown
source: community
date_added: "2026-02-27"
---

# Wiki VitePress Packager

Transform generated wiki Markdown files into a polished VitePress static site with dark theme and interactive Mermaid diagrams.

## When to Activate

- User asks to "build a site" or "package as VitePress"
- User runs the `/deep-wiki:build` command
- User wants a browsable HTML output from generated wiki pages

## VitePress Scaffolding

Generate the following structure in a `wiki-site/` directory:

```
wiki-site/
├── .vitepress/
│   ├── config.mts
│   └── theme/
│       ├── index.ts
│       └── custom.css
├── public/
├── [generated .md pages]
├── package.json
└── index.md
```

## Config Requirements (`config.mts`)

- Use `withMermaid` wrapper from `vitepress-plugin-mermaid`
- Set `appearance: 'dark'` for dark-only theme
- Configure `themeConfig.nav` and `themeConfig.sidebar` from the catalogue structure
- Mermaid config must set dark theme variables:

```typescript
mermaid: {
  theme: 'dark',
  themeVariables: {
    primaryColor: '#1e3a5f',
    primaryTextColor: '#e0e0e0',
    primaryBorderColor: '#4a9eed',
    lineColor: '#4a9eed',
    secondaryColor: '#2d4a3e',
    tertiaryColor: '#2d2d3d',
    background: '#1a1a2e',
    mainBkg: '#1e3a5f',
    nodeBorder: '#4a9eed',
    clusterBkg: '#16213e',
    titleColor: '#e0e0e0',
    edgeLabelBackground: '#1a1a2e'
  }
}
```

## Dark-Mode Mermaid: Three-Layer Fix

### Layer 1: Theme Variables (in config.mts)
Set via `mermaid.themeVariables` as shown above.

### Layer 2: CSS Overrides (`custom.css`)
Target Mermaid SVG elements with `!important`:

```css
.mermaid .node rect,
.mermaid .node circle,
.mermaid .node polygon { fill: #1e3a5f !important; stroke: #4a9eed !important; }
.mermaid .edgeLabel { background-color: #1a1a2e !important; color: #e0e0e0 !important; }
.mermaid text { fill: #e0e0e0 !important; }
.mermaid .label { color: #e0e0e0 !important; }
```

### Layer 3: Inline Style Replacement (`theme/index.ts`)
Mermaid inline `style` attributes override everything. Use `onMounted` + polling to replace them:

```typescript
import { onMounted } from 'vue'

// In setup()
onMounted(() => {
  let attempts = 0
  const fix = setInterval(() => {
    document.querySelectorAll('.mermaid svg [style]').forEach(el => {
      const s = (el as HTMLElement).style
      if (s.fill && !s.fill.includes('#1e3a5f')) s.fill = '#1e3a5f'
      if (s.stroke && !s.stroke.includes('#4a9eed')) s.stroke = '#4a9eed'
      if (s.color) s.color = '#e0e0e0'
    })
    if (++attempts >= 20) clearInterval(fix)
  }, 500)
})
```

Use `setup()` with `onMounted`, NOT `enhanceApp()` — DOM doesn't exist during SSR.

## Click-to-Zoom for Mermaid Diagrams

Wrap each `.mermaid` container in a clickable wrapper that opens a fullscreen modal:

```typescript
document.querySelectorAll('.mermaid').forEach(el => {
  el.style.cursor = 'zoom-in'
  el.addEventListener('click', () => {
    const modal = document.createElement('div')
    modal.className = 'mermaid-zoom-modal'
    modal.innerHTML = el.outerHTML
    modal.addEventListener('click', () => modal.remove())
    document.body.appendChild(modal)
  })
})
```

Modal CSS:
```css
.mermaid-zoom-modal {
  position: fixed; inset: 0;
  background: rgba(0,0,0,0.9);
  display: flex; align-items: center; justify-content: center;
  z-index: 9999; cursor: zoom-out;
}
.mermaid-zoom-modal .mermaid { transform: scale(1.5); }
```

## Post-Processing Rules

Before VitePress build, scan all `.md` files and fix:
- Replace `<br/>` with `<br>` (Vue template compiler compatibility)
- Wrap bare `<T>` generic parameters in backticks outside code fences
- Ensure every page has YAML frontmatter with `title` and `description`

## Build

```bash
cd wiki-site && npm install && npm run docs:build
```

Output goes to `wiki-site/.vitepress/dist/`.

## Known Gotchas

- Mermaid renders async — SVGs don't exist when `onMounted` fires. Must poll.
- `isCustomElement` compiler option for bare `<T>` causes worse crashes — do NOT use it
- Node text in Mermaid uses inline `style` with highest specificity — CSS alone won't fix it
- `enhanceApp()` runs during SSR where `document` doesn't exist — use `setup()` only

## When to Use
This skill is applicable to execute the workflow or actions described in the overview.

## Source: references/skills/documentation/references/legacy/code-documentation-code-explain/SKILL.md

---
name: code-documentation-code-explain
description: "You are a code education expert specializing in explaining complex code through clear narratives, visual diagrams, and step-by-step breakdowns. Transform difficult concepts into understandable expl..."
risk: unknown
source: community
date_added: "2026-02-27"
---

# Code Explanation and Analysis

You are a code education expert specializing in explaining complex code through clear narratives, visual diagrams, and step-by-step breakdowns. Transform difficult concepts into understandable explanations for developers at all levels.

## Use this skill when

- Explaining complex code, algorithms, or system behavior
- Creating onboarding walkthroughs or learning materials
- Producing step-by-step breakdowns with diagrams
- Teaching patterns or debugging reasoning

## Do not use this skill when

- The request is to implement new features or refactors
- You only need API docs or user documentation
- There is no code or design to analyze

## Context
The user needs help understanding complex code sections, algorithms, design patterns, or system architectures. Focus on clarity, visual aids, and progressive disclosure of complexity to facilitate learning and onboarding.

## Requirements
$ARGUMENTS

## Instructions

- Assess structure, dependencies, and complexity hotspots.
- Explain the high-level flow, then drill into key components.
- Use diagrams, pseudocode, or examples when useful.
- Call out pitfalls, edge cases, and key terminology.
- If detailed examples are required, open `resources/implementation-playbook.md`.

## Output Format

- High-level summary of purpose and flow
- Step-by-step walkthrough of key parts
- Diagram or annotated snippet when helpful
- Pitfalls, edge cases, and suggested next steps

## Resources

- `resources/implementation-playbook.md` for detailed examples and templates.

## Source: references/skills/documentation/references/legacy/code-documentation-doc-generate/SKILL.md

---
name: code-documentation-doc-generate
description: "You are a documentation expert specializing in creating comprehensive, maintainable documentation from code. Generate API docs, architecture diagrams, user guides, and technical references using AI..."
risk: unknown
source: community
date_added: "2026-02-27"
---

# Automated Documentation Generation

You are a documentation expert specializing in creating comprehensive, maintainable documentation from code. Generate API docs, architecture diagrams, user guides, and technical references using AI-powered analysis and industry best practices.

## Use this skill when

- Generating API, architecture, or user documentation from code
- Building documentation pipelines or automation
- Standardizing docs across a repository

## Do not use this skill when

- The project has no codebase or source of truth
- You only need ad-hoc explanations
- You cannot access code or requirements

## Context
The user needs automated documentation generation that extracts information from code, creates clear explanations, and maintains consistency across documentation types. Focus on creating living documentation that stays synchronized with code.

## Requirements
$ARGUMENTS

## Instructions

- Identify required doc types and target audiences.
- Extract information from code, configs, and comments.
- Generate docs with consistent terminology and structure.
- Add automation (linting, CI) and validate accuracy.
- If detailed examples are required, open `resources/implementation-playbook.md`.

## Safety

- Avoid exposing secrets, internal URLs, or sensitive data in docs.

## Output Format

- Documentation plan and artifacts to generate
- File paths and tooling configuration
- Assumptions, gaps, and follow-up tasks

## Resources

- `resources/implementation-playbook.md` for detailed examples and templates.

## Source: references/skills/documentation/references/legacy/documentation-generation-doc-generate/SKILL.md

---
name: documentation-generation-doc-generate
description: "You are a documentation expert specializing in creating comprehensive, maintainable documentation from code. Generate API docs, architecture diagrams, user guides, and technical references using AI..."
risk: unknown
source: community
date_added: "2026-02-27"
---

# Automated Documentation Generation

You are a documentation expert specializing in creating comprehensive, maintainable documentation from code. Generate API docs, architecture diagrams, user guides, and technical references using AI-powered analysis and industry best practices.

## Use this skill when

- Generating API, architecture, or user documentation from code
- Building documentation pipelines or automation
- Standardizing docs across a repository

## Do not use this skill when

- The project has no codebase or source of truth
- You only need ad-hoc explanations
- You cannot access code or requirements

## Context
The user needs automated documentation generation that extracts information from code, creates clear explanations, and maintains consistency across documentation types. Focus on creating living documentation that stays synchronized with code.

## Requirements
$ARGUMENTS

## Instructions

- Identify required doc types and target audiences.
- Extract information from code, configs, and comments.
- Generate docs with consistent terminology and structure.
- Add automation (linting, CI) and validate accuracy.
- If detailed examples are required, open `resources/implementation-playbook.md`.

## Safety

- Avoid exposing secrets, internal URLs, or sensitive data in docs.

## Output Format

- Documentation plan and artifacts to generate
- File paths and tooling configuration
- Assumptions, gaps, and follow-up tasks

## Resources

- `resources/implementation-playbook.md` for detailed examples and templates.

## Source: references/skills/documentation/references/legacy/documentation-templates/SKILL.md

---
name: documentation-templates
description: "Documentation templates and structure guidelines. README, API docs, code comments, and AI-friendly documentation."
risk: unknown
source: community
date_added: "2026-02-27"
---

# Documentation Templates

> Templates and structure guidelines for common documentation types.

---

## 1. README Structure

### Essential Sections (Priority Order)

| Section | Purpose |
|---------|---------|
| **Title + One-liner** | What is this? |
| **Quick Start** | Running in <5 min |
| **Features** | What can I do? |
| **Configuration** | How to customize |
| **API Reference** | Link to detailed docs |
| **Contributing** | How to help |
| **License** | Legal |

### README Template

```markdown
# Project Name

Brief one-line description.

## Quick Start

[Minimum steps to run]

## Features

- Feature 1
- Feature 2

## Configuration

| Variable | Description | Default |
|----------|-------------|---------|
| PORT | Server port | 3000 |

## Documentation

- API Reference
- Architecture

## License

MIT
```

---

## 2. API Documentation Structure

### Per-Endpoint Template

```markdown
## GET /users/:id

Get a user by ID.

**Parameters:**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| id | string | Yes | User ID |

**Response:**
- 200: User object
- 404: User not found

**Example:**
[Request and response example]
```

---

## 3. Code Comment Guidelines

### JSDoc/TSDoc Template

```typescript
/**
 * Brief description of what the function does.
 * 
 * @param paramName - Description of parameter
 * @returns Description of return value
 * @throws ErrorType - When this error occurs
 * 
 * @example
 * const result = functionName(input);
 */
```

### When to Comment

| ✅ Comment | ❌ Don't Comment |
|-----------|-----------------|
| Why (business logic) | What (obvious) |
| Complex algorithms | Every line |
| Non-obvious behavior | Self-explanatory code |
| API contracts | Implementation details |

---

## 4. Changelog Template (Keep a Changelog)

```markdown
# Changelog

## [Unreleased]
### Added
- New feature

## [1.0.0] - 2025-01-01
### Added
- Initial release
### Changed
- Updated dependency
### Fixed
- Bug fix
```

---

## 5. Architecture Decision Record (ADR)

```markdown
# ADR-001: [Title]

## Status
Accepted / Deprecated / Superseded

## Context
Why are we making this decision?

## Decision
What did we decide?

## Consequences
What are the trade-offs?
```

---

## 6. AI-Friendly Documentation (2025)

### llms.txt Template

For AI crawlers and agents:

```markdown
# Project Name
> One-line objective.

## Core Files
- [src/index.ts]: Main entry
- [src/api/]: API routes
- [docs/]: Documentation

## Key Concepts
- Concept 1: Brief explanation
- Concept 2: Brief explanation
```

### MCP-Ready Documentation

For RAG indexing:
- Clear H1-H3 hierarchy
- JSON/YAML examples for data structures
- Mermaid diagrams for flows
- Self-contained sections

---

## 7. Structure Principles

| Principle | Why |
|-----------|-----|
| **Scannable** | Headers, lists, tables |
| **Examples first** | Show, don't just tell |
| **Progressive detail** | Simple → Complex |
| **Up to date** | Outdated = misleading |

---

> **Remember:** Templates are starting points. Adapt to your project's needs.

## When to Use
This skill is applicable to execute the workflow or actions described in the overview.

## Source: references/skills/documentation/references/legacy/readme/SKILL.md

---
name: readme
description: "When the user wants to create or update a README.md file for a project. Also use when the user says 'write readme,' 'create readme,' 'document this project,' 'project documentation,' or asks for he..."
risk: safe
source: "https://github.com/Shpigford/skills/tree/main/readme"
date_added: "2026-02-27"
---

# README Generator

You are an expert technical writer creating comprehensive project documentation. Your goal is to write a README.md that is absurdly thorough—the kind of documentation you wish every project had.

## When to Use This Skill

Use this skill when:

- User wants to create or update a README.md file
- User says "write readme" or "create readme"
- User asks to "document this project"
- User requests "project documentation"
- User asks for help with README.md

## The Three Purposes of a README

1. **Local Development** - Help any developer get the app running locally in minutes
2. **Understanding the System** - Explain in great detail how the app works
3. **Production Deployment** - Cover everything needed to deploy and maintain in production

---

## Before Writing

### Step 1: Deep Codebase Exploration

Before writing a single line of documentation, thoroughly explore the codebase. You MUST understand:

**Project Structure**

- Read the root directory structure
- Identify the framework/language (Gemfile for Rails, package.json, go.mod, requirements.txt, etc.)
- Find the main entry point(s)
- Map out the directory organization

**Configuration Files**

- .env.example, .env.sample, or documented environment variables
- Rails config files (config/database.yml, config/application.rb, config/environments/)
- Credentials setup (config/credentials.yml.enc, config/master.key)
- Docker files (Dockerfile, docker-compose.yml)
- CI/CD configs (.github/workflows/, .gitlab-ci.yml, etc.)
- Deployment configs (config/deploy.yml for Kamal, fly.toml, render.yaml, Procfile, etc.)

**Database**

- db/schema.rb or db/structure.sql
- Migrations in db/migrate/
- Seeds in db/seeds.rb
- Database type from config/database.yml

**Key Dependencies**

- Gemfile and Gemfile.lock for Ruby gems
- package.json for JavaScript dependencies
- Note any native gem dependencies (pg, nokogiri, etc.)

**Scripts and Commands**

- bin/ scripts (bin/dev, bin/setup, bin/ci)
- Procfile or Procfile.dev
- Rake tasks (lib/tasks/)

### Step 2: Identify Deployment Target

Look for these files to determine deployment platform and tailor instructions:

- `Dockerfile` / `docker-compose.yml` → Docker-based deployment
- `vercel.json` / `.vercel/` → Vercel
- `netlify.toml` → Netlify
- `fly.toml` → Fly.io
- `railway.json` / `railway.toml` → Railway
- `render.yaml` → Render
- `app.yaml` → Google App Engine
- `Procfile` → Heroku or Heroku-like platforms
- `.ebextensions/` → AWS Elastic Beanstalk
- `serverless.yml` → Serverless Framework
- `terraform/` / `*.tf` → Terraform/Infrastructure as Code
- `k8s/` / `kubernetes/` → Kubernetes

If no deployment config exists, provide general guidance with Docker as the recommended approach.

### Step 3: Ask Only If Critical

Only ask the user questions if you cannot determine:

- What the project does (if not obvious from code)
- Specific deployment credentials or URLs needed
- Business context that affects documentation

Otherwise, proceed with exploration and writing.

---

## README Structure

Write the README with these sections in order:

### 1. Project Title and Overview

```markdown
# Project Name

Brief description of what the project does and who it's for. 2-3 sentences max.

## Key Features

- Feature 1
- Feature 2
- Feature 3
```

### 2. Tech Stack

List all major technologies:

```markdown
## Tech Stack

- **Language**: Ruby 3.3+
- **Framework**: Rails 7.2+
- **Frontend**: Inertia.js with React
- **Database**: PostgreSQL 16
- **Background Jobs**: Solid Queue
- **Caching**: Solid Cache
- **Styling**: Tailwind CSS
- **Deployment**: [Detected platform]
```

### 3. Prerequisites

What must be installed before starting:

```markdown
## Prerequisites

- Node.js 20 or higher
- PostgreSQL 15 or higher (or Docker)
- pnpm (recommended) or npm
- A Google Cloud project for OAuth (optional for development)
```

### 4. Getting Started

The complete local development guide:

```markdown
## Getting Started

### 1. Clone the Repository

\`\`\`bash
git clone https://github.com/user/repo.git
cd repo
\`\`\`

### 2. Install Ruby Dependencies

Ensure you have Ruby 3.3+ installed (via rbenv, asdf, or mise):

\`\`\`bash
bundle install
\`\`\`

### 3. Install JavaScript Dependencies

\`\`\`bash
yarn install
\`\`\`

### 4. Environment Setup

Copy the example environment file:

\`\`\`bash
cp .env.example .env
\`\`\`

Configure the following variables:

| Variable           | Description                  | Example                                    |
| ------------------ | ---------------------------- | ------------------------------------------ |
| `DATABASE_URL`     | PostgreSQL connection string | `postgresql://localhost/myapp_development` |
| `REDIS_URL`        | Redis connection (if used)   | `redis://localhost:6379/0`                 |
| `SECRET_KEY_BASE`  | Rails secret key             | `bin/rails secret`                         |
| `RAILS_MASTER_KEY` | For credentials encryption   | Check `config/master.key`                  |

### 5. Database Setup

Start PostgreSQL (if using Docker):

\`\`\`bash
docker run --name postgres -e POSTGRES_PASSWORD=postgres -p 5432:5432 -d postgres:16
\`\`\`

Create and set up the database:

\`\`\`bash
bin/rails db:setup
\`\`\`

This runs `db:create`, `db:schema:load`, and `db:seed`.

For existing databases, run migrations:

\`\`\`bash
bin/rails db:migrate
\`\`\`

### 6. Start Development Server

Using Foreman/Overmind (recommended, runs Rails + Vite):

\`\`\`bash
bin/dev
\`\`\`

Or manually:

\`\`\`bash

# Terminal 1: Rails server

bin/rails server

# Terminal 2: Vite dev server (for Inertia/React)

bin/vite dev
\`\`\`

Open [http://localhost:3000](http://localhost:3000) in your browser.
```

Include every step. Assume the reader is setting up on a fresh machine.

### 5. Architecture Overview

This is where you go absurdly deep:

```markdown
## Architecture

### Directory Structure

\`\`\`
├── app/
│ ├── controllers/ # Rails controllers
│ │ ├── concerns/ # Shared controller modules
│ │ └── api/ # API-specific controllers
│ ├── models/ # ActiveRecord models
│ │ └── concerns/ # Shared model modules
│ ├── jobs/ # Background jobs (Solid Queue)
│ ├── mailers/ # Email templates
│ ├── views/ # Rails views (minimal with Inertia)
│ └── frontend/ # Inertia.js React components
│ ├── components/ # Reusable UI components
│ ├── layouts/ # Page layouts
│ ├── pages/ # Inertia page components
│ └── lib/ # Frontend utilities
├── config/
│ ├── routes.rb # Route definitions
│ ├── database.yml # Database configuration
│ └── initializers/ # App initializers
├── db/
│ ├── migrate/ # Database migrations
│ ├── schema.rb # Current schema
│ └── seeds.rb # Seed data
├── lib/
│ └── tasks/ # Custom Rake tasks
└── public/ # Static assets
\`\`\`

### Request Lifecycle

1. Request hits Rails router (`config/routes.rb`)
2. Middleware stack processes request (authentication, sessions, etc.)
3. Controller action executes
4. Models interact with PostgreSQL via ActiveRecord
5. Inertia renders React component with props
6. Response sent to browser

### Data Flow

\`\`\`
User Action → React Component → Inertia Visit → Rails Controller → ActiveRecord → PostgreSQL
↓
React Props ← Inertia Response ←
\`\`\`

### Key Components

**Authentication**

- Devise/Rodauth for user authentication
- Session-based auth with encrypted cookies
- `authenticate_user!` before_action for protected routes

**Inertia.js Integration (`app/frontend/`)**

- React components receive props from Rails controllers
- `inertia_render` in controllers passes data to frontend
- Shared data via `inertia_share` for layout props

**Background Jobs (`app/jobs/`)**

- Solid Queue for job processing
- Jobs stored in PostgreSQL (no Redis required)
- Dashboard at `/jobs` for monitoring

**Database (`app/models/`)**

- ActiveRecord models with associations
- Query objects for complex queries
- Concerns for shared model behavior

### Database Schema

\`\`\`
users
├── id (bigint, PK)
├── email (string, unique, not null)
├── encrypted_password (string)
├── name (string)
├── created_at (datetime)
└── updated_at (datetime)

posts
├── id (bigint, PK)
├── title (string, not null)
├── content (text)
├── published (boolean, default: false)
├── user_id (bigint, FK → users)
├── created_at (datetime)
└── updated_at (datetime)

solid_queue_jobs (background jobs)
├── id (bigint, PK)
├── queue_name (string)
├── class_name (string)
├── arguments (json)
├── scheduled_at (datetime)
└── ...
\`\`\`
```

### 6. Environment Variables

Complete reference for all env vars:

```markdown
## Environment Variables

### Required

| Variable           | Description                       | How to Get                             |
| ------------------ | --------------------------------- | -------------------------------------- |
| `DATABASE_URL`     | PostgreSQL connection string      | Your database provider                 |
| `SECRET_KEY_BASE`  | Rails secret for sessions/cookies | Run `bin/rails secret`                 |
| `RAILS_MASTER_KEY` | Decrypts credentials file         | Check `config/master.key` (not in git) |

### Optional

| Variable            | Description                                       | Default                      |
| ------------------- | ------------------------------------------------- | ---------------------------- |
| `REDIS_URL`         | Redis connection string (for caching/ActionCable) | -                            |
| `RAILS_LOG_LEVEL`   | Logging verbosity                                 | `debug` (dev), `info` (prod) |
| `RAILS_MAX_THREADS` | Puma thread count                                 | `5`                          |
| `WEB_CONCURRENCY`   | Puma worker count                                 | `2`                          |
| `SMTP_ADDRESS`      | Mail server hostname                              | -                            |
| `SMTP_PORT`         | Mail server port                                  | `587`                        |

### Rails Credentials

Sensitive values should be stored in Rails encrypted credentials:

\`\`\`bash

# Edit credentials (opens in $EDITOR)

bin/rails credentials:edit

# Or for environment-specific credentials

RAILS_ENV=production bin/rails credentials:edit
\`\`\`

Credentials file structure:
\`\`\`yaml
secret_key_base: xxx
stripe:
public_key: pk_xxx
secret_key: sk_xxx
google:
client_id: xxx
client_secret: xxx
\`\`\`

Access in code: `Rails.application.credentials.stripe[:secret_key]`

### Environment-Specific

**Development**
\`\`\`
DATABASE_URL=postgresql://localhost/myapp_development
REDIS_URL=redis://localhost:6379/0
\`\`\`

**Production**
\`\`\`
DATABASE_URL=<production-connection-string>
RAILS_ENV=production
RAILS_SERVE_STATIC_FILES=true
\`\`\`
```

### 7. Available Scripts

```markdown
## Available Scripts

| Command                       | Description                                         |
| ----------------------------- | --------------------------------------------------- |
| `bin/dev`                     | Start development server (Rails + Vite via Foreman) |
| `bin/rails server`            | Start Rails server only                             |
| `bin/vite dev`                | Start Vite dev server only                          |
| `bin/rails console`           | Open Rails console (IRB with app loaded)            |
| `bin/rails db:migrate`        | Run pending database migrations                     |
| `bin/rails db:rollback`       | Rollback last migration                             |
| `bin/rails db:seed`           | Run database seeds                                  |
| `bin/rails db:reset`          | Drop, create, migrate, and seed database            |
| `bin/rails routes`            | List all routes                                     |
| `bin/rails test`              | Run test suite (Minitest)                           |
| `bundle exec rspec`           | Run test suite (RSpec, if used)                     |
| `bin/rails assets:precompile` | Compile assets for production                       |
| `bin/rubocop`                 | Run Ruby linter                                     |
| `yarn lint`                   | Run JavaScript/TypeScript linter                    |
```

### 8. Testing

```markdown
## Testing

### Running Tests

\`\`\`bash

# Run all tests (Minitest)

bin/rails test

# Run all tests (RSpec, if used)

bundle exec rspec

# Run specific test file

bin/rails test test/models/user_test.rb
bundle exec rspec spec/models/user_spec.rb

# Run tests matching a pattern

bin/rails test -n /creates_user/
bundle exec rspec -e "creates user"

# Run system tests (browser tests)

bin/rails test:system

# Run with coverage (SimpleCov)

COVERAGE=true bin/rails test
\`\`\`

### Test Structure

\`\`\`
test/ # Minitest structure
├── controllers/ # Controller tests
├── models/ # Model unit tests
├── integration/ # Integration tests
├── system/ # System/browser tests
├── fixtures/ # Test data
└── test_helper.rb # Test configuration

spec/ # RSpec structure (if used)
├── models/
├── requests/
├── system/
├── factories/ # FactoryBot factories
├── support/
└── rails_helper.rb
\`\`\`

### Writing Tests

**Minitest example:**
\`\`\`ruby
require "test_helper"

class UserTest < ActiveSupport::TestCase
test "creates user with valid attributes" do
user = User.new(email: "test@example.com", name: "Test User")
assert user.valid?
end

test "requires email" do
user = User.new(name: "Test User")
assert_not user.valid?
assert_includes user.errors[:email], "can't be blank"
end
end
\`\`\`

**RSpec example:**
\`\`\`ruby
require "rails_helper"

RSpec.describe User, type: :model do
describe "validations" do
it "is valid with valid attributes" do
user = build(:user)
expect(user).to be_valid
end

    it "requires an email" do
      user = build(:user, email: nil)
      expect(user).not_to be_valid
      expect(user.errors[:email]).to include("can't be blank")
    end

end
end
\`\`\`

### Frontend Testing

For Inertia/React components:

\`\`\`bash
yarn test
\`\`\`

\`\`\`typescript
import { render, screen } from '@testing-library/react'
import { Dashboard } from './Dashboard'

describe('Dashboard', () => {
it('renders user name', () => {
render(<Dashboard user={{ name: 'Josh' }} />)
expect(screen.getByText('Josh')).toBeInTheDocument()
})
})
\`\`\`
```

### 9. Deployment

Tailor this to detected platform (look for Dockerfile, fly.toml, render.yaml, kamal/, etc.):

```markdown
## Deployment

### Kamal (Recommended for Rails)

If using Kamal for deployment:

\`\`\`bash

# Setup Kamal (first time)

kamal setup

# Deploy

kamal deploy

# Rollback to previous version

kamal rollback

# View logs

kamal app logs

# Run console on production

kamal app exec --interactive 'bin/rails console'
\`\`\`

Configuration lives in `config/deploy.yml`.

### Docker

Build and run:

\`\`\`bash

# Build image

docker build -t myapp .

# Run with environment variables

docker run -p 3000:3000 \
 -e DATABASE_URL=postgresql://... \
 -e SECRET_KEY_BASE=... \
 -e RAILS_ENV=production \
 myapp
\`\`\`

### Heroku

\`\`\`bash

# Create app

heroku create myapp

# Add PostgreSQL

heroku addons:create heroku-postgresql:mini

# Set environment variables

heroku config:set SECRET_KEY_BASE=$(bin/rails secret)
heroku config:set RAILS_MASTER_KEY=$(cat config/master.key)

# Deploy

git push heroku main

# Run migrations

heroku run bin/rails db:migrate
\`\`\`

### Fly.io

\`\`\`bash

# Launch (first time)

fly launch

# Deploy

fly deploy

# Run migrations

fly ssh console -C "bin/rails db:migrate"

# Open console

fly ssh console -C "bin/rails console"
\`\`\`

### Render

If `render.yaml` exists, connect your repo to Render and it will auto-deploy.

Manual setup:

1. Create new Web Service
2. Connect GitHub repository
3. Set build command: `bundle install && bin/rails assets:precompile`
4. Set start command: `bin/rails server`
5. Add environment variables in dashboard

### Manual/VPS Deployment

\`\`\`bash

# On the server:

# Pull latest code

git pull origin main

# Install dependencies

bundle install --deployment

# Compile assets

RAILS_ENV=production bin/rails assets:precompile

# Run migrations

RAILS_ENV=production bin/rails db:migrate

# Restart application server (e.g., Puma via systemd)

sudo systemctl restart myapp
\`\`\`
```

### 10. Troubleshooting

```markdown
## Troubleshooting

### Database Connection Issues

**Error:** `could not connect to server: Connection refused`

**Solution:**

1. Verify PostgreSQL is running: `pg_isready` or `docker ps`
2. Check `DATABASE_URL` format: `postgresql://USER:PASSWORD@HOST:PORT/DATABASE`
3. Ensure database exists: `bin/rails db:create`

### Pending Migrations

**Error:** `Migrations are pending`

**Solution:**
\`\`\`bash
bin/rails db:migrate
\`\`\`

### Asset Compilation Issues

**Error:** `The asset "application.css" is not present in the asset pipeline`

**Solution:**
\`\`\`bash

# Clear and recompile assets

bin/rails assets:clobber
bin/rails assets:precompile
\`\`\`

### Bundle Install Failures

**Error:** Native extension build failures

**Solution:**

1. Ensure system dependencies are installed:
   \`\`\`bash

   # macOS

   brew install postgresql libpq

   # Ubuntu

   sudo apt-get install libpq-dev
   \`\`\`

2. Try again: `bundle install`

### Credentials Issues

**Error:** `ActiveSupport::MessageEncryptor::InvalidMessage`

**Solution:**
The master key doesn't match the credentials file. Either:

1. Get the correct `config/master.key` from another team member
2. Or regenerate credentials: `rm config/credentials.yml.enc && bin/rails credentials:edit`

### Vite/Inertia Issues

**Error:** `Vite Ruby - Build failed`

**Solution:**
\`\`\`bash

# Clear Vite cache

rm -rf node_modules/.vite

# Reinstall JS dependencies

rm -rf node_modules && yarn install
\`\`\`

### Solid Queue Issues

**Error:** Jobs not processing

**Solution:**
Ensure the queue worker is running:
\`\`\`bash
bin/jobs

# or

bin/rails solid_queue:start
\`\`\`
```

### 11. Contributing (Optional)

Include if open source or team project.

### 12. License (Optional)

---

## Writing Principles

1. **Be Absurdly Thorough** - When in doubt, include it. More detail is always better.

2. **Use Code Blocks Liberally** - Every command should be copy-pasteable.

3. **Show Example Output** - When helpful, show what the user should expect to see.

4. **Explain the Why** - Don't just say "run this command," explain what it does.

5. **Assume Fresh Machine** - Write as if the reader has never seen this codebase.

6. **Use Tables for Reference** - Environment variables, scripts, and options work great as tables.

7. **Keep Commands Current** - Use `pnpm` if the project uses it, `npm` if it uses npm, etc.

8. **Include a Table of Contents** - For READMEs over ~200 lines, add a TOC at the top.

---

## Output Format

Generate a complete README.md file with:

- Proper markdown formatting
- Code blocks with language hints (`bash, `typescript, etc.)
- Tables where appropriate
- Clear section hierarchy
- Linked table of contents for long documents

Write the README directly to `README.md` in the project root.

## Source: references/skills/documentation/references/legacy/wiki-changelog/SKILL.md

---
name: wiki-changelog
description: "Analyzes git commit history and generates structured changelogs categorized by change type. Use when the user asks about recent changes, wants a changelog, or needs to understand what changed in th..."
risk: unknown
source: community
date_added: "2026-02-27"
---

# Wiki Changelog

Generate structured changelogs from git history.

## When to Activate

- User asks "what changed recently", "generate a changelog", "summarize commits"
- User wants to understand recent development activity

## Procedure

1. Examine git log (commits, dates, authors, messages)
2. Group by time period: daily (last 7 days), weekly (older)
3. Classify each commit: Features (🆕), Fixes (🐛), Refactoring (🔄), Docs (📝), Config (🔧), Dependencies (📦), Breaking (⚠️)
4. Generate concise user-facing descriptions using project terminology

## Constraints

- Focus on user-facing changes
- Merge related commits into coherent descriptions
- Use project terminology from README
- Highlight breaking changes prominently with migration notes

## When to Use
This skill is applicable to execute the workflow or actions described in the overview.

## Source: references/skills/documentation/references/legacy/wiki-page-writer/SKILL.md

---
name: wiki-page-writer
description: "Generates rich technical documentation pages with dark-mode Mermaid diagrams, source code citations, and first-principles depth. Use when writing documentation, generating wiki pages, creating tech..."
risk: unknown
source: community
date_added: "2026-02-27"
---

# Wiki Page Writer

You are a senior documentation engineer that generates comprehensive technical documentation pages with evidence-based depth.

## When to Activate

- User asks to document a specific component, system, or feature
- User wants a technical deep-dive with diagrams
- A wiki catalogue section needs its content generated

## Depth Requirements (NON-NEGOTIABLE)

1. **TRACE ACTUAL CODE PATHS** — Do not guess from file names. Read the implementation.
2. **EVERY CLAIM NEEDS A SOURCE** — File path + function/class name.
3. **DISTINGUISH FACT FROM INFERENCE** — If you read the code, say so. If inferring, mark it.
4. **FIRST PRINCIPLES** — Explain WHY something exists before WHAT it does.
5. **NO HAND-WAVING** — Don't say "this likely handles..." — read the code.

## Procedure

1. **Plan**: Determine scope, audience, and documentation budget based on file count
2. **Analyze**: Read all relevant files; identify patterns, algorithms, dependencies, data flow
3. **Write**: Generate structured Markdown with diagrams and citations
4. **Validate**: Verify file paths exist, class names are accurate, Mermaid renders correctly

## Mandatory Requirements

### VitePress Frontmatter
Every page must have:
```
---
title: "Page Title"
description: "One-line description"
---
```

### Mermaid Diagrams
- **Minimum 2 per page**
- Use `autonumber` in all `sequenceDiagram` blocks
- Choose appropriate types: `graph`, `sequenceDiagram`, `classDiagram`, `stateDiagram-v2`, `erDiagram`, `flowchart`
- **Dark-mode colors (MANDATORY)**: node fills `#2d333b`, borders `#6d5dfc`, text `#e6edf3`
- Subgraph backgrounds: `#161b22`, borders `#30363d`, lines `#8b949e`
- If using inline `style`, use dark fills with `,color:#e6edf3`
- Do NOT use `<br/>` (use `<br>` or line breaks)

### Citations
- Every non-trivial claim needs `(file_path:line_number)`
- Minimum 5 different source files cited per page
- If evidence is missing: `(Unknown – verify in path/to/check)`

### Structure
- Overview (explain WHY) → Architecture → Components → Data Flow → Implementation → References
- Use Markdown tables for APIs, configs, and component summaries
- Use comparison tables when introducing technologies
- Include pseudocode in a familiar language when explaining complex code paths

### VitePress Compatibility
- Escape bare generics outside code fences: `` `List<T>` `` not bare `List<T>`
- No `<br/>` in Mermaid blocks
- All hex colors must be 3 or 6 digits

## When to Use
This skill is applicable to execute the workflow or actions described in the overview.

## Source: references/skills/documentation/references/legacy/wiki-qa/SKILL.md

---
name: wiki-qa
description: "Answers questions about a code repository using source file analysis. Use when the user asks a question about how something works, wants to understand a component, or needs help navigating the code..."
risk: unknown
source: community
date_added: "2026-02-27"
---

# Wiki Q&A

Answer repository questions grounded entirely in source code evidence.

## When to Activate

- User asks a question about the codebase
- User wants to understand a specific file, function, or component
- User asks "how does X work" or "where is Y defined"

## Procedure

1. Detect the language of the question; respond in the same language
2. Search the codebase for relevant files
3. Read those files to gather evidence
4. Synthesize an answer with inline citations

## Response Format

- Use `##` headings, code blocks with language tags, tables, bullet lists
- Cite sources inline: `(src/path/file.ts:42)`
- Include a "Key Files" table mapping files to their roles
- If information is insufficient, say so and suggest files to examine

## Rules

- ONLY use information from actual source files
- NEVER invent, guess, or use external knowledge
- Think step by step before answering

## When to Use
This skill is applicable to execute the workflow or actions described in the overview.

## Source: references/skills/documentation/references/legacy/wiki-vitepress/SKILL.md

---
name: wiki-vitepress
description: "Packages generated wiki Markdown into a VitePress static site with dark theme, dark-mode Mermaid diagrams with click-to-zoom, and production build output. Use when the user wants to create a browsa..."
risk: unknown
source: community
date_added: "2026-02-27"
---

# Wiki VitePress Packager

Transform generated wiki Markdown files into a polished VitePress static site with dark theme and interactive Mermaid diagrams.

## When to Activate

- User asks to "build a site" or "package as VitePress"
- User runs the `/deep-wiki:build` command
- User wants a browsable HTML output from generated wiki pages

## VitePress Scaffolding

Generate the following structure in a `wiki-site/` directory:

```
wiki-site/
├── .vitepress/
│   ├── config.mts
│   └── theme/
│       ├── index.ts
│       └── custom.css
├── public/
├── [generated .md pages]
├── package.json
└── index.md
```

## Config Requirements (`config.mts`)

- Use `withMermaid` wrapper from `vitepress-plugin-mermaid`
- Set `appearance: 'dark'` for dark-only theme
- Configure `themeConfig.nav` and `themeConfig.sidebar` from the catalogue structure
- Mermaid config must set dark theme variables:

```typescript
mermaid: {
  theme: 'dark',
  themeVariables: {
    primaryColor: '#1e3a5f',
    primaryTextColor: '#e0e0e0',
    primaryBorderColor: '#4a9eed',
    lineColor: '#4a9eed',
    secondaryColor: '#2d4a3e',
    tertiaryColor: '#2d2d3d',
    background: '#1a1a2e',
    mainBkg: '#1e3a5f',
    nodeBorder: '#4a9eed',
    clusterBkg: '#16213e',
    titleColor: '#e0e0e0',
    edgeLabelBackground: '#1a1a2e'
  }
}
```

## Dark-Mode Mermaid: Three-Layer Fix

### Layer 1: Theme Variables (in config.mts)
Set via `mermaid.themeVariables` as shown above.

### Layer 2: CSS Overrides (`custom.css`)
Target Mermaid SVG elements with `!important`:

```css
.mermaid .node rect,
.mermaid .node circle,
.mermaid .node polygon { fill: #1e3a5f !important; stroke: #4a9eed !important; }
.mermaid .edgeLabel { background-color: #1a1a2e !important; color: #e0e0e0 !important; }
.mermaid text { fill: #e0e0e0 !important; }
.mermaid .label { color: #e0e0e0 !important; }
```

### Layer 3: Inline Style Replacement (`theme/index.ts`)
Mermaid inline `style` attributes override everything. Use `onMounted` + polling to replace them:

```typescript
import { onMounted } from 'vue'

// In setup()
onMounted(() => {
  let attempts = 0
  const fix = setInterval(() => {
    document.querySelectorAll('.mermaid svg [style]').forEach(el => {
      const s = (el as HTMLElement).style
      if (s.fill && !s.fill.includes('#1e3a5f')) s.fill = '#1e3a5f'
      if (s.stroke && !s.stroke.includes('#4a9eed')) s.stroke = '#4a9eed'
      if (s.color) s.color = '#e0e0e0'
    })
    if (++attempts >= 20) clearInterval(fix)
  }, 500)
})
```

Use `setup()` with `onMounted`, NOT `enhanceApp()` — DOM doesn't exist during SSR.

## Click-to-Zoom for Mermaid Diagrams

Wrap each `.mermaid` container in a clickable wrapper that opens a fullscreen modal:

```typescript
document.querySelectorAll('.mermaid').forEach(el => {
  el.style.cursor = 'zoom-in'
  el.addEventListener('click', () => {
    const modal = document.createElement('div')
    modal.className = 'mermaid-zoom-modal'
    modal.innerHTML = el.outerHTML
    modal.addEventListener('click', () => modal.remove())
    document.body.appendChild(modal)
  })
})
```

Modal CSS:
```css
.mermaid-zoom-modal {
  position: fixed; inset: 0;
  background: rgba(0,0,0,0.9);
  display: flex; align-items: center; justify-content: center;
  z-index: 9999; cursor: zoom-out;
}
.mermaid-zoom-modal .mermaid { transform: scale(1.5); }
```

## Post-Processing Rules

Before VitePress build, scan all `.md` files and fix:
- Replace `<br/>` with `<br>` (Vue template compiler compatibility)
- Wrap bare `<T>` generic parameters in backticks outside code fences
- Ensure every page has YAML frontmatter with `title` and `description`

## Build

```bash
cd wiki-site && npm install && npm run docs:build
```

Output goes to `wiki-site/.vitepress/dist/`.

## Known Gotchas

- Mermaid renders async — SVGs don't exist when `onMounted` fires. Must poll.
- `isCustomElement` compiler option for bare `<T>` causes worse crashes — do NOT use it
- Node text in Mermaid uses inline `style` with highest specificity — CSS alone won't fix it
- `enhanceApp()` runs during SSR where `document` doesn't exist — use `setup()` only

## When to Use
This skill is applicable to execute the workflow or actions described in the overview.

