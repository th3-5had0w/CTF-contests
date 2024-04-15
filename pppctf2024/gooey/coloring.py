# thank you my pal d4rkn19ht


mod = 1454077510067338869372316944847370699315973030897976908309312512336980481738317971337352174999857054574561953999845406588476984323763
N = 1000


import sys 
sys.setrecursionlimit(100000)
#calculate note
leafnode = pow(68, N + 1, mod) * pow(67, N-1, mod) % mod
f= [None for i in range(1001)]

leafnode = 845940199165880131154467934065543040051236143686123185433313869256868344230448440972712550210309176679444331356692040781444769235280


###theory tester
# haha = [[[0 for j in range(68)] for j in range(68) ] for k in range(1000)]

# for i in range(68):
#     haha[0][i][i] = 1


# for i in range(1, 1000):
#     for j in range(68):
#         for k in range(68):
#             for l in range(68):
#                 if l!=k:
#                     haha[i][j][k] += haha[i-1][j][l]
#                     haha[i][j][k] %= mod 

# sum = 0
# for i in range(68):
#     for j in range(68):
#         if i!=j :
#             sum += haha[999][i][j]
#             sum %= mod 
# sum = sum * pow(68, N, mod) % mod 
# print(sum)
# print(leafnode)
####


ans = 0
f[0] = f[1] = leafnode

for i in range(2, 1001):
    f[i] = (f[i-1] * f[i-2] * 68 * 67) % mod 

ans = f[1000] * 69 % mod 

print(ans)

