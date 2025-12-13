# Functions: Exercise 1 (Basic Function)
# Program Description: Favorite Book

def favorite_book(name, title):
   return f"{name.title()}'s favorite book is {title.title()}."

def main():
   name = input("Enter name: ")
   book = input("Enter favorite book: ")
   print(favorite_book(name, book))

main()