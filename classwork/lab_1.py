# row and column
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
quantity = int(input())
for i in range(1, quantity + 1):
    for j in range(quantity):
        print(letters[j] + str(quantity - i + 1), end = ' ')
    print()