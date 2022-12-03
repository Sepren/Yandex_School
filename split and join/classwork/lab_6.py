quantity_numbers = input().split()
numbers = [int(number) ** 2 for number in quantity_numbers if int(number) % 2 != 0 and int(number) ** 2 % 10 != 9]
print(*numbers)