from pwn import *

io = process('./note')

def write(data):
    print(io.recvuntil('> '))
    io.sendline('1')
    print(io.recv())
    io.send(data)
def read():
    print(io.recvuntil('> '))
    io.sendline('2')
def append(data):
    print(io.recvuntil('> '))
    io.sendline('3')
    print(io.recv())
    io.send(data)


write('````````')
read()
data = io.recvline()
print(data)
num1 = int(data, 16) ^ 0x6060606060606060
write('````````')
read()
data = io.recvline()
print(data)
num2 = int(data, 16) ^ 0x6060606060606060
write('````````')
read()
data = io.recvline()
print(data)
num3 = int(data, 16) ^ 0x6060606060606060

a = (num3 - num2) /  (num2 - num1)
b = ((num1 * num3) - num2) / (num1 - num2)


print(num2)
print(num1 *a + b)
