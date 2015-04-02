__author__ = 'Renato'
__project__ = 'cuarentadefiebre'
__date__ = '21/02/2015'

import win32con
import time
import ctypes

user32 = ctypes.windll.user32


def press_release(key_code, scan_code):
    user32.keybd_event(key_code, scan_code, win32con.KEYEVENTF_EXTENDEDKEY | 0, 0)
    user32.keybd_event(key_code, scan_code, win32con.KEYEVENTF_EXTENDEDKEY | win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(0.2)


def toggle_num_lock():
    return press_release(win32con.VK_NUMLOCK, 0)


def toggle_cap_lock():
    return press_release(win32con.VK_CAPITAL, 0)


def repeat_x_times(x, fn):
    for x in range(0, x):
        fn()

repeat_x_times(6, toggle_num_lock)
repeat_x_times(6, toggle_cap_lock)
print(hex(209))
print(int(0xDD))
print(int(0x53))

# win32api.keybd_event(win32con.VK_NUMLOCK, 0x45, win32con.KEYEVENTF_EXTENDEDKEY | 0, 0)
# win32api.keybd_event(win32con.VK_NUMLOCK, 0x45, win32con.KEYEVENTF_EXTENDEDKEY | win32con.KEYEVENTF_KEYUP, 0)
