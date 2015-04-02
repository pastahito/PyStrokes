__author__ = 'Renato'

from PIL import ImageGrab
import time

def shoot():
    im = ImageGrab.grab()
    im.save(time.strftime('%Hh%Mm%Ss %d-%m-%y') + '.png','PNG')

shoot()
