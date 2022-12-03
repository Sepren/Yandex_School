quantity = int(input())
strings = []
position = []
for i in range(quantity):
    string = input()
    strings.append(string)
new_quantity = int(input())
for i in range(new_quantity):
    position.append(int(input()) - 1)
k = 0
for i in range(new_quantity):
    print(strings[position[k]])
    k += 1