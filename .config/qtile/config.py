# pylint: disable=invalid-name
from libqtile import qtile
from libqtile.config import Key
from libqtile.lazy import lazy
from libqtile.log_utils import logger

from conf.defaults import REC_TRIGGER, mod, terminal
from conf.keys import keys, mouse
from conf.groups import groups, group_keys
from conf.layouts import layouts, floating_layout
from conf.screens import screens
from conf.hooks import *


@hook.subscribe.client_focus
def check_recording(*args):
    logger.warning(qtile.current_screen.index)
    if qtile.current_screen.index == 1 and 'REC' == qtile.current_screen.group.name and qtile.current_screen.group.windows:
        if not REC_TRIGGER.is_file():
            with REC_TRIGGER.open('w', encoding='utf-8') as file:
                file.write('')
        logger.warning('warnin record')
    else:
        logger.warning('no record')
        REC_TRIGGER.unlink(missing_ok=True)


def go_to_group(qqtile, group_name, screen):
    qqtile.focus_screen(screen)
    qqtile.groups_map[group_name].cmd_toscreen(toggle=False)
    qqtile.warp_to_screen()


keys.append(Key([mod], "0", lazy.function(go_to_group, "REC", 1)))
keys.extend(group_keys)

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False

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
