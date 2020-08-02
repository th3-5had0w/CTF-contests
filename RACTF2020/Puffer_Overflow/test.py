def smart_input():
    """
    This function aims to make python 3's input smart:tm:
    It checks if you're piping or redirecting, and switches to reading
    from stdin directly.
    """
    import os, sys, stat
    mode = os.fstat(0).st_mode

    if stat.S_ISREG(mode) or stat.S_ISFIFO(mode):
        return sys.stdin.buffer.read()
    return input().encode()




print('Hello!')
print('Name?')
name = smart_input()
