__author__ = 'Renato'
__project__ = 'cuarentadefiebre'
__date__ = '21/02/2015'

import win32gui
import win32api
import win32con
import time
import ctypes

user32 = ctypes.windll.user32

#key code - directinput:
#0x26, 0xC8 UP
#0x28, 0xD0 DOWN
#0x5A, 0x2C Z
#0x58, 0x2D X
def window_exists(windowname):

    w = win32gui.FindWindow(None, windowname)
    if w is 0:
        print ('not running', windowname)
    else:
        y1 = win32gui.ShowWindow(w, win32con.SW_SHOWMINIMIZED)
        y2 = win32gui.ShowWindow(w, win32con.SW_RESTORE)
        #y2 = win32gui.ShowWindow(w, win32con.SW_MINIMIZE)
        win32api.SendMessage(w, win32con.WM_SETFOCUS, 0, 0)
        #win32api.SendMessage(w, win32con.WM_ACTIVATE, 0, 0)
        #win32api.SendMessage(w, win32con.WM_SETCURSOR, 0, 0)

        try:
            for y in range(0x01, 0x02):
                print (hex(y))
                time.sleep(1)
                user32.keybd_event(0x5A, 0x50, win32con.KEYEVENTF_EXTENDEDKEY, 0)
                #win32api.keybd_event(0, 0xC8, win32con.KEYEVENTF_EXTENDEDKEY, 0)
                time.sleep(0.020)
                user32.keybd_event(0x5A, 0x50, win32con.KEYEVENTF_EXTENDEDKEY | win32con.KEYEVENTF_KEYUP, 0)
                #win32api.keybd_event(0, 0xC8, win32con.KEYEVENTF_KEYUP, 0)

        except:
            print ('exception')
        print ('running process fdfs', w, y1, y2)


window_exists('Touhou Hisoutensoku ver1.10a (eng v1.1a)')