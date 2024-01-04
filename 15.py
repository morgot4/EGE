# P = [x for x in range(25,50)]
# Q = [x for x in range(32,47)]
# U = [x for x in range(1000)]
# A = U.copy()
# for x in U:
#     if not(((not(x in A)) <= (not(x in P))) <= ((x in A) <= (x in Q))):
#         A.remove(x)
# print(len(A))

def DEL(n, m):
    return n % m == 0
res = []
for A in range(0, 1000):
    flag = True
    for x in range(1000):
        for y in range(1000):
            if not((2*x <= A) or (y <= A) or (x + 2*y > 145)):
                flag = False
                break
        if not flag:
            break
    if flag:
        print(A)
print(res)