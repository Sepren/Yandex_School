quantity_numbers = input().split()
numbers = [int(number) ** 2 for number in quantity_numbers]
print(*numbers)