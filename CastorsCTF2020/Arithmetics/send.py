from pwn import *
from word2number import w2n
p = remote('chals20.cybercastors.com', 14429)
print p.recv()
p.sendline('\x10')
while (True):
    a = p.recv()
    print a
    s=a.split()
    if s[3]=='+' or s[3]=='plus':
        p.sendline(str(w2n.word_to_num(s[2])+w2n.word_to_num(s[4])))
    elif s[3]=='-' or s[3]=='minus' or s[3]=='subtract':
        p.sendline(str(w2n.word_to_num(s[2])-w2n.word_to_num(s[4])))
    elif s[3]=='*' or s[3]=='multiplied-by':
        p.sendline(str(w2n.word_to_num(s[2])*w2n.word_to_num(s[4])))
    elif s[3]=='//' or s[3]=='divided-by':
        p.sendline(str(w2n.word_to_num(s[2])/w2n.word_to_num(s[4])))
    print p.recv()
