from pwn import *

def create_sc(io, shellcode):
    print io.recvuntil('> ')
    io.sendline('2')
    print io.recv()
    io.sendline(str(len(shellcode)))
    print io.recv()
    p.send(shellcode)

def list_sc(io):
    print io.recvuntil('> ')
    io.sendline('1')

def edit_sc(io, index, shellcode):
    print io.recvuntil('> ')
    io.sendline('3')
    print io.recv()
    io.sendline(str(index))
    print io.recv()
    io.sendline(str(len(shellcode)))
    print io.recv()
    p.send(shellcode)

def delete_sc(index):
    print io.recvuntil('> ')
    io.sendline('4')
    print io.recv()
    io.sendline(str(index))
