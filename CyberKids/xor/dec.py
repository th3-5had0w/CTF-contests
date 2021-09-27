import codecs

f = open('output.txt', 'r')
data = codecs.decode(f.read().split()[1][2:], 'hex_codec')


for i in range(256):
    key = i+1
    string = ''
    tmp = list(data)
    for j in tmp:
        string += chr(j ^ key)

    if ('CTF{' in string):
        print(string)
        break
