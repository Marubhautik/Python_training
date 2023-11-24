import re
import datetime
class Customer:
    def __init__(self, name, email, phone, street, city, state, country, company, type):
        self.name = name
        self.email = email
        self.phone = phone
        self.street = street
        self.city = city
        self.state = state
        self.country = country
        self.company = company
        self.type = type

        # Validate company (if applicable)
        if type == "company" and not isinstance(company, Customer):
            print("Company must be a Customer object.")

    def validate_phone(self):
        if not re.match(r"\d{3}-\d{3}-\d{4}", self.phone):
            print("Invalid phone number format")

    def validate_email(self):
        if not re.match(r"^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", self.email):
            print("Invalid email address format")

    def validate_name_city_state_country(self, field_name):
        if re.search(r"\d", field_name):
            print(f"{field_name} cannot contain numbers")

    def validate_type(self):
        if self.type not in ["company", "contact", "billing", "shipping"]:
            print("Invalid customer type")

    def validate_all(self):
        self.validate_phone()
        self.validate_email()
        self.validate_name_city_state_country("name")
        self.validate_name_city_state_country("city")
        self.validate_name_city_state_country("state")
        self.validate_name_city_state_country("country")
        self.validate_type()

    def display_details(self):
        print(f"Customer Name: {self.name}")
        print(f"Email Address: {self.email}")
        print(f"Phone Number: {self.phone}")
        print(f"Street Address: {self.street}")
        print(f"City: {self.city}")
        print(f"State: {self.state}")
        print(f"Country: {self.country}")
        print(f"Company:", self.company.name if self.company else None)
        print(f"Customer Type: {self.type}")

class OrderLine:
    def __init__(self, order, product, quantity, price):
        self.order = order
        self.product = product
        self.quantity = quantity
        self.price = price
        self.subtotal = self.quantity * self.price

    def display_details(self):
        print("Product:", self.product)
        print("Quantity:", self.quantity)
        print("Price:", self.price)
        print("Subtotal:", self.subtotal)

class Order:
    def __init__(self, number, date, company, billing, shipping, order_lines):
        self.number = number
        if date < datetime.date.today():
            print("Order date cannot be in the past.")
        self.date = date
        self.company = company
        self.billing = billing
        self.shipping = shipping
        self.total_amount = 0
        self.order_lines = order_lines
        for order_line in self.order_lines:
            self.total_amount += order_line.subtotal

    def display_order_details(self):
        print("Order Details:")
        print("Order Number:", self.number)
        print("Order Date:", self.date)
        print("Company:")
        self.company.display_details()
        print("Billing:")
        self.billing.display_details()
        print("Shipping:")
        self.shipping.display_details()
        print("Order Lines:")
        for order_line in self.order_lines:
            order_line.display_details()
        print("Total Amount:", self.total_amount)

        # Sort orders based on "date"
    def sort_orders_by_date(self, orders):
        return sorted(orders, key=lambda order: order.date)

        # Filter orders for the current month
    def filter_orders_for_current_month(self, orders):
        current_month = datetime.date.today().month
        filtered_orders = [order for order in orders if order.date.month == current_month]
        return filtered_orders

        # Search orders from their number
    def search_orders_by_number(self, orders, order_number):
        matching_orders = [order for order in orders if order.number == order_number]
        return matching_orders

        # List all orders of a specific product
    def list_orders_by_product(self, orders, product):
        matching_orders = [order for order in orders for order_line in order.order_lines if
                           order_line.product == product]
        return matching_orders

# Create Customer objects
company = Customer("ABC Company", "company@example.com", "123-456-7890", "123 Main St", "Anytown", "CA", "USA", None, "contact")
company.validate_all()
billing = Customer("John Doe", "johndoe@example.com", "123-456-7890", "456 Elm St", "Anytown", "CA", "USA", company, "billing")
billing.validate_all()
shipping = Customer("Jane Doe", "janedoe@example.com", "987-654-3210", "789 Oak St", "Anytown", "CA", "USA", company, "billing")
shipping.validate_all()

order_line1 = OrderLine(None, "laptop", 2,1000 )
order_line2 = OrderLine(None, "Computer", 1,2000)

order_line = [order_line1, order_line2]
order_date = datetime.date.today()
order1 = Order(12345, order_date, company, billing, shipping, [order_line1, order_line2])
order2 = Order(56789, datetime.date(2023, 12, 10), company, billing, shipping, [order_line1, order_line2])
order3 = Order(98765, datetime.date(2023, 11, 20), company, billing, shipping, [order_line1, order_line2])


order1.display_order_details()
order2.display_order_details()
order3.display_order_details()

# order_line1 = OrderLine(order1, "laptop", 2,1000 )
# order_line2 = OrderLine(order1, "Computer", 1,2000)
#
# order_lines = [order_line1, order_line2]
orders = [order3,order2,order1]
for a in order1.sort_orders_by_date(orders):
    print(a.date)

print('\nFilter orders for the current month')
orders = [order3,order2,order1]
for a in order1.filter_orders_for_current_month(orders):
    print(a.date)


