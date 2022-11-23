quantity = int(input())
indexes = 1
for i in range(1, quantity + 1):
    text = input()
    if 'кот' in text:
        cat = text.find('кот')
        print(i, cat + 1)