from z3 import *

s = Solver()

encrypted = open("flag.txt.enc", "rb").read()
lel = [BitVec("x%d"%i, 8) for i in range(len(encrypted))]

lel2 = [0] * len(encrypted)

s.add(lel[0] == ord('I'))
s.add(lel[1] == ord('J'))
s.add(lel[2] == ord('C'))
s.add(lel[3] == ord('T'))
s.add(lel[4] == ord('F'))
s.add(lel[5] == ord('{'))

for i in range(0, len(encrypted), 2):
    v7 = (lel[i] >> 4) + 16 * lel[i + 1]
    v6 = (lel[i + 1] >> 4) + 16 * lel[i]
    v1 = If(v7 >= 0, 2 * v7, (2 * v7) | 1)
    v2 = If(v1 >= 0, 2 * v1, (2 * v1) | 1)
    v3 = If(v2 >= 0, 2 * v2, (2 * v2) | 1)
    v8 = v3
    v4 = If( v6 >= 0 , 2 * v6, (2 * v6) | 1)
    v5 = If( v4 >= 0 , 2 * v4, (2 * v4) | 1)
    lel2[i] = v8 ^ 0x13
    lel2[i + 1] = v5 ^ 0x37

for i in range(100):
    s.add(lel2[i] == encrypted[i])

if(s.check() == sat):
    m = s.model()
    flag = ""
    for _ in lel:
        flag += chr(m[_].as_long())

    print(flag)
else:
    print("No solution.")