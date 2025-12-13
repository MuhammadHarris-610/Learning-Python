# Functions: Exercise 2 (Keyword Arguments)
# Program Description: T-Shirts

def t_shirts(size, text):
    return f"Size: {size.title()}\nText to be printed: '{text}'"

def main():
    shirt_size = input("Enter the size: ")
    message = input("Enter the text to be printed: ")
    print(t_shirts(text=message, size=shirt_size))

main()