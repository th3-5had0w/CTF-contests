from pwn import *
import json
import base64
import codecs
from Crypto.Util.number import long_to_bytes, bytes_to_long

io = remote('socket.cryptohack.org', 13377)

def interact():
    jsonfile = json.loads(io.recv())
    if (jsonfile['type'] == 'base64'):
        res = base64.b64decode(jsonfile['encoded'])
        a = {'decoded':res.decode('utf-8')}
        io.sendline(json.dumps(a))
    elif (jsonfile['type'] == 'hex'):
        res = long_to_bytes(int(jsonfile['encoded'], 16))
        a = {'decoded': res.decode('utf-8')}
        io.sendline(json.dumps(a))
    elif (jsonfile['type'] == 'rot13'):
        res = codecs.decode(jsonfile['encoded'], 'rot13') 
        a = {'decoded': res}
        io.sendline(json.dumps(a))
    elif (jsonfile['type'] == 'bigint'):
        res = long_to_bytes(int(jsonfile['encoded'], 16))
        a = {'decoded': res.decode('utf-8')}
        io.sendline(json.dumps(a))
    elif (jsonfile['type'] == 'utf-8'):
        res = ''
        for i in jsonfile['encoded']:
            res+=chr(i)
        a = {'decoded': res}
        io.sendline(json.dumps(a))


for j in  range(100):
    interact()


print(io.recvall())
