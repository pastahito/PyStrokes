__author__ = 'Renato'

from time import sleep
from input_structures import *  # Here ctypes is imported implicitly and user32 is bound to windll.user32
from pyctionary import arrows, numbers, letters


def mouse_event():
    print('Mouse Event not implemented yet...')


def hardware_event():
    print('Hardware event not implemented yet...')


def keyboard_letter_event(key, go_down):
    input_structure = InputI()
    up_down_event = 2  # Code for release a letter key
    if go_down is True:
        up_down_event = 8  # Code for pressing a letter key
    values = letters[key]
    input_structure.ki = KeyBdInput(values[0], values[1], up_down_event, 1, None)
    c = FInputs((1, input_structure),)  # 1 means keyboard input
    user32.SendInput(1, pointer(c), sizeof(c[0]))  # this works omitting 'pointer', receiving only 'c' as parameter


def keyboard_arrow_event(key, go_down):
    input_structure = InputI()
    up_down_event = 2  # Code for release an arrow key
    if go_down is True:
        up_down_event = 1  # Code for pressing an arrow key
    values = arrows[key]
    input_structure.ki = KeyBdInput(values[0], values[1], up_down_event, 1, None)
    c = FInputs((1, input_structure),)  # 1 means keyboard input
    user32.SendInput(1, pointer(c), sizeof(c[0]))  # this works omitting 'pointer', receiving only 'c' as parameter


def keyboard_number_event(key, go_down):
    input_structure = InputI()
    up_down_event = 2  # Code for release a number key
    if go_down is True:
        up_down_event = 8  # Code for pressing a number key # 8 for LoL and 1 for Touhou
    values = numbers[key]
    input_structure.ki = KeyBdInput(values[0], values[1], up_down_event, 1, None)
    c = FInputs((1, input_structure),)  # 1 means keyboard input
    user32.SendInput(1, pointer(c), sizeof(c[0]))  # this works omitting 'pointer', receiving only 'c' as parameter


# Pressing a key
def press(key):
    if letters.__contains__(key):
        keyboard_letter_event(key, True)
    elif arrows.__contains__(key):
        keyboard_arrow_event(key, True)
    elif numbers.__contains__(key):
        keyboard_number_event(key, True)


# Releasing a key
def release(key):
    if letters.__contains__(key):
        keyboard_letter_event(key, False)
    elif arrows.__contains__(key):
        keyboard_arrow_event(key, False)
    elif numbers.__contains__(key):
        keyboard_number_event(key, False)


# Pressing and releasing a key
def press_release(key, toggle_time=0.016):
    if letters.__contains__(key):
        keyboard_letter_event(key, True)
        sleep(toggle_time)
        keyboard_letter_event(key, False)
    elif arrows.__contains__(key):
        keyboard_arrow_event(key, True)
        sleep(toggle_time)
        keyboard_arrow_event(key, False)
    elif numbers.__contains__(key):
        keyboard_number_event(key, True)
        sleep(toggle_time)
        keyboard_number_event(key, False)

# sleep(1)
# press_release('left')
# sleep(1)
# press_release(0)
# sleep(1)
# press_release('a')