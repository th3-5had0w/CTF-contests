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
passphrase = input("Xin hãy nhập mật khẩu của bạn: ")
key = sha256(passphrase)
bimat = open("bimat.txt").read()

# Mã hóa dùng key (được tạo từ sha256 của passphrase)
ciphertext = encrypt(bimat, key)

# Xuất ra độ dài key và bản mã vào file output.txt
# Độ dài key = độ dài message nên chắc mã hóa này an toàn lắm đây ^^
f = open("output.txt", "w")
f.write('Key length: %d\n' % len(key))
f.write('Message length: %d\n' % len(bimat))
f.write('Ciphertext: 0x' + ciphertext.hex())
f.close()
