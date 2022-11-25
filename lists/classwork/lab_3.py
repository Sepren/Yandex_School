quantity = int(input())
strings = []
for i in range(quantity):
    string = input()
    strings.append(string)
index = int(input())
new_word = ''
for i in strings:
    new_word += i[index - 1]
print(new_word)