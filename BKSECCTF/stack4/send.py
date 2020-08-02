from pwn import *

p = ELF('./stack4')
p.process()
libc = ELF('libc.so.6')

print('/bin/sh: ', (hex(p.search('/bin/sh').next())))
system = p.symbols['system']
print('system: ', hex(system))
