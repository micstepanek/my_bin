#!/usr/bin/env python3
import subprocess
title_command = 'xdotool getactivewindow getwindowname'
window_title = subprocess.check_output(title_command.split()).decode()
#window_title = "Kurose, James F._ Ross, Keith W. - Computer networking _ a top-down approach (2017).pdf - 23/867 (102 dpi)"
file_name, rest = window_title.rsplit(' - ', 1)
current_page = rest.split('/', 1)[0]
print(current_page)
#print(file_name)
find_command = 'find /home/h/Downloads/ /home/h/aa/ -xdev -name'
split_command = find_command.split()
split_command.append(file_name)
print(split_command)
path = subprocess.check_output(split_command).decode()
print(path)
directory = path.rsplit('/', 1)[0]
#subprocess.run(['urxvtc', '-hold', '-e', 'echo', directory, file_name, current_page])
#subprocess.run(['vifm_print', directory, file_name, '-pages', current_page])
subprocess.run(['urxvtc', '-e', 'vifm_print', directory, file_name, '-pages', current_page])
