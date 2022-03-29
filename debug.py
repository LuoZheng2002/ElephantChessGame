debug_on = {
    'if': False,
    'for_loop_hint': False,
    'iterator_value': False,
    'for_end_value': False,
    'size': False
}


def dout(token: str, message: str):
    global debug_on
    if debug_on[token]:
        print(message)
