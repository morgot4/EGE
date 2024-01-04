from itertools import product

el = '0123456789ABCDEFGHI'
main_counter = 0
for num in list(product("123456789ABCDEFGHI", el, el, el, el, el, el ,el, el)):
    count = 0
    for i in 'ABCDEFGHI':
        count += num.count(i)
    if count != 2:
        continue
    main_counter += 1
print(main_counter)

