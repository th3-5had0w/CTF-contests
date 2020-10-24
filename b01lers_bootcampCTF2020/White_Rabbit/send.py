from pwn import *

p = process('./whiterabbit')

print p.recv()
p.sendline('\x66\x6c\x61\x67')
print p.recv()
