from pwn import *

payload = 'A'*0x20+p32()
