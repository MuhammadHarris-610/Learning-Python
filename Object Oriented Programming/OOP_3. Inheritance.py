# OOP: Exercise 3 (Using Inheritance)
# Program Description: Expanding the restaurant program to be able to incorporate different types of restaurants

class Restaurant: # Defining Parent Class
    # Modelling Parent Class
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

class IceCreamStand(Restaurant): # Defining Child Class
    # Modelling Child Class
    def __init__(self, name, cuisine_type, flavours):
        super().__init__(name, cuisine_type)
        self.flavours = flavours

    def display_flavours(self):
        print("Available Flavours:")
        for flavour in self.flavours:
            print(flavour.title())


# Testing
stand1 = IceCreamStand("Ice Scream", "Ice Cream", ["chocolate", "vanilla", "strawberry", "mango", "blueberry"])
stand1.describe_restaurant()
stand1.open_restaurant()
stand1.print_served_customers()
stand1.set_numbers_served(55)
stand1.print_served_customers()
stand1.display_flavours()