def f(a):
    if a == 1:
        return 1
    elif a < 1:
        return 0
    return f(a-1) + f(a // 2)
print(f(30))