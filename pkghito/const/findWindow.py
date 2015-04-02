__author__ = 'Renato'
__project__ = 'cuarentadefiebre'
__date__ = '20/02/2015'

import win32gui
import win32api
import win32con
import ctypes
import time

user32 = ctypes.windll.user32


def window_exists(windowname):


    w = win32gui.FindWindow(None, windowname)

    if w is 0:
        print ('not running', windowname)
    else:
        y1 = win32gui.ShowWindow(w, win32con.SW_SHOWMINIMIZED)
        y2 = win32gui.ShowWindow(w, win32con.SW_RESTORE)
        win32api.SendMessage(w, win32con.WM_SETFOCUS, 0, 0)
        # print ('running process fdfs', w, y1, y2)
    return w


# window_exists('go.txt: Bloc de notas')