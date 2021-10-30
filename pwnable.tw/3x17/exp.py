from pwn import *

io = process('./3x17')
elf = ELF('./3x17')

print(hex(elf.bss()))
