quantity_numbers = input().split()
numbers = [int(number) for number in quantity_numbers]
for i in numbers:
    print(i * '*')