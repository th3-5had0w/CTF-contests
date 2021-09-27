from Crypto.Util.number import long_to_bytes, bytes_to_long
from pwn import *

string = long_to_bytes(int('73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d', 16))

print(string)


secret = string[0] ^ ord('c')
s=''

for i in string:
    s+= chr(i ^ secret)


print(s)
