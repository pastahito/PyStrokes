__author__ = 'Renato'
__project__ = 'cuarentadefiebre'
__date__ = '22/02/2015'

import time
from ctypes import *
user32 = windll.user32
from input_structures import *

# Abrir touhou
# w = win32gui.FindWindow(None, 'Touhou Hisoutensoku ver1.10a (eng v1.1a)')
# y18 = win32gui.ShowWindow(w, win32con.SW_SHOWMINIMIZED)
# y28 = win32gui.ShowWindow(w, win32con.SW_RESTORE)
# win32api.SendMessage(w, win32con.WM_SETFOCUS, 0, 0)

# #Key up
# click_up = Input_I()
# click_up.ki = KeyBdInput(0x26, 0xC8, 0x0001, 1, pointer(extra))
# release_up = Input_I()
# release_up.ki = KeyBdInput(0x26, 0xC8, 0x0002, 1, pointer(extra))
# c_up = FInputs((1, click_up))
# r_up = FInputs((1, release_up))
#
# #Key down
# click_down = Input_I()
# click_down.ki = KeyBdInput(0x28, 0xD0, 0x0001, 1, pointer(extra))
# release_down = Input_I()
# release_down.ki = KeyBdInput(0x28, 0xD0, 0x0002, 1, pointer(extra))
# c_down = FInputs((1, click_down))
# r_down = FInputs((1, release_down))
#
# # Z key
# click_z = Input_I()
# click_z.ki = KeyBdInput(0x5A, 0x2C, 0x0008, 1, pointer(extra))
# release_z = Input_I()
# release_z.ki = KeyBdInput(0x5A, 0x2C, 0x0002, 1, pointer(extra))
# c_z = FInputs((1, click_z))
# r_z = FInputs((1, release_z))
#
# # X key
# click_x = Input_I()
# click_x.ki = KeyBdInput(0x58, 0x2D, 0x0008, 1, pointer(extra))
# release_x = Input_I()
# release_x.ki = KeyBdInput(0x58, 0x2D, 0x0002, 1, pointer(extra))
# c_x = FInputs((1, click_x))
# r_x = FInputs((1, release_x))


# # Press Q Key Ability
click_q = InputI()
click_q.ki = KeyBdInput(0x51, 0x10, 0x0008, 1, pointer(extra))
release_q = InputI()
release_q.ki = KeyBdInput(0x51, 0x10, 0x0002, 1, pointer(extra))
c_q = FInputs((1, click_q),)
r_q = FInputs((1, release_q),)

# # Press W Key Ability
click_w = InputI()
click_w.ki = KeyBdInput(0x57, 0x11, 0x0008, 1, pointer(extra))
release_w = InputI()
release_w.ki = KeyBdInput(0x57, 0x11, 0x0002, 1, pointer(extra))
c_w = FInputs((1, click_w),)
r_w = FInputs((1, release_w),)

# Press E Key Ability
click_e = InputI()
click_e.ki = KeyBdInput(0x57, 0x12, 0x0008, 1, pointer(extra))
release_e = InputI()
release_e.ki = KeyBdInput(0x57, 0x12, 0x0002, 1, pointer(extra))
c_e = FInputs((1, click_e),)
r_e = FInputs((1, release_e),)
time.sleep(3)
user32.SendInput(1, pointer(c_q), sizeof(c_q[0]))
time.sleep(0.016)
user32.SendInput(1, pointer(r_q), sizeof(r_q[0]))

time.sleep(0.30)
user32.SendInput(1, pointer(c_w), sizeof(c_w[0]))
time.sleep(0.016)
user32.SendInput(1, pointer(r_w), sizeof(r_w[0]))

time.sleep(0.016)
user32.SendInput(1, pointer(c_e), sizeof(c_e[0]))
time.sleep(0.016)
user32.SendInput(1, pointer(r_e), sizeof(r_e[0]))
#
# # # Press Q Key Ability
# time.sleep(0.60)
# user32.SendInput(1, pointer(c_q), sizeof(c_q[0]))
# time.sleep(0.020)
# user32.SendInput(1, pointer(r_q), sizeof(r_q[0]))


