from pwn import *

elf = ELF('./nullptr')

print hex(elf.got['getc'])
