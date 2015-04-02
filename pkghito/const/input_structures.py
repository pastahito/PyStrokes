__author__ = 'Renato'

from ctypes import *
user32 = windll.user32

# START SENDINPUT TYPE DECLARATIONS
PUL = POINTER(c_ulong)


#
class KeyBdInput(Structure):
    _fields_ = [("wVk", c_ushort),
                ("wScan", c_ushort),
                ("dwFlags", c_ulong),
                ("time", c_ulong),
                ("dwExtraInfo", PUL)]


#
class HardwareInput(Structure):
    _fields_ = [("uMsg", c_ulong),
                ("wParamL", c_ushort),
                ("wParamH", c_ushort)]


#
class MouseInput(Structure):
    _fields_ = [("dx", c_long),
                ("dy", c_long),
                ("mouseData", c_ulong),
                ("dwFlags", c_ulong),
                ("time", c_ulong),
                ("dwExtraInfo", PUL)]


class InputI(Union):
    _fields_ = [("mi", MouseInput),
                ("ki", KeyBdInput),
                ("hi", HardwareInput)]


class Input(Structure):
    _fields_ = [("type", c_ulong),
                ("ii", InputI)]


class POINT(Structure):
    _fields_ = [("x", c_ulong),
                ("y", c_ulong)]

# END SEND_INPUT TYPE DECLARATIONS

FInputs = Input * 1
extra = c_ulong(0)