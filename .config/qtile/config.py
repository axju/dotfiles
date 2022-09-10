# pylint: disable=invalid-name
from pathlib import Path
from datetime import datetime
from libqtile import qtile
from libqtile.log_utils import logger

from conf.keys import keys, mouse
from conf.groups import groups, group_keys
from conf.layouts import layouts, floating_layout
from conf.screens import screens, widget_defaults, extension_defaults
from conf.hooks import *


REC_TRIGGER = Path('~/.local/share/qtile/REC').expanduser()
REC_STORAGE = Path('~/records/raw/' + datetime.now().strftime('%Y/%m/%d')).expanduser()
REC_SCREEN = 1
REC_GROUPS = ['REC']


@hook.subscribe.client_focus
def check_recording(*args):
    logger.warning(qtile.current_screen.index)
    if qtile.current_screen.index == REC_SCREEN and qtile.current_screen.group.windows and qtile.current_screen.group.name in REC_GROUPS:
        if not REC_TRIGGER.is_file():
            with REC_TRIGGER.open('w', encoding='utf-8') as file:
                file.write('')
        logger.warning('warnin record')
    else:
        logger.warning('no record')
        REC_TRIGGER.unlink(missing_ok=True)


keys.extend(group_keys)

dgroups_key_binder = None
dgroups_app_rules = []
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False

auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wl_input_rules = None
wmname = "LG3D"
