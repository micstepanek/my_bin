#!/usr/bin/env python3
import subprocess
get_title_command = 'xdotool getactivewindow getwindowname'
title = subprocess.check_output(get_title_command.split()).decode()
file = title.rsplit(' - ', 1)[0]
#file = 'Kurose, James F._ Ross, Keith W. - Computer networking _ a top-down approach (2017).pdf'
get_path_string = 'find /home/h/Downloads/ /home/h/aa/ -xdev -name'
get_path_list = get_path_string.split()
get_path_list.append(file)
path = subprocess.check_output(get_path_list).decode()
directory = path.rsplit('/', 1)[0]
#subprocess.run(['urxvtc', '-hold', '-e', 'echo', directory, file])
subprocess.run(['urxvtc', '-e', 'print_vifm.py', directory, file])
