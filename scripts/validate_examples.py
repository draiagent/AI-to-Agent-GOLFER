#!/usr/bin/env python3
"""Validate example YAML files against the Enterprise AI Golfer schemas."""

from pathlib import Path
import sys

import yaml
from jsonschema import Draft202012Validator, FormatChecker


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_DIR = ROOT / "schemas"
EXAMPLES_DIR = ROOT / "examples"
KINDS = ("vad", "memory", "decision", "workflow", "verify", "vac", "brand")


def load_yaml(path: Path):
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def validate() -> list[str]:
    failures: list[str] = []
    checked = 0
    for kind in KINDS:
        schema_path = SCHEMA_DIR / f"{kind}.schema.yaml"
        schema = load_yaml(schema_path)
        Draft202012Validator.check_schema(schema)
        validator = Draft202012Validator(schema, format_checker=FormatChecker())
        matches = sorted(EXAMPLES_DIR.glob(f"**/{kind}.yaml"))
        if not matches:
            failures.append(f"missing example: {kind}.yaml")
            continue
        for example_path in matches:
            checked += 1
            for error in sorted(validator.iter_errors(load_yaml(example_path)), key=lambda item: list(item.path)):
                location = ".".join(str(part) for part in error.path) or "<root>"
                failures.append(f"{example_path.relative_to(ROOT)}:{location}: {error.message}")
    print(f"Validated {checked} example files across {len(KINDS)} schemas.")
    return failures


if __name__ == "__main__":
    problems = validate()
    if problems:
        print("\n".join(f"ERROR: {item}" for item in problems), file=sys.stderr)
        raise SystemExit(1)
    print("All examples are valid.")
