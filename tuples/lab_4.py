quantity = int(input())
alphabet = []
for i in range(quantity):
    alphabet.append(input())
print(*sorted(alphabet), sep = '\n')