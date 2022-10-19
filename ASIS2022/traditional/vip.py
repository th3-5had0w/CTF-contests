lower = list(b'abcdefghijklmnopqrstuvwxyz')
shift19_lower = list(b'tuvwxyzabcdefghijklmnopqrs')

upper           =   list(b'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
shift14_upper   =   list(b'OPQRSTUVWXYZABCDEFGHIJKLMN')

num= list(b'0123456789')
shift5_num  = list(b'5678901234')


cip = list(b'4TrGsT5ByJKBrJdwsW6LdBRxq57L8IeMyBRHp6IGsm8IXBJE')
import string
a = [0 for i in range(len(cip))]

for i in range(len(cip)):
    if cip[i] < (65  + 26) and cip[i] >= 65:
        ind = shift14_upper.index(cip[i])
        a[i]= upper[ind]
    elif cip[i] < 58 and cip[i] >= 48:
        ind = shift5_num.index(cip[i])
        a[i]= num[ind]
    elif cip[i] < (97  + 26) and cip[i] >= 97:
        ind = shift19_lower.index(cip[i])
        a[i]= lower[ind]
    else:
        print("error")



# print(a)
import base64
a1 = bytes(a)[::-1]
# print(a1)
print(base64.b64decode(a1))