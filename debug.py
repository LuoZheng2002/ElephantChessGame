debug_on_all = True
debug_on = {
    'if': False,
    'for_loop_hint': False,
    'iterator_value': False,
    'for_end_value': False,
    'size': False,
    'process': True,
    'return': False,
    'register': False,
    'line': True,
    'warning': True
}


def dout(token: str, message: str):
    global debug_on, debug_on_all
    if debug_on_all and debug_on[token]:
        print(message)
