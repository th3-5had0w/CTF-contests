from pwn import *

#io = remote('jupiter.challenges.picoctf.org', 39673)

io = process('./sice_cream')

print(io.recv())
