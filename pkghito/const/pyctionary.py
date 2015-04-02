__author__ = 'Renato'

from hardware_scan_code import *
from virtual_key_code import *
from itertools import chain


arrows = {'left': [37, 0xCB], 'down': [40, 208], 'right': [39, 205], 'up': [38, 200]}  # key:[VKC,HSC]
# number_generator = {x%10: [0x30+x, x+1] for x in range(0,10)}  # HSC for 0 key must be 11
numbers = {0: [48, 11], 1: [49, 2], 2: [50, 3], 3: [51, 4], 4: [52, 5],
          5: [53, 6], 6: [54, 7], 7: [55, 8], 8: [56, 9], 9: [57, 10]}
# vkx_letter = dict(zip('abcdefghijklmnopqrstuvwxyz', range(0x41, 0x5A+1)))
# hsc_letter = dict(zip('qwertyuiopasdfghjklzxcvbnm', chain(range(SC_Q,SC_P+1),range(SC_A,SC_L+1),range(SC_Z,SC_M+1))))
# letter_generator = dict(zip('abcdefghijklmnopqrstuvwxyz',
#                             list([vkx_letter[x], hsc_letter[x]] for x in 'abcdefghijklmnopqrstuvwxyz')))
letters = {'m': [77, 50], 'g': [71, 34], 'k': [75, 37], 'j': [74, 36], 'd': [68, 32], 'q': [81, 16], 'w': [87, 17],
          'p': [80, 25], 'y': [89, 21], 's': [83, 31], 'b': [66, 48], 'h': [72, 35], 'l': [76, 38], 'r': [82, 19],
          'i': [73, 23], 'z': [90, 44], 't': [84, 20], 'v': [86, 47], 'e': [69, 18], 'c': [67, 46], 'u': [85, 22],
          'n': [78, 49], 'x': [88, 45], 'f': [70, 33], 'o': [79, 24], 'a': [65, 30]}

# letters_2 = {v[1]:k for k,v in letters.items()}
# number_generator_hsc = { x+1:x%10 for x in range(1,11)}-.,`+´ç--.
translate = {1: 'esc', 2: 1, 3: 2, 4: 3, 5: 4, 6: 5, 7: 6, 8: 7, 9: 8, 10: 9, 11: 0,
             12:'-', 13: '=', 14:'backspace', 15: 'tab',
             16: 'q', 17: 'w', 18: 'e', 19: 'r', 20: 't', 21: 'y', 22: 'u', 23: 'i', 24: 'o', 25: 'p',
             26: '{', 27: '}', 28: 'enter', 29: 'l_control',
             30: 'a', 31: 's', 32: 'd', 33: 'f', 34: 'g', 35: 'h', 36: 'j', 37: 'k', 38: 'l',
             39: ';', 40: '`', 41: 'accent_grave', 42: 'l_shift', 43: '\\',
             44: 'z', 45: 'x', 46: 'c', 47: 'v', 48: 'b', 49: 'n', 50: 'm',
             51: ',', 52: '.', 53: '/', 54:' r_shift', 55: '*', 56: 'l_alt', 57: 'space', 58: 'cap_lock',
             # 59: 'F1', 60: 'F2', 61: 'F3', 62: 'F4', 63: 'F5', 64: 'F6', 65: 'F7', 66: 'F8', 67: 'F9', 68: 'F10',
             69: 'num_lock', 70: 'scroll_lock', 71: '7_np', 72: '8_np', 73: '9_np', 74: '-_np', 75: '4_np', 76: '5_np',
             77: '6_np', 78:'+', 79:'1_np', 80: '2_np', 81: '3_np', 82: '0_np', 83: '._np',
             # 87: 'F11', 88: 'F12',

             0xC8: 'up', 0xCB: 'left', 0xCD: 'right', 0xD0: 'down'
             }


