with open("17_16.11.2023.txt", 'r') as f:
    data = f.read().split("\n")[:-1]
    data = list(map(int, data))
    min_el = min(data)
    count = 0
    max_s = 0
    for i in range(len(data) - 1):
        if data[i] % 20 == min_el or data[i+1] % 20 == min_el:
            max_s = max(max_s, data[i] + data[i+1])
            count += 1
print(count, max_s)

