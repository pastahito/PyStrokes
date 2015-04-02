__author__ = 'Renato'

from collections import namedtuple
from pyctionary import translate

KeyboardEvent = namedtuple('KeyboardEvent', ['event_type', 'key_code',
                                             'scan_code', 'alt_pressed',
                                             'time'])


# Blocking method. You must call this once, second call and on will not be executed since this method is blocking.
def execute(*la):
    # for a in la:
    #     handlers.append(a)
    if len(la) > 0:
        global def_list
        def_list = la
        listen()


def listen():
    hook_id = None
    """
    Calls `handlers` for each keyboard event received. This is a blocking call.
    """
    # Adapted from http://www.hackerthreads.org/Topic-42395
    from ctypes import windll, CFUNCTYPE, POINTER, c_int, c_void_p, byref
    import win32con, win32api, win32gui, atexit

    event_types = {win32con.WM_KEYDOWN: 'key down',
                   win32con.WM_KEYUP: 'key up',
                   0x104: 'key down', # WM_SYSKEYDOWN, used for Alt key.
                   0x105: 'key up', # WM_SYSKEYUP, used for Alt key.
                  }

    def low_level_handler(nCode, wParam, lParam):
        """
        Processes a low level Windows keybqoard event.
        """
        if wParam == win32con.WM_KEYUP or wParam == 0x105:
            # event = KeyboardEvent(event_types[wParam], lParam[0], lParam[1], lParam[2] == 32, lParam[3])
            # print(lParam[0]>>32)
            event = str(translate[lParam[0]>>32])

            # Question: how to turn this loop parallel?
            for handler in def_list:
                if handler(event): break

        # Be a good neighbor and call the next hook.
        return windll.user32.CallNextHookEx(hook_id, nCode, wParam, lParam)

    # Our low level handler signature.
    CMPFUNC = CFUNCTYPE(c_int, c_int, c_int, POINTER(c_void_p))
    # Convert the Python handler into C pointer.
    pointer = CMPFUNC(low_level_handler)

    # Hook bot key up and key down events for common keys (non-system).
    hook_id = windll.user32.SetWindowsHookExA(win32con.WH_KEYBOARD_LL, pointer,
                                             win32api.GetModuleHandle(None), 0)

    # Register to remove the hook when the interpreter exits. Unfortunately a
    # try/finally block doesn't seem to work here.
    atexit.register(windll.user32.UnhookWindowsHookEx, hook_id)
    while True:
        msg = win32gui.GetMessage(None, 0, 0)
        win32gui.TranslateMessage(byref(msg))
        win32gui.DispatchMessage(byref(msg))



