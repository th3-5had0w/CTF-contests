enc = [0xc7, 0xc7, 0x25, 0x1d, 0x63, 0x0d, 0xf3, 0x56]
mag = [0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A]


tmp1 = []
tmp2 = []

for i in range(8):
    mag[i] += i


for i in range(8):
    tmp1.append(bin(mag[i]).split('b')[1])
    while (len(tmp1[i]) < 8):
        tmp1[i] = '0' + tmp1[i]

    print(tmp1[i])
    print(tmp1[i][0:8-i]+' '+tmp1[i][8-i:8])
    tmp2.append(tmp1[i][8-i:8]+tmp1[i][0:8-i])


flag = ''

for i in range(8):
    flag += chr(int(tmp2[i], 2) ^ enc[i])


print(flag)



