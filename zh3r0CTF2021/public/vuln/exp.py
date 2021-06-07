from pwn import *

io = process('./more-printf')
payload = b'\0'*31
io.send(payload)
print(io.recvall())
