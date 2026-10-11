"""Write github-profile-3d-contrib settings from the profile's config.yml.

Keeps config.yml as the single source of truth: theme, username and motion
are read from there and translated into a single "normal" 3D theme with a
darkMode block, so one SVG (profile-3d-contrib/profile-space.svg) adapts to
GitHub's light and dark themes by itself.

Usage:
    python tools/theme_to_3d_settings.py [config.yml] [output.json]

Defaults write conf/github-profile-3d-contrib.json.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import yaml

from generator.config import ConfigError, validate_config
from generator.themes import get_theme, mix

SPANISH = {
    "commit": "Commits",
    "repo": "Repos",
    "review": "Revisiones",
    "pullreq": "PRs",
    "issue": "Incidencias",
    "contrib": "contribuciones",
}

# mix() interpolates accent over background: t=0 gives the background, t=1 the
# accent. The five steps are the five contribution levels (NONE..FOURTH).
RAMP_STEPS = (0.12, 0.30, 0.52, 0.76, 1.0)


def _contrib_ramp(accent: str, background: str) -> list[str]:
    return [mix(accent, background, t) for t in RAMP_STEPS]


def to_3d_settings(theme, growing_animation: bool) -> dict:
    """A "normal" 3D theme for one palette mode."""
    return {
        "type": "normal",
        "backgroundColor": theme.bg,
        "foregroundColor": theme.ink,
        # Amber for the dark headline counters, the deep-sky blue in light mode.
        "strongColor": theme.dorm,
        "weakColor": theme.mute,
        # The radar echoes the violet arm; in light mode it turns blue.
        "radarColor": theme.dust[1][0],
        "growingAnimation": growing_animation,
        "contribColors": _contrib_ramp(theme.now, theme.bg),
        "l10n": SPANISH,
    }


def main(argv=None) -> int:
    args = list(argv if argv is not None else sys.argv[1:])
    config_path = ROOT / (args[0] if args else "config.yml")
    out_path = ROOT / (args[1] if len(args) > 1 else "conf/github-profile-3d-contrib.json")

    try:
        with open(config_path, encoding="utf-8") as handle:
            config = validate_config(yaml.safe_load(handle))
    except (ConfigError, OSError, yaml.YAMLError) as error:
        print(f"Invalid config: {error}", file=sys.stderr)
        return 1

    themes = config["themes"]
    # Hex overrides only paint the dark palette; light mode is the fixed
    # deep-sky "paper" palette, so the 3D matches how galaxy-profile itself renders.
    dark = get_theme(themes["dark"], "dark", themes["overrides"])
    light = get_theme(themes["light"], "light")

    settings = to_3d_settings(light, growing_animation=config["motion"])
    settings["fileName"] = "profile-space.svg"
    settings["darkMode"] = to_3d_settings(dark, growing_animation=config["motion"])

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(
        json.dumps([settings], ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"Wrote {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())