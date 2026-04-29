#!/usr/bin/env python3
"""Export each super skill as a standalone product folder.

The master catalogue remains the source of truth. This script copies each
`super-*` skill into a sibling products directory and adds shared repository
files so each product can be published as its own repository.
"""

from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT.parent / "skill-products"

SHARED_FILES = [
    "LICENSE",
    ".gitignore",
]


def read_catalog() -> dict:
    catalog_path = ROOT / "catalog.json"
    if not catalog_path.exists():
        raise SystemExit(f"Missing catalogue: {catalog_path}")
    return json.loads(catalog_path.read_text())


def copy_skill(skill: dict, output_dir: Path, force: bool) -> Path:
    source = ROOT / skill["folder"]
    target = output_dir / skill["folder"]

    if not source.exists():
        raise SystemExit(f"Missing skill folder: {source}")

    if target.exists():
        if not force:
            raise SystemExit(
                f"Target exists: {target}. Re-run with --force to replace exported files."
            )
        shutil.rmtree(target)

    shutil.copytree(
        source,
        target,
        ignore=shutil.ignore_patterns(".git", "__pycache__", ".DS_Store"),
    )

    for filename in SHARED_FILES:
        shared = ROOT / filename
        if shared.exists():
            shutil.copy2(shared, target / filename)

    write_product_manifest(skill, target)
    write_product_publishing_notes(skill, target)
    return target


def write_product_manifest(skill: dict, target: Path) -> None:
    manifest = {
        "name": skill["name"],
        "title": skill["title"],
        "description": skill["description"],
        "version": (target / "VERSION").read_text().strip()
        if (target / "VERSION").exists()
        else "0.1.0",
        "source_catalogue": "skills-super",
        "skill_entrypoint": "SKILL.md",
        "modules": skill["modules"],
    }
    (target / "product.json").write_text(json.dumps(manifest, indent=2) + "\n")


def write_product_publishing_notes(skill: dict, target: Path) -> None:
    notes = f"""# Publishing

This folder is a standalone product export for `{skill["name"]}`.

## Repository Model

- Publish this folder as its own repository when the skill needs separate issues, releases, documentation, or branding.
- Keep `SKILL.md` as the installable entry point.
- Keep `references/modules/` bundled so the skill works without the master catalogue.
- Keep `README.md`, `CHANGELOG.md`, `VERSION`, and `examples/` updated for every release.

## Suggested Repository Name

`{skill["name"]}`

## Suggested First Release

`v0.1.0`

## Sync Rule

The master catalogue can regenerate this product with:

```bash
python3 scripts/export_skill_products.py --force
```

Review changes before committing in the standalone product repository.
"""
    (target / "PUBLISHING.md").write_text(notes)


def main() -> None:
    parser = argparse.ArgumentParser(description="Export standalone skill products.")
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
        help=f"Output directory. Default: {DEFAULT_OUTPUT}",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Replace existing exported product folders.",
    )
    args = parser.parse_args()

    catalog = read_catalog()
    args.output.mkdir(parents=True, exist_ok=True)

    exported = []
    for skill in catalog["skills"]:
        exported.append(copy_skill(skill, args.output, args.force))

    print(f"Exported {len(exported)} products to {args.output}")
    for path in exported:
        print(path)


if __name__ == "__main__":
    main()
