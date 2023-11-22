class Location:
    def __init__(self, name, code):
        self.name = name
        self.code = code

    def __str__(self):
        return f"Location: {self.name}"


class Movement:
    def __init__(self, from_location, to_location, product, quantity):
        self.from_location = from_location
        self.to_location = to_location
        self.product = product
        self.quantity = quantity

    def __str__(self):
        return f"Movement: From {self.from_location},\n          To {self.to_location}, \n          Product: {self.product}, \n          Quantity: {self.quantity}"

    @staticmethod
    def movements_by_product(product):
        movements = []
        for movement in all_movements:
            if movement.product == product:
                movements.append(movement)
        return movements


class Product:
    def __init__(self, name, code, stock_at_locations=None):
        self.name = name
        self.code = code
        if stock_at_locations is None:
            stock_at_locations = {}
        self.stock_at_locations = stock_at_locations

    def __str__(self):
        return f"{self.name}"

    def move_product(self, from_location, to_location, quantity):
        if quantity > self.stock_at_locations.get(from_location, 0):
            raise Exception(f"Insufficient stock of product {self.name} at location {from_location}")

        self.stock_at_locations[from_location] -= quantity
        if to_location not in self.stock_at_locations:
            self.stock_at_locations[to_location] = 0
        self.stock_at_locations[to_location] += quantity


# Create location objects
location1 = Location("Warehouse", "WH1234")
location2 = Location("Store 1", "ST1234")
location3 = Location("Store 2", "ST5678")
location4 = Location("Store 3", "ST5678")
location5 = Location("Store 4", "ST5678")

# Create product objects
product1 = Product("Laptop", "LAP1234")
product2 = Product("Keyboard", "KEYBO4321")
product3 = Product("Mouse", "MOUS6543")
product4 = Product("Tablet", "MUS6543")
product5 = Product("Mobile", "ghUS6543")


# Add stock to products
product1.stock_at_locations[location1] = 200
product2.stock_at_locations[location2] = 100
product3.stock_at_locations[location1] = 100

# Move products from one location to another
try:
    product1.move_product(location1, location2, 100)
    product2.move_product(location2, location3, 50)
    product3.move_product(location1, location3, 40)
except Exception as e:
    print(e)

# Create movement objects
movement1 = Movement(location1, location2, product1, 100)
movement2 = Movement(location2, location3, product2, 50)
movement3 = Movement(location2, location3, product3, 40)

# Add movements to a list
all_movements = [movement1, movement2,movement3]

# Display movements of each product
# for product in [product1, product2, product3]:
#     movements = Movement.movements_by_product(product)
#     print(f"Product: {product} ")
#     for movement in movements:
#         print(movement)
#
# # Display product details with its stock at various locations
# for product in [product1, product2, product3]:
#     print(f"Product: {product}")
#     for location, stock in product.stock_at_locations.items():
#         print(f"from: {location}, Stock: {stock}")

# Display product list by location
product_list_by_location = {}
for product in [product1, product2, product3, product4, product5]:
    for location, stock in product.stock_at_locations.items():
        if stock > 0:
            if location not in product_list_by_location:
                product_list_by_location[location] = []