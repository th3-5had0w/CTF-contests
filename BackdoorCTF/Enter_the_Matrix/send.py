from pwn import *

matrix1 = [1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0]
matrix2 = [1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

p = process('./matrix')
print p.recvuntil('Choice:')
pause()
p.sendline('2')
print p.recv()
p.sendline('Neo')
print p.recv()
p.sendline('7')
print p.recv()
for i in matrix1:
    p.sendline(str(i))
print p.recv()
for j in matrix2:
    p.sendline(str(j))
print p.recv()
