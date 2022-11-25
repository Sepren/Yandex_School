quantity = int(input())
numbers = []
for i in range(quantity):
    numbers.append(int(input()))
for i in range(quantity - 1):
    print(numbers[i] + numbers[i + 1])