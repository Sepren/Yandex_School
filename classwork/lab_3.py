first_text = input()
second_text = input()
same_index = 0
same_symbols = 0
for i in range(len(first_text)):
    if first_text[i] == second_text[i]:
        same_index += 1
    else:
        for j in range(i, len(first_text)):
            if second_text[j] in first_text and first_text[i] != second_text[i]:
                same_symbols += 1
            break
print(same_index, same_symbols)
