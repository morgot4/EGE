def DEL(n,m):
    return n % m == 0

count = 0
res = []
for A in range(-1000, 1001):
    flag = True
    for x in range(-1000, 1000):
        if (x & A != 0) and (x & 58 == 0) and (x & 22 == 0):
            flag = False
            break
    if flag:
        print(A)
        


                