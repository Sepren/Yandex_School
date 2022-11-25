quantity = int(input())
shopping_list = []
for i in range(quantity):
    shopping = input()
    shopping_list.append(shopping)
print(*shopping_list, sep = '\n')