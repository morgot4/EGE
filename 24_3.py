
with open("24DATA/k7data/k7c-1.txt", 'r') as f:
    text = f.read()

count = 0
for i, symbol in enumerate(text[:-2]):
    if symbol in "BCD" and text[i+1] in "BDE" and text[i+2] in "BCE" and text[i+2] != text[i+1] and symbol != text[i+1]:
        count += 1
print(count)



