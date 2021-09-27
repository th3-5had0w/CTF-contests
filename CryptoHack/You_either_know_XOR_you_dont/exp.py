from Crypto.Util.number import long_to_bytes

string = long_to_bytes(int('0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104', 16))

key = 'myXORkey'

res = ''
cnt = 0
for i in string:
    res+= chr(i ^ ord(key[cnt]))
    cnt+=1
    if (cnt==8):
        cnt = 0

print(res)
