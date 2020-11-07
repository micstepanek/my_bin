#!/usr/bin/env python3
from i3ipc import Connection

i3 = Connection()
conf = i3.get_bar_config()
print(conf.mode)
if conf.mode == 'invisible':
    i3.command('bar mode dock')
else:
    i3.command('bar mode invisible')
