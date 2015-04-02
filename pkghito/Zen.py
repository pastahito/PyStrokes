__author__ = 'Renato'

from time import sleep
from pressreleasev2 import press_release, press, release
from Hook3v2 import execute


# print("3:", hex(17179869235), hex(17179869235>>32), hex(17179869235%256))
# print("Q:", hex(68719476817), hex(68719476817>>32), hex(68719476817%256))
# print("W:", hex(73014444119), hex(73014444119>>32), hex(73014444119%256))
# print("E:", hex(77309411397), hex(77309411397>>32), hex(77309411397%256))
# print("R:", hex(81604378706), hex(81604378706>>32), hex(81604378706%256))
# print("T:", hex(85899346004), hex(85899346004>>32), hex(85899346004%256))
# print("Y:", hex(90194313305), hex(90194q313305>>32), hex(90194313305%256))
# print("U:", hex(94489280597), hex(944892q80597>>32), hex(94489280597%256))
# print("I:", hex(98784247881), hex(98784q247881>>32), hex(98784247881%256))
# print("O:", hex(103079215183), hex(103079215183>>32), hex(103079215183%256))
# print("P:", hex(107374182480), hex(107374182480>>32), hex(107374182480%256))4e4e4e4e4
def patchouli(a):
    if a == 'w':
        press_release('down')
        sleep(0.02)
        press('down')
        sleep(0.02)
        press_release('c')
        sleep(0.02)
        release('down')
    elif a == 'e':
        press_release('down')
        sleep(0.017)
        press('down')
        sleep(0.017)
        press('left')
        sleep(0.017)
        release('down')
        sleep(0.017)
        press('x')
        sleep(1)
        release('left')
        sleep(0.017)
        release('x')
    elif a == '2':
        sleep(0.11)
        press_release('e')
    else:
        print("No handler bounded to:", a)


def katarina(a):
    if a == '2':
        sleep(0.1)
        press_release('e')
    else:
        print("No handler bounded to:", a)


def lee_sin(a):
    if a == '2' or a == '1':
        sleep(0.1)
        press_release('w')
    else:
        print("No handler bounded to:", a)


def jax(a):
    print("jax def", a)
    if a == '2':
        sleep(0.07)
        press_release('q')
        return 1


def lee_dragon(a):
    # print(a)
    if a == '2':
        sleep(0.1)
        press_release('w')
    # elif a == '1':
    #     press_release('q')
    #     sleep(0.6)
    #     press_release(2)
    #     sleep(0.1)
    #     press_release('w')

# up para los anteriores


# down
def quinn(a):
    print("quinn def", a)
    if a == '1':
        press_release('q')
        sleep(0.05)
        press_release('e')
        return 1
        # I strongly recommend return 1 for each if statement for efficiency (for the sake of my design)
        # If not, each def will be run


def ryze(a):
    if a == '2':
        press_release('q')
        sleep(0.09)
        press_release('w')
        sleep(0.05)
        press_release('e')
        sleep(0.05)


execute(jax, quinn)
