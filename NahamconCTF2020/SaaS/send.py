from pwn import *

elf = ELF('./saas')
print hex(elf.bss())
