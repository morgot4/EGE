# print('x y z w')
# for x in 0,1:
#     for y in 0,1:
#         for z in 0,1:
#             for w in 0,1:
#                 if (x or y) and (y != z) and (not w):
#                     print(x,y,z,w)

# def f(n):
#     bin_n = bin(n)[2:]
#     summ = sum(list(map(int, list(bin_n))))
#     bin_n += str(summ % 2)
#     summ = sum(list(map(int, list(bin_n))))
#     bin_n += str(summ % 2)
#     return int(bin_n,2)

# ans = []
# for n in range(3, 1000):
#     if f(n) > 85:
#         ans.append(n)
# print(min(ans))

# import turtle

# t = turtle.Turtle()
# ZOOM = 30
# MARGIN = -300
# t.speed(0)
# turtle.delay(0)
# for i in range(30):
#     for j in range(23):
#         t.penup()
#         t.goto(i*ZOOM + MARGIN, j*ZOOM + MARGIN,)
#         t.dot(3)
# t.penup()
# t.goto(MARGIN,MARGIN+5*ZOOM)
# t.left(90)
# t.pendown()
# for _ in range(10):
#     t.forward(10 * ZOOM)
#     t.right(60)
# turtle.mainloop()
# print((1024*2**13) / (1600 * 1200))
# from itertools import product
# count = 0
# for i in product('ТИМОФЕЙ', repeat=5):
#     i = ''.join(i)
#     if i.count('Й') == 0:
#         count += 1
#         continue
#     idx = i.index('Й')
#     if i.count('Й') == 1 and idx not in [0,4] and i[idx-1] != 'И' and i[idx+1] != 'И':
#         count += 1
    
# print(count)
# from collections import Counter
# with open("9_1.csv") as f:
#     file_data = f.read().split('\n')[:-1]
#     data = []

#     for line in file_data:
#         data.append(list(map(int, line.split(';'))))


#     count = 0
#     for line in data:
#         info = list(Counter(line).values())
#         if info.count(2) == 2 and info.count(1) == 3:
#             avg2 = 0
#             avg1 = 0
#             print(info)
#             for num in line:
#                 if line.count(num) == 2:
#                     avg2 += num
#                 else:
#                     avg1 += num
#             avg2 /= 4
#             avg1 /= 3

#             if avg1 > avg2:
#                 count += 1
# print(count)

s = '1' * 100
while '111' in s:
    s = s.replace('11', '2', 1)
    s = s.replace('22', '1', 1)
print(s)
# s = 49 ** 8 + 7 ** 24 - 7
# n = 7
# data = [0] * n
# while s:
#     data[s%n] += 1
#     s //= n
# print(data)
# ans = []
# for A in range(0, 1000):
#     flag = True
#     for x in range(0, 1000):
#         for y in range(0, 1000):
#             if not((4 * x + 3*y < A) or (x >= y) or (y >= 13)):
#                 flag = False
#                 break
#         if not flag:
#             break
#     if flag:
#         print(A)
#         ans.append(A)

# def f(n):
#     if n == 1:
#         return 0
#     if n == 2:
#         return 1
#     if n == 3:
#         return 1
#     return f(n-3) + f(n-2) + f(n-1)

# print(f(11))

# with open('17.txt', 'r') as f:
#     data = f.read().split("\n")[:-1]
# data = list(map(int , data))
# max_num = 0
# for num in data:
#     if str(num).endswith('15'):
#         max_num = max(num, max_num)

# count = 0
# sum_max = 0
# for i in range(len(data) - 2):
#     tri = [data[i], data[i+1], data[i+2]]
#     count4 = 0
#     for num in tri:
#         if 1000 <= num <= 9999:
#             count4 += 1
#     if count4 != 1:
#         continue
#     if sum(tri) >= max_num:
#         count += 1
#         sum_max = max(sum_max, sum(tri))
# print(count, sum_max)
