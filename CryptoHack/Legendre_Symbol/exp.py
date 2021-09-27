f = open('output.txt', 'r')
p = int(f.readline().split()[2])
f.readline()
for i in f.readline().split('=')[1].split(']')[0].split('[')[1].split(','):
    ti = int(i)
    if (pow(ti, (p-1)//2, p) == 1):
        print(ti, 'is Quadratic Residue!')
    elif (pow(ti, (p-1)//2, p) == -1):
        print(ti, 'is not Quadratic Residue!')
    elif (pow(ti, (p-1)//2, p) == 0):
        print(ti, 'is dividable by p')


print(p)
