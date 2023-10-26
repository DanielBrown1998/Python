from copy import deepcopy as copia

products = [
    {'name': 'Asus ROG Zephyrus G14', 'price': 7999.90},
    {'name': 'Motorola MOTO G53', 'price': 1899.90},
    {'name': 'Apple Iphone 12 mini', 'price': 4549.99},
    {'name': 'Gigabyte GeForce RTX 4070 Ti Aorus', 'price': 6999.90},
    {'name': 'AMD Ryzen 7 7700X', 'price': 1999.90}]


x = (f"{item['name']} => R$,{item['price']:.2f}" for item in products)

news_products = [{**item, 'price': round(item['price']*1.1, 2)}for item in copia(products)]

# news_products.sort(key=lambda item: item['name'], reverse=True)
ordered_products_words = copia(sorted(products, key=lambda item: item['name'], reverse=True))

# news_products.sort(key=lambda item: item['price'], reverse=False)
ordered_products_numbers = copia(sorted(products, key=lambda item: item['price'], reverse=False))

print('Lista de produtos')
while True:
    try:
        print(x.__next__())
    except StopIteration:
        print('\n')
        break

print('Aumentando o preço em 10%')
for item in news_products:
    print(f"{item['name']} => R$,{item['price']:.2f}")

print('\nPondo em ordem alfabética decrescente')
print(*list([f"{item['name']} => R$,{item['price']:.2f}\n" for item in ordered_products_words]))

print('Ponde em ordem numérica crescente')
print(*list([f"{item['name']} => R$,{item['price']:.2f}\n" for item in ordered_products_numbers]))
