N = int(input().strip())
line = input()
line = line.strip()
part = line.split()
numbers = set(map(int, part))
final_list = []
for y in numbers:
    final_list.append(y)
final_list.sort()
final_list.reverse()
print(final_list[1])
