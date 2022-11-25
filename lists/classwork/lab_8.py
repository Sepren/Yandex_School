quantity = int(input())
numbers = []
for i in range(quantity):
    numbers.append(int(input()))
sum_start_position = int(input())
sum_end_position = int(input())
print(sum(numbers[sum_start_position - 1: sum_end_position]))