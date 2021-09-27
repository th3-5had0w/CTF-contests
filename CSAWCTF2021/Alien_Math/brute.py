res = list('7759406485255323229225')
arr = list('7000000000000000000000')
cum = '7'

def func(a1, a2):
    return (12 * (a2 - 48) - 4 + 48 * (a1 - 48) - (a2 - 48)) % 10

for i in range(len(arr)-1):
    for j in range(10):
        arr[i+1] = str(j)
        v1 = ord(arr[i+1]) - 48
        arr[i+1] = chr((v1 + func(ord(arr[i]), ord(arr[i])+i)) % 10 + 48)
        if (arr[i+1] == res[i+1]):
            cum+=str(j)
            break

print(cum)
