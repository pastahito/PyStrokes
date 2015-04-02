__author__ = 'Renato'
__project__ = 'cuarentadefiebre'
__date__ = '21/02/2015'

from ctypes import *
from KeyboardHook import KeyboardHook
import win32con
user32 = windll.user32

keyboardHook = KeyboardHook()

##################################################
# returns a function pointer to the fn paramater #
# assumes the function takes three params:       #
# c_int, c_int, and POINTER(c_void_p)            #
##################################################
def getFunctionPointer(fn):
    CMPFUNC = CFUNCTYPE(c_int, c_int, c_int, POINTER(c_void_p))
    return CMPFUNC(fn)

#############################################
# Sample function to handle keyboard events #
#############################################
def kbEvent(nCode, wParam, lParam):
    if wParam is not win32con.WM_KEYDOWN: # It just occured to me that I should aso be checking for WM_SYSKEYDOWN as well
        return user32.CallNextHookEx(keyboardHook.kbHook, nCode, wParam, lParam)
    print (lParam[0])
    return user32.CallNextHookEx(keyboardHook.kbHook, nCode, wParam, lParam)

pointer = getFunctionPointer(kbEvent)
if keyboardHook.installHook(pointer):
    print ("installed hook")
# keyboardHook.uninstallHook()
# print ("removed hook")
keyboardHook.keepAlive()
