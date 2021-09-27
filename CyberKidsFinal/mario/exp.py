from pwn import *
import base64
from PIL import Image
import os

io = remote('178.128.19.56', 19999)

print(io.recvuntil('(y/n): '))
io.sendline('y')

for k in range(30):
    print(io.recvline())
    data = io.recvuntil('\n')
    procd = data.split()[0]
    fh = open("image.png", "wb")
    fh.write(base64.decodestring(procd))
    fh.close()
    image = Image.open("image.png")
    w, h = image.size
    pixels = image.load()
    code = ''
    outbreak = 0
    pos = 0
    for i in range(h):
        if (outbreak == 1):
            break
        for j in range(w):
            if (pixels[j, i][:3] != (0, 0, 0)):
                if (j < w//2):
                    if (i < h//2):
                        pos = 2
                    elif (i > h//2):
                        pos = 3
                elif (j > w//2):
                    if (i < h//2):
                        pos = 1
                    elif (i > h//2):
                        pos = 4
                outbreak = 1
                break
    image.close()
    os.system("rm image.png")
    io.sendline(str(pos))

print(io.recvall())
