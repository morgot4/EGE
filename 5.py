def f(n):
    binary_n = "".join(to3(n))
    if n % 3 == 0:
        binary_n = "1" + binary_n + '02'
    else:
        binary_n += "".join(to3((n % 3) * 4))
    return int(binary_n,3)

def to3(n):
    res = ''
    while n:
        res += str(n % 3)
        n //= 3
    res = list(res)
    res.reverse()
    return res

# def f(n):
#     bin_n = bin(n)[2:]
#     if sum(list(map(int, list(bin_n)))) % 2 == 0:
#         bin_n = '10' + bin_n[2:] + '0'
#     else:
#         bin_n = '11' + bin_n[2:] + '1'
#     return int(bin_n, 2)

ans = []
for n in range(1, 8000):
    if f(n) < 199:
        ans.append(n)

print(max(ans))