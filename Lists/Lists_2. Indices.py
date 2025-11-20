# Lists: Exercise 2 (Working with Indices)

# Program Description: Menu
menu = ['Karahi', 'Biryani', 'Pulao',  'Nehari', 'Paaye', ]

print(f"Breakfast: {menu[-1]} and {menu[-2]}")
print(f"Lunch: {menu[0]} and {menu[-1]}")

removed = menu.pop(2)
print(f"{removed} is no longer on menu as {menu[1]} is already there.")

desert = 'Gulaab Jamun'
menu.insert(0, desert)
print(f"Desert: {menu[0]}")
print(f"Final menu: {menu}")

