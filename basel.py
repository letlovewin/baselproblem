def basel_nth(n):
    x = 0
    for i in range(1, n+1):
        x += 1/pow(i,2)
    return x
