#!/usr/bin/env python3
"""Validate Karabiner-Elements complex modification JSON files.

Checks that each JSON file under any `karabiner` directory is valid JSON and
contains the required top-level keys: `title` and `rules`.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Iterable

REQUIRED_KEYS = {"title", "rules"}


def find_karabiner_json_files(root: Path) -> Iterable[Path]:
    for path in root.rglob("*.json"):
        if "karabiner" in path.parts:
            yield path


def validate_file(path: Path) -> list[str]:
    errors: list[str] = []
    try:
        with path.open("r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as exc:  # noqa: BLE001 - want to report any JSON parsing error
        errors.append(f"{path}: invalid JSON ({exc})")
        return errors

    missing = REQUIRED_KEYS - set(data.keys())
    if missing:
        errors.append(f"{path}: missing required keys: {', '.join(sorted(missing))}")
    return errors


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    errors: list[str] = []

    for json_file in find_karabiner_json_files(root):
        errors.extend(validate_file(json_file))

    if errors:
        for err in errors:
            print(err)
        return 1

    print("All Karabiner JSON files are valid.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
