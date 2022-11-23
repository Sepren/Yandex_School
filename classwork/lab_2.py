symbols = 'qwertyuiopasdfghjklzxcvbnm_1234567890'
text = input()
index = 0
while len(text) != index:
    if text[index] not in symbols:
        print(f' Неверный символ: {text[index]}')
        break
    index += 1
else:
    print("OK")