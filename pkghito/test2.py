__author__ = 'Renato'
__project__ = 'cuarentadefiebre'
__date__ = '19/02/2015'

import time


def shoot():
    print (time.strftime('%Hh%Mm%Ss %d-%m-%y'))


def main():
    shoot()


if __name__ == '__main__':
    main()