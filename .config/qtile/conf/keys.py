# pylint: disable=invalid-name
import subprocess
from pathlib import Path
from libqtile import bar, layout, widget, hook, qtile
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.log_utils import logger

REC_PATH = Path('~/.local/share/qtile/REC').expanduser()

mod = "mod4"
terminal = guess_terminal()


def go_to_group(qqtile, group_name, screen):
    qqtile.focus_screen(screen)
    qqtile.groups_map[group_name].cmd_toscreen(toggle=False)
    qqtile.warp_to_screen()


@hook.subscribe.startup_once
def autostart():
    path = Path('~/.config/qtile/autostart.sh').expanduser()
    subprocess.call([path])


@hook.subscribe.client_focus
def check_recording(*args):
    logger.warning(qtile.current_screen.index)
    if qtile.current_screen.index == 1 and 'REC' == qtile.current_screen.group.name and qtile.current_screen.group.windows:
        if not REC_PATH.is_file():
            with REC_PATH.open('w', encoding='utf-8') as file:
                file.write('')
        logger.warning('warnin record')
    else:
        logger.warning('no record')
        REC_PATH.unlink(missing_ok=True)


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

    Key([mod, "control"], "Return",
        lazy.spawn("dm-run"),
        desc="Launch dmenu"
    ),

    Key([mod, "shift"], "Return",
        lazy.spawn("ulauncher-toggle"),
        desc="Launch ulauncher"
    ),

    Key([mod, "mod1"], "h", lazy.to_screen(0)),
    Key([mod, "mod1"], "j", lazy.to_screen(1)),

    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -c 0 set Master 2db+")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -c 0 set Master 2db-")),

    Key([mod], "F10", lazy.spawn("xbacklight -inc 10")),
    Key([mod], "F9", lazy.spawn("xbacklight -dec 10")),

]


groups = [Group("DEV", layout='monadtall'),
          Group("WWW", layout='monadtall'),
          Group("SYS", layout='monadtall'),
          Group("DOC", layout='monadtall'),
          Group("CHAT", layout='monadtall'),
          Group("MUS", layout='monadtall'),
          Group("VID", layout='monadtall'),
          Group("GFX", layout='floating')]


for no, i in enumerate(groups, 1):
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
               [mod],
               str(no),
               lazy.group[i.name].toscreen(),
               desc=f"Switch to group {i.name}",
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                str(no),
                lazy.window.togroup(i.name, switch_group=True),
                desc=f"Switch to & move focused window to group {i.name}",
            ),
        ]
    )

groups.append(Group("REC", layout='monadtall'))
keys.append(Key([mod], "0", lazy.function(go_to_group, "REC", 1)))

colors = [["#282c34", "#282c34"],
          ["#1c1f24", "#1c1f24"],
          ["#dfdfdf", "#dfdfdf"],
          ["#ff6c6b", "#ff6c6b"],
          ["#98be65", "#98be65"],
          ["#da8548", "#da8548"],
          ["#51afef", "#51afef"],
          ["#c678dd", "#c678dd"],
          ["#46d9ff", "#46d9ff"],
          ["#a9a1e1", "#a9a1e1"]]



layout_theme = {"border_width": 2,
                "margin": 8,
                "border_focus": "e1acff",
                "border_normal": "1D2330"
                }


layouts = [
    #layout.Columns(**layout_theme),
    #layout.Max(**layout_theme),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    layout.Bsp(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.Max(**layout_theme),
    layout.Stack(**layout_theme),
    #layout.RatioTile(**layout_theme),
    #layout.Tile(**layout_theme),
    #layout.TreeTab(**layout_theme),
    #layout.VerticalTile(**layout_theme),
    layout.Floating(**layout_theme),
]

widget_defaults = dict(
    # font="hack",
    font="Ubuntu Bold",
    fontsize=16,
    padding=2,
    background=colors[0],
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.CurrentLayoutIcon(
                       foreground = colors[2],
                       background = colors[0],
                       padding = 0,
                       scale = 0.7
                       ),
                widget.GroupBox(
                       borderwidth = 3,
                       active = colors[2],
                       inactive = colors[7],
                       highlight_color = colors[1],
                       highlight_method = "line",
                       this_current_screen_border = colors[6],
                       this_screen_border = colors [4],
                       other_current_screen_border = colors[6],
                       other_screen_border = colors[4],
                       foreground = colors[2],
                       ),
                widget.WindowName(padding=20),
                widget.Systray(),
                widget.Clock(format="%Y-%m-%d %a %H:%M"),
            ],
            26,
        ),
    ),
    Screen(
        top=bar.Bar(
            [
                widget.CurrentLayoutIcon(
                       foreground = colors[2],
                       background = colors[0],
                       padding = 0,
                       scale = 0.7
                       ),
                widget.GroupBox(
                       borderwidth = 3,
                       active = colors[2],
                       inactive = colors[7],
                       highlight_color = colors[1],
                       highlight_method = "line",
                       this_current_screen_border = colors[6],
                       this_screen_border = colors [4],
                       other_current_screen_border = colors[6],
                       other_screen_border = colors[4],
                       foreground = colors[2],
                       ),
                widget.WindowName(padding=20),
                widget.Clock(format="%Y-%m-%d %a %H:%M"),
            ],
            26,
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    border_width=2,
    #margin": 8,
    border_focus="e1acff",
    border_normal="1D2330",
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        #Match(title="ulauncher"),
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
