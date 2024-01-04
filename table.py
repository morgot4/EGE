def f(now, end):
    if now == end:
        return 1
    elif now < end:
        return 0
    return f(now-1, end) + f(now//2, end)

print(f(30, 13) * f(13, 1))