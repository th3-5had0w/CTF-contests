from pwn import *

io = remote('light-fever.satellitesabove.me', 5030)
print(io.recv())
io.sendline(b'ticket{xray754336papa2:GM43c9VQEqjELXaZlVosW4MlkpnwclTNt-RF4w8TCQrAw-s8Xx2fcZ1zp7mGHqpxGg}')
while True:
    a = io.recv()
    print(a)
    if a.split()[1] == b'+':
        ans = int(a.split()[0])+int(a.split()[2])
        io.sendline(str(ans))
