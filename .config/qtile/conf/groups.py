from libqtile.config import Group, Key
from libqtile.lazy import lazy

from .defaults import mod


groups = [Group("DEV", layout='monadtall'), Group("WWW", layout='monadtall'), Group("SYS", layout='monadtall'),
          Group("DOC", layout='monadtall'), Group("MUS", layout='monadtall'), Group("REC", layout='monadtall')]

group_keys = []
for no, i in enumerate(groups, 1):
    group_keys.extend(
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
