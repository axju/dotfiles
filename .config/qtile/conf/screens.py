from libqtile import bar, widget
from libqtile.config import Screen


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