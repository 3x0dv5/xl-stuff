"""Validate Karabiner-Elements complex modification JSON files.

Ensures Karabiner JSON in this repo conforms to the latest expected structure:
- valid JSON with `title` and `rules` keys
- each rule has a description and manipulators
- each manipulator has required `from` and output definitions.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Iterable

REQUIRED_TOP_LEVEL_KEYS = {"title", "rules"}
FROM_KEY_OPTIONS = {"key_code", "consumer_key_code", "pointing_button"}
OUTPUT_ACTION_KEYS = {
    "key_code",
    "consumer_key_code",
    "pointing_button",
    "shell_command",
    "select_input_source",
    "mouse_key",
    "set_variable",
}
OUTPUT_FIELDS = ["to", "to_if_alone", "to_after_key_up", "to_delayed_action"]


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

    if missing := REQUIRED_TOP_LEVEL_KEYS - set(data.keys()):
        errors.append(
            f"{path}: missing required top-level keys: {', '.join(sorted(missing))}"
        )

    if not isinstance(data.get("rules"), list) or not data.get("rules"):
        errors.append(f"{path}: `rules` must be a non-empty list.")
        return errors

    for rule_index, rule in enumerate(data["rules"], start=1):
        errors.extend(validate_rule(path, rule_index, rule))

    return errors


def validate_rule(path: Path, rule_index: int, rule: object) -> list[str]:
    errors: list[str] = []
    if not isinstance(rule, dict):
        errors.append(f"{path}: rule #{rule_index} is not an object.")
        return errors

    if "description" not in rule or not isinstance(rule.get("description"), str):
        errors.append(f"{path}: rule #{rule_index} is missing a string `description`.")

    manipulators = rule.get("manipulators")
    if not isinstance(manipulators, list) or not manipulators:
        errors.append(f"{path}: rule #{rule_index} must include a non-empty `manipulators` list.")
        return errors

    for manip_index, manipulator in enumerate(manipulators, start=1):
        errors.extend(
            validate_manipulator(
                path,
                rule_index,
                manip_index,
                rule.get("description", f"rule #{rule_index}"),
                manipulator,
            )
        )

    return errors


def validate_manipulator(
    path: Path,
    rule_index: int,
    manip_index: int,
    rule_description: str,
    manipulator: object,
) -> list[str]:
    errors: list[str] = []
    context = f"{path}: rule '{rule_description}' manipulator #{manip_index}"

    if not isinstance(manipulator, dict):
        errors.append(f"{context} is not an object.")
        return errors

    if not isinstance(manipulator.get("type"), str):
        errors.append(f"{context} is missing string `type`.")

    from_def = manipulator.get("from")
    if not isinstance(from_def, dict):
        errors.append(f"{context} is missing `from` object.")
    elif not any(key in from_def for key in FROM_KEY_OPTIONS):
        errors.append(
            f"{context} `from` must include one of: {', '.join(sorted(FROM_KEY_OPTIONS))}."
        )

    if not any(field in manipulator for field in OUTPUT_FIELDS):
        errors.append(
            f"{context} must include at least one output field: {', '.join(OUTPUT_FIELDS)}."
        )

    for field in ("to", "to_if_alone", "to_after_key_up"):
        if field in manipulator:
            validate_output_actions(manipulator[field], f"{context} `{field}`", errors)

    if "to_delayed_action" in manipulator:
        delayed = manipulator["to_delayed_action"]
        if not isinstance(delayed, dict):
            errors.append(f"{context} `to_delayed_action` must be an object.")
        else:
            for delayed_field in ("to_if_invoked", "to_if_canceled"):
                if delayed_field in delayed:
                    validate_output_actions(
                        delayed[delayed_field],
                        f"{context} `to_delayed_action.{delayed_field}`",
                        errors,
                    )

    return errors


def validate_output_actions(actions: object, label: str, errors: list[str]) -> None:
    if not isinstance(actions, list) or not actions:
        errors.append(f"{label} must be a non-empty list.")
        return

    for idx, action in enumerate(actions, start=1):
        if not isinstance(action, dict):
            errors.append(f"{label} entry #{idx} is not an object.")
            continue

        if not any(key in action for key in OUTPUT_ACTION_KEYS):
            errors.append(
                f"{label} entry #{idx} must include at least one of: {', '.join(sorted(OUTPUT_ACTION_KEYS))}."
            )


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
