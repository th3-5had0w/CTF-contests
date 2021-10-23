from pwn import *


def ror(num, turn):
    tmp1 = bin(num)[2:]
    tmp1 = (32 - len(tmp1))*'0'+tmp1
    if (turn >= 32):
        turn = turn % 32
    return int(tmp1[(32 - turn):]+tmp1[:(32-turn)], 2)

def pad_hex(data):
    if (len(data) != 8):
        return '0'*(8-len(data))+data
    else:
        return data

#io = process('./keygen')
io = remote('125.235.240.166', 20100)
print(io.recvuntil('Name: '))
a = io.recvline().split(b'\n')[0]

value2 = 0
print(a)

for char in a:
    v5 = char + value2
    v5 = ror(v5, 12)
    value2 = v5 ^ 0x55aa

value1 = 0


for char in a:
    value1 = ror(char + value1, 4)

print(io.recv())
license = pad_hex(hex(value1).upper()[2:])+'-'+pad_hex(hex(value2).upper()[2:])
io.sendline(license)
print(io.recv())
