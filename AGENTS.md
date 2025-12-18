# Project Agent Instructions
- Keep all Karabiner mappings documented alongside the corresponding profile docs.
- Group configuration rules by profile to make future expansions clearer.
- Keep Terminal/iTerm exceptions explicitly listed in both config and docs.
- Prefer minimal, reversible remaps; avoid overloading behaviors.
- Never break Ctrl+C in Terminal/iTerm unless explicitly requested.
- Run `python tools/validate_json.py` after changing any Karabiner JSON to ensure required fields stay aligned with current Karabiner-Elements expectations.
