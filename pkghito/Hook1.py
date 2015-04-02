__author__ = 'Renato'

import msvcrt
import sys
sys.path.insert(0,"C:\Workspaces\Python\win32test\pkghito\combo")
sys.path.insert(0,"C:\Workspaces\Python\win32test\pkghito\const")
sys.path.insert(0,"C:\Workspaces\Python\win32test\pkghito")
from pressreleasev2 import press_release
from findWindow import window_exists


def olaf():
    window_exists('go.txt: Bloc de notas')
    while True:
        if msvcrt.kbhit():
            ch = msvcrt.getch().decode()
            if ch == 'q':
                press_release('a')
                print("Q was pressed")
            elif ch == 'x':
                print("X was pressed")
                break
            else:
               print("Key Pressed:", ch)

olaf()