quantity = int(input())
white_lists = []
words = []
for i in range(quantity):
    white_lists.append(input())
quantity_words = int(input())
for i in range(quantity_words):
    words.append(input())
for j in words:
    if j in white_lists:
        print(j)