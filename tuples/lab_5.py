quantity = int(input())
alphabet = []
for i in range(quantity):
    alphabet.append(input())
new_list = sorted(alphabet, key = len)
print(*new_list, sep = '\n')