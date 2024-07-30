from decimal import Decimal

from collections import namedtuple

# print(0.1 + 0.2 == 0.3)
# print(Decimal("0.1") + Decimal("0.2"))

# person = namedtuple('persons', ['name', 'age', 'birthdate', 'email'])
# person1 = person(name='Akbar', age=23, birthdate='')
# person2 = person(name='John', age=32)
# print(person1)
color = namedtuple('color', ['red', 'green', 'blue'])
black = color(red=0, green=0, blue=0)
white = color(red=255, green=255, blue=255)
orange = color(red=169, green=255, blue=0)

""". Userni kunlik umumiy chiqimlarini hisoblab beruvchi dastur tuzing, u sizga qanchadir
miqdorda sarflarini quyidagi
ko'rinishda kiritadi,
    reason, 0.5 dollar
    EXM:
        - for coffee, 0.7
        - for taxi, 1.3
        - charity, 5.5

    Sizni vazifangiz uumiy hisobni va ro'yxatni chiqarib berish"""

products = {}
total_price = 0
while True:
    product = input("Product: ")
    if product == '':
        break
    price = float(input("Price: "))
    total_price += Decimal(price)
    products.update({f"- {product}": price})
for i, j in products.items():
    print(f"{i}, {j}-sum")
print('total price: ', total_price)
