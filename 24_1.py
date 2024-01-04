with open("24_09122023.txt", 'r') as f:
    text = f.read()


res = 0
count = 0
current = False
for i,symbol in enumerate(text[:-1]):
    if (symbol == 'B' and text[i+1] == 'A') or (symbol == 'C' and text[i+1] == 'A'):
        current = True
        count += 2
        res = max(res, count)
        continue
    elif current:
        current = False
        continue
    res = max(res, count)
    count = 0
print(max(res, count))
    
    

  