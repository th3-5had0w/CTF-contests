from pwn import *

p = remote('jh2i.com', 50031)
print p.recvuntil('land!')
while True:
    print p.recvuntil('Gold: ')
    a = p.recvuntil('\n')
    print a
    print p.recvuntil('Weapon level: ')
    b = p.recvuntil('\n')
    print b
    print p.recv()
    if int(b)==0:
        p.sendline(str(6))
        print p.recv()
        p.sendline(str(1))
    elif int(b)==1:
        if int(a)<1000:
            p.sendline(str(5))
        elif int(a)>=1000:
            p.sendline(str(6))
            print p.recv()
            p.sendline(str(2))
    elif int(b)==3:
        if int(a)<2000:
            p.sendline(str(4))
        elif int(a)>=2000:
            p.sendline(str(6))
            print p.recv()
            p.sendline(str(3))
    elif int(b)==5:
        if int(a)<10000:
            p.sendline(str(3))
        elif int(a)>=10000:
            p.sendline(str(6))
            print p.recv()
            p.sendline(str(4))
    elif int(b)==7:
        if int(a)<100000:
            p.sendline(str(2))
        elif int(a)>=100000:
            p.sendline(str(6))
            print p.recv()
            p.sendline(str(5))
    elif int(b)==10:
        p.sendline(str(1))
        print p.recv()
        print p.recv()
        print p.recv()
