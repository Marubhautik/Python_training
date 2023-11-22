class Category:
    def __init__(self, name, code):
        self.name = name
        self.code = code
        self.no_of_products = 0

    def __str__(self):
        return f"Category: {self.name}, Code: {self.code}, Number of Products: {self.no_of_products}"

class Product:
    def __init__(self, name, code, category, price):
        self.name = name
        self.code = code
        self.category = category
        self.price = price

        category.no_of_products += 1

    def __str__(self):
        return f"Product: {self.name}, Code: {self.code}, Category: {self.category.name}, Price: {self.price}"

    def searchcode(self,products, code):
        for product in products:
            if product.code == code:
                return product
        return None

    def sort_products_high_to_low(self, products):
        for i in range(len(products) - 1, 0, -1):
            for j in range(i):
                if products[j].price < products[j + 1].price:
                    products[j], products[j + 1] = products[j + 1], products[j]

    def sort_products_low_to_high(self, products):
        for i in range(len(products)):
            for j in range(i, len(products)):
                if products[j].price < products[i].price:
                    products[j], products[i] = products[i], products[j]

# Create electronics category object
electronics_category = Category("Electronics", "ELEC")
Clothing_category = Category("Clothing","SHIRT345")
# Create product objects
product1 = Product("Laptop", "LAP1234", electronics_category, 1200.00)
product2 = Product("Keyboard", "KEYBO4321", electronics_category, 50.00)
product3 = Product("Mouse", "MOUS6543", electronics_category, 30.00)

product11 = Product("Laptop", "LAP1234", Clothing_category, 1200.00)
product22 = Product("Keyboard", "KEYBO4321", Clothing_category, 50.00)
product33 = Product("Mouse", "MOUS6543", Clothing_category, 30.00)
# Print category information
print("Category Information:")
print(electronics_category)
print(Clothing_category)

products = [product1, product2, product3, product11, product22, product33]

Product.sort_products_high_to_low(Product, products)

print("\nProducts sorted by price (High to Low):")
for product in products:
    print(product)

print("\nProducts sorted by price (Low to High):")
Product.sort_products_low_to_high(Product, products)
for product in products:
    print(product)



products = [product1, product2, product3, product11, product22, product33]
def searchcode(products, code):
    for product in products:
        if product.code == code:
            return product
    return None

print("\nserching using code")
product_found = searchcode(products, "LAP1234")
if product_found:
    print("Product found:", product_found)
else:
    print("Product with code not found")