class Product:
    def __init__(self, name, code, category, price):
        self.name = name
        self.code = code
        self.category = category
        self.price = price
        category.no_of_products += 1
class Category:
    def __init__(self, name, code, parent=None):
        self.name = name
        self.code = code
        self.no_of_products = 0
        self.parent = parent
        self.display_name = self.generate_display_name()
        self.products = []

    def generate_display_name(self):
        display_name = self.name
        if self.parent:
            display_name = self.parent.generate_display_name() + " > " + display_name
        return display_name
        # if self.parent is None:
        #     self.display_name = self.name
        # else:
        #     self.display_name = self.parent.display_name + " > " + self.name

# Create category objects

vehicle_category = Category("Vehicle","VHC")
car_category = Category("Car", "CAR", vehicle_category)
petrol_category = Category("Petrol", "PTR", car_category)
diesel_category = Category("Diesel", "DSL", petrol_category)
electric_category = Category("Electric", "ELC", diesel_category)

# Set parent-child relationships
# vehicle_category.parent = test
# car_category.parent = vehicle_category
# petrol_category.parent = car_category
# diesel_category.parent = car_category
# electric_category.parent = car_category
# # vehicle_category.parent = test

# Generate display names
# test.generate_display_name()
# vehicle_category.generate_display_name()
# car_category.generate_display_name()
# petrol_category.generate_display_name()
# diesel_category.generate_display_name()
# electric_category.generate_display_name()
# Add products to categories
vehicle_category.products.append(Product("Swift", "SWF", vehicle_category, 12000))
vehicle_category.products.append(Product("Dzire", "DZR", vehicle_category, 8000))
vehicle_category.products.append(Product("Ertiga", "ERT", vehicle_category, 4000))

car_category.products.append(Product("Swift", "SWF", car_category, 12000))
car_category.products.append(Product("Dzire", "DZR", car_category, 8000))
car_category.products.append(Product("Ertiga", "ERT", car_category, 500))

petrol_category.products.append(Product("Swift", "SWF", petrol_category, 1200))
petrol_category.products.append(Product("Dzire", "DZR", petrol_category, 3400))
petrol_category.products.append(Product("Ertiga", "ERT", petrol_category, 4500))

diesel_category.products.append(Product("Swift", "SWF", diesel_category, 100000))
diesel_category.products.append(Product("Dzire", "DZR", diesel_category, 80000))
diesel_category.products.append(Product("Ertiga", "ERT", diesel_category, 120000))

electric_category.products.append(Product("Swift", "SWF", electric_category, 100000))
electric_category.products.append(Product("Dzire", "DZR", electric_category, 80000))
electric_category.products.append(Product("Ertiga", "ERT", electric_category, 120000))

# print("Category name:", vehicle_category.name)
# print("Category code:", vehicle_category.code)
# print("Number of products:", vehicle_category.no_of_products)
# print("Vehicle category display name:", vehicle_category.display_name)
# print("Products:")
# for product in vehicle_category.products:
#     print(product.name,product.code,product.category,product.price)
#
# print("Category name:", car_category.name)
# print("Category code:", car_category.code)
# print("Number of products:", car_category.no_of_products)
# print("Car category display name:", car_category.display_name)
# print("Products:")
# for product in car_category.products:
#     print(product.name,product.code,product.category,product.price)
#
# print("Category name:", petrol_category.name)
# print("Category code:", petrol_category.code)
# print("Number of products:", petrol_category.no_of_products)
# print("Petrol category display name:", petrol_category.display_name)
# print("Products:")
# for product in petrol_category.products:
#     print(product.name,product.code,product.category,product.price)
for category in [vehicle_category, car_category, petrol_category, diesel_category, electric_category]:
    print(f"Category Code: {category.code}")
    print(f"Category Name: {category.name}")
    print(f"Display Name: {category.display_name}")
    print(f"Number of Products: {category.no_of_products}")
    print("-" * 40)
    print("Product Details:")
    for product in category.products:
        print(f"Product Name: {product.name}")
        print(f"Product code: {product.code}")
        print(f"Product price: {product.price}")
        print("-" * 20)
    print("-" * 80)

# # Display product list by category
# for category in [vehicle_category, car_category, petrol_category, diesel_category, electric_category]:
#     print("Category:", category.name)
#     for product in category.products:
#         for product1 in sorted(category.display_name):
#             print("  - Product:", product1.name )
#
# categories = [vehicle_category, car_category, petrol_category, diesel_category, electric_category]
# for category in categories:
#     print("Category:", category.display_name)
#     for product in sorted(category.products):
#         print(product.name)



for category in [vehicle_category, car_category, petrol_category, diesel_category, electric_category]:
    print(category.display_name)
    for product in sorted(category.products, key=lambda product: product.name):
        print(" - " + product.code)

        