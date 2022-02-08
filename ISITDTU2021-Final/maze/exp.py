from pwn import *

io = remote('34.124.217.71', 9002)
print(io.recvuntil(b'This is an example, using character "urdl" as up right down left, type "'))
fa = io.recvuntil(b'"').split(b'"')[0]
print(io.recv())
io.sendline(fa)
print(fa)
print(io.recvuntil(b'wrong direction.\n'))
m = len(io.recvline().split(b'\n')[0])
n = 0
max = 0
ar = []
a = io.recvline()
while (b'Input: ' not in a):
    tmp = a.split(b'\n')[0][1:]
    n+=1
    print(list(tmp))
    if (len(tmp) > max):
        max = len(tmp)
    ar.append(tmp)
    a = io.recvline()

maze = [ [0]*m for i in range(n)]

for i in range(len(ar)):
    for j in range(len(ar[i])):
        if (ar[i][j] != 32):
            maze[i][j] = ar[i][j]

for i in range(len(maze)):
    print(maze[i])

      