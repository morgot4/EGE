from itertool import product

# with open("24DATA/k7data/k7b-6.txt") as f:
#     text = f.read()
# res = 0
# count = 0
# text = text.replace("DAF", "###").replace("#DA", "*##").replace("#D", '*#')
# text = text.replace("#AF", "*##").replace("#F","*#")
# for symbol in text:
#     if symbol != "#":
#         res = max(res, count)
#         count = 0
#         continue
#     count += 1
# print(res)


# with open("24DATA/k7data/k7b-6.txt") as f:
#     text = f.read()

# count = 0
# res = 0
# fragment = 'ABCDA'
# for i, symbol in enumerate(text[:-1]):
#     if symbol in fragment and
with open("24DATA/24_19.txt") as f:
    text = f.read()

combs = product("BCD",'AE')
for comb in list(combs):
    text = text.replace("".join(comb), '*')
for i in 'ABCDE':
    text = text.replace(i, ' ')

print(len(max(sorted(text.split()))))
# count = 0
# max_count = 0
# flag = False
# for i, symbol in enumerate(text[:-1]):
#     if symbol in "BCD" and text[i+1] in "AE":
#         count += 1
#         flag = True
#     elif flag:
#         flag = False
#     else:
#         max_count = max(count, max_count)
#         count = 0
# print(max(count, max_count))