quantity = int(input())
marks = []
for i in range(quantity):
    marks.append(input())
print(*marks, sep = '\n')
print()
for i in marks:
    if '4' in i or '5' in i:
        print(i)
    