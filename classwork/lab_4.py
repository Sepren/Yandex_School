stop_word = 'стоп'
word = input()
max_word_len = -1
min_word_len = 1000000
min_word = ''
max_word = ''
while word != stop_word:
    if len(word) >= max_word_len:
        max_word_len = len(word)
        max_word = word
    if len(word) <= min_word_len:
        min_word_len = len(word)
        min_word = word
    word = input()

index = 0
for i in range(len(min_word)):
    if min_word[i] not in max_word:
        print("НЕТ")
        break
    else:
        index += 1
if index == len(min_word):
    print("ДА")