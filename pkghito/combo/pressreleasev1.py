__author__ = 'Renato'

from time import sleep
from ctypes import *
user32 = windll.user32
from input_structures import *
import hardware_scan_code as sc
import virtual_key_code as vk


def mouse_event():
        print('Mouse Event not implemented yet...')


def hardware_event():
        print('Hardware event not implemented yet...')


def keyboard_event(virtual_code, hardware_code, go_down, input_structure):
        up_down_event = 2
        if go_down is True:
            up_down_event = 8
        input_structure.ki = KeyBdInput(virtual_code, hardware_code, up_down_event, 1, None)


def event(virtual_code, hardware_code, go_down, type_input):
    input_structure = InputI()
    if type_input == 0:
        mouse_event()
    elif type_input == 1:
        keyboard_event(virtual_code, hardware_code, go_down, input_structure)
    elif type_input == 3:
        hardware_event()
    c = FInputs((type_input, input_structure),)
    user32.SendInput(1, pointer(c), sizeof(c[0]))


def press(virtual_code, hardware_code):
    event(virtual_code, hardware_code, True, 1)


def release(virtual_code, hardware_code):
    event(virtual_code, hardware_code, False, 1)


def press_release(virtual_code, hardware_code, toggle_lapse):
    press(virtual_code, hardware_code)
    sleep(toggle_lapse)
    release(virtual_code, hardware_code)

# click_q = InputI()
# click_q.ki = KeyBdInput(0x51, 0x10, 8, 1, None)
# release_q = InputI()
# release_q.ki = KeyBdInput(0x51, 0x10, 2, 1, None)
# c_q = FInputs((1, click_q),)
# r_q = FInputs((1, release_q),)
# sleep(1)
# user32.SendInput(1, pointer(c_q), sizeof(c_q[0]))
# sleep(0.016)
# user32.SendInput(1, pointer(r_q), sizeof(r_q[0]))

sleep(3)
press_release(vk.VK_X, sc.SC_X, 0.016)