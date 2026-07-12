# Argus

Argus quietly records which app you're using every 5 seconds.

**No cloud. No account. No tracking — of you. Your data stays on your machine.**

## What is TUI?

TUI stands for **Text-based User Interface**. Instead of buttons and windows, it draws an interactive interface using plain text and characters, right inside your terminal. Think of it like a dashboard that lives in your command-line — no GUI window needed.

For a system like Argus, this matters: it means one command (`argus tui`) starts both the tracker and the dashboard at the same time, no background service setup required. It's lightweight and keyboard-driven.

## Features

- **Every 5 seconds** — records the active app, window title, and timestamps silently in the background
- **Auto-categorises** — groups time into Browser, IDE, Communication, Gaming, Media, and more
- **Local-only** — all data stored in a simple SQLite file on your computer; nothing sent anywhere
- **Cross-platform** — works on Windows and Linux

## Screenshots
Functional screenshots
<img width="3200" height="1904" alt="1" src="https://github.com/user-attachments/assets/017a3611-0ecd-49d2-bc9e-56a6133ec6ed" />
<img width="3200" height="1904" alt="2" src="https://github.com/user-attachments/assets/db1c7762-a1f4-4823-928c-ba378c52d601" />

Theme changes
![Argus TUI dashboard — Gruvbox theme](docs/screenshots/tui-dashboard-gruvbox.png)

![Argus TUI dashboard — teal dark theme](docs/screenshots/tui-dashboard-teal.png)

---

## Design rationale

```
Requirements Definition → Basic System Design → Detailed System Design
```

---

### Requirements Definition

**functionality requirement**

| # | Feature | Details |
|---|---|---|
| R1 | Tracks your active window | Every 5 seconds, silently |
| R2 | Auto-categorises apps | Browser, IDE, Terminal, Chat, etc. — 11 categories |
| R3 | Stores data locally | SQLite file, no server, no account |
| R4 | TUI runs the tracker too | `argus tui` starts both dashboard and tracker — no daemon needed |
| R5 | Auto-starts on login | OS-specific, one command to enable |
| R6 | 6 UI languages | Press `L` in the TUI to switch |
| R7 | 12 colour themes | Press `T` in the TUI to cycle |

**Non-functionality requirement :**

| # | Quality | Details |
|---|---|---|
| R8 | Privacy | All data stays on your machine — zero network calls |
| R9 | Cross-platform | Windows, Linux |
| R10 | Lightweight | Uses less than 1% CPU on normal desktop use |
| R11 | Idle detection | Pauses recording when you're away |
| R12 | Small storage | One row per 5-second snapshot |
| R13 | Modular | Clean layer separation for easy maintenance |

---

**Project structure:**

```
src/
├── main.py               # CLI entry point — delegates to argus/
└── argus/
    ├── __init__.py       # version
    ├── config.py         # constants, category rules, settings
    ├── i18n.py           # UI strings (6 languages)
    ├── tracker.py        # active window + idle detection (per OS)
    ├── storage.py        # SQLite read/write
    ├── daemon.py         # background polling loop
    ├── report.py         # daily/weekly/status reports
    ├── tui.py            # live dashboard
    └── autostart.py      # login auto-start (per OS)
build.py                  # PyInstaller build script → dist/argus[.exe]
requirements.txt          # runtime dependencies
requirements-dev.txt      # runtime + build tools
dist/                     # compiled executables (git-ignored)
```

**TUI — Keyboard shortcuts:**

| Key | Action |
|---|
| `R` | Refresh data immediately |
| `T` | Cycle through colour themes |
| `L` | Cycle through UI languages (6 languages) |
| `A` | Toggle Auto Start |
| `O` | Open the data folder |
| `[` `]` | Previous / next day |
| `{` `}` | Previous / next week |
| `Q` | Quit |

`argus tui` opens a live full-terminal dashboard powered by [Textual](https://textual.textualize.io/). It also runs the tracker in the background — no separate `start` command needed.



