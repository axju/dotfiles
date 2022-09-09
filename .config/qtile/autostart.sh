#!/usr/bin/env bash

nm-applet --no-agent &

volumeicon &
cbatticon &
synology-drive &
ulauncher --hide-window --no-window-shadow &
unclutter --jitter 200 &

find /usr/share/backgrounds/ -type f | shuf -n 1 | xargs xwallpaper --stretch &
conky -c $HOME/.config/conky/qtile/doom-one-01.conkyrc

libreoffice ~/sync/work/files/2022.ods &

python $HOME/.config/qtile/record.py &

