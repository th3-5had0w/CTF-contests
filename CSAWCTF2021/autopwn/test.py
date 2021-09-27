from pwn import *

elf = ELF('./real')
print(hex(elf.sym['win'])[5:])
print(hex(elf.sym['win'] - 0x400000))
