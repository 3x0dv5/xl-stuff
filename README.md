# Windows/KDE Muscle Memory for macOS (Karabiner-Elements)

This repository provides Karabiner-Elements complex modifications that bring Windows/KDE keyboard habits to macOS while keeping terminal safety in mind.

## Installation
1. Copy the desired profile JSON into Karabiner's complex modifications directory:
   ```bash
   cp profiles/windows-kde-macos/karabiner/windows_kde_on_macos.json ~/.config/karabiner/assets/complex_modifications/
   ```
2. Open **Karabiner-Elements** → **Complex Modifications** → **Add rule**.
3. Enable the rules from **"Windows/KDE muscle memory on macOS"**.

## Application coverage
- The mappings are global for non-terminal apps, so editors like **PyCharm**, **Visual Studio Code**, and browsers such as **Chrome** (including DevTools) pick up the Windows/KDE-style shortcuts automatically.
- Terminal-safe handling is limited to the standalone **Terminal** and **iTerm** apps to preserve Ctrl+C as an interrupt. Integrated terminals inside other apps will still receive the remaps; add those bundle identifiers to the exclusion list in the JSON if you prefer native terminal behavior.

### Editor and browser-friendly additions
- **Ctrl+Shift+F/P/T/N** → **Cmd+Shift+F/P/T/N** for project search, command palette, reopen tab/file, and new incognito/private window or project.
- **Ctrl+L** → **Cmd+L** to jump focus to the address/search bar.
- **Ctrl+Y** → **Cmd+Shift+Z** for redo where macOS expects Cmd+Shift+Z.

## How the remapping works
- Karabiner-Elements runs in user space on macOS and intercepts keyboard events before they reach apps; it does **not** flash firmware or alter hardware-level mappings.
- Rules can be toggled or removed at any time from Karabiner's UI, making the changes fully reversible without affecting the keyboard itself.

## Profiles
- `profiles/windows-kde-macos/karabiner/windows_kde_on_macos.json`: Primary profile with Windows/KDE mappings and terminal exceptions.

## Tooling
- `tools/validate_json.py`: Validate Karabiner JSON files for required keys and JSON correctness.
