__author__ = 'Renato'
__project__ = 'cuarentadefiebre'
__date__ = '20/02/2015'

import win32api
import win32con
from time import sleep


def left_click():
    while 1:
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
        sleep(.020)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
        print ("Click.")


sleep(4)
