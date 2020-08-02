from enchant import *
from pwn import *

d = Dict("en_US")

p = remote('jh2i.com', 50012)

'''
print p.recvline()
    
a = p.recv()
print a
b = len(a.split())
count = b-1
for i in range(0,b-1):
    if (d.check(a.split()[i])):
        count-=1
p.sendline(str(count))


print p.recvline()
print p.recvline()
a = p.recv()
print a
b = len(a.split())

string = ''
for i in range(0,b-1):
    if (d.check(a.split()[i])==False):
        string+=a.split()[i]+' '

p.sendline(string)
print p.recvline()
print p.recvline()
a = p.recv()
print a
b = len(a.split())

listd = []
for i in range(0, b-1):
    if (d.check(a.split()[i])==False):
        listd.append(a.split()[i])
listd.sort()
rlist = ' '.join(listd)
p.sendline(rlist)
print p.recvline()
print p.recvline()
'''
while True:
    a = p.recvline()
    print a
    if 'CHRONOLOGICAL' in a:
        if 'ARE' in a:
            a = p.recvline()
            print p.recv()
            print a
            b = len(a.split())
            string = ''
            for i in range(0,b):
                if (d.check(a.split()[i])==True):
                    string+=a.split()[i]+' '
            p.sendline(string)
            print p.recvline()
        else:
            a = p.recvline()
            print p.recv()
            print a
            b = len(a.split())
            string = ''
            for i in range(0,b):
                if (d.check(a.split()[i])==False):
                    string+=a.split()[i]+' '
            p.sendline(string)
            print p.recvline()
    elif 'ALPHABETICAL' in a:
        if 'ARE' in a:
            a = p.recvline()
            print p.recv()
            print a
            b = len(a.split())
            listd = []
            for i in range(0, b):
                if (d.check(a.split()[i])==True):
                    listd.append(a.split()[i])
            listd.sort()
            rlist = ' '.join(listd)
            p.sendline(rlist)
            print p.recvline()
        else:
            a = p.recvline()
            print p.recv()
            print a
            b = len(a.split())
            listd = []
            for i in range(0, b):
                if (d.check(a.split()[i])==False):
                    listd.append(a.split()[i])
            listd.sort()
            rlist = ' '.join(listd)
            p.sendline(rlist)
            print p.recvline()
    elif 'ARE' in a:
        a = p.recvline()
        print p.recv()
        print a
        b = len(a.split())
        count = 0
        for i in range(0, b):
            if (d.check(a.split()[i])):
                count+=1
        p.sendline(str(count))
        print p.recvline()
    else:
        a = p.recvline()
        print p.recv()
        print a
        b = len(a.split())
        count = b
        for i in range(0,b):
            if (d.check(a.split()[i])):
                count-=1
        p.sendline(str(count))
        print p.recvline()
