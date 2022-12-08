numbers = input().split()
numbers = [int(number) for number in numbers]
start_position, end_position = map(int, input().split())
print(sum(numbers[start_position:end_position + 1]))