# class Product:
#     def __init__(self, product_id, name, price, stock):
#         self.product_id = product_id
#         self.name = name
#         self.price = price
#         self.stock = stock

#     def update_stock(self, quantity):
#         if quantity <= self.stock:
#             self.stock -= quantity
#             return True
#         return False

# class Customer:
#     def __init__(self, customer_id, name):
#         self.customer_id = customer_id
#         self.name = name
#         self.cart = Cart()

# class Cart:
#     def __init__(self):
#         self.items = {}

#     def add_item(self, product, quantity):
#         if product.update_stock(quantity):
#             if product.product_id in self.items:
#                 self.items[product.product_id]["quantity"] += quantity
#             else:
#                 self.items[product.product_id] = {"product": product, "quantity": quantity}
#             return True
#         return False

#     def calculate_total(self):
#         return sum(item["product"].price * item["quantity"] for item in self.items.values())

# class Order:
#     def __init__(self, customer):
#         self.customer = customer
#         self.total_cost = customer.cart.calculate_total()

#     def process_order(self):
#         print(f"Order placed for {self.customer.name}. Total Cost: ${self.total_cost:.2f}")

# # Example Usage
# product1 = Product(1, "Laptop", 800, 10)
# product2 = Product(2, "Phone", 500, 5)

# customer = Customer(101, "Alice")
# customer.cart.add_item(product1, 2)
# customer.cart.add_item(product2, 1)

# order = Order(customer)
# order.process_order()


class Vehicle:
    def __init__(self, vehicle_id, model, daily_rate, available=True):
        self.vehicle_id = vehicle_id
        self.model = model
        self.daily_rate = daily_rate
        self.available = available

    def rent_vehicle(self):
        if self.available:
            self.available = False
            return True
        return False

    def return_vehicle(self):
        self.available = True

class RentalAgency:
    def __init__(self, name):
        self.name = name
        self.vehicles = {}

    def add_vehicle(self, vehicle):
        self.vehicles[vehicle.vehicle_id] = vehicle

    def check_availability(self, vehicle_id):
        return self.vehicles.get(vehicle_id, None) and self.vehicles[vehicle_id].available

class RentalTransaction:
    def __init__(self, customer_name, vehicle, rental_days):
        self.customer_name = customer_name
        self.vehicle = vehicle
        self.rental_days = rental_days
        self.total_cost = vehicle.daily_rate * rental_days if vehicle.rent_vehicle() else 0

    def process_rental(self):
        if self.total_cost > 0:
            print(f"{self.customer_name} rented {self.vehicle.model} for {self.rental_days} days. Total: ${self.total_cost:.2f}")
        else:
            print("Vehicle not available!")

car1 = Vehicle(101, "Toyota Corolla", 40)
car2 = Vehicle(102, "Honda Civic", 50)

agency = RentalAgency("Quick Rentals")
agency.add_vehicle(car1)
agency.add_vehicle(car2)

rental = RentalTransaction("Bob", car1, 3)
rental.process_rental()