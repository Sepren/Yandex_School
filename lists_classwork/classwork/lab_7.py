quantity = int(input())
search_word = []
strings = []
search_words = []
for i in range(quantity):
    string = input()
    strings.append(string)
quantity_words = int(input())
for i in range(quantity_words):
    search_words.append(input())
for i in strings:
    k = 0
    for j in search_words:
        if j in i:
            k += 1
    if k == len(search_words):
        print(i)