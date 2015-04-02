__author__ = 'Renato'

from time import sleep
from timeit import Timer
from hardware_scan_code import *
from itertools import chain


letters = {'m': [77, 50], 'g': [71, 34], 'k': [75, 37], 'j': [74, 36], 'd': [68, 32], 'q': [81, 16], 'w': [87, 17],
          'p': [80, 25], 'y': [89, 21], 's': [83, 31], 'b': [66, 48], 'h': [72, 35], 'l': [76, 38], 'r': [82, 19],
          'i': [73, 23], 'z': [90, 44], 't': [84, 20], 'v': [86, 47], 'e': [69, 18], 'c': [67, 46], 'u': [85, 22],
          'n': [78, 49], 'x': [88, 45], 'f': [70, 33], 'o': [79, 24], 'a': [65, 30]}

def test1_1():
    key_located = letters['z']
    a = key_located[0]
    b = key_located[1]

def test1_2():
    a = letters['z'][0]
    b = letters['z'][1]

#
# def test2():
#     dic3 = dict(zip('qwertyuiop',range(SC_Q,SC_P+1)))
#     dic4 = dict(zip('asdfghjkl',range(SC_A,SC_L+1)))
#     dic5 = dict(zip('zxcvbnm',range(SC_Z,SC_M+1)))
#     z = dict(dic3, **dic4)

# For use as one single line operation
# t = Timer('for i in range(10): oct(i)', 'gc.enable()')
# print(t.timeit(1000000))

if __name__=='__main__':
    sleep(1)
    t = Timer("test1_1()", "from __main__ import test1_1 \ngc.enable()")
    print('test 1.1:', t.timeit(1))
    sleep(1)
    t = Timer("test1_2()", "from __main__ import test1_2 \ngc.enable()")
    print('test 1.2:', t.timeit(1))
    # sleep(1)
    # t = Timer("test2()", "from __main__ import test2")
    # print('test 2.1:', t.timeit(100000))

