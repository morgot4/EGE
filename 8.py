from itertools import *

# count = 0
# words = product("012345", repeat=3)
# for i,word in enumerate(words):
#     if word[0] == '2':
#         print(i+1)
#         break
#=================================================================
# def valid(s):
#   s = [' '] + list(s) + [' ']
#   print(s)
#   for i in range(1,len(s)-1):
#      if s[i] == 'A' and s[i-1] != 'D' and s[i+1] != 'D':
#         return False
#      if s[i] == 'C' and ((s[i-1] == 'B') or (s[i+1] == 'B')):
#         return False
#   return True
# candidates = product('ABCD', repeat=3)
# v = [s for s in candidates if valid(s)]
# print( len(v) )
#=================================================================
# words = product("0123", repeat=5)
# flag = False
# count = 0
# for word in words:
#     word = "".join(word)
#     print(word)
#     if flag:
#         count += 1
#     if word == '10203':
#         flag = True
#         count = 1
#     if word == '30102':
#         flag = False
#         print(count)
#         break