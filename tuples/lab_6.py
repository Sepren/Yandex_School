quantity = int(input())
soldiers = []
for i in range(quantity):
    soldiers.append(input())
punisment = int(input())
attemps = int(input())
for i in range(attemps):
    for j in range(1, len(soldiers) + 1, punisment):
        soldiers.remove(soldiers[j])
