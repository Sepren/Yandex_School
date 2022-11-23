quantity = int(input())
advices = []
for i in range(quantity):
    text = input().lower()
    if 'не' not in text:
        advices.append(text)
    else:
        not_advice = text.find('не')
        new_text = text[:not_advice] + text[not_advice + 2:]
        advices.append(new_text)
print(advices)