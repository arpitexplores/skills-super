#!/usr/bin/env python3
"""Validate SUPER Skills packaging and public-readiness basics."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_PRODUCTS = ROOT.parent / "skill-products"
EXPECTED_VERSION = "1.0.0"

REQUIRED_ROOT_FILES = [
    "README.md",
    "INSTALL.md",
    "VERSION",
    "CHANGELOG.md",
    "LICENSE",
]

REQUIRED_SKILL_FILES = REQUIRED_ROOT_FILES + [
    "SKILL.md",
    "examples/README.md",
]

REQUIRED_CATALOGUE_SKILL_FILES = [
    "README.md",
    "INSTALL.md",
    "VERSION",
    "CHANGELOG.md",
    "SKILL.md",
    "examples/README.md",
]

BADGE_MARKERS = [
    "img.shields.io/badge/version-1.0.0-blue",
    "img.shields.io/badge/licence-MIT-green",
    "img.shields.io/badge/Markdown-skill-2b2f36",
    "img.shields.io/badge/AI%20vibe%20coding-ready-ffb000",
]

FORBIDDEN_PUBLIC_BRANDS = [
    "claude",
    "codex",
    "antigravity",
]


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def add_error(errors: list[str], repo: Path, message: str) -> None:
    errors.append(f"{repo.name}: {message}")


def check_required_files(repo: Path, required: list[str], errors: list[str]) -> None:
    for relative in required:
        if not (repo / relative).exists():
            add_error(errors, repo, f"missing {relative}")


def check_version(repo: Path, errors: list[str]) -> None:
    version_file = repo / "VERSION"
    if version_file.exists() and read_text(version_file).strip() != EXPECTED_VERSION:
        add_error(errors, repo, f"VERSION is not {EXPECTED_VERSION}")

    changelog = repo / "CHANGELOG.md"
    if changelog.exists() and f"## {EXPECTED_VERSION} - Public Launch" not in read_text(changelog):
        add_error(errors, repo, "CHANGELOG.md missing public launch entry")


def check_readme(repo: Path, errors: list[str]) -> None:
    readme = repo / "README.md"
    if not readme.exists():
        return

    text = read_text(readme)
    for marker in BADGE_MARKERS:
        if marker not in text:
            add_error(errors, repo, f"README.md missing badge marker {marker}")

    required_phrases = [
        "AI vibe coding",
        "SUPER Skills",
        "INSTALL.md",
    ]
    for phrase in required_phrases:
        if phrase not in text:
            add_error(errors, repo, f"README.md missing phrase: {phrase}")


def check_install(repo: Path, errors: list[str]) -> None:
    install = repo / "INSTALL.md"
    if not install.exists():
        return

    text = read_text(install)
    required_phrases = [
        "Download ZIP",
        "Install One Skill With A Terminal",
        "SKILL.md",
        "Compatibility",
    ]
    for phrase in required_phrases:
        if phrase not in text:
            add_error(errors, repo, f"INSTALL.md missing phrase: {phrase}")


def check_skill(repo: Path, errors: list[str]) -> None:
    skill = repo / "SKILL.md"
    if not skill.exists():
        return

    text = read_text(skill)
    if not text.startswith("---"):
        add_error(errors, repo, "SKILL.md missing front matter")
    if "name:" not in text or "description:" not in text:
        add_error(errors, repo, "SKILL.md missing name or description")

    module_dir = repo / "references" / "modules"
    if not module_dir.exists():
        add_error(errors, repo, "missing references/modules")
    elif not any(module_dir.glob("*.md")):
        add_error(errors, repo, "references/modules has no Markdown modules")


def check_product_manifest(repo: Path, errors: list[str]) -> None:
    manifest = repo / "product.json"
    if not manifest.exists():
        return

    try:
        data = json.loads(read_text(manifest))
    except json.JSONDecodeError as exc:
        add_error(errors, repo, f"product.json is invalid JSON: {exc}")
        return

    if data.get("version") != EXPECTED_VERSION:
        add_error(errors, repo, f"product.json version is not {EXPECTED_VERSION}")
    if data.get("skill_entrypoint") != "SKILL.md":
        add_error(errors, repo, "product.json skill_entrypoint is not SKILL.md")


def check_public_branding(repo: Path, errors: list[str]) -> None:
    files = list(repo.glob("*.md"))
    files += list((repo / "examples").glob("*.md")) if (repo / "examples").exists() else []

    for path in files:
        text = read_text(path).lower()
        for brand in FORBIDDEN_PUBLIC_BRANDS:
            if re.search(rf"\b{re.escape(brand)}\b", text):
                add_error(errors, repo, f"{path.name} contains platform-specific brand: {brand}")


def check_repo(repo: Path, required: list[str], errors: list[str]) -> None:
    check_required_files(repo, required, errors)
    check_version(repo, errors)
    check_readme(repo, errors)
    check_install(repo, errors)
    check_skill(repo, errors)
    check_product_manifest(repo, errors)
    check_public_branding(repo, errors)


def main() -> int:
    parser = argparse.ArgumentParser(description="Check SUPER Skills public-readiness.")
    parser.add_argument(
        "--products",
        type=Path,
        default=DEFAULT_PRODUCTS,
        help=f"Standalone products directory. Default: {DEFAULT_PRODUCTS}",
    )
    args = parser.parse_args()

    errors: list[str] = []

    check_repo(ROOT, REQUIRED_ROOT_FILES, errors)

    catalogue_skills = sorted(path for path in ROOT.glob("super-*") if path.is_dir())
    for skill in catalogue_skills:
        check_repo(skill, REQUIRED_CATALOGUE_SKILL_FILES, errors)

    if args.products.exists():
        for product in sorted(path for path in args.products.glob("super-*") if path.is_dir()):
            check_repo(product, REQUIRED_SKILL_FILES + ["product.json", "PUBLISHING.md"], errors)
    else:
        errors.append(f"missing products directory: {args.products}")

    if errors:
        print("Quality check failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    total = 1 + len(catalogue_skills)
    if args.products.exists():
        total += len(list(args.products.glob("super-*")))

    print(f"Quality check passed for {total} repositories/folders.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
