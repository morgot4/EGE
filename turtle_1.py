from itertools import product
el = '012345'
nums = product(el, el, el, el, el)
for i, num in enumerate(list(nums)):
    if ''.join(num) == '55550':
        print(i)