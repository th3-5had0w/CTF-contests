from pwn import *

BEDUG = True
if BEDUG == True:
    io = process('./mno2')
    gdb.attach(io)
else:
    io = remote('0.0.0.0', 1337)

payload = b'\0'*29107+b'ABCDEFGH'

io.sendline(payload)
io.interactive()
