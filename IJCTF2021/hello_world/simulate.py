lel = 'IJCTF'

i=0
while (i<100):
    result=i
    v7 = (lel[i] >> 4) + 16 * lel[i+1]
    v6 = (lel[i+1] >> 4) + 16 * lel[i]
    if (v7 >= 0):
        v1 = 2 * v7
    else:
        v1 = (2 * v7) | 1
    if (v1 >= 0):
        v2 = 2 * v1
    else
