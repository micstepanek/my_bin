#!/usr/bin/env python3
from shutil import copy
import os
import tty
import sys
new_file_name = input('create command:')
os.system('clear')
print('similar to:')
PATH = '/home/h/aa/bin'
os.chdir(PATH)
files = [f for f in os.listdir('.') if os.path.isfile(f)]
files.sort()
rest = [x + ' ' for x in files]
show = rest.copy()
show.append("")
h = len(show)//2
start = show[:h]
end = show[h:]
for i,row in enumerate(start):
    print('{0:28}{1}'.format(row, end[i]))
#print('{0:28}{1}'.format('',rest[-1]))
i = 0
t = ''
tty.setraw(sys.stdin.fileno())
while len(rest) > 1:
    c = sys.stdin.read(1)
    if ord(c) == 13:
        rest = [x for x in rest if len(x) == i+1]
        break
    if ord(c) == 27:
        os.system("stty sane")
        exit()
    print(i) 
    if c not in [x[i] for x in rest]:
        continue
    os.system('clear')
    t = t + c
    rest = [x for x in rest if x[i] == c]
    if len(rest) == 1:
        break
    while len(set([x[i+1] for x in rest])) == 1:
        i += 1
        t = t + rest[0][i]
    i += 1
    p = [x[i:] for x in rest if i < len(x)]
    print(t)
    for row in p:
        print('\r',"-",row)

    #print('\r', t, '    -', '  - '.join(p))
os.system("stty sane")
rest = rest[0][:-1]
print('\r', rest)
#input()
copy('{}/{}'.format(PATH, rest), '{}/{}'.format(PATH, new_file_name))
os.system('nohup gvim {}/{} &'.format(PATH, new_file_name))
#os.system('restart_i3')
