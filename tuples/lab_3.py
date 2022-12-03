quantity = int(input())
numbers = []
flag = 'НЕТ'
for i in range(quantity):
    number = int(input())
    numbers.append(number)
answer = int(input())
for i in range(quantity - 1):
    for j in range(i + 1, quantity):
        if numbers[i] * numbers[j] == answer:
            flag = 'ДА'
            break
print(flag)