# Contributing

Thanks for improving Super Skills. The goal is to keep each skill easy to install, easy to understand, and useful across different AI agents.

## Structure

- Keep one `SKILL.md` at the root of each `super-*` folder.
- Do not add nested `SKILL.md` files.
- Put detailed workflows in `references/modules/*.md`.
- Keep bundled scripts and assets only when they directly support the skill.

## Writing Guidelines

- Keep `SKILL.md` concise and marketable.
- Use clear sections: overview, user intent examples, capabilities, routing map, default flow, minimal intake questions, output format, compatibility notes, and guardrails.
- Make modules practical: purpose, when to use, workflow, expected output, and validation steps.
- Avoid AI coding app names in general instructions. Use generic terms like "AI assistant", "agent", or "agent CLI" unless the content is specifically about a named platform.
- Keep product and platform names when they are the actual subject, such as AWS, Azure, Google, GitHub, Salesforce, Shopify, or Stripe.

## Quality Checks

Before publishing changes:

```bash
find . -path '*/SKILL.md' | sort
find . -name '.DS_Store' -print
rg -n "references/skills/" .
```

Expected:

- One `SKILL.md` per `super-*` folder.
- No `.DS_Store` files.
- No active routes pointing to `references/skills/`.

## Updating Skills

When adding new material:

- Add it to the most relevant existing module when it strengthens that module.
- Create a new module only when the workflow is meaningfully different.
- Do not split modules just because they are large.
- If the same knowledge is needed in more than one module, copy only the necessary section and keep it self-contained.
