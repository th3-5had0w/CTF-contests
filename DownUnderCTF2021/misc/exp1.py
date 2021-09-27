from pwn import *

io = remote('pwn-2021.duc.tf', 31906)
print(io.recv())
io.sendline('f')
print(io.re)
