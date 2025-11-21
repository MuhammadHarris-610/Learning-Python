#User Input and While Loops: Exercise 3 (Input with While Loop)

# Program Description: Pizza Toppings

print("Please enter the Pizza toppings you want on your pizza.\nEnter 'quit' when you have completed your order: ")
toppings = []
active = True
while active:
   topping = input("Enter Your Topping/Finish you order: ")
   if topping != 'quit':
      toppings.append(topping.title())
   else:
      print(f"Your Toppings: {toppings}")
      active = False