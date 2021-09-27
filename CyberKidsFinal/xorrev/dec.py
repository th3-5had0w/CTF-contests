#/usr/bin/python3

import hashlib

def sha256(s: str):
    m = hashlib.sha256()
    m.update(s.encode('ascii'))
    return m.digest()

def encrypt(message: str, key: bytes) -> bytes:
    # chuyển string message thành byte
    byte_message = message.encode('utf-8')

    ciphertext = []
    for index in range(len(byte_message)):
        current = byte_message[index] ^ key[index]
        ciphertext.append(current)
    return bytes(ciphertext)

# Nhập vào passphrase để mã hóa file bí mật

dat = open('output.txt').readlines()[2].split()[1][2:]
data = list(bytes(bytearray.fromhex(dat)))

poss = list('thrwcWRTHC13!#')

for d1 in poss:
    for d2 in poss:
        for d3 in poss:
            for d4 in poss:
                for d5 in poss:
                    for d6 in poss:
                        for d7 in poss:
                            passphrase = ''
                            tmp = data
                            passphrase+= d1+d2+d3+d4+d5+d6+d7
                            print('Testing: '+passphrase)
                            key = list(sha256(passphrase))
                            plain = []
                            for index in range(len(tmp)):
                                current = tmp[index] ^ key[index]
                                if (current < 0x20 or current > 0x7e):
                                    break
                                plain.append(current)
                            if (b'CTF{' in bytes(plain)):
                                print(bytes(plain))
                                exit(0)


# Mã hóa dùng key (được tạo từ sha256 của passphrase)
#ciphertext = encrypt(bimat, key)
