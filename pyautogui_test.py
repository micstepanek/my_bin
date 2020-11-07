#!/usr/bin/env python3
import pyautogui as p
import i3ipc.aio

i3 = i3ipc.aio.Connection()
p.moveTo(100,100)
print(1)
