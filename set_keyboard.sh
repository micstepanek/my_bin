#!/usr/bin/env bash

#setxkbmap jp -print
#read
setxkbmap mc
#setxkbmap mc -print
#setxkbmap -print -verbose 10
#setxkbmap mus,mc -option caps:escape,altwin:swap_lalt_lwin,grp:lalt_toggle && xmodmap ~/.Xmodmap
setxkbmap mc -option lv5:rwin_switch_lock -print && xmodmap ~/aa/keyboard/Xmodmap && echo xmodmap success
#setxkbmap mus -option  caps:escape,grp:lwin_toggle && xmodmap ~/.Xmodmap
#setxkbmap -print -verbose 10

