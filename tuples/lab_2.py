Tribonacci = [1, 1, 1]
quantity = int(input())
if quantity > 3:
    for i in range(quantity - 3):
        Tribonacci.append(Tribonacci[i] + Tribonacci[i + 1] + Tribonacci[i + 2])
print(*Tribonacci)