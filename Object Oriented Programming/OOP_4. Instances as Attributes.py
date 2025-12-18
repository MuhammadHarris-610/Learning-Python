# OOP: Exercise 4 (Using Instances as Attributes)
# Program Description: Expanding the User program to incorporate Admins

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

class Privilages:
    def __init__(self, privilages=["can remove user", "can add user", "can delete files", "can give privilages"]):
        self.privilages = privilages 
    def show_privilages(self):
        print("Privilages")
        for privilage in self.privilages:
            print(privilage.title())


class Admin(User):
    def __init__(self, first_name, last_name, age, country, email):
        super().__init__(first_name, last_name, age, country, email)
        self.privilages = Privilages()



admin1 = Admin("Muhammad", "Harris", 18, "Pakistan", "str84word610@gmail.com")
admin1.describe_user()
admin1.greet_user()
admin1.privilages.show_privilages()

