# Windows/KDE Muscle Memory for macOS (Karabiner-Elements)

This repository provides Karabiner-Elements complex modifications that bring Windows/KDE keyboard habits to macOS while keeping terminal safety in mind.

## Installation
1. Copy the desired profile JSON into Karabiner's complex modifications directory:
   ```bash
   cp profiles/windows-kde-macos/karabiner/windows_kde_on_macos.json ~/.config/karabiner/assets/complex_modifications/
   ```
2. Open **Karabiner-Elements** → **Complex Modifications** → **Add rule**.
3. Enable the rules from **"Windows/KDE muscle memory on macOS"**.

## Profiles
- `profiles/windows-kde-macos/karabiner/windows_kde_on_macos.json`: Primary profile with Windows/KDE mappings and terminal exceptions.

## Tooling
- `tools/validate_json.py`: Validate Karabiner JSON files for required keys and JSON correctness.
