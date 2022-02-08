f = open('message.txt', 'r')
a = f.read()
b = bytes(bytearray.fromhex(a))

print(b)
print(chr(b[0] ^ ord('C')))
print(chr(b[1] ^ ord('h')))
print(chr(b[2] ^ ord('r')))
print(chr(b[3] ^ ord('i')))
print(chr(b[4] ^ ord('s')))
print(chr(b[5] ^ ord('t')))
print(b[6] ^ ord('C'))
print(b[7] ^ ord('T'))
print(b[8] ^ ord('F'))
print(b[9] ^ ord('{'))
print(b[-1] ^ ord('}'))

res = ''
for j in b:
    res+=chr(j^i)
    if 'ChristCTF{' in res:
        print(res)
        break
