__author__ = 'Renato'

from time import sleep
from input_structures import *  # Here ctypes is imported implicitly and user32 is bound to windll.user32
from pyctionary import arrows, numbers, letters


def mouse_event():
    print('Mouse Event not implemented yet...')


def hardware_event():
    print('Hardware event not implemented yet...')


def keyboard_event(key, go_down):
    input_structure = InputI()
    up_down_event = 2  # Code for release a letter key
    if go_down is True:
        up_down_event = 8  # Code for pressing a letter key
    if letters.__contains__(key):
        values = letters[key]
    elif arrows.__contains__(key):
        values = arrows[key]
        up_down_event %= 7  # Touhou requires 1 as flag for pressing an arrow key
    elif numbers.__contains__(key):
        values = numbers[key]
    else:
        values = [0, 0]
    input_structure.ki = KeyBdInput(values[0], values[1], up_down_event, 1, None)
    c = FInputs((1, input_structure),)  # 1 means keyboard input
    user32.SendInput(1, pointer(c), sizeof(c[0]))  # this works omitting 'pointer', receiving only 'c' as parameter


# Pressing a key
def press(key):
    keyboard_event(key, True)


# Releasing a key
def release(key):
    keyboard_event(key, False)


# Pressing and releasing a key
def press_release(key, toggle_time=0.016):
    keyboard_event(key, True)
    sleep(toggle_time)
    keyboard_event(key, False)

# Down+Down+C Combo
# sleep(2)
# press_release('down')
# sleep(0.02)
# press('down')
# sleep(0.02)
# press_release('c')
# sleep(0.02)
# release('down')

# sleep(2)
# press_release('down')
# sleep(0.017)
# press('down')
# sleep(0.017)
# press('left')
# sleep(0.017)
# release('down')
# sleep(0.017)
# press('c')
# sleep(1)
# release('left')
# sleep(0.017)
# release('c')

# Combo alistar
# sleep(5)
# press_release('w')
# sleep(0.010)
# press_release('q')

