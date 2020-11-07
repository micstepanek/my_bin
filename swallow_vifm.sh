#!/usr/bin/env bash
VIFM=$(xdotool getactivewindow)
i3-msg [id="$VIFM"] move window to workspace hidden
$@
i3-msg [id="$VIFM"] move window to workspace current
