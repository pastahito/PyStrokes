__author__ = 'Renato'
__project__ = 'cuarentadefiebre'
__date__ = '19/02/2015'
import win32api,win32com


def get_cords():
    x, y = 0, 0
    while 1:
        m, n = win32api.GetCursorPos()
        if m != x and n != y:
            x, y = m, n
            print (x, y)


get_cords()