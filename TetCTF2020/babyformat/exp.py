from pwn import *

io = process('./babyformat')

print(io.recv())
payload = 
io.sendline(payload)
print(io.recvall())
