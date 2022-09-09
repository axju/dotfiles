# pylint: disable=invalid-name
from libqtile.config import Key, Click, Drag
from libqtile.lazy import lazy

from .defaults import mod, terminal


keys = [
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),

    Key([mod, "shift"], "Left", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),

    Key([mod, "control"], "Left", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "Right", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "Down", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "Up", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),

    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    Key([mod, "control"], "Return", lazy.spawn("dm-run"), desc="Launch dmenu"),
    Key([mod, "shift"], "Return", lazy.spawn("ulauncher-toggle"), desc="Launch ulauncher"),

    Key([mod, "mod1"], "h", lazy.to_screen(0)),
    Key([mod, "mod1"], "j", lazy.to_screen(1)),

    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -c 0 set Master 2db+")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -c 0 set Master 2db-")),

    Key([mod], "F10", lazy.spawn("xbacklight -inc 10")),
    Key([mod], "F9", lazy.spawn("xbacklight -dec 10")),
]


# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]
