from pwn import *

io = remote('128.199.234.122', 2222)

while True:
    io.recvuntil('Money: ')
    a = io.recv().split(b'$')
    print('Money: ', a[0])
    io.sendline('1')
    io.recvuntil('> ')
    io.sendline(a[0])
    if int(a[0])<=0:
        io.close()
        io = remote('128.199.234.122', 2222)
    if int(a[0])>696969696969:
        io.recvuntil('Money: ')
        io.recv()
        io.sendline('2')
        print(io.recvuntil('}'))
        break
