# Publishing Model

This collection supports two publishing modes from day one:

- `skills-super` as the master catalogue.
- One standalone repository per `super-*` skill.

## Master Catalogue

Use the master catalogue for:

- Discovering all skills in one place.
- Updating shared structure and validation.
- Regenerating standalone product exports.
- Keeping a complete list in `CATALOG.md` and `catalog.json`.

## Standalone Skill Products

Each skill folder is product-ready and can be published as its own repository.

Every standalone skill product should contain:

```text
SKILL.md
README.md
CHANGELOG.md
VERSION
examples/
references/
agents/
product.json
PUBLISHING.md
LICENSE
.gitignore
```

Optional folders such as `scripts/` and `assets/` should stay with the product when they are needed by the skill.

## Export Products

From the master catalogue:

```bash
python3 scripts/export_skill_products.py --force
```

By default, this writes standalone products to:

```text
../skill-products/
```

Each folder in `../skill-products/` can be initialised as its own git repository and pushed to a separate remote.

## Repository Naming

Use the skill name as the repository name:

```text
super-seo-growth
super-marketing-execution
super-design-core
```

## Release Versioning

- Start each standalone skill at `v0.1.0`.
- Update the product `VERSION` file for product-specific releases.
- Update product `CHANGELOG.md` for every public release.
- The master catalogue version can move separately from individual product versions.

## Sync Rule

The master catalogue is the canonical working copy until a skill has a separate release process.

Recommended workflow:

1. Update the skill in `skills-super`.
2. Run `python3 scripts/export_skill_products.py --force`.
3. Review the exported product diff.
4. Commit and release in the standalone product repository.

Once a standalone skill matures, it can become source-of-truth for that skill, with changes mirrored back into the catalogue.
