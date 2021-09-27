from pwn import *

io = remote('167.71.204.85', 9797)

print(io.recv())
for i in range(100):
    a = io.recv()
    print(a)
    b = a.split()
    cipher = b[3]
    fromd = b[5]
    tod = b[7]
    if (b'8' in b[5]):
        if (b'10' in b[7]):
            data = int(b[3], 8)
            print(data)
            io.sendline(str(data))
        elif (b'2' in b[7]):
            data = bin(int(b[3], 8))[2:]
            print(data)
            io.sendline(str(data))
        elif (b'16' in b[7]):
            data = hex(int(b[3], 8))[2:]
            print(data)
            io.sendline(str(data))
    elif (b'2' in b[5]):
        if (b'10' in b[7]):
            data = int(b[3], 2)
            print(data)
            io.sendline(str(data))
        elif (b'16' in b[7]):
            data = hex(int(b[3], 2))[2:]
            print(data)
            io.sendline(str(data))
        elif (b'8' in b[7]):
            data = oct(int(b[3], 2))[2:]
            print(data)
            io.sendline(str(data))
    elif (b'10' in b[5]):
        if (b'2' in b[7]):
            data = bin(int(b[3], 10))[2:]
            print(data)
            io.sendline(str(data))
        elif (b'8' in b[7]):
            data = oct(int(b[3], 10))[2:]
            print(data)
            io.sendline(str(data))
        elif (b'16' in b[7]):
            data = hex(int(b[3], 10))[2:]
            print(data)
            io.sendline(str(data))
    elif (b'16' in b[5]):
        if (b'10' in b[7]):
            data = int(b[3], 16)
            print(data)
            io.sendline(str(data))
        elif (b'8' in b[7]):
            data = oct(int(b[3], 16))[2:]
            print(data)
            io.sendline(str(data))
        elif (b'2' in b[7]):
            data = bin(int(b[3], 16))[2:]
            print(data)
            io.sendline(str(data))

    print('DONE round ', str(i))
print(io.recv())
