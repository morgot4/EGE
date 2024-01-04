# def f(n):
#     bin_n = bin(n)[2:]
#     sum_num = sum(list(map(int, list(bin_n))))
#     bin_n += str(sum_num % 2)
#     sum_num = sum(list(map(int, list(bin_n))))
#     bin_n += str(sum_num % 2)
#     return int(bin_n, 2)

# ans = []
# for n in range(1, 1000):
#     if f(n) < 100:
#         ans.append(f(n))
# print(ans, max(ans))
# print(2**10)
# from itertools import product
# el = '1234'
# nums = product(el, el, el, el, el)
# count = 0 
# for num in list(nums):
#     # if num.count('1') != 2:
#     #     continue
#     count += 1

# print(count)
# from collections import Counter
# with open("9_before_akr.csv", 'r') as f:
#     file_data = f.read().split('\n')[:-1]
# count = 0
# max_sum = 0
# for line in file_data:
#     line = list(map(int, line.split(";")))
#     info = list(Counter(line).values())
#     povtor = 0
#     ne_povtor = 0
#     if info.count(4) == 1:
#         for num in line:
#             if line.count(num) == 4:
#                 povtor =num
#             else:
#                 ne_povtor += num
#         if povtor > (ne_povtor / 3):
#             count += 1
    

# print(count)

# s = 4**511 + 2**511 - 511
# n = 2
# data = [0] * n
# while s:
#     data[s%n] += 1
#     s //= n
# print(data)
# for A in range(0, 1000):
#     flag = True
#     for x in range(0, 1000):
#         for y in range(0, 1000):
#             if not((4 * x + 3 * y < A) or (x > y) or (y > 13)):
#                 flag = False
#                 break
#         if not flag:
#             break 
#     if flag:
#         print(A)

# with open("17_before_akr.txt", 'r') as f:
#     data = list(map(int, f.read().split("\n")[:-1]))
#     max_17 = 0
#     for num in data:
#         if str(num).endswith("17"):
#             max_17 = max(num, max_17)

# count = 0
# max_tri = 0
# for i in range(len(data)-2):
#     tri = [data[i], data[i-1], data[i-2]]

#     chet = 0
#     for num in tri:
#         if 1000 <= num <= 9999:
#             chet += 1
#     if chet != 2:
#         continue

#     del_p = 0
#     for num in tri:
#         if num % 5 == 0:
#             del_p += 1
#     if del_p == 0:
#         continue

#     if sum(tri) <= max_17:
#         continue
#     count += 1
#     max_tri = max(max_tri, sum(tri))

# print(count, max_tri)

# def f(n):
#     if n == 10:
#         return 1
#     elif n > 10:
#         return 0
#     return f(n + 1) + f(n + 3) + f(n + (n - 1))

# print(f(2))
   
# with open("24.txt", 'r') as f:
#     text = f.read()
# count = 0
# max_count = 0
# for i, el in enumerate(text):
#     if el == 'L' and text[i-1] == 'K':
#         max_count = max(count, max_count)
#         count = 1
#         continue
#     if el == 'K' and text[i-1] == 'L':
#         max_count = max(count, max_count)
#         count = 1
#         continue
#     count += 1
# print(max(count, max_count))

# import re

# for x in range(2622, 10**8, 2622):
#     if re.match(r"^1[0-9]4[0-9]*6[0-9]8$", str(x)):
#         print(x, x // 2622)
#===================================================

# def f(n):
#     bin_n = bin(n)[2:]
#     #=============================
#     if bin_n.count("0") == bin_n.count('1'):
#         bin_n += bin_n[-1]
#     elif bin_n.count("0") > bin_n.count('1'):
#         bin_n += '1'
#     elif bin_n.count("1") > bin_n.count('0'):
#         bin_n += '0'
#     #=============================
#     if bin_n.count("0") == bin_n.count('1'):
#         bin_n += bin_n[-1]
#     elif bin_n.count("0") > bin_n.count('1'):
#         bin_n += '1'
#     elif bin_n.count("1") > bin_n.count('0'):
#         bin_n += '0'
#     #=============================
#     if bin_n.count("0") == bin_n.count('1'):
#         bin_n += bin_n[-1]
#     elif bin_n.count("0") > bin_n.count('1'):
#         bin_n += '1'
#     elif bin_n.count("1") > bin_n.count('0'):
#         bin_n += '0'
#     #=============================
#     return int(bin_n, 2)

# ans = []
# for n in range(100, 1000):
#     if f(n) % 4 == 0:
#         ans.append(n)

# print(ans)


# import turtle

# t = turtle.Turtle()
# t.speed(0)
# turtle.delay(0)
# turtle.tracer(0)
# ZOOM = 30
# MARGIN = -200

# for i in range(20):
#     for j in range(20):
#         t.penup()
#         t.goto(i*ZOOM + MARGIN, j*ZOOM + MARGIN)
#         t.dot(size=3)


# t.goto(MARGIN, MARGIN)
# t.left(90)
# t.left(315)
# t.pendown()
# for _ in range(7):
#     t.forward(16 * ZOOM)
#     t.left(45)
#     t.forward(8 * ZOOM)
#     t.left(135)
# turtle.mainloop()
# from itertools import product
# el = '0123'
# nums = product(el,el,el,el)
# for i,num in enumerate(list(nums)):
#     if i == 248:
#         print(num)

# with open("9_test1.csv", 'r') as f:
#     data = f.read().split('\n')[:-1]
    

# count = 0
# for line in data:
#     line = list(map(int, line.split(';')))
#     min_line = min(line)
#     if (sum(line) - min_line) / min_line <= 6:
#         continue
#     if (min(line) * max(line)) <= (sorted(line)[1] * sorted(line)[2]):
#         continue
#     count += 1

# print(count)









# lst = [3,4,5,536,75]
# lst.sort()
# # lst = sorted(lst)
# print(lst)

# for x in "012345678":

#     M = int(f'842{x}5', 9)
#     N = int(f'8{x}725', 9)

#     for A in range(1, 1000):
#         if (M + A) % N == 0:
#             print(A)
#             break


def f(n):
    if n <= 1:
        return 0
    elif n > 1 and n % 2 != 0:
        return f(n-1) + 3 * n**2
    elif n > 1 and n % 2 == 0:
        return n/2 + f(n-1) + 2
    
