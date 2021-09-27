from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


plaintext = "USERNAME=A\x00BIOGRAPHY=AAAAAAAAAA\x00ROLE=1"

'''
print(len(plaintext))

#cipher = AES.new(KEY, AES.MODE_ECB)
pad_plaintext = pad(plaintext.encode('utf-8'),16)
print(len(pad_plaintext))
'''

def decrypt_aes(ciphertext):
    decipher = AES.new(KEY, AES.MODE_ECB)
    unpad_plaintext = decipher.decrypt(ciphertext)
    return unpad(unpad_plaintext,16)

cre = 'ac18c3cd45d5927595b66fba48183f7a8763bf6c487e8995e413d0fb3f94dc058e8ba23e845d28b7ebe04db40a4fccdb'

plaintext = decrypt_aes(bytes.fromhex(cre)).decode('utf-8')

print(plaintext)
