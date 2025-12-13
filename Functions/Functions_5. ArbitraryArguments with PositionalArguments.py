# Functions: Exercise 5 (Arbitrary Arguments with positional Arguments)
# Program Description: Sandwich Maker
def sandwich(*items):
    print(f"Your sandwich contains these items:")
    for item in items:
        print(item.title())
sandwich('cake', 'cherry', 'pizza', 'egg', 'burger')