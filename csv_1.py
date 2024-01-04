from collections import Counter

with open("9_02.12.2024.csv") as f:
    text = f.read()

text = text.split('\n')[:-1]
a = []
for line in text:
    a.append(list(map(int, line.split(";"))))
count = 0
for line in a:
    info = list(Counter(line).values())
    if info.count(3) != 1 and info.count(1) != 3:
        continue
    sum3 = 0
    ap = 1
    for num in line:
        if line.count(num) == 1:
            sum3 += num
        else:
            ap *= num
    print(line, sum3, ap)
    if sum3 * 3 > ap:
        continue
    count += 1

    
print(count)

