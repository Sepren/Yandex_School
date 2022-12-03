quantity = int(input())
text = []
for i in range(quantity):
    text.append(input())
text = [string for string in text if 'лук' not in string]
print(*text, sep = ', ')