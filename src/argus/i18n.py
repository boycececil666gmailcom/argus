"""Internationalisation — UI string catalogue for Argus.

Supported language codes
------------------------
en  English
"""

from __future__ import annotations

# region Language registry

LANGUAGES: dict[str, str] = {
    "en": "English",
}

# endregion

# region String catalogue

STRINGS: dict[str, dict[str, str]] = {
    # ── English ───────────────────────────────────────────────────────────────
    "en": {
        "subtitle":             "Activity Tracker",
        "help":                 "Help",
        "get_started":          "Get Started",
        "app":                  "App",
        "time":                 "Time",
        "bar":                  "Bar",
        "pct":                  "%",
        "category":             "Category",
        "day":                  "Day",
        "active":               "Active",
        "top_app":              "Top App",
        "window":               "Window",
        "idle_header":          "Idle",
        "snapshots":            "Snapshots",
        "today_label":          "Today — {}",
        "week_label":           "This Week — {} – {}",
        "total_active_today":   "Total active today: {}  ·  {} snapshots",
        "no_data_today":        "No data recorded today.",
        "weekly_total":         "Weekly active total: {}",
        "no_data_week":         "No data for this week.",
        "day_past_label":       "Day — {}",
        "week_past_label":      "{} – {}",
        "nav_today":            "Today",
        "nav_this_week":        "This week",
        "open_db_folder":       "Open saved data folder",
        "auto_start_on":        "Auto Start  ON",
        "auto_start_off":       "Auto Start  OFF",
        "autostart_enabled":    "Auto Start enabled — Argus will launch at login.",
        "autostart_disabled":   "Auto Start disabled.",
        "autostart_error":      "Could not toggle Auto Start: {}",
        "no_window":            "No active window detected.",
        "idle":                 "IDLE — {}s",
        "active_sec":           "{}s active",
    },
}

# endregion

# region State

_current_lang: str = "en"

# endregion

# region Public API


def set_language(code: str) -> None:
    """Set the active language. Silently ignores unknown codes."""
    global _current_lang
    if code in STRINGS:
        _current_lang = code


def get_language() -> str:
    """Return the active language code (e.g. 'en')."""
    return _current_lang


def cycle_language() -> str:
    """Advance to the next language in rotation and return the new code."""
    global _current_lang
    codes = list(LANGUAGES)
    idx = codes.index(_current_lang) if _current_lang in codes else 0
    _current_lang = codes[(idx + 1) % len(codes)]
    return _current_lang


def t(key: str, *args: object) -> str:
    """Translate *key* in the active language, optionally formatting with *args*.

    Falls back to the English catalogue, then to the bare key string.
    """
    catalogue = STRINGS.get(_current_lang, STRINGS["en"])
    template = catalogue.get(key) or STRINGS["en"].get(key) or key
    return template.format(*args) if args else template


# endregion
