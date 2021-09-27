from pwn import *

io = remote('167.71.204.85', 20001)

print(io.recv())
print(io.recv())
io.sendline(b'100')
io.sendline(str(int(io.recv().split()[9], 10)))
print(io.recv())
print(io.recv())
