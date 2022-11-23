max_quantity = int(input())
quantity_articles = int(input())
all_articles = []
for i in range(quantity_articles):
    articles = input()
    if len(articles) > max_quantity:
        all_articles.append(articles[:max_quantity] + '...')
    else:
        all_articles.append(articles)

print("\n".join(all_articles))