# Hàm này sẽ XOR từng ký tự trong message với khóa dài 1 byte
def encrypt(message: str, key: int) -> bytes:
    # chuyển string message thành byte
    byte_message = message.encode('utf-8')

    ciphertext = []
    # đi qua từng byte trong message và xor với khóa dài 1 byte
    for ch in byte_message:
        current = ch ^ key
        ciphertext.append(current)
    return bytes(ciphertext)

# Đọc khóa bí mật
key = open("secret_key.txt", "rb").read()

# Có lẽ chỉ cần dùng 1 byte trong khóa bí mật?
simple_key = key[0]

# Đọc file message.txt và mã hóa bằng khóa dài 1 byte
message = open("message.txt").read()
ciphertext = encrypt(message, simple_key)
print('Ciphertext: 0x' + ciphertext.hex())