# Jump + Z key
# time.sleep(0.5)
# print ('Star: Jump + Z key')
# user32.SendInput(1, pointer(c_up), sizeof(c_up[0]))
# time.sleep(0.6)
# user32.SendInput(1, pointer(c_z), sizeof(c_z[0]))
# time.sleep(0.020)
# user32.SendInput(1, pointer(r_z), sizeof(r_z[0]))
# time.sleep(0.4)
# user32.SendInput(1, pointer(r_up), sizeof(r_up[0]))
# print ('End: Jump + Z key')

# Down press & release
# time.sleep(1)
# print 'Start: Down press & release'
# user32.SendInput(1, pointer(c_down), sizeof(c_down[0]))
# time.sleep(0.1)
# user32.SendInput(1, pointer(r_down), sizeof(r_down[0]))
# time.sleep(0.5)
# user32.SendInput(1, pointer(c_down), sizeof(c_down[0]))
# time.sleep(0.05)
# user32.SendInput(1, pointer(r_down), sizeof(r_down[0]))
# time.sleep(0.5)
# user32.SendInput(1, pointer(c_down), sizeof(c_down[0]))
# time.sleep(0.025)
# user32.SendInput(1, pointer(r_down), sizeof(r_down[0]))

# Combo down+down+X
# time.sleep(1)
# user32.SendInput(1, pointer(c_down), sizeof(c_down[0]))
# time.sleep(0.025)
# user32.SendInput(1, pointer(r_down), sizeof(r_down[0]))
# time.sleep(0.025)
# user32.SendInput(1, pointer(c_down), sizeof(c_down[0]))
# time.sleep(0.025)
# user32.SendInput(1, pointer(c_x), sizeof(c_x[0]))
# time.sleep(0.020)
# user32.SendInput(1, pointer(r_x), sizeof(r_x[0]))
# time.sleep(0.4)
# user32.SendInput(1, pointer(r_down), sizeof(r_down[0]))


#Flag combination for non direction keys:x
# 1+2 doesn't work
# 1+8 Z key is pressed but not released
# 8+2 Z key is pressed and released :D
# click = Input_I()
# click.ki = KeyBdInput(0x5A, 0x2C, 0x0008, 1, pointer(extra))
# release = Input_I()
# release.ki = KeyBdInput(0x5A, 0x2C, 0x0002, 1, pointer(extra))
# x = FInputs((1, click))
# y = FInputs((1, release))
# time.sleep(1.5)
# print 'about to click'
# user32.SendInput(1, pointer(x), sizeof(x[0]))
# print 'about to release'
# time.sleep(0.020)# entre (5,12) a veces no captura el evento
# user32.SendInput(1, pointer(y), sizeof(y[0]))

#KEY UP&DOWN

#PRIMERA FORMA: Funciona para touhou y cualquier otro programa
# click = Input_I()
# click.ki = KeyBdInput(0x26, 0xC8, 0x0001, 1, pointer(extra))
# release = Input_I()
# release.ki = KeyBdInput(0x26, 0xC8, 0x0002, 1, pointer(extra))
#
# x = FInputs((1, click))
# y = FInputs((1, release))
# time.sleep(1)
# print 'about to click'
# time.sleep(0.5)
# user32.SendInput(1, pointer(x), sizeof(x[0]))
# #print 'about to release'
# time.sleep(0.013)#menos de esto mi HW no lo detecta creo
# user32.SendInput(1, pointer(y), sizeof(y[0]))

# SEGUNDA FORMA: Touhou no lo detecta, otros programas si
# click2 = Input_I()
# click2.ki = KeyBdInput(0x26, 0xC8, 0x0001, 1300, pointer(extra))
# release2 = Input_I()
# release2.ki = KeyBdInput(0x26, 0xC8, 0x0002, 1, pointer(extra))
# z = FInputs((1, click2),(1, release2))
# time.sleep(1)
# print 'about to click again'
# time.sleep(0.5)
# user32.SendInput(2, pointer(z), sizeof(z[0]))
# time.sleep(0.5)
# print 'end'