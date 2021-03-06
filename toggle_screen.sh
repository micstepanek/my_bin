#!/usr/bin/env python3.6
from subprocess import run, check_output
import time

def run_(command):
    run(command.split())

def battery_ok():
    battery_command = 'upower -i /org/freedesktop/UPower/devices/battery_BAT0'
    battery_bytes = check_output(battery_command.split())
    battery_string = battery_bytes.decode()
    battery_list = battery_string.split('\n')
    state = battery_list[11]
    percentage = battery_list[20]
#battery_list = battery_string.split('\n')
#battery_lists = [x.split(':') for x in battery_list]
#interesting = ('    percentage','    state')
#[print(x[0],x[-1]) for x in battery_lists if x[0] in interesting]

    if 'discharging' in state:
        run_('i3-msg fullscreen disable')
        print(state)
        print(percentage)
        print('turning off display in')
        for i in reversed(range(2)):
            print(i)
            time.sleep(1)

        #from readchar import readchar
        #reply = readchar()
        return True
    else:
        return True



#screens
def external_screen_connected():
    return b'\nDP1 connected' in xrandr

def external_screen_on():
    return b'\nDP1 connected 1' in xrandr 

def laptop_screen_on():
    return b'\neDP1 connected primary 1' in xrandr

def turn(screen, change):
    translation = {'external_screen':'DP1',
                   'laptop_screen':'eDP1',
                   'off':'--off',
                   'on':'--auto'}
    xrandr_output = translation[screen]
    xrandr_option = translation[change]
    run(['xrandr','--output', xrandr_output, xrandr_option]) 

# should he do something in the meantime
#input('What should I do?')
# backup, update ?

xrandr = check_output('xrandr')

if external_screen_connected():
    if external_screen_on():
        if battery_ok():
            turn('external_screen', 'off')
    else:
        turn('external_screen', 'on')
        if laptop_screen_on():
            turn('laptop_screen', 'off')
elif laptop_screen_on():
    if battery_ok():
        turn('laptop_screen', 'off')
else:
    turn('laptop_screen', 'on')
# do in the meantime
