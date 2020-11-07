#!/usr/bin/env python3
#
from i3ipc import Connection
i3 = Connection()
window_tree = i3.get_tree()
focused_window = window_tree.find_focused()
clazz = focused_window.window_class
title = focused_window.window_title
if clazz == "MuPDF":
    i3.command('mode mupdf') 
elif title == "mtool":
    i3.command('mode mtool')
elif clazz == "Firefox":
    i3.command('mode firefox command') 
elif clazz == "Chromium-browser":
    i3.command('mode chromium') 
else:
    i3.command('mode other')
#i3.command('exec xdotool mousemove 1920 1080') 
