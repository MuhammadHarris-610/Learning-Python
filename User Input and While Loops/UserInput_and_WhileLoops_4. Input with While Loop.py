#User Input and While Loops: Exercise 4 (Input with While Loop)

# Program Description: Historic Site Tickets

print("Welcome To The Lahore Fort!")
while True:
   age = int(input("Enter age: "))
   if age <= 3:
      ticket_price = 0
   elif age > 3 and age <= 12:
      ticket_price = 10
   else:
      ticket_price = 15
   print(f"Your Ticket Price: ${ticket_price}")
   break

