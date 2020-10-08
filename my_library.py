def get_clipboard():
    from subprocess import check_output 
    try:
        return check_output(['xclip', '-selection', 'clip', '-o'])
    except: 
        return b''

def get_address_bar():
    from subprocess import run
    s1 = get_clipboard()
    for i in range(10):
        run(['xdotool', 'key', 'F6'])
        run(['xdotool', 'key', 'ctrl+c'])
        s2 = get_clipboard()
        if s1 != s2 and b'http' in s2:
            return s2.decode()
     
def wait_for(window_class):
    from subprocess import run
    from i3ipc import Connection,Event
    i3 = Connection()
    i3.on(Event.WINDOW_FOCUS,
          lambda i3,event : check_window_class(i3,event,expected_window_class))
    i3.main()

def check_window_class(i3, event, expected_window_class):
    if event.container.window_class == expected_window_class:
        i3.main_quit()
    else:
        exit()

def move_us_to_workspace(desired):
    from i3ipc import Connection
    from subprocess import run
    i3 = Connection()
    workspaces = i3.get_workspaces()
    current = [x for x in workspaces if x.focused == True]
    if current[0].name == desired:
        exit()
    else:
        run(['i3-msg','move', 'container', 'to', 'workspace', desired])
        run(['i3-msg','workspace', desired])

def move_me_to_workspace(desired):
    exit_if_already_there(desired)
    from subprocess import run
    run(['i3-msg','workspace', desired])

def exit_if_already_there(desired):
    from i3ipc import Connection
    from subprocess import run
    i3 = Connection()
    workspaces = i3.get_workspaces()
    current = [x for x in workspaces if x.focused == True]
    if current[0].name == desired:
        exit()

