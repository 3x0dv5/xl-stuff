# Windows/KDE Muscle Memory on macOS (Karabiner-Elements)

This profile mirrors familiar Windows/KDE shortcuts on macOS with reversible remaps. All changes are grouped per profile, and terminal exceptions are called out explicitly.

## Mapping overview

| row_number | kde | macos | short description |
| --- | --- | --- | --- |
| 1 | Ctrl+C | Cmd+C | Copy outside Terminal/iTerm |
| 2 | Ctrl+V | Cmd+V | Paste outside Terminal/iTerm |
| 3 | Ctrl+X | Cmd+X | Cut outside Terminal/iTerm |
| 4 | Ctrl+Z | Cmd+Z | Undo outside Terminal/iTerm |
| 5 | Ctrl+A | Cmd+A | Select all outside Terminal/iTerm |
| 6 | Ctrl+S | Cmd+S | Save outside Terminal/iTerm |
| 7 | Ctrl+F | Cmd+F | Find outside Terminal/iTerm |
| 8 | Ctrl+W | Cmd+W | Close tab outside Terminal/iTerm |
| 9 | Ctrl+T | Cmd+T | New tab outside Terminal/iTerm |
| 10 | Ctrl+Shift+F | Cmd+Shift+F | Project/code search outside Terminal/iTerm |
| 11 | Ctrl+Shift+P | Cmd+Shift+P | Command palette outside Terminal/iTerm |
| 12 | Ctrl+Shift+T | Cmd+Shift+T | Reopen closed tab/file outside Terminal/iTerm |
| 13 | Ctrl+Shift+N | Cmd+Shift+N | New window/incognito outside Terminal/iTerm |
| 14 | Ctrl+L | Cmd+L | Focus location bar or search field |
| 15 | Ctrl+Y | Cmd+Shift+Z | Redo outside Terminal/iTerm |
| 16 | Ctrl+Shift+C | Cmd+C | Copy in Terminal/iTerm without altering Ctrl+C |
| 17 | Ctrl+Shift+V | Cmd+V | Paste in Terminal/iTerm |
| 18 | Win+E | Finder | Open Finder from Windows launcher habit |
| 19 | Win+R | Cmd+Space | Spotlight/launcher from Windows habit |
| 20 | Win+L | Ctrl+Cmd+Q | Lock screen |
| 21 | Alt+F4 | Cmd+Q | Quit app |
| 22 | Alt+Space | Cmd+Space | Spotlight/launcher |
| 23 | Alt+F2 | Cmd+Space | Spotlight/launcher |
| 24 | Ctrl+Alt+T | Terminal | Open Terminal |
| 25 | Home | Cmd+Left | Jump to line start |
| 26 | End | Cmd+Right | Jump to line end |
| 27 | PageUp | PageUp | Preserve native Page Up |
| 28 | PageDown | PageDown | Preserve native Page Down |
| 29 | Print Screen | Cmd+Shift+3 | Screenshot |

### Command-style shortcuts outside terminals
- **Ctrl+C/V/X/Z/A/S/F/W/T → Cmd+C/V/X/Z/A/S/F/W/T** (blocked in Terminal/iTerm to preserve Unix signals)

- **Ctrl+Shift+F → Cmd+Shift+F** (find in project/code search)
- **Ctrl+Shift+P → Cmd+Shift+P** (command palette in editors/browsers)
- **Ctrl+Shift+T → Cmd+Shift+T** (reopen closed tab/file)
- **Ctrl+Shift+N → Cmd+Shift+N** (new incognito/private window or project)
- **Ctrl+L → Cmd+L** (focus location bar / search field)
- **Ctrl+Y → Cmd+Shift+Z** (redo where macOS uses Cmd+Shift+Z)


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

## App coverage notes
- Non-terminal apps (e.g., PyCharm, Visual Studio Code, Chrome/DevTools, Office apps) inherit the Windows/KDE-style Ctrl and Win/Alt shortcuts automatically.
- Terminal-safe behavior currently targets standalone Terminal and iTerm. Integrated terminals inside other apps will receive the Ctrl→Cmd mappings; add their bundle identifiers to the exclusion list if you prefer native terminal shortcuts there.

## Implementation note
- Karabiner-Elements remaps keys in macOS user space by intercepting HID events; it does not modify keyboard firmware or hardware-level mappings, so the changes are reversible by disabling or removing the profile.
