# OOP: Exercise 1 (A Basic Class)
# Program Description: Making a class for a restaurant

class Restaurant: # Defining the class

# Modelling the class
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.orders_served = 0

    def describe_restaurant(self):
        print(f"Welcome to {self.name}!")
        print(f"Here you will find all sorts of {self.cuisine_type} dishes.")

    def open_restaurant(self):
        print(f"{self.name} is now open.")

    def print_served_customers(self):
        print(f"Customers Served so far: {self.orders_served}")

    def set_numbers_served(self, number):
        self.orders_served = number

    def increment_number_served(self, increment):
        self.orders_served += increment

# Testing the class by creating an instance
restaurant1 = Restaurant("Mehrab", "Continental")
restaurant1.describe_restaurant()
restaurant1.open_restaurant()
restaurant1.set_numbers_served(500)
restaurant1.increment_number_served(30)
restaurant1.print_served_customers()