from pwn import *
elf = ELF('./cookie_library')
print elf.got['printf']
