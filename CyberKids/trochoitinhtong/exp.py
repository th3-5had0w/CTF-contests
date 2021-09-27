f= open('dayso.txt', 'r')
a = 0
for i in f.read().split():
    a+=int(i, 10)

print(a)
