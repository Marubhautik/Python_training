class Product:
    def __init__(self, name, code, category, price):
        self.name = name
        self.code = code
        self.category = category
        self.price = price

    def __str__(self):
        return f"Product: {self.name}, Code: {self.code}, Category: {self.category}, Price: {self.price}"

# Create product objects
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

def searchcode(products, code):
    for product in products:
        if product.code == code:
            return product
    return None


product_found = searchcode(products, "TOYCAR12934")
if product_found:
    print("Product found:", product_found)
else:
    print("Product with code not found")


class Product:
    def __init__(self, name, code, category, price):
        self.name = name
        self.code = code
        self.category = category
        self.price = price

    def __str__(self):
        return f"Product: {self.name}, Code: {self.code}, Category: {self.category}, Price: {self.price}"


def sort_products_high_to_low(products):
    for i in range(len(products) - 1, 0, -1):
        for j in range(i):
            if products[j].price < products[j + 1].price:
                products[j], products[j + 1] = products[j + 1], products[j]


def sort_products_low_to_high(products):
    for i in range(len(products)):
        for j in range(i, len(products)):
            if products[j].price < products[i].price:
                products[j], products[i] = products[i], products[j]


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


# Sort products by price (high to low) using bubble sort
sort_products_high_to_low(products)

print("\nProducts sorted by price (High to Low):")
for product in products:
    print(product)

print("\nProducts sorted by price (Low to High):")
sort_products_low_to_high(products)
for product in products:
    print(product)
