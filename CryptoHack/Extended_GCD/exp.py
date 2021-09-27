def solve(a, b):
    x0 = 1
    y0 = 0
    x1 = 0
    y1 = 1
    while (b != 0):
        q = a // b
        r = a % b
        tmpx = x1
        tmpy = y1
        x1 = x0 - q * x1
        y1 = y0 - q * y1
        x0 = tmpx
        y0 = tmpy
        a = b
        b = r
    return (x0, y0)

xn, yn = solve(26513, 32321)
print(xn ,yn)
