#!/bin/sh

userresources=$HOME/.Xresources
usermodmap=$HOME/.Xmodmap
sysresources=/etc/X11/xinit/.Xresources
sysmodmap=/etc/X11/xinit/.Xmodmap

# merge in defaults and keymaps
if [ -f $sysresources ]; then
    xrdb -merge $sysresources
fi

if [ -f $sysmodmap ]; then
    xmodmap $sysmodmap
fi

if [ -f "$userresources" ]; then
    xrdb -merge "$userresources"
fi

if [ -f "$usermodmap" ]; then
    xmodmap "$usermodmap"
fi

# start some nice programs

if [ -d /etc/X11/xinit/xinitrc.d ] ; then
 for f in /etc/X11/xinit/xinitrc.d/?*.sh ; do
  [ -x "$f" ] && . "$f"
 done
 unset f
fi

setxkbmap de

xrandr --output Virtual-1 --mode 1920x1080

conky -c $HOME/.config/conky/qtile/doom-one-01.conkyrc
volumeicon &

### UNCOMMENT ONLY ONE OF THE FOLLOWING THREE OPTIONS! ###
# 1. Uncomment to restore last saved wallpaper
# xargs xwallpaper --stretch < ~/.cache/wall &
# 2. Uncomment to set a random wallpaper on login
find /usr/share/backgrounds/axju/ -type f | shuf -n 1 | xargs xwallpaper --stretch &
# 3. Uncomment to set wallpaper with nitrogen
# nitrogen --restore &

exec qtile start

