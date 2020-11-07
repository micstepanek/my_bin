#!/usr/bin/env python3
#2
from i3ipc import Connection, Event
from tkinter import Tk, Label, Frame

config = '''

'''

class ColorLabel():
    def __init__(self, name, color):
        LEFT = 'w'
        self.label = Label(top_container.frame, anchor=LEFT, text=name, bg=color)
        self.label.pack(expand=True, fill='x')
class Container:
    def __init__(self):
        self.frame = Frame(root)
        self.frame.pack()
    def reset(self):
        self.frame.destroy()
        self.frame = Frame(root)
        self.frame.pack()
    def add_existing_workspaces(self):
        workspaces = i3.get_workspaces()
        workspaces = [(x.name, 'yellow' if x.urgent else 'lightgreen' if x.focused else None) for x in workspaces]
        workspaces.sort()
        [ColorLabel(x[0], x[1] ) for x in workspaces]
    def add_deprecated_workspaces(self):
        #deprecated = ['h','l','m','q']
        #[ColorLabel(x, 'white') for x in deprecated]
        deprecated_workspaces = 'hlmq'
        ColorLabel(deprecated_workspaces, None)
    def add_mode(self):
        pass

def show_workspaces():
    pass

def show_mode(mode):
    active_window = i3.get_tree().find_focused()
    window_id = active_window.id
    window_location = active_window.rect
    x = (window_location.x) 
    y = (window_location.y) + 75

    top_container.reset()
    mode_list = mode.split('|')
    [ColorLabel(x, None) for x in mode_list]
    if mode_list[0].startswith('move '):
        top_container.add_existing_workspaces()
        top_container.add_deprecated_workspaces()

    root.geometry('+%d+%d'%(x,y))  
    root.deiconify()
    i3.command('[con_id={}]focus'.format(window_id))
    root.update()



from time import sleep

from subprocess import run
import threading
import keyboard

i3 = Connection()
i3.command('bar mode invisible')

def show():
    active_window = i3.get_tree().find_focused()
    window_id = active_window.id
    window_location = active_window.rect
    x = (window_location.x) 
    y = (window_location.y) + 75


    workspaces = i3.get_workspaces()
    workspaces = [(x.name, 'yellow' if x.urgent else 'lightgreen' if x.focused else None) for x in workspaces]
    workspaces.sort()

    top_container.reset()
    [ColorLabel(x[0], x[1] ) for x in workspaces]

    root.geometry('+%d+%d'%(x,y))  
    root.deiconify()

def do_sth(event):
    print('pressed',event.keycode)
    if event.keysym == 'Escape':
        root.withdraw()
    elif event.keysym == 'u':
        run(['urxvtc'])
        root.withdraw()



def on_keypress(event):
    threading.Thread(target=do_sth, args=[event]).start()

keyboard.add_hotkey('F12', show)

root = Tk()
root.bind('<Key>', on_keypress)
root.title('async_test')
root.attributes('-type', 'dialog')
#root.attributes('-topmost', True)
top_container = Container()
root.withdraw()
root.mainloop()

