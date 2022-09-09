import subprocess
from pathlib import Path
from libqtile import hook


@hook.subscribe.startup_once
def autostart():
    path = Path('~/.config/qtile/autostart.sh').expanduser()
    subprocess.call([path])
