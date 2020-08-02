from pwn import *

p = remote('ctf.bitx.tw', 10103)
print p.recvuntil('!!!')
for i in range(0,1000):
    a = p.recv()
    print a
    if a.split()[1]=='+':
        ans = str(int(a.split()[0],10)+int(a.split()[2],10))
        p.sendline(ans)
    elif a.split()[1]=='*':
        ans = str(int(a.split()[0],10)*int(a.split()[2],10))
        p.sendline(ans)
    elif a.split()[1]=='-':
        ans = str(int(a.split()[0],10)-int(a.split()[2],10))
        p.sendline(ans)
    elif a.split()[1]=='/':
        ans = str(int(a.split()[0],10)/int(a.split()[2],10))
        p.sendline(ans)

print p.recv()
