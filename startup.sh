#!/usr/bin/env bash
i3-msg rename workspace to f
set_keyboard.sh &
nohup firefox &
#nohup sxhkd &
urxvtd --quiet --opendisplay --fork
i3tags.sh & disown
#nohup keylogger &
#xxkb &
#urxvtc -e echo 'keynav' && keynav &
#urxvt -e python3 /py/creativity.py
#xrdb ~/.Xresources &
#nohup urxvtc -e i3log &
#nohup blink &
feh --bg-tile ~/aa/background/pc_list.png
xset -dpms
xset s off
#del?#xrandr --output DP1 --brightness 1 && xrandr --output eDP1 --off
#i3-msg [class='Firefox'] move container to workspace f
