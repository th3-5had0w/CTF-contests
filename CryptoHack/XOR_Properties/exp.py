from Crypto.Util.number import long_to_bytes, bytes_to_long

key1 = 'a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313'

key23 = 'c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1'

kfinal = '04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf'

k1 = long_to_bytes(int(key1, 16))
k23 = long_to_bytes(int(key23, 16))
kf = long_to_bytes(int(kfinal, 16))

s = ''

for i in range(len(k1)):
    s+=chr(k1[i] ^ k23[i] ^ kf[i])

print(s)
