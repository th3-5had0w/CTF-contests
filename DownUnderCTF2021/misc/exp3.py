from pwn import *
import urllib.parse
import base64
import codecs


io = remote('pwn-2021.duc.tf', 31905)
print(io.recv())
io.sendline()
print(io.recv())
io.sendline('2')
print(io.recvuntil('number (base 10): '))
io.sendline(str(int(io.recvline(), 16)))
print(io.recvuntil('the original ASCII letter: '))
io.sendline(chr(int(io.recvline(), 16)))
print(io.recvuntil('the original ASCII symbols: '))
io.send(urllib.parse.unquote(io.recvline().decode('utf-8')))
print(io.recvuntil('base64 string and provide me the plaintext: '))
io.sendline(base64.b64decode(io.recvline()))
print(io.recvuntil('provide me the Base64: '))
io.sendline(base64.b64encode(io.recvline().split(b'\n')[0]))
print(io.recvuntil('provide me the plaintext: '))
io.send(codecs.encode(io.recvline().decode('utf-8'), 'rot13'))
print(io.recvuntil('provide me the ROT13 equilavent: '))
io.send(codecs.decode(io.recvline().decode('utf-8'), 'rot13'))
print(io.recvuntil('provide me the original number (base 10): '))
io.sendline(str(int(io.recvline(), 2)))
print(io.recvuntil(': '))
io.sendline(bin(int(io.recvline())))
print(io.recv())
io.sendline('DUCTF')
print(io.recv())
