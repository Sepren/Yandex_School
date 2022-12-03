quantity = int(input())
savings = []
for i in range(quantity):
    savings.append(int(input()))

print(*savings, sep = '\n')
print()
for i in savings:
    i *= 3
    print(i)
