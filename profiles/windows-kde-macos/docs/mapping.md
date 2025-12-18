# Windows/KDE Muscle Memory on macOS (Karabiner-Elements)

This profile mirrors familiar Windows/KDE shortcuts on macOS with reversible remaps. All changes are grouped per profile, and terminal exceptions are called out explicitly.

## Mapping overview

### Command-style shortcuts outside terminals
- **Ctrl+C/V/X/Z/A/S/F/W/T → Cmd+C/V/X/Z/A/S/F/W/T** (blocked in Terminal/iTerm to preserve Unix signals)

### Terminal exceptions
- **Ctrl+Shift+C → Cmd+C** in Terminal/iTerm
- **Ctrl+Shift+V → Cmd+V** in Terminal/iTerm
- **Ctrl+C** remains the default interrupt (never remapped)

### Windows key launcher habits
- **Win+E → open Finder** (`open -a Finder`)
- **Win+R → Spotlight** (Cmd+Space)
- **Win+L → Lock Screen** (Ctrl+Cmd+Q)

### Alt-based shortcuts
- **Alt+F4 → Quit app** (Cmd+Q)
- **Alt+Space → Spotlight** (Cmd+Space)
- **Alt+F2 → Spotlight** (Cmd+Space)
- **Ctrl+Alt+T → Open Terminal** (`open -a Terminal`)

### Navigation and print screen
- **Home → Cmd+Left** (line start)
- **End → Cmd+Right** (line end)
- **PageUp/PageDown → Native Page Up/Down**
- **Print Screen → macOS screenshot** (Cmd+Shift+3)

## Rationale
- Keep muscle memory consistent when moving between Windows/KDE and macOS.
- Avoid conflicting with built-in terminal interrupts; clipboard shortcuts in terminals require Shift to avoid breaking Ctrl+C.
- Use minimal, reversible remaps that align with macOS defaults (e.g., Spotlight via Cmd+Space, Finder launch, and standard quit behavior).
- Document every mapping alongside the profile for clarity and future profile additions.
