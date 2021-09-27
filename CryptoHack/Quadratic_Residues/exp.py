def solve(integer):
    for i in range(29):
        if (((i ** 2) % 29) == integer):
            print(str(integer), i)
            break
