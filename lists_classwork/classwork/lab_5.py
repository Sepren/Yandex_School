soups = ["щи", "борщ", "щавелевый суп", "овсяный суп", "суп по-чабански"]
days = int(input())
for i in range(0, days):
    print(soups[i % 5])