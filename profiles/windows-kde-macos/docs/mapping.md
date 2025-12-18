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
| 13 | Ctrl+Shift+N | Cmd+Shift+N | New window/incognito (and Finder new folder) outside Terminal/iTerm |
| 14 | Ctrl+L | Cmd+L (or Cmd+Shift+G in Finder) | Focus location bar/search; Go to Folder path entry in Finder |
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
| 30 | Shift+Insert | Cmd+V | Paste everywhere |
| 31 | Ctrl+O | Cmd+S | Save outside Terminal/iTerm (nano WriteOut) |
| 32 | Ctrl+K | Cmd+X | Cut outside Terminal/iTerm (nano cut) |
| 33 | Ctrl+U | Cmd+V | Paste outside Terminal/iTerm (nano uncut) |
| 34 | Ctrl+\ | Cmd+Alt+F | Replace outside Terminal/iTerm (nano replace) |
| 35 | F10 | Cmd+Shift+N | New folder in Finder (Dolphin habit) |

### Command-style shortcuts outside terminals
- **Ctrl+C/V/X/Z/A/S/F/W/T → Cmd+C/V/X/Z/A/S/F/W/T** (blocked in Terminal/iTerm to preserve Unix signals)

- **Ctrl+Shift+F → Cmd+Shift+F** (find in project/code search)
- **Ctrl+Shift+P → Cmd+Shift+P** (command palette in editors/browsers)
- **Ctrl+Shift+T → Cmd+Shift+T** (reopen closed tab/file)
- **Ctrl+Shift+N → Cmd+Shift+N** (new incognito/private window or project; new folder in Finder)
- **F10 → Cmd+Shift+N** (new folder in Finder like Dolphin)
- **Ctrl+L → Cmd+L** (focus location bar / search field; Finder uses Cmd+Shift+G for editable path)
- **Ctrl+Y → Cmd+Shift+Z** (redo where macOS uses Cmd+Shift+Z)


### Terminal exceptions
- **Ctrl+Shift+C → Cmd+C** in Terminal/iTerm
- **Ctrl+Shift+V → Cmd+V** in Terminal/iTerm
- **Ctrl+C** remains the default interrupt (never remapped)
- **Shift+Insert → Cmd+V** everywhere, including Terminal/iTerm, to match Linux paste muscle memory

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

### Nano muscle memory outside Terminal/iTerm
- **Ctrl+O → Cmd+S** for save/write-out outside terminals
- **Ctrl+K → Cmd+X** for cut outside terminals
- **Ctrl+U → Cmd+V** for paste/uncut outside terminals
- **Ctrl+\ → Cmd+Option+F** for replace outside terminals

> Want nano's on-screen help to mirror those muscle-memory keys instead of the stock `^O`, `^K`, `^U`, and `^\\` labels? Add bindings like the following to `~/.nanorc` so the footer advertises Ctrl+S/K/U/\ while keeping the original functions:

```nanorc
bind ^S savefile main
bind ^K cut main
bind ^U uncut main
bind ^\\ replace main
```

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

## Dock options without admin rights
You can keep the stock Dock for stability and add a user-space taskbar-style dock without admin access by installing apps into `~/Applications` instead of `/Applications`:

- **uBar**: Windows-style taskbar that can show one icon per window, includes previews, and can place a bar on each display.
- **ActiveDock**: Customizable Dock replacement with per-window thumbnails, grouped apps, and multi-monitor placement options.
- **DockMate**: Adds hover previews and window lists to the built-in Dock; runs as a user app without needing elevated installation.
- **uDock**: Lightweight launcher/dock that lives in the menu bar or screen edge and works from a per-user install.
- **InfyniDock**: InfyniClick's dock/taskbar with window-level icons and multi-display placement; grab the GitHub release DMG/ZIP and drop it in `~/Applications` to avoid admin prompts.

> Tip: For any of these, dragging the app bundle to `~/Applications` avoids admin prompts while keeping them available to your user account.
