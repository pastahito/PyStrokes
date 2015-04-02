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
    #i = win32gui.SendMessage(w, win32con.WM_ACTIVATE, 0, 0)
    #j = win32gui.SendMessage(w, win32con.WM_SETFOCUS, 0, 0)
    #k = win32gui.SendMessage(w, win32con.WM_SETCURSOR, 0, 0)
    #l = win32gui.SendMessage(w, win32con.WM_KEYDOWN, 0, 0x41)
    #m = win32gui.SendMessage(w, win32con.WM_KEYUP, 0, 0x41)

    # if user32.RegisterHotKey(None, 100, win32con.MOD_ALT, win32con.VK_DOWN):
    #   print ("Registered id", 100)


    #i = win32gui.SendMessage(w, win32con.WM_ACTIVATE, 0, 0)


    #k = win32gui.SendMessage(w, win32con.WM_SETCURSOR, 0, 0)
    #time.sleep(2)
    #win32api.SendMessage(w, win32con.WM_CHAR, 0x20, 0)
    #win32api.SendMessage(w, win32con.WM_CHAR, 0x20, 0)
    #win32api.SendMessage(w, win32con.WM_KEYDOWN, 0, 0x41)
    #win32api.SendMessage(w, win32con.WM_KEYUP, 0, 0x41)

    if w is 0:
        print ('not running', windowname)
    else:
        y1 = win32gui.ShowWindow(w, win32con.SW_SHOWMINIMIZED)
        y2 = win32gui.ShowWindow(w, win32con.SW_RESTORE)
        #y2 = win32gui.ShowWindow(w, win32con.SW_MAXIMIZE)
        win32api.SendMessage(w, win32con.WM_SETFOCUS, 0, 0)
        try:
            time.sleep(0.5)
            #SPACE PRESS&RELEASE
            win32api.keybd_event(win32con.VK_SPACE, 0x39, win32con.KEYEVENTF_EXTENDEDKEY, 0)
            win32api.keybd_event(win32con.VK_SPACE, 0x39, win32con.KEYEVENTF_KEYUP, 0)
            time.sleep(0.2)
            #Z PRESS&RELEASE
            win32api.keybd_event(0x5A, 0x2C, win32con.KEYEVENTF_EXTENDEDKEY, 0)
            win32api.keybd_event(0x5A, 0x2C, win32con.KEYEVENTF_KEYUP, 0)
        except:
            print ('exception')
        print ('running process fdfs', w, y1, y2)


        #msg = win32gui.GetMessage(w, 0, 0)
        #while msg is not None:
        #    print msg.hnwd
         #   win32gui.TranslateMessage(msg)
         #   win32gui.DispatchMessage(msg)
         #   msg = win32gui.GetMessage(w, 0, 0)

window_exists('go.txt: Bloc de notas')