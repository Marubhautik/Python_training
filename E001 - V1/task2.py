class Product:
    def __init__(self, name, code, category, price):
        self.name = name
        self.code = code
        self.category = category
        self.price = price

    def __str__(self):
        return "Product: {self.name}, Code: {self.code}, Category: {self.category}, Price: {self.price}"

product = Product("Laptop", "LAPTOP123", "Electronics", 1200)
print(product.name)
print(product.code)
print(product.category)
print(product.price)

class Product:
    def __init__(self, name, code, category, price):
        self.name = name
        self.code = code
        self.category = category
        self.price = price

    def __str__(self):
        return f"Product Name: {self.name}, Product Code: {self.code}, Product Category: {self.category}, Product Price: {self.price}"


products = []
product1 = Product("Laptop", "LAPTOP123", "Electronics", 1200)
products.append(product1)

product2 = Product("Smartphone", "SMARTPHONE234", "Electronics", 800)
products.append(product2)

product3 = Product("Shirt", "SHIRT345", "Clothing", 50)
products.append(product3)

product4 = Product("Jeans", "JEANS456", "Clothing", 80)
products.append(product4)

product5 = Product("Toy Car", "TOYCAR567", "Toys", 30)
products.append(product5)

product6 = Product("Toy Doll", "TOYDOLL678", "Toys", 40)
products.append(product6)

product7 = Product("Headphones", "HEADPHONES789", "Electronics", 150)
products.append(product7)

product8 = Product("Shoes", "SHOES890", "Clothing", 100)
products.append(product8)

product9 = Product("Watch", "WATCH901", "Accessories", 200)
products.append(product9)

product10 = Product("Book", "BOOK012", "Books", 25)
products.append(product10)

for product in products:
    print(product)

