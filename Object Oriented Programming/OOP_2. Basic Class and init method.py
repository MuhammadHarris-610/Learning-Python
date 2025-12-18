# OOP: Exercise 2 (A Basic Class)
# Program Description: Creating a class to demonstrate a user login

class User:

    def __init__(self, first_name, last_name, age, country, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country
        self.email = email
        self.name = f"{self.first_name} {self.last_name}"
        self.login_attempts = 0

    def describe_user(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Country: {self.country}")
        print(f"Email: {self.email}")

    def greet_user(self):
        print(f"Welcome {self.name}")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

user1 = User("Muhammad", "Harris", 18, "Pakistan", "str84word610@gmail.com")
user1.describe_user()
user1.greet_user()
