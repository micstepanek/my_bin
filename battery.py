#!/usr/bin/env python3
from subprocess import check_output, run 

def run_(command):
    run(command.split())

battery_bytes = check_output(['upower', '-i', '/org/freedesktop/UPower/devices/battery_BAT0'])
battery_string = battery_bytes.decode()
battery_list = battery_string.split('\n')
state = battery_list[11]
percentage = battery_list[20][1:]
percentage_int = int(percentage[-4:-1])
new_line = '''
'''
print(state)
print(percentage)
if 'discharging' not in state or 20 < percentage_int < 90:
    exit()
#elif 94 < percentage_int < 101:
#    run(['urxvtc', '-hold', '-e', 'echo', state, new_line, percentage])
elif -1 < percentage_int < 20:
    run_('i3-msg fullscreen disable')
    run(['urxvtc', '-hold', '-e', 'echo', state, new_line, percentage])
input()
