# Super Office Docs Presentation

Create, analyse, and improve documents, PDFs, slides, spreadsheets, and documentation workflows.

## Install

Copy this folder into your agent's skills directory, then restart or reload the agent.

```bash
cp -R super-office-docs-presentation ~/.your-agent/skills/
```

Use it by name:

```text
Use $super-office-docs-presentation to help with this request.
```

## Best For

- documents and PDFs
- presentations
- spreadsheets
- office automation
- documentation workflows

## Outputs

- document plan or edits
- slide outline or deck guidance
- spreadsheet structure
- automation workflow
- quality checklist

## Modules

| Module | Purpose |
| --- | --- |
| `docs-pdf-ppt.md` | Documents, PDFs, presentations, formatting, redlining, and publishing workflows |
| `office-productivity.md` | Spreadsheets, office automation, documentation systems, and productivity workflows |

## Example Prompts

- `Use $super-office-docs-presentation to turn this outline into a presentation.`
- `Use $super-office-docs-presentation to analyse this spreadsheet workflow.`
- `Use $super-office-docs-presentation to create a documentation template.`

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
