quantity = int(input())
search_word = []
strings = []
for i in range(quantity):
    string = input()
    strings.append(string)
word = input()
for i in strings:
    if word in i:
        print(i)