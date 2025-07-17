n = int(input().strip())
counts = {} #Dictioneary
order = []

for _ in range(n):
    w = input().strip()
    if w not in counts:
        counts[w] = 0
        order.append(w)
    counts[w] += 1

print(len(order))
print(' '.join(str(counts[w]) for w in order))
