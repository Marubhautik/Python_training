class Product:
    def __init__(self, name, code, category, price):
        self.name = name
        self.code = code
        self.category = category
        self.price = price

    def __str__(self):
        return f"Product: {self.name}, Code: {self.code}, Category: {self.category}, Price: {self.price}"

def sort_products_high_to_low(products):
    sorted_products = []

    while products:
        highest_price_index = 0
        for i in range(1, len(products)):
            if products[i].price > products[highest_price_index].price:
                highest_price_index = i

        sorted_products.append(products[highest_price_index])
        products.pop(highest_price_index)

    return sorted_products

def sort_products_low_to_high(products):
    sorted_products = []

    while products:
        highest_price_index = 0
        for i in range(1, len(products)):
            if products[i].price < products[highest_price_index].price:
                highest_price_index = i

        sorted_products.append(products[highest_price_index])
        products.pop(highest_price_index)

    return sorted_products

product1 = Product("Laptop", "LAP1234", "Electronics", 1200.00)
product2 = Product("Keyboard", "KEYBO4321", "Electronics", 50.00)
product3 = Product("Mouse", "MOUS6543", "Electronics", 30.00)
product4 = Product("Shirt", "SHIRT1234", "Clothing", 25.00)
product5 = Product("Pants", "PANTS4321", "Clothing", 35.00)
product6 = Product("Dress", "DRESS6543", "Clothing", 45.00)
product7 = Product("Toy Car", "TOYCAR1234", "Toys", 20.00)
product8 = Product("Toy Doll", "TOYDOLL4321", "Toys", 15.00)
product9 = Product("Toy Robot", "TOYROBOT6543", "Toys", 30.00)
product10 = Product("Book", "BOOK1234", "Books", 10.00)

products = [product1, product2, product3, product4, product5, product6, product7, product8, product9, product10]

products_sorted_high_to_low = sort_products_high_to_low(products[:])


print("\nProducts sorted by price (High to Low):")
for product in products_sorted_high_to_low:
    print(product)
products_sorttedlowtohige = sort_products_low_to_high(products[:])

print("\n products sorted by price low to high")
for product in products_sorttedlowtohige:
    print(product)