quantity = int(input())
for i in range(quantity):
    string = input().find('кот')
    if string != -1:
        print(i + 1, string + 1)