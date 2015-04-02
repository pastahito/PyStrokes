__author__ = 'Renato'
__project__ = 'cuarentadefiebre'
__date__ = '19/02/2015'

from PIL import ImageGrab
import time


def shoot():
    im = ImageGrab.grab()
    im.save(time.strftime('%Hh%Mm%Ss %d-%m-%y') + '.png', 'PNG')


def main():
    shoot()


if __name__ == '__main__':
    main()