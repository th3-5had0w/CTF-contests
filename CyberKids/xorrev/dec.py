import codecs

f = open('output.txt', 'r')
data = codecs.decode(f.read().split()[4][2:], 'hex_codec')
bm = list(data)


for d1 in range(257):
    for d2 in range(257):
        for d3 in range(257):
            for d4 in range(257):
                for d5 in range(257):
                    for d6 in range(257):
                        for d7 in range(257):
                            for d8 in range(257):
                                for d9 in range(257):
                                    for d10 in range(257):
                                        for d11 in range(257):
                                            for d12 in range(257):
                                                for d13 in range(257):
                                                    for d14 in range(257):
                                                        for d15 in range(257):
                                                            for d16 in range(257):
                                                                for d17 in range(257):
                                                                    for d18 in range(257):
                                                                        for d19 in range(257):
                                                                            for d20 in range(257):
                                                                                for d21 in range(257):
                                                                                    for d22 in range(257):
                                                                                        for d23 in range(257):
                                                                                            for d24 in range(257):
                                                                                                for d25 in range(257):
                                                                                                    for d26 in range(257):
                                                                                                        for d27 in range(257):
                                                                                                            for d28 in range(257):
                                                                                                                for d29 in range(257):
                                                                                                                    for d30 in range(257):
                                                                                                                        for d31 in range(257):
                                                                                                                            for d32 in range(257):
                                                                                                                                a = []
                                                                                                                                a.append(d1)
                                                                                                                                a.append(d2)
                                                                                                                                a.append(d3)
                                                                                                                                a.append(d4)
                                                                                                                                a.append(d5)
                                                                                                                                a.append(d6)
                                                                                                                                a.append(d7)
                                                                                                                                a.append(d8)
                                                                                                                                a.append(d9)
                                                                                                                                a.append(d10)
                                                                                                                                a.append(d11)
                                                                                                                                a.append(d12)
                                                                                                                                a.append(d13)
                                                                                                                                a.append(d14)
                                                                                                                                a.append(d15)
                                                                                                                                a.append(d16)
                                                                                                                                a.append(d17)
                                                                                                                                a.append(d18)
                                                                                                                                a.append(d19)
                                                                                                                                a.append(d20)
                                                                                                                                a.append(d21)
                                                                                                                                a.append(d22)
                                                                                                                                a.append(d23)
                                                                                                                                a.append(d24)
                                                                                                                                a.append(d25)
                                                                                                                                a.append(d26)
                                                                                                                                a.append(d27)
                                                                                                                                a.append(d28)
                                                                                                                                a.append(d29)
                                                                                                                                a.append(d30)
                                                                                                                                a.append(d31)
                                                                                                                                a.append(d32)
                                                                                                                                res = b''
                                                                                                                                for index in range(len(bm)):
                                                                                                                                    current = bm[index] ^ a[index % len(a)]
                                                                                                                                    if (current < 0x20 or current > 0x7e):
                                                                                                                                        break
                                                                                                                                    res+=chr(current)
                                                                                                                                if ('CTF{' in res):
                                                                                                                                    print(res)
